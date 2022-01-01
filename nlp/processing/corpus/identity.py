
import re

global ABBREVIATION_LENGTH, NUMBER_CONTEXT

ABBREVIATION_LENGTH = 3
NUMBER_CONTEXT = 2

WORDS = "alpha_char_only"
QUOTES = "quotes_only"
SENTENCES = "sentences_only"
QUESTIONS = "questions_only"
EXCLAMATIONS = "exclamation_only"
ENCLOSURES = "paren_brack_curly_only"
ABBREVIATIONS = "possible_abbreviations_only"
NUMBERS = "numbers_only"
NUMBERS_WITH_EXPRESSION = "numbers_with_referring_expression"

char_word = r'(\b([a-z]+[\_\&\@\.\%\^\*\-\+\']?[0-9]?)+([a-z]{1,})?\b)'
char_quote = r'(\".*\")'
char_sentence = r'(\b([a-z]\s?(@|&|#|"|,)?\s?\.?)+\."?)'
char_question = r'(\b(((?!=|\?|\.|\!).(\".*\")?)+)(\?)+)'
char_exclamation = r'(\b(((?!=|\?|\.|\!).(\".*\")?)+)(\!)+)'
char_enclosure = r'(\(((?!=|\)).)*\))|(\{((?!=|\}).)*\})|(\[((?!=|\]).)*\])'  # NOQA
char_abbreviation = r'(\b[a-z]{2,%d}\.|\s[a-z]{2,%d}\.\s)' % (ABBREVIATION_LENGTH,ABBREVIATION_LENGTH)  # NOQA
char_number = r'\b[0-9]{1,}'
char_number_with_expression = r'(\b[0-9]((,?\s?x?\s?:?[0-9])+)?((\s?[a-z]+){0,%d})?)' % NUMBER_CONTEXT  # NOQA
tag_opening = r'\<(?!=|\/)[a-z]+\-?[a-z]+[0-9]*\>'
tag_closing = r'\<\/[a-z]+\-?[a-z]+[0-9]*\>'
long_date = r'[a-z]+ ?[0-9]+, ?[0-9]{4}'

GROUP_NAMES = [WORDS, QUOTES, SENTENCES, QUESTIONS, EXCLAMATIONS,
               ENCLOSURES, ABBREVIATIONS, NUMBERS, NUMBERS_WITH_EXPRESSION]
GROUP_SEQUENCES = [char_word, char_quote, char_sentence, char_question,
                   char_exclamation, char_enclosure, char_abbreviation,
                   char_number, char_number_with_expression]


def getWords(contexts):
    '''
    IN: contexts, group(text)
    OUT: list(words)
    '''
    words = []
    for context in contexts:
        matches = re.findall(char_word, context[0], flags=re.I | re.M | re.U)
        if matches != []:
            if type(matches[0]) == tuple:
                words += [i[0] for i in matches]
            else:
                words += matches

    return words


def group(body, sanitizer=(lambda x: x)):
    ''''
    IN: body: str, a single string representing the entire input
    OUT: group_map: dict(re.match), a dictionary of matches per group
    '''
    group_map = {}

    for i, party in enumerate(GROUP_SEQUENCES):
        matches = re.findall(party, body, flags=re.I | re.M | re.U)
        if matches != []:
            if type(matches[0]) == tuple:
                group_map[GROUP_NAMES[i]] = [sanitizer(i[0]) for i in matches]
            else:
                group_map[GROUP_NAMES[i]] = sanitizer(matches)

    return group_map


def checkNGrams(n, text, word, pattern=[]):
    '''
    IN: n, int, number of grams before/after word
    IN: text, list(str), context
    IN: word, str, word of interest
    IN: pattern, list(str), negative-like words
    OUT: recursively try to identify context of pattern
    '''
    # TODO: Optimize this
    relevant = 0
    for i, t in enumerate(text):
        if word == t:
            relevant = i

    lowest = (lambda x: x-n if x > n else 0)
    highest = (lambda y: y+n if y+n < len(text) else len(text)-1)

    if lowest(relevant) == highest(relevant):
        return 0
    if len(text[lowest(relevant):highest(relevant)]) == 1:
        if text[lowest(relevant):highest(relevant)][0] in pattern:
            return 1
        else:
            return 0

    if text[lowest(relevant)] in pattern:
        return 1 + checkNGrams(n-1, text[1:], word, pattern)
    if text[highest(relevant)] in pattern:
        # TODO: test this
        return ((2*n+1-i)/(2*n+1)) + \
                checkNGrams(n-1, text[lowest(i):i] + text[i+1:], word, pattern)
    return checkNGrams(n-1, text, word, pattern)
