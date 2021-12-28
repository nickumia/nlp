
from nlp.processing.corpus.representativeness import ttr

def test_ttr_all_unique():
    test_body = ['this', 'is', 'a', 'list', 'of', 'completely',
                 'unique', 'strings']

    types,tokens = ttr(test_body)

    assert types == len(test_body)
    assert tokens == len(test_body)
    assert types/tokens == 1

