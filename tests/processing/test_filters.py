
import nlp.processing.filters as npf


def test_pre_sanitize():
    assert npf.pre_sanitize("Do you think they'd answer?") == \
            "do you think they would answer?"


def test_semi_sanitize():
    assert npf.semi_sanitize("What're they going to do about the PIZZA?!") == \
            "What are they going to do about the PIZZA?!"


def test_lowercase():
    assert npf.lowercase("SUPER Important!") == "super important!"


def test_sortabasedonb():
    assert npf.sortabasedonb([[1, 2, 4, 3], [3, 4, 2, 1]]) == \
        ([1, 2, 3, 4], [3, 4, 1, 2])


def test_combinelikevalues():
    a = [1, 1, 1, 2, 3, 4]
    b = ['a', 'a', 'a', 'b', 'c', 'd']
    assert npf.combineLikeValues([a, b]) == ([3, 2, 3, 4],
                                             ['a', 'b', 'c', 'd'])
