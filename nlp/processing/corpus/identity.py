
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
