
from nlp.processing.inputs import BasicText
from nlp.processing.corpus.representativeness import occurences


def test_basictext_init():
    text = BasicText('this is an interesting string')

    assert text.getWords() == ['this', 'is', 'an', 'interesting',
                               'string']


def test_occurences():
    text = BasicText('this string is the more interesting string')
    computed = occurences(text.getWords())

    assert computed == {'this': 1, 'string': 2, 'the': 1, 'is': 1, 'more': 1,
                        'interesting': 1}
