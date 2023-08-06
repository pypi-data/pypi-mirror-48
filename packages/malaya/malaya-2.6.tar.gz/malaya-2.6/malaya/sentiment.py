import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter('ignore')

from ._utils import _softmax_class
from ._utils._paths import PATH_SENTIMENT, S3_PATH_SENTIMENT


def available_sparse_deep_model():
    """
    List available sparse deep learning sentiment analysis models.
    """
    return ['fast-text-char']


def available_deep_model():
    """
    List available deep learning sentiment analysis models.
    """
    return ['self-attention', 'bahdanau', 'luong']


def sparse_deep_model(model = 'fast-text-char', validate = True):
    """
    Load deep learning sentiment analysis model.

    Parameters
    ----------
    model : str, optional (default='luong')
        Model architecture supported. Allowed values:

        * ``'fast-text-char'`` - Fast-text architecture for character based n-grams, embedded and logits layers only.
    validate: bool, optional (default=True)
        if True, malaya will check model availability and download if not available.

    Returns
    -------
    SPARSE_SOFTMAX: malaya._models._tensorflow_model.SPARSE_SOFTMAX class
    """
    return _softmax_class.sparse_deep_model(
        PATH_SENTIMENT,
        S3_PATH_SENTIMENT,
        'sentiment',
        ['negative', 'positive'],
        2,
        model = model,
        validate = validate,
    )


def deep_model(model = 'luong', validate = True):
    """
    Load deep learning sentiment analysis model.

    Parameters
    ----------
    model : str, optional (default='luong')
        Model architecture supported. Allowed values:

        * ``'self-attention'`` - Fast-text architecture, embedded and logits layers only with self attention.
        * ``'bahdanau'`` - LSTM with bahdanau attention architecture.
        * ``'luong'`` - LSTM with luong attention architecture.
    validate: bool, optional (default=True)
        if True, malaya will check model availability and download if not available.

    Returns
    -------
    SOFTMAX: malaya._models._tensorflow_model.SOFTMAX class
    """
    if not isinstance(model, str):
        raise ValueError('model must be a string')
    if not isinstance(validate, bool):
        raise ValueError('validate must be a boolean')
    model = model.lower()
    if model not in available_deep_model():
        raise Exception(
            'model is not supported, please check supported models from malaya.sentiment.available_deep_model()'
        )

    return _softmax_class.deep_model(
        PATH_SENTIMENT,
        S3_PATH_SENTIMENT,
        'sentiment',
        ['negative', 'positive'],
        model = model,
        validate = validate,
    )


def multinomial(validate = True):
    """
    Load multinomial sentiment model.

    Parameters
    ----------
    validate: bool, optional (default=True)
        if True, malaya will check model availability and download if not available.

    Returns
    -------
    BAYES : malaya._models._sklearn_model.BAYES class
    """
    return _softmax_class.multinomial(
        PATH_SENTIMENT,
        S3_PATH_SENTIMENT,
        'sentiment',
        ['negative', 'positive'],
        validate = validate,
    )


def xgb(validate = True):
    """
    Load XGB sentiment model.

    Parameters
    ----------
    validate: bool, optional (default=True)
        if True, malaya will check model availability and download if not available.

    Returns
    -------
    XGB : malaya._models._sklearn_model.XGB class
    """
    return _softmax_class.xgb(
        PATH_SENTIMENT,
        S3_PATH_SENTIMENT,
        'sentiment',
        ['negative', 'positive'],
        validate = validate,
    )


def bert(validate = True):
    """
    Load BERT sentiment model.

    Parameters
    ----------
    validate: bool, optional (default=True)
        if True, malaya will check model availability and download if not available.

    Returns
    -------
    XGB : malaya._models._tensorflow_model.BINARY_BERT class
    """
    if not isinstance(validate, bool):
        raise ValueError('validate must be a boolean')
    return _softmax_class.bert(
        PATH_SENTIMENT,
        S3_PATH_SENTIMENT,
        'sentiment',
        ['negative', 'positive'],
        validate = validate,
    )
