
from nlp.efficiency import Time


def test_efficiency_ttr():
    iterations = 1000
    A = Time('''
from nlp.efficiency import ttr1
body=["a", "b", "c", "b"]*50
             ''',
             '''ttr1(body)''', iterations)
    B = Time('''
from nlp.efficiency import ttr2
body=["a", "b", "c", "b"]*50
             ''',
             '''ttr2(body)''', iterations)

    print('A: %f' % A.run())
    print('B: %f' % B.run())
    assert A.run() < B.run()