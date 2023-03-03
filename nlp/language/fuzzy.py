# This is a method of fuzzily assigning the 'meaning' (read: definition)
# of words based on their context.

import nlp.processing.corpus.identity as npci
import nlp.processing.filters as npf
import nlp.processing.appraisal.dictionary as npad
from nlp.language import constants
import nltk


def posTag(statement, word=None, whole=False):
    '''
    IN: statement, list(str), a list of words within context
    IN: word, str, if statement is more than one word, return the POS for
                   this word
    IN: whole, bool, whether all of the word's POS tags shoud be returned

    OUT: if whole:
        pos_tags, list(tuple(str)), a list of words paired with their pos
    OUT: if not whole:
        pos_tags, str, the tag for the provided word
    '''

    if whole:
        return nltk.pos_tag(statement)
    tags = nltk.pos_tag(statement)
    if word:
        for pair in tags:
            if pair[0] == word:
                return pair[1]
    return tags[0][1]


def checkBasePower(pos):
    '''
    IN: word, str, pos
    OUT: int, base power of word
    '''
    return constants.BASE_POWER[pos]


def checkSenses(word, remote=False):
    '''
    IN: word, str
    OUT: int, # of sense/definitions
    '''
    if remote:
        return npad.DICTIONARY.numberOfSenses(word)
    return 0


def getFuzzyMeaning(word_groups, context, frequency, total,
                    sanitizer=npf.lowercase, remote=False):
    '''
    IN: word_groups, processing.corpus.identity.group(text)
    IN: context, processing.corpus.identity.generate(1, text)
    IN: frequency, processing.corpus.representativeness.occurences(text)[word]
    IN: total, processing.corpus.representativeness.totalcount(tokens)
    '''
    # TODO: optimize sanitation
    (keyness, base, amplify, damp) = assignKeyness(context, frequency,
                                                   total, normal=False,
                                                   remote=remote)
    keyness_confidence = keynessConfidence(keyness, base, amplify, damp)

    real_words = {}
    fuzzy_meaning = {}

    for word, conx in context.items():
        word = sanitizer(word)
        real_words[word] = sorted([w for w in npci.getWords(conx)])
        real_words[word] = npf.sortabasedonb(npf.combineLikeValues(
            [[keyness[sanitizer(inst)] for inst in real_words[word]],
             [sanitizer(w) for w in real_words[word]]]
        ))

    for word, conx in context.items():
        word = sanitizer(word)
        if word in fuzzy_meaning.keys():
            fuzzy_meaning[word] = fuzzy_meaning[word] + (real_words[word],
                                                         conx)
        else:
            fuzzy_meaning[word] = (real_words[word], conx)

    return fuzzy_meaning, keyness_confidence


def assignKeyness(context, frequency, total, normal=False,
                  sanitizer=npf.lowercase, remote=False):
    '''
    IN: context, dict(list)
    IN: frequency, dict(float)
    IN: total, float
    IN: normal, bool
    OUT: dict(float), key of each word
    OUT: list(float), list of all base powers (for normalization)
    OUT: list(float), ""          amplifiers   ""
    OUT: list(float), ""          dampers      ""
    '''
    keyness = {}
    base_powers = {}
    amplifiers = {}
    dampers = {}

    for i, word in enumerate(context.keys()):
        word = sanitizer(word)
        (kn, bp, am, da) = getExplicitMeaning(word, frequency[word],
                                              total, keynessFuzziness,
                                              remote=remote)
        keyness[word] = kn
        base_powers[word] = bp
        amplifiers[word] = am
        dampers[word] = da

    if normal:
        normalizer = max(max([i for i in keyness.values()]), 0)
        for word in keyness.keys():
            keyness[word] = keyness[word]/normalizer

    return keyness, base_powers, amplifiers, dampers


def getExplicitMeaning(word, frequency, total, fuzzification, remote=False):
    '''
    IN: word, str (to look up definitions)
    IN: frequency, float, # of occurences
    IN: total, float, total # of words
    IN: fuzzification, func, function to fuzzify numbers
    '''
    # TODO: base power should pos tag based on statement, not just word
    base_power = checkBasePower(posTag([word]))
    amplifier = frequency
    damper = checkSenses(word, remote=remote)

    return fuzzification(base_power, amplifier, damper, total), \
        base_power, amplifier, damper


