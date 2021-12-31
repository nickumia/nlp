
import nlp.processing.filters as npf


def test_lowercase():
    assert npf.lowercase("SUPER Important!") == "super important!"


def test_sortabasedonb():
    assert npf.sortabasedonb([[1, 2, 4, 3], [3, 4, 2, 1]]) == \
        ([1, 2, 3, 4], [3, 4, 1, 2])
