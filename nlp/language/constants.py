# See docs/language/word_categories for more info

DT = 'DT'
EX = 'EX'
IN = 'IN'
IS = 'IS'
RP = 'RP'
TO = 'TO'

POS = 'POS'
PRP = 'PRP'
PRPs = 'PRP$'
CD = 'CD'
JJ = 'JJ'
NN = 'NN'
NNS = 'NNS'
RB = 'RB'
VB = 'VB'
VBD = 'VBD'
VBG = 'VBG'
VBN = 'VBN'
VBP = 'VBP'
VBZ = 'VBZ'
CC = 'CC'
JJR = 'JJR'
JJS = 'JJS'
MD = 'MD'
PDT = 'PDT'
RBR = 'RBR'
RBS = 'RBS'

FW = 'FW'
NNP = 'NNP'
NNPS = 'NNPS'
UH = 'UH'
WDT = 'WDT'
WP = 'WP'
WPs = 'WP$'
WRB = 'WRB'

BASE_POWER = {}

# Function Words
FUNCTION_WORDS = [DT, EX, IN, IS, RP, TO]
BASE_POWER.update(dict.fromkeys(FUNCTION_WORDS, 1))

# Content Words
CONTENT_WORDS_1 = [POS, PRP, PRPs]
CONTENT_WORDS_2 = [CD, JJ, NN, NNS, RB, VB, VBD, VBG, VBN, VBP, VBZ]
CONTENT_WORDS_3 = [CC, JJR, JJS, MD, PDT, RBR, RBS]
CONTENT_WORDS = [POS, PRP, PRPs, CD, JJ, NN, NNS, RB, VB, VBD, VBG, VBN, VBP,
                 VBZ, JJR, JJS, MD, PDT, RBR, RBS]
BASE_POWER.update(dict.fromkeys(CONTENT_WORDS_1, 2.2))
BASE_POWER.update(dict.fromkeys(CONTENT_WORDS_2, 3))
BASE_POWER.update(dict.fromkeys(CONTENT_WORDS_3, 3.8))

# Unique Words
UNIQUE_WORDS = [FW, NNP, NNPS, UH, WDT, WP, WPs, WRB]
BASE_POWER.update(dict.fromkeys(UNIQUE_WORDS, 5))


# Fuzzy params
FUZZY_LOW = "low"
FUZZY_MED = "med"
FUZZY_HIG = "high"

FUZZY_EX = "extreme"
FUZZY_EW = "extra"
FUZZY_CR = "critical"
FUZZY_EN = "enduring"
FUZZY_VU = "vulnerable"
FUZZY_NT = "not_timely"
FUZZY_LC = "least_concern"

FUZZY_KEYNESS_CONFIDENCE = [0.1, 0.3, 0.4, 0.7]
CONFIDENCES = {
    FUZZY_LC: 7.14,
    FUZZY_NT: 21.43,
    FUZZY_VU: 35.71,
    FUZZY_EN: 50.00,
    FUZZY_CR: 64.29,
    FUZZY_EW: 78.57,
    FUZZY_EX: 92.86
}
