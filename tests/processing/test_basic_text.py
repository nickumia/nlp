
from nlp.processing.inputs import BasicText


def test_basictext_init():
    text = BasicText('this is an interesting string.')

    assert text.getWords() == ['this', 'is', 'an', 'interesting',
                               'string.']
