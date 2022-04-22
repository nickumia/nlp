
import nlp.processing.corpus.identity as npci
import nlp.language.fuzzy as nlf


def test_postag_single():
    word = ["What"]

    tag = nlf.posTag(word)

    assert tag == 'WP'


def test_postag_multi():
    sentence = "What should I write about"
    words = npci.group(sentence, specific=npci.char_word)

    tags = nlf.posTag(words, whole=True)

    assert tags == [('What', 'WP'), ('should', 'MD'), ('I', 'PRP'),
                    ('write', 'VB'), ('about', 'IN')]
