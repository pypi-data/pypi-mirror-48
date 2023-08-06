import numbers

from AnyQt.QtWidgets import QFormLayout
from AnyQt.QtGui import QColor
from AnyQt.QtCore import Qt

import numpy
import pyqtgraph as pg

from Orange.data import Table, Domain, StringVariable, ContinuousVariable
from Orange.data.sql.table import SqlTable, AUTO_DL_LIMIT
from Orange.preprocess import preprocess
from Orange.projection import PCA
from Orange.widgets import widget, gui, settings
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.widget import Input, Output


# Maximum number of PCA components that we can set in the widget
MAX_COMPONENTS = 100


class OWPCA(widget.OWWidget):
    name = "PCA"
    description = "Principal component analysis with a scree-diagram."
    icon = "icons/PCA.svg"
    priority = 3050
    keywords = ["principal component analysis", "linear transformation"]

    class Inputs:
        data = Input("Data", Table)

    class Outputs:
        transformed_data = Output("Transformed data", Table)
        components = Output("Components", Table)
        pca = Output("PCA", PCA, dynamic=False)

    settingsHandler = settings.DomainContextHandler()

    ncomponents = settings.Setting(2)
    variance_covered = settings.Setting(100)
    auto_commit = settings.Setting(True)
    normalize = settings.ContextSetting(True)
    maxp = settings.Setting(20)
    axis_labels = settings.Setting(10)

    graph_name = "plot.plotItem"

    class Warning(widget.OWWidget.Warning):
        trivial_components = widget.Msg(
            "All components of the PCA are trivial (explain 0 variance). "
            "Input data is constant (or near constant).")

    class Error(widget.OWWidget.Error):
        no_features = widget.Msg("At least 1 feature is required")
        no_instances = widget.Msg("At least 1 data instance is required")

    def __init__(self):
        super().__init__()
        self.data = None

        self._pca = None
        self._transformed = None
        self._variance_ratio = None
        self._cumulative = None
        self._line = False
        self._init_projector()

        # Components Selection
        box = gui.vBox(self.controlArea, "Components Selection")
        form = QFormLayout()
        box.layout().addLayout(form)

        self.components_spin = gui.spin(
            box, self, "ncomponents", 1, MAX_COMPONENTS,
            callback=self._update_selection_component_spin,
            keyboardTracking=False
        )
        self.components_spin.setSpecialValueText("All")

        self.variance_spin = gui.spin(
            box, self, "variance_covered", 1, 100,
            callback=self._update_selection_variance_spin,
            keyboardTracking=False
        )
        self.variance_spin.setSuffix("%")

        form.addRow("Components:", self.components_spin)
        form.addRow("Variance covered:", self.variance_spin)

        # Options
        self.options_box = gui.vBox(self.controlArea, "Options")
        self.normalize_box = gui.checkBox(
            self.options_box, self, "normalize",
            "Normalize data", callback=self._update_normalize
        )

        self.maxp_spin = gui.spin(
            self.options_box, self, "maxp", 1, MAX_COMPONENTS,
            label="Show only first", callback=self._setup_plot,
            keyboardTracking=False
        )

        self.controlArea.layout().addStretch()

        gui.auto_commit(self.controlArea, self, "auto_commit", "Apply",
                        checkbox_label="Apply automatically")

        self.plot = pg.PlotWidget(background="w")

        axis = self.plot.getAxis("bottom")
        axis.setLabel("Principal Components")
        axis = self.plot.getAxis("left")
        axis.setLabel("Proportion of variance")
        self.plot_horlabels = []
        self.plot_horlines = []

        self.plot.getViewBox().setMenuEnabled(False)
        self.plot.getViewBox().setMouseEnabled(False, False)
        self.plot.showGrid(True, True, alpha=0.5)
        self.plot.setRange(xRange=(0.0, 1.0), yRange=(0.0, 1.0))

        self.mainArea.layout().addWidget(self.plot)
        self._update_normalize()

    @Inputs.data
    def set_data(self, data):
        self.closeContext()
        self.clear_messages()
        self.clear()
        self.information()
        self.data = None
        if isinstance(data, SqlTable):
            if data.approx_len() < AUTO_DL_LIMIT:
                data = Table(data)
            else:
                self.information("Data has been sampled")
                data_sample = data.sample_time(1, no_cache=True)
                data_sample.download_data(2000, partial=True)
                data = Table(data_sample)
        if isinstance(data, Table):
            if len(data.domain.attributes) == 0:
                self.Error.no_features()
                self.clear_outputs()
                return
            if len(data) == 0:
                self.Error.no_instances()
                self.clear_outputs()
                return

        self.openContext(data)
        self._init_projector()

        self.data = data
        self.fit()

    def fit(self):
        self.clear()
        self.Warning.trivial_components.clear()
        if self.data is None:
            return

        data = self.data

        if self.normalize:
            self._pca_projector.preprocessors = \
                self._pca_preprocessors + [preprocess.Normalize(center=False)]
        else:
            self._pca_projector.preprocessors = self._pca_preprocessors

        if not isinstance(data, SqlTable):
            pca = self._pca_projector(data)
            variance_ratio = pca.explained_variance_ratio_
            cumulative = numpy.cumsum(variance_ratio)

            if numpy.isfinite(cumulative[-1]):
                self.components_spin.setRange(0, len(cumulative))
                self._pca = pca
                self._variance_ratio = variance_ratio
                self._cumulative = cumulative
                self._setup_plot()
            else:
                self.Warning.trivial_components()

            self.unconditional_commit()

    def clear(self):
        self._pca = None
        self._transformed = None
        self._variance_ratio = None
        self._cumulative = None
        self._line = None
        self.plot_horlabels = []
        self.plot_horlines = []
        self.plot.clear()

    def clear_outputs(self):
        self.Outputs.transformed_data.send(None)
        self.Outputs.components.send(None)
        self.Outputs.pca.send(self._pca_projector)

    def _setup_plot(self):
        self.plot.clear()
        if self._pca is None:
            return

        explained_ratio = self._variance_ratio
        explained = self._cumulative
        p = min(len(self._variance_ratio), self.maxp)

        self.plot.plot(numpy.arange(p), explained_ratio[:p],
                       pen=pg.mkPen(QColor(Qt.red), width=2),
                       antialias=True,
                       name="Variance")
        self.plot.plot(numpy.arange(p), explained[:p],
                       pen=pg.mkPen(QColor(Qt.darkYellow), width=2),
                       antialias=True,
                       name="Cumulative Variance")

        cutpos = self._nselected_components() - 1
        self._line = pg.InfiniteLine(
            angle=90, pos=cutpos, movable=True, bounds=(0, p - 1))
        self._line.setCursor(Qt.SizeHorCursor)
        self._line.setPen(pg.mkPen(QColor(Qt.black), width=2))
        self._line.sigPositionChanged.connect(self._on_cut_changed)
        self.plot.addItem(self._line)

        self.plot_horlines = (
            pg.PlotCurveItem(pen=pg.mkPen(QColor(Qt.blue), style=Qt.DashLine)),
            pg.PlotCurveItem(pen=pg.mkPen(QColor(Qt.blue), style=Qt.DashLine)))
        self.plot_horlabels = (
            pg.TextItem(color=QColor(Qt.black), anchor=(1, 0)),
            pg.TextItem(color=QColor(Qt.black), anchor=(1, 1)))
        for item in self.plot_horlabels + self.plot_horlines:
            self.plot.addItem(item)
        self._set_horline_pos()

        self.plot.setRange(xRange=(0.0, p - 1), yRange=(0.0, 1.0))
        self._update_axis()

    def _set_horline_pos(self):
        cutidx = self.ncomponents - 1
        for line, label, curve in zip(self.plot_horlines, self.plot_horlabels,
                                      (self._variance_ratio, self._cumulative)):
            y = curve[cutidx]
            line.setData([-1, cutidx], 2 * [y])
            label.setPos(cutidx, y)
            label.setPlainText("{:.3f}".format(y))

    def _on_cut_changed(self, line):
        # cut changed by means of a cut line over the scree plot.
        value = int(round(line.value()))
        self._line.setValue(value)
        current = self._nselected_components()
        components = value + 1

        if not (self.ncomponents == 0 and
                components == len(self._variance_ratio)):
            self.ncomponents = components

        self._set_horline_pos()

        if self._pca is not None:
            var = self._cumulative[components - 1]
            if numpy.isfinite(var):
                self.variance_covered = int(var * 100)

        if current != self._nselected_components():
            self._invalidate_selection()

    def _update_selection_component_spin(self):
        # cut changed by "ncomponents" spin.
        if self._pca is None:
            self._invalidate_selection()
            return

        if self.ncomponents == 0:
            # Special "All" value
            cut = len(self._variance_ratio)
        else:
            cut = self.ncomponents

        var = self._cumulative[cut - 1]
        if numpy.isfinite(var):
            self.variance_covered = int(var * 100)

        if numpy.floor(self._line.value()) + 1 != cut:
            self._line.setValue(cut - 1)

        self._invalidate_selection()

    def _update_selection_variance_spin(self):
        # cut changed by "max variance" spin.
        if self._pca is None:
            return

        cut = numpy.searchsorted(self._cumulative,
                                 self.variance_covered / 100.0) + 1
        cut = min(cut, len(self._cumulative))
        self.ncomponents = cut
        if numpy.floor(self._line.value()) + 1 != cut:
            self._line.setValue(cut - 1)
        self._invalidate_selection()

    def _update_normalize(self):
        self.fit()
        if self.data is None:
            self._invalidate_selection()

    def _init_projector(self):
        self._pca_projector = PCA(n_components=MAX_COMPONENTS)
        self._pca_projector.component = self.ncomponents
        self._pca_preprocessors = PCA.preprocessors

    def _nselected_components(self):
        """Return the number of selected components."""
        if self._pca is None:
            return 0

        if self.ncomponents == 0:
            # Special "All" value
            max_comp = len(self._variance_ratio)
        else:
            max_comp = self.ncomponents

        var_max = self._cumulative[max_comp - 1]
        if var_max != numpy.floor(self.variance_covered / 100.0):
            cut = max_comp
            assert numpy.isfinite(var_max)
            self.variance_covered = int(var_max * 100)
        else:
            self.ncomponents = cut = numpy.searchsorted(
                self._cumulative, self.variance_covered / 100.0) + 1
        return cut

    def _invalidate_selection(self):
        self.commit()

    def _update_axis(self):
        p = min(len(self._variance_ratio), self.maxp)
        axis = self.plot.getAxis("bottom")
        d = max((p-1)//(self.axis_labels-1), 1)
        axis.setTicks([[(i, str(i+1)) for i in range(0, p, d)]])

    def commit(self):
        transformed = components = None
        if self._pca is not None:
            if self._transformed is None:
                # Compute the full transform (MAX_COMPONENTS components) only once.
                self._transformed = self._pca(self.data)
            transformed = self._transformed

            domain = Domain(
                transformed.domain.attributes[:self.ncomponents],
                self.data.domain.class_vars,
                self.data.domain.metas
            )
            transformed = transformed.from_table(domain, transformed)
            # prevent caching new features by defining compute_value
            dom = Domain([ContinuousVariable(a.name, compute_value=lambda _: None)
                          for a in self._pca.orig_domain.attributes],
                         metas=[StringVariable(name='component')])
            metas = numpy.array([['PC{}'.format(i + 1)
                                  for i in range(self.ncomponents)]],
                                dtype=object).T
            components = Table(dom, self._pca.components_[:self.ncomponents],
                               metas=metas)
            components.name = 'components'

        self._pca_projector.component = self.ncomponents
        self.Outputs.transformed_data.send(transformed)
        self.Outputs.components.send(components)
        self.Outputs.pca.send(self._pca_projector)

    def send_report(self):
        if self.data is None:
            return
        self.report_items((
            ("Normalize data", str(self.normalize)),
            ("Selected components", self.ncomponents),
            ("Explained variance", "{:.3f} %".format(self.variance_covered))
        ))
        self.report_plot()

    @classmethod
    def migrate_settings(cls, settings, version):
        if "variance_covered" in settings:
            # Due to the error in gh-1896 the variance_covered was persisted
            # as a NaN value, causing a TypeError in the widgets `__init__`.
            vc = settings["variance_covered"]
            if isinstance(vc, numbers.Real):
                if numpy.isfinite(vc):
                    vc = int(vc)
                else:
                    vc = 100
                settings["variance_covered"] = vc
        if settings.get("ncomponents", 0) > MAX_COMPONENTS:
            settings["ncomponents"] = MAX_COMPONENTS

        # Remove old `decomposition_idx` when SVD was still included
        settings.pop("decomposition_idx", None)

        # Remove RemotePCA settings
        settings.pop("batch_size", None)
        settings.pop("address", None)
        settings.pop("auto_update", None)


if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWPCA).run(Table("housing"))
