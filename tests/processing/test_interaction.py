
import nlp.processing.interaction.text as npit


def test_terminal_yes_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    a = npit.terminal_yes_no("Is this true?")
    assert a

    monkeypatch.setattr('builtins.input', lambda _: "a")
    b = npit.terminal_yes_no("Is this true?")
    assert b is False