def keynessFuzziness(m, a, d, n):
    '''
    IN: m, float, Word category (Function vs. Context. vs. Unique)
    IN: a, float, Frequency of use
    IN: d, float, Total number of possible meanings (definite + indefinite)
        ALSO, the number of 'senses'
    IN: n, int, number of words
    OUT: individual value (or power) of word
    '''
    return m * ((a + d) / n)


def keynessConfidence(keyness, bases, freqs, senses):
    '''
    IN: keyness, float, a measure of importance for a word
    IN: freq_max, float, for normalization
    IN: sense_max, float, for normalization
    OUT: float, confidence in that measure
    '''
    confidence = {}
    freq_max = max(max(freqs.values()), 1)
    sense_max = max(max(senses.values()), 1)

    for key, n in keyness.items():
        # Normalize values
        # base only has max of 5
        # frequency normalized by most frequent word
        # senses normalized by word with most senses
        base, bc = fuzzymath(bases[key]/5)
        frequency, fc = fuzzymath(freqs[key]/freq_max)
        sense, sc = fuzzymath(senses[key]/sense_max)

        temp_confidence = []
        check = (lambda x: temp_confidence.append(x) if x is not None else 0)
        check(evaluaterules(frequency, base, sense))
        check(evaluaterules(frequency, base, sc))
        check(evaluaterules(frequency, bc, sense))
        check(evaluaterules(frequency, bc, sc))
        check(evaluaterules(fc, base, sense))
        check(evaluaterules(fc, base, sc))
        check(evaluaterules(fc, bc, sense))
        check(evaluaterules(fc, bc, sc))

        confidence[key] = sum([i[0]*i[1] for i in temp_confidence]) \
            / len(temp_confidence)

    return confidence


def fuzzymath(x):
    '''
    IN: x, float, a value to plot on fuzzy graph
    OUT: ((str, float), (str, float)), a tuple of fuzzy groups
    '''
    # TODO: optimize code
    a = constants.FUZZY_KEYNESS_CONFIDENCE[0]
    b = constants.FUZZY_KEYNESS_CONFIDENCE[1]
    c = constants.FUZZY_KEYNESS_CONFIDENCE[2]
    d = constants.FUZZY_KEYNESS_CONFIDENCE[3]

    if x <= a:
        return (constants.FUZZY_LOW, 1), (None)
    if x >= b and x <= c:
        return (constants.FUZZY_MED, 1), (None)
    if x >= d:
        return (constants.FUZZY_HIG, 1), (None)

    slope = 1/(b-a)
    if x > a and x < b:
        return (constants.FUZZY_LOW, slope*(x-b)), \
                (constants.FUZZY_MED, slope*(x-a))

    slope = 1/(d-c)
    if x > c and x < d:
        return (constants.FUZZY_MED, slope*(x-b)), \
                (constants.FUZZY_HIG, slope*(x-a))


def evaluaterules(f, b, s):
    '''
    IN: f, tuple(str, float), fuzzy metric
    IN: b, tuple(str, float), fuzzy metric
    IN: s, tuple(str, float), fuzzy metric
    OUT: tuple(str, float), confidence semantics, confidence value
    '''

    if f is not None and b is not None and s is not None:

        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_CR], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_NT], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_LC], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EN], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_VU], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_NT], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EX], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EW], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_LOW and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return ((constants.CONFIDENCES[constants.FUZZY_CR]+constants.CONFIDENCES[constants.FUZZY_EN])/2, (f[1]+b[1]+s[1])/3)  # NOQA  E501

        # ---------------------------------------------------------------------------

        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EN], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_VU], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_NT], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_CR], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EN], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_VU], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EX], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EW], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_MED and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_CR], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        # ---------------------------------------------------------------------------

        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EN], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_VU], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_LOW and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_NT], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EW], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_CR], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_MED and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EN], (f[1]+b[1]+s[1])/3)  # NOQA  E501

        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_LOW:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EX], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_MED:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_EW], (f[1]+b[1]+s[1])/3)  # NOQA  E501
        if f[0] == constants.FUZZY_HIG and b[0] == constants.FUZZY_HIG and s[0] == constants.FUZZY_HIG:  # NOQA  E501
            return (constants.CONFIDENCES[constants.FUZZY_CR], (f[1]+b[1]+s[1])/3)  # NOQA  E501
