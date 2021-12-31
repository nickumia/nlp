
from nlp.processing.inputs import BasicText
import nlp.language.fuzzy as nlf
from nlp.processing.corpus.representativeness import occurences, totalCount
import nlp.processing.corpus.identity as npci


npci.ABBREVIATION_LENGTH = 2


def test_basictext_init():
    text = BasicText('Grass is green.  Green is a nice color.  Green makes '
                     'me happy!  But colorless green ideas sleep furiously.')

    wmeaning, confidence = nlf.getFuzzyMeaning(text.groups,
                                               text.contexts,
                                               occurences(text.words),
                                               totalCount(text.words))
    print(wmeaning)
    print(confidence)
