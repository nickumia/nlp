# See docs/language/word_categories for more info

DT = 'Determiners'
EX = 'Existential'
IN = 'Subordinating preposition or conjunction'
IS = 'List item marker'
RP = 'Particle'
TO = 'To'

POS = 'Possesiveness'
PRP = 'Personal Pronoun'
PRPs = 'Possesive Pronoun'
CD = 'Cardinal numeral'
JJ = 'Ordinal adjective or numeral'
NN = 'Common noun'
NNS = 'Plural common noun'
RB = 'Adverb'
VB = 'Base Verb'
VBD = 'Past Tense Verb'
VBG = 'Gerund Verb'
VBN = 'Past participle verb'
VBP = 'Present tense verb'
VBZ = 'Third person verb'
CC = 'Coordinating conjunction'
JJR = 'Comparative adjective'
JJS = 'Superlative adjective'
MD = 'Modal auxilary'
PDT = 'Pre-determiner'
RBR = 'Comparative adverb'
RBS = 'Superlative adverb'

FW = 'Foreign word'
NNP = 'Proper noun'
NNPS = 'Plural proper noun'
UH = 'Interjection'
WDT = 'WH-determiner'
WP = 'WH-pronoun'
WPs = 'WH-possesive'
WRB = 'WH-adverb'

FUNCTION_WORDS = dict.fromkeys([DT, EX, IN, IS, RP, TO], 1)
CONTENT_WORDS = dict.fromkeys([POS, PRP, PRPs], 2.2)
CONTENT_WORDS.update(dict.fromkeys(
    [CD, JJ, NN, NNS, RB, VB, VBD, VBG, VBN, VBP, VBZ], 3))
CONTENT_WORDS.update(dict.fromkeys([CC, JJR, JJS, MD, PDT, RBR, RBS], 3.8))
UNIQUE_WORDS = dict.fromkeys([FW, NNP, NNPS, UH, WDT, WP, WPs, WRB], 5)
