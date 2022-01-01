
from nlp.processing.inputs import BasicText
from nlp.processing.filters import sanitize
from nlp.processing.corpus.representativeness import occurences
import nlp.processing.corpus.identity as npci
import nlp.processing.appraisal.basic_text as npac


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
                                        ' get higher than Mt.', 'Everest.',
                                        'the world may never know") (..']
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


def test_context_generation():
    text = sanitize('Grass is green.  Green is a nice color.  Green makes '
                    'me happy!  But colorless green ideas sleep furiously.')

    partial = npci.group(text)
    computed = npac.generate(partial, text)

    assert computed['grass'] == [('grass is green.', npci.SENTENCES, 0)]
    assert computed['green'] == [
        ('grass is green.', npci.SENTENCES, 0),
        ('green is a nice color.', npci.SENTENCES, 17),
        ('but colorless green ideas sleep furiously.', npci.SENTENCES, 64),
        ('green makes me happy!', npci.EXCLAMATIONS, 41)]


def test_checkNgrams_before():
    text = ['this', 'is', 'not', 'a', 'negative', 'statement']
    text2 = ['this', 'is', 'a', 'positive', 'statement']
    text3 = ['this', 'is', 'truly', 'a', 'negative', 'statement']
    negative = ['not', 'negative']

    assert npci.checkNGrams(3, text2, 'statement', pattern=negative) == 0
    assert npci.checkNGrams(3, text3, 'statement', pattern=negative) == 1
    assert npci.checkNGrams(3, text, 'statement', pattern=negative) == 2


def test_checkNgrams_full():
    negative = ['not', 'negative']
    text4 = ['this', 'is', 'a', 'sentence', 'with', 'some', 'paddinging',
             'surrounding', 'the', 'negative', 'word', 'because', 'we',
             'need', 'to', 'test', 'before', 'and', 'after']

    assert npci.checkNGrams(3, text4, 'word', pattern=negative) == 1
    assert npci.checkNGrams(3, text4, 'statement', pattern=negative) == 0


def test_checkNgrams_empty_pattern():
    text = ['this', 'is', 'truly', 'a', 'negative', 'statement']

    assert npci.checkNGrams(3, text, 'word') == 0
