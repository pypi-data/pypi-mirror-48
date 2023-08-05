import abc
import typing

from .. import base


__all__ = [
    'BinaryMetric',
    'MultiClassMetric',
    'RegressionMetric'
]


class Metric(abc.ABC):

    @abc.abstractmethod
    def get(self) -> float:
        """Returns the current value of the metric."""

    @abc.abstractmethod
    def works_with(self, model) -> bool:
        """Tells if a metric can work with a given model or not."""

    @property
    @abc.abstractmethod
    def bigger_is_better(self) -> bool:
        """Indicates if a high value is better than a low one or not."""

    def __str__(self):
        """Returns the class name along with the current value of the metric."""
        return f'{self.__class__.__name__}: {self.get():.6f}'.rstrip('0')

    def __repr__(self):
        return str(self)


class ClassificationMetric(Metric):

    @property
    @abc.abstractmethod
    def requires_labels(self) -> bool:
        """Helps to indicate if labels are required instead of probabilities."""


class BinaryMetric(ClassificationMetric):

    @abc.abstractmethod
    def update(self, y_true: bool, y_pred: typing.Union[bool, base.Probas]) -> 'BinaryMetric':
        """Updates the metric."""

    def works_with(self, model) -> bool:
        return isinstance(model, base.BinaryClassifier)


class MultiClassMetric(BinaryMetric):

    @abc.abstractmethod
    def update(self, y_true: base.Label,
               y_pred: typing.Union[base.Label, base.Probas]) -> 'MultiClassMetric':
        """Updates the metric."""

    def works_with(self, model) -> bool:
        return isinstance(model, (base.BinaryClassifier, base.MultiClassifier))


class RegressionMetric(Metric):

    @abc.abstractmethod
    def update(self, y_true: float, y_pred: float) -> 'RegressionMetric':
        """Updates the metric."""

    @property
    def bigger_is_better(self):
        return False

    def works_with(self, model) -> bool:
        return isinstance(model, base.Regressor)


class MultiOutputClassificationMetric(ClassificationMetric):

    def update(self, y_true: typing.Dict[str, base.Label],
               y_pred: typing.Dict[str, typing.Union[base.Label, base.Probas]]):
        """Updates the metric."""

    def works_with(self, model) -> bool:
        return isinstance(model, base.MultiOutputClassifier)


class MultiOutputRegressionMetric(RegressionMetric):

    def update(self, y_true: typing.Dict[str, float], y_pred: typing.Dict[str, float]):
        """Updates the metric."""

    def works_with(self, model) -> bool:
        return isinstance(model, base.MultiOutputRegressor)
