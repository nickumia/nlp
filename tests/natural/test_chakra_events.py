
from nlp.processing.inputs import BasicText
from nlp.processing.corpus.representativeness import occurences, totalCount
import nlp.language.fuzzy as nlf
import nlp.natural.chakras as nnc
import nlp.natural.chakra_event as nne


def test_influence_basic():
    a = nnc.make_body()
    text = BasicText('A very very simple exam.')

    meanings, confidence = nlf.getFuzzyMeaning(text.groups,
                                               text.contexts,
                                               occurences(text.words),
                                               totalCount(text.words))

    nne.determineInfluence(a, meanings, confidence)
    # TODO: Finish this test
