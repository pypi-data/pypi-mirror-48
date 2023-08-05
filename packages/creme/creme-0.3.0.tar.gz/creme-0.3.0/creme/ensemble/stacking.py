from .. import base


__all__ = ['StackingBinaryClassifier']


class StackingBinaryClassifier(base.BinaryClassifier):
    """Stacking for binary classification.

    Parameters:
        classifiers (list of `base.BinaryClassifier`)
        meta_classifier (`base.BinaryClassifier`)
        include_features (bool): Indicates whether or not the original features should be provided
            to the meta-model along with the predictions from each model.

    Example:

        ::

            >>> from creme import compose
            >>> from creme import ensemble
            >>> from creme import linear_model
            >>> from creme import metrics
            >>> from creme import model_selection
            >>> from creme import preprocessing
            >>> from creme import stream
            >>> from sklearn import datasets

            >>> X_y = stream.iter_sklearn_dataset(
            ...     dataset=datasets.load_breast_cancer(),
            ...     shuffle=False
            ... )
            >>> model = compose.Pipeline([
            ...     ('scale', preprocessing.StandardScaler()),
            ...     ('stack', ensemble.StackingBinaryClassifier(
            ...         classifiers=[
            ...             linear_model.PAClassifier(mode=0),
            ...             linear_model.PAClassifier(mode=1),
            ...             linear_model.PAClassifier(mode=2)
            ...         ],
            ...         meta_classifier=linear_model.LogisticRegression()
            ...     ))
            ... ])
            >>> metric = metrics.F1()

            >>> model_selection.online_score(X_y, model, metric)
            F1: 0.95212

    References:
        1. `A Kaggler's Guide to Model Stacking in Practice <http://blog.kaggle.com/2016/12/27/a-kagglers-guide-to-model-stacking-in-practice/>`_

    """

    def __init__(self, classifiers, meta_classifier, include_features=True):
        self.classifiers = classifiers
        self.meta_classifier = meta_classifier
        self.include_features = include_features

    def fit_one(self, x, y):

        # Ask each model to make a prediction and then update it
        oof = {}
        for i, reg in enumerate(self.classifiers):
            oof[f'oof_{i}'] = reg.predict_proba_one(x).get(True, 0.5)
            reg.fit_one(x, y)

        # Optionally, add the base features
        if self.include_features:
            oof.update(x)

        # Update the meta-classifier using the predictions from the base classifiers
        self.meta_classifier.fit_one(oof, y)

        return self

    def predict_proba_one(self, x):

        oof = {
            f'oof_{i}': reg.predict_proba_one(x).get(True, 0.5)
            for i, reg in enumerate(self.classifiers)
        }

        if self.include_features:
            oof.update(x)

        return self.meta_classifier.predict_proba_one(oof)
