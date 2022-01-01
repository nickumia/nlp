
import nlp.processing.inputs as npi
import nlp.processing.interaction.text as npit
import nlp.natural.chakras.chandni as nncc


def test_chandni(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")

    text = npit.load_plain_text('/pac/tests/natural/example.txt')
    assert text[0:10] == 'Perhaps on'
    assert text[-10:] == 'P Quest...'

    A = nncc.Chandni(text)
    B = npi.BasicText(text)
