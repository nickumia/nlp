
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


def test_efficiency_max():
    iterations = 1000
    A = Time('''
from nlp.efficiency import dictmax
body={i:i for i in range(1000)}
             ''',
             '''dictmax(body)''', iterations)
    B = Time('''
from nlp.efficiency import listmax
body=[i for i in range(1000)]
             ''',
             '''listmax(body)''', iterations)

    print('A: %f' % A.run())
    print('B: %f' % B.run())
    assert A.run() > B.run()


# def test_efficiency_group():
#     iterations = 1
#     # partial = npci.group(text)
#     # computed = npac.generate(partial, text)
#     A = Time('''
# import nlp.processing.corpus.identity as npci
# text="test string"
#              ''',
#              '''npci.group(text)''', iterations)
#     B = Time('''
# import nlp.processing.corpus.identity as npci
# text="test string "*500
#              ''',
#              '''npci.group(text)''', iterations)
#
#     print('A: %f' % A.run())
#     print('B: %f' % B.run())
#     assert A.run() < B.run()
#     assert B.run() < 3
