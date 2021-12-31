
from nlp.processing.inputs import BasicText
import nlp.language.fuzzy as nlf
from nlp.processing.corpus.representativeness import occurences, totalCount
import nlp.processing.corpus.identity as npci


npci.ABBREVIATION_LENGTH = 2


def test_basictext_init():
    text = BasicText('A very very simple exam.')

    meanings, confidence = nlf.getFuzzyMeaning(text.groups,
                                               text.contexts,
                                               occurences(text.words),
                                               totalCount(text.words))
    # This is subject to change when definition lookups are enabled
    assert meanings['exam'][0][0][0] == 0.2
    assert meanings['exam'][0][0][1] == 0.6000000000000001
    assert meanings['exam'][0][0][2] == 0.6000000000000001
    assert meanings['exam'][0][0][3] == 2.4000000000000004
    assert meanings['exam'][0][1] == ['A', 'exam', 'simple', 'very']
    assert meanings['exam'][1] == [('A very very simple exam.',
                                    'sentences_only',0)]
    assert int(confidence['exam']) == 92
    assert int(confidence['very']) == 96
