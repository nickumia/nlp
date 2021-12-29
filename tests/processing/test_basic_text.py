
from nlp.processing.inputs import BasicText
from nlp.processing.corpus.representativeness import occurences
import nlp.processing.corpus.identity as npci


npci.ABBREVIATION_LENGTH = 2


def test_basictext_init():
    text = BasicText('this is an interesting string')

    assert text.getWords() == ['this', 'is', 'an', 'interesting',
                               'string']


def test_occurences():
    text = BasicText('this string is the more interesting string')
    computed = occurences(text.getWords())

    assert computed == {'this': 1, 'string': 2, 'the': 1, 'is': 1, 'more': 1,
                        'interesting': 1}


def test_group_all():
    text = ('Mr. Shark went to an M&M party to get higher than Mt. Everest.  '
            'He was 9 ft tall, but felt taller than 90 million miles on '
            'April 10, 2014!  Who was with him?  ("the world may never know")'
            ' (..or will they?)')

    computed = npci.group(text)

    assert computed[npci.WORDS] == ['Mr', 'Shark', 'went', 'to', 'an', 'M&M',
                                    'party', 'to', 'get', 'higher', 'than',
                                    'Mt', 'Everest', 'He', 'was', 'ft',
                                    'tall', 'but', 'felt', 'taller', 'than',
                                    'million', 'miles', 'on', 'April', 'Who',
                                    'was', 'with', 'him', 'the', 'world',
                                    'may', 'never', 'know', 'or', 'will',
                                    'they']
    assert computed[npci.QUOTES] == ['"the world may never know"']
    assert computed[npci.SENTENCES] == ['Mr.', 'Shark went to an M&M party to'
                                        ' get higher than Mt.', 'Everest.']
    assert computed[npci.EXCLAMATIONS] == ['He was 9 ft tall, but felt taller'
                                           ' than 90 million miles on April '
                                           '10, 2014!']

    assert computed[npci.ENCLOSURES] == ['("the world may never know")',
                                         '(..or will they?)']
    assert computed[npci.ABBREVIATIONS] == ['Mr.', ' Mt. ']
    assert computed[npci.NUMBERS] == ['9', '90', '10', '2014']
    assert computed[npci.NUMBERS_WITH_EXPRESSION] == ['9 ft tall',
                                                      '90 million miles',
                                                      '10, 2014']
