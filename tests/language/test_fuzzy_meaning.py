
import botocore

from nlp.processing.inputs import BasicText
import nlp.language.fuzzy as nlf
from nlp.processing.corpus.representativeness import occurences, totalCount
import nlp.processing.corpus.identity as npci
import nlp.processing.appraisal.dictionary as npad


npci.ABBREVIATION_LENGTH = 2


def test_basictext_init():
    text = BasicText('A very very simple exam.')

    meanings, confidence = nlf.getFuzzyMeaning(text.groups,
                                               text.contexts,
                                               occurences(text.words),
                                               totalCount(text.words))
    # This is the test case where there is no knowledge of word definitions
    assert meanings['exam'][0][0][0] == 0.2
    assert meanings['exam'][0][0][1] == 0.6000000000000001
    assert meanings['exam'][0][0][2] == 0.6000000000000001
    assert meanings['exam'][0][0][3] == 2.4000000000000004
    assert meanings['exam'][0][1] == ['a', 'exam', 'simple', 'very']
    assert meanings['exam'][1] == [('A very very simple exam.',
                                    'sentences_only', 0)]
    assert int(confidence['exam']) == 92
    assert int(confidence['very']) == 96


def test_basictext_init_lookup():
    text = BasicText('A very very simple exam.')
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except (FileNotFoundError, botocore.exceptions.ClientError):
        npad.DICTIONARY.prepopulate(text.words)
    npad.DICTIONARY.backup('dictionary.dump')

    meanings, confidence = nlf.getFuzzyMeaning(text.groups,
                                               text.contexts,
                                               occurences(text.words),
                                               totalCount(text.words),
                                               remote=True)
    # These vary based on definition lookup
    # The values should be lower than w/o definitions because the
    # definitions add uncertainty
    assert meanings['exam'][0][0][0] > 0.2
    assert meanings['exam'][0][0][1] > 0.6
    assert meanings['exam'][0][0][2] > 0.6
    assert meanings['exam'][0][0][3] > 2.4
    assert meanings['exam'][0][1] == ['a', 'exam', 'simple', 'very']
    assert meanings['exam'][1] == [('A very very simple exam.',
                                    'sentences_only', 0)]
    assert int(confidence['exam']) < 92
    assert int(confidence['very']) < 96
