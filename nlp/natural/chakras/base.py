# Chakra control

import nlp.processing.stats as nps

# # Chakras
EARTH = "earth_chakra"
WATER = "water_chakra"
FIRE = "fire_chakra"
HEART = "heart_chakra"
SOUND = "sound_chakra"
LIGHT = "light_chakra"
COSMIC = "thought_chakra"
INVERSE_CHAKRA = "negation_chakra"
CONFIDENCE = "confidence_level"
POWER_LEVEL = "chakra_level"

CHAKRA_SPEC = [EARTH, WATER, FIRE, HEART, SOUND, LIGHT, COSMIC,
               INVERSE_CHAKRA, CONFIDENCE, POWER_LEVEL]
CHAKRA_ONLY = [EARTH, WATER, FIRE, HEART, SOUND, LIGHT, COSMIC]

INTERNAL = "internal"
EXTERNAL = "external"


class Chakras():
    def __init__(self):
        self.P_CHAKRA = 'positive chakra'
        self.N_CHAKRA = 'negative chakra'
        self.Q_CHAKRA = 'change chakra'

        self.CHAKRAS = {
            self.P_CHAKRA: dict.fromkeys(CHAKRA_SPEC, 0),
            self.N_CHAKRA: dict.fromkeys(CHAKRA_SPEC, 0),
            self.Q_CHAKRA: dict.fromkeys(CHAKRA_SPEC, 0)
        }

        self.STATES = {
            self.P_CHAKRA: dict.fromkeys(CHAKRA_ONLY, True),
            self.N_CHAKRA: dict.fromkeys(CHAKRA_ONLY, True),
            self.Q_CHAKRA: dict.fromkeys(CHAKRA_ONLY, True)
        }

        self.CHAKRA_INFLUENCE = dict.fromkeys(CHAKRA_ONLY, [])
        self.CHAKRA_INFLUENCE[INVERSE_CHAKRA] = []
        self.CHAKRA_NONINFLUENCE = dict.fromkeys(CHAKRA_ONLY, [])
        self.CHAKRA_NONINFLUENCE[INVERSE_CHAKRA] = []

        self.CHAKRA_TEST_HISTORY = {}
        self.CHAKRA_TRAIN_HISTORY = {}
        self.EVENT_WORDS = {}

    def addPower(self, version=None):
        if version is None:
            return sum([self.CHAKRAS[self.P_CHAKRA][EARTH],
                       self.CHAKRAS[self.P_CHAKRA][WATER],
                       self.CHAKRAS[self.P_CHAKRA][FIRE],
                       self.CHAKRAS[self.P_CHAKRA][HEART],
                       self.CHAKRAS[self.P_CHAKRA][SOUND],
                       self.CHAKRAS[self.P_CHAKRA][LIGHT],
                       self.CHAKRAS[self.P_CHAKRA][COSMIC]])
        if version in [self.P_CHAKRA, self.N_CHAKRA, self.Q_CHAKRA]:
            return sum([self.CHAKRAS[version][EARTH],
                       self.CHAKRAS[version][WATER],
                       self.CHAKRAS[version][FIRE],
                       self.CHAKRAS[version][HEART],
                       self.CHAKRAS[version][SOUND],
                       self.CHAKRAS[version][LIGHT],
                       self.CHAKRAS[version][COSMIC]])
        return 0

    def reset(self):
        self.P_CHAKRA = dict.fromkeys(CHAKRA_SPEC, 0)
        self.N_CHAKRA = dict.fromkeys(CHAKRA_SPEC, 0)
        self.Q_CHAKRA = dict.fromkeys(CHAKRA_SPEC, 0)

        self.P_STATE = dict.fromkeys(CHAKRA_ONLY, True)
        self.N_STATE = dict.fromkeys(CHAKRA_ONLY, True)
        self.Q_STATE = dict.fromkeys(CHAKRA_ONLY, True)

        self.CHAKRA_INFLUENCE = dict.fromkeys(CHAKRA_ONLY, [])
        self.CHAKRA_INFLUENCE[INVERSE_CHAKRA] = []
        self.CHAKRA_NONINFLUENCE = dict.fromkeys(CHAKRA_ONLY, [])
        self.CHAKRA_NONINFLUENCE[INVERSE_CHAKRA] = []

    def disturb(self, chakra, value, single=None):
        if single is None:
            for part in self.STATES.keys():
                if self.STATES[part][chakra]:
                    self.CHAKRAS[part][chakra] -= value
        else:
            if self.STATES[single][chakra]:
                self.CHAKRAS[single][chakra] -= value

    def recover(self, chakra, value, single=None):
        if single is None:
            for part in self.STATES.keys():
                if self.STATES[part][chakra]:
                    self.CHAKRAS[part][chakra] += value
        else:
            if self.STATES[single][chakra]:
                self.CHAKRAS[single][chakra] += value

    def balance(self, chakra, single=None):
        if single is None:
            for part in self.CHAKRAS.keys():
                if self.STATES[part][chakra]:
                    self.CHAKRAS[part][chakra] = 0.0
        else:
            if self.STATES[single][chakra]:
                self.CHAKRAS[single][chakra] = 0.0

    def block(self, chakra, single=None):
        if single is None:
            for part in self.STATES.keys():
                if self.STATES[part][chakra]:
                    self.STATES[part][chakra] = False
        else:
            if self.STATES[single][chakra]:
                self.STATES[single][chakra] = False

    def unblock(self, chakra, single=None):
        if single is None:
            for part in self.STATES.keys():
                if not self.STATES[part][chakra]:
                    self.STATES[part][chakra] = True
        else:
            if not self.STATES[single][chakra]:
                self.STATES[single][chakra] = True

    def chakraDistribution(self, chakra):
        new = {}
        anti_chakra = []
        for chak, val in self.CHAKRAS[chakra].items():
            if chak in CHAKRA_ONLY:
                anti_chakra.append(val)

        mean, standard_dev = nps.standard_deviation(anti_chakra)

        for chak, val in self.CHAKRAS[chakra].items():
            if chak in CHAKRA_ONLY:
                new[chak] = round(nps.confidence_level(val, mean,
                                                       standard_dev), 2)

        new[CONFIDENCE] = round(self.CHAKRAS[chakra][CONFIDENCE]*100, 2)
        new[POWER_LEVEL] = round(sum(anti_chakra), 2)

        return new


def infuse(word, confidence, category=INTERNAL):
    if category == INTERNAL:
        return word*confidence/100.0
    else:
        return word*confidence/200.0


def make_body():
    model = Chakras()
    return model
