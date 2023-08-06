import warnings
from functools import partial
from itertools import chain

import numpy as np

from AnyQt.QtWidgets import QHeaderView, QStyledItemDelegate, QMenu
from AnyQt.QtGui import QStandardItemModel, QStandardItem
from AnyQt.QtCore import Qt, QSize, QObject, pyqtSignal as Signal
from sklearn.exceptions import UndefinedMetricWarning

from Orange.data import Variable, DiscreteVariable, ContinuousVariable
from Orange.evaluation import scoring
from Orange.widgets import gui
from Orange.widgets.gui import OWComponent
from Orange.widgets.settings import Setting


def check_results_adequacy(results, error_group, check_nan=True):
    error_group.add_message("invalid_results")
    error_group.invalid_results.clear()

    def anynan(a):
        return np.any(np.isnan(a))

    if results is None:
        return None
    if results.data is None:
        error_group.invalid_results(
            "Results do not include information on test data")
    elif not results.data.domain.has_discrete_class:
        error_group.invalid_results(
            "Discrete outcome variable is required")
    elif check_nan and (anynan(results.actual) or
                        anynan(results.predicted) or
                        (results.probabilities is not None and
                         anynan(results.probabilities))):
        error_group.invalid_results(
            "Results contains invalid values")
    else:
        return results


def results_for_preview(data_name=""):
    from Orange.data import Table
    from Orange.evaluation import CrossValidation
    from Orange.classification import \
        LogisticRegressionLearner, SVMLearner, NuSVMLearner

    data = Table(data_name or "ionosphere")
    results = CrossValidation(
        data,
        [LogisticRegressionLearner(penalty="l2"),
         LogisticRegressionLearner(penalty="l1"),
         SVMLearner(probability=True),
         NuSVMLearner(probability=True)
        ],
        store_data=True
    )
    results.learner_names = ["LR l2", "LR l1", "SVM", "Nu SVM"]
    return results


BUILTIN_SCORERS_ORDER = {
    DiscreteVariable: ("AUC", "CA", "F1", "Precision", "Recall"),
    ContinuousVariable: ("MSE", "RMSE", "MAE", "R2")}


def learner_name(learner):
    """Return the value of `learner.name` if it exists, or the learner's type
    name otherwise"""
    return getattr(learner, "name", type(learner).__name__)


def usable_scorers(target: Variable):
    order = {name: i
             for i, name in enumerate(BUILTIN_SCORERS_ORDER[type(target)])}
    # 'abstract' is retrieved from __dict__ to avoid inheriting
    usable = (cls for cls in scoring.Score.registry.values()
              if cls.is_scalar and not cls.__dict__.get("abstract")
              and isinstance(target, cls.class_types))
    return sorted(usable, key=lambda cls: order.get(cls.name, 99))


def scorer_caller(scorer, ovr_results, target=None):
    def thunked():
        with warnings.catch_warnings():
            # F-score and Precision return 0 for labels with no predicted
            # samples. We're OK with that.
            warnings.filterwarnings(
                "ignore", "((F-score|Precision)) is ill-defined.*",
                UndefinedMetricWarning)
            if scorer.is_binary:
                return scorer(ovr_results, target=target, average='weighted')
            else:
                return scorer(ovr_results)

    return thunked


class ScoreTable(OWComponent, QObject):
    shown_scores = \
        Setting(set(chain(*BUILTIN_SCORERS_ORDER.values())))

    shownScoresChanged = Signal()

    class ItemDelegate(QStyledItemDelegate):
        def sizeHint(self, *args):
            size = super().sizeHint(*args)
            return QSize(size.width(), size.height() + 6)

    def __init__(self, master):
        QObject.__init__(self)
        OWComponent.__init__(self, master)

        self.view = gui.TableView(
            wordWrap=True, editTriggers=gui.TableView.NoEditTriggers
        )
        header = self.view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setDefaultAlignment(Qt.AlignCenter)
        header.setStretchLastSection(False)
        header.setContextMenuPolicy(Qt.CustomContextMenu)
        header.customContextMenuRequested.connect(self.show_column_chooser)

        self.model = QStandardItemModel(master)
        self.model.setHorizontalHeaderLabels(["Method"])
        self.view.setModel(self.model)
        self.view.setItemDelegate(self.ItemDelegate())

    def _column_names(self):
        return (self.model.horizontalHeaderItem(section).data(Qt.DisplayRole)
                for section in range(1, self.model.columnCount()))

    def show_column_chooser(self, pos):
        # pylint doesn't know that self.shown_scores is a set, not a Setting
        # pylint: disable=unsupported-membership-test
        def update(col_name, checked):
            if checked:
                self.shown_scores.add(col_name)
            else:
                self.shown_scores.remove(col_name)
            self._update_shown_columns()

        menu = QMenu()
        header = self.view.horizontalHeader()
        for col_name in self._column_names():
            action = menu.addAction(col_name)
            action.setCheckable(True)
            action.setChecked(col_name in self.shown_scores)
            action.triggered.connect(partial(update, col_name))
        menu.exec(header.mapToGlobal(pos))

    def _update_shown_columns(self):
        # pylint doesn't know that self.shown_scores is a set, not a Setting
        # pylint: disable=unsupported-membership-test
        header = self.view.horizontalHeader()
        for section, col_name in enumerate(self._column_names(), start=1):
            header.setSectionHidden(section, col_name not in self.shown_scores)
        self.view.resizeColumnsToContents()
        self.shownScoresChanged.emit()

    def update_header(self, scorers):
        # Set the correct horizontal header labels on the results_model.
        self.model.setColumnCount(1 + len(scorers))
        self.model.setHorizontalHeaderItem(0, QStandardItem("Model"))
        for col, score in enumerate(scorers, start=1):
            item = QStandardItem(score.name)
            item.setToolTip(score.long_name)
            self.model.setHorizontalHeaderItem(col, item)
        self._update_shown_columns()
