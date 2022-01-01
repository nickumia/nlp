
import nlp.processing.inputs as npi
import nlp.processing.interaction.text as npit
from nlp.processing.corpus.representativeness import occurences, totalCount
import nlp.language.fuzzy as nlf
import nlp.natural.chakras.chandni as nncc


def test_chandni_basic(monkeypatch):
    ''' Test that code is functional '''
    monkeypatch.setattr('builtins.input', lambda _: "y")

    text = npit.load_plain_text('/pac/tests/natural/example.txt')
    assert text[0:10] == 'Perhaps on'
    assert text[-10:] == 'P Quest...'

    A = nncc.Chandni(text)
    B = npi.BasicText(text)
    meanings, confidence = nlf.getFuzzyMeaning(B.groups,
                                               B.contexts,
                                               occurences(B.words),
                                               totalCount(B.words))
    A.train(meanings, confidence, "test 1")
    assert A.match == 1
