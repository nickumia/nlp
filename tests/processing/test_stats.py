
import nlp.processing.stats as nps


def test_mean():
    a = [1, 2, 3, 4, 5]
    assert nps.mean(a) == 3


def test_std_dev():
    a = [2, 4, 6]
    assert nps.standard_deviation(a)[1] == 1.632993161855452


def test_range():
    a = [1, 2, 5, 10]
    assert nps.s_range(a) == 9


def test_list_add():
    a = [1, 3, 5, 6, 7]
    b = [2, 4, 8, 9, 10]

    nps.list_add(a, b) == [3, 7, 13, 15, 17]


def test_confidence_level():
    assert nps.confidence_level(10, 15, 2.5) == 32
    assert nps.confidence_level(15, 10, 2.5) == 68
    assert nps.confidence_level(3.5, 4, 1) == 41
    assert nps.confidence_level(990, 100, .5) == 99

