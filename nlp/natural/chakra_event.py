# Event modeling support functions

import math
import nlp.processing.corpus.identity as npci
import nlp.natural.chakras as nnc


def determineInfluence(model, meanings, confidence, learn=False):
    '''
    IN: meanings, language.fuzzy.getFuzzyMeaning
    IN: confidence rating, language.fuzzy.keynessConfidence
    OUT: chakra influence
    '''
    plevel = 0; ptotal = 0  # NOQA E702
    nlevel = 0; ntotal = 0  # NOQA E702
    qlevel = 0; qtotal = 0  # NOQA E702

    negative_meaning = inverseInfluence(meanings)
    is_negative = (lambda word: negative_meaning[word]
                   if word in negative_meaning.keys() else 1)

    for i, word in enumerate(meanings.keys()):
        meaning = meanings[word]
        for chakra in nnc.CHAKRA_SPEC:
            for j, sense in enumerate(meaning[0][1]):
                if chakra not in [nnc.CONFIDENCE, nnc.POWER_LEVEL]:
                    if chakra == nnc.INVERSE_CHAKRA:
                        for negate in model.CHAKRA_INFLUENCE[chakra]:
                            for chak in model.CHAKRAS[model.P_CHAKRA].keys():
                                if negate in sense:
                                    model.EVENT_WORDS[sense] = True
                                    model.recover(chak, nnc.infuse(
                                        meaning[0][0][i]*is_negative(sense),
                                        confidence[sense]))
                                    ptotal += sum(meaning[0][0])
                                    plevel += nnc.infuse(sum(meaning[0][0]),
                                                         confidence[sense])
                    else:
                        if sense in model.CHAKRA_INFLUENCE[chakra]:
                            model.EVENT_WORDS[sense] = True
                            model.recover(chakra, nnc.infuse(
                                meaning[0][0][i]*is_negative(sense),
                                confidence[sense]), single=model.P_CHAKRA)
                            ptotal += sum(meaning[0][0])
                            plevel += nnc.infuse(sum(meaning[0][0]),
                                                 confidence[sense])
                        elif sense in model.CHAKRA_NONINFLUENCE[chakra]:
                            model.EVENT_WORDS[sense] = True
                            model.recover(chakra, nnc.infuse(
                                meaning[0][0][i]*is_negative(sense),
                                confidence[sense]), single=model.Q_CHAKRA)
                            qtotal += sum(meaning[0][0])
                            qlevel += nnc.infuse(sum(meaning[0][0]),
                                                 confidence[sense])
                        else:
                            if learn:
                                a = input(("Does " + sense + " influence "
                                           "" + chakra + "\n\n?"))
                                if a == 'y':
                                    model.CHAKRA_INFLUENCE[chakra] += sense
                                else:
                                    model.CHAKRA_NONINFLUENCE[chakra] += sense
                            else:
                                model.EVENT_WORDS[sense] = False
                else:
                    model.CHAKRAS[model.P_CHAKRA][chakra] += plevel
                    model.CHAKRAS[model.N_CHAKRA][chakra] += nlevel
                    model.CHAKRAS[model.Q_CHAKRA][chakra] += qlevel
                    plevel = 0
                    nlevel = 0
                    qlevel = 0

    if ptotal != 0:
        model.CHAKRAS[model.P_CHAKRA][nnc.CONFIDENCE] /= ptotal
    if ntotal != 0:
        model.CHAKRAS[model.N_CHAKRA][nnc.CONFIDENCE] /= ntotal
    if qtotal != 0:
        model.CHAKRAS[model.Q_CHAKRA][nnc.CONFIDENCE] /= qtotal

    model.CHAKRAS[model.P_CHAKRA][nnc.POWER_LEVEL] = model.addPower()
    model.CHAKRAS[model.N_CHAKRA][nnc.POWER_LEVEL] = \
        model.addPower(version=model.N_CHAKRA)
    model.CHAKRAS[model.Q_CHAKRA][nnc.POWER_LEVEL] = \
        model.addPower(version=model.Q_CHAKRA)

    return 0


def inverseInfluence(meaning):
    '''
    IN: meaning, one instance
    OUT: is the influence inversely affected?
    '''
    ngram = {}
    for word, sense in meaning.items():
        instances = npci.checkNGrams(3, sense[0][1], word)
        ngram[word] = math.pow(-1, instances)

    return ngram
