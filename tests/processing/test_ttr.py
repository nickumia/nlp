
from nlp.processing.corpus.representativeness import ttr


def test_ttr_all_unique():
    test_body = ['this', 'is', 'a', 'list', 'of', 'completely',
                 'unique', 'strings']

    types, tokens = ttr(test_body)

    assert types == 8
    assert tokens == 8
    assert types/tokens == 1


def test_ttr_all_mixed():
    test_body = ['this', 'is', 'not', 'a', 'list', 'of', 'completely',
                 'unique', 'strings', 'because', 'of', 'this']

    types, tokens = ttr(test_body)

    assert types == 10
    assert tokens == 12
