# This is a method of fuzzily assigning the 'meaning' (read: definition)
# of words based on their context.

from nlp.language import constants
import nltk


def posTag(statement):
    '''
    IN: statement, list(str), a list of words within context
    OUT: pos_tags, list(tuple(str)), a list of words paired with their pos
    '''
    return nltk.pos_tag(statement)


def checkBasePower(word):
    '''
    IN: word, tuple, (word, pos)
    OUT: int, base power of word
    '''
    return constants.BASE_POWER[word[1]]


def fuzzifykeyness(m, a, d, n):
    '''
    IN: m, float, Word category (Function vs. Context. vs. Unique)
    IN: a, float, Frequency of use
    IN: d, float, Total number of possible meanings (definite + indefinite)
        ALSO, the number of 'senses'
    IN: n, int, number of words
    OUT: individual value (or power) of word
    '''
    return m * ((a + d) / n)
