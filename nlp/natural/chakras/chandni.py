
import nlp.natural.chakras.base as nncb
import nlp.natural.chakras.events as nnce
import numpy


class Chandni():
    def __init__(self, text):
        self.model = nncb.make_body()
        # self.text = BasicText(text)
        self.events = numpy.zeros((7,7))
        self.texts = numpy.zeros((7,7))
        self.match = 0

        self.PCHAKRA = {}
        self.QCHAKRA = {}

    def run(self, meanings, confidence, learn):
        nnce.determineInfluence(self.model, meanings, confidence, learn=learn)
        self.PCHAKRA = self.model.chakraDistribution(model.P_CHAKRA)
        self.QCHAKRA = self.model.chakraDistribution(model.Q_CHAKRA)

    def train(self, meanings, confidence, particle):
        # meanings, confidence = nlf.getFuzzyMeaning(self.text.groups,
        #                                            self.text.contexts,
        #                                            occurences(self.text.words),  # NOQA
        #                                            totalCount(self.text.words))  # NOQA
        self.run(meanings, confidence, True)
        self.model.CHAKRA_TRAIN_HISTORY[particle] = (
            (self.model.CHAKRAS[model.P_CHAKRA][model.POWER_LEVEL] - \
             self.model.CHAKRAS[model.Q_CHAKRA][model.POWER_LEVEL]),
            self.model.CHAKRAS[model.P_CHAKRA],
            self.model.CHAKRAS[model.Q_CHAKRA]
        )

        for i, chakra1 in enumerate(nncb.CHAKRA_ONLY):
            batman = nnce.eventChange(self.PCHAKRA[chakra1])
            for j, chakra2 in enumerate(nncb.CHAKRA_ONLY):
                superman = nnce.eventChange(self.PCHAKRA[chakra2])

                self.events[i][j] += round(batman - superman,2)
                self.texts[i][j] += round(batman - superman,2)

                if self.events[i][j] < 0 and self.texts[i][j] < 0:
                    self.match += 1
                elif self.events[i][j] > 0 and self.texts[i][j] > 0:
                    self.match += 1
                elif self.events[i][j] == 0 and self.texts[i][j] == 0:
                    self.match += 1

        self.match = round(self.match/49, 2)

    def test(self, meanings, confidence, particle):
        self.run(meanings, confidence, False)
        self.model.CHAKRA_TEST_HISTORY[particle] = (
            (self.model.CHAKRAS[self.model.P_CHAKRA][self.model.POWER_LEVEL] - \  # NOQA
             self.model.CHAKRAS[self.model.Q_CHAKRA][self.model.POWER_LEVEL]),
            self.model.CHAKRAS[self.model.P_CHAKRA],
            self.model.CHAKRAS[self.model.Q_CHAKRA]
        )

        x_survival = []
        x_pleasure = []
        x_willpower = []
        x_love = []
        x_truth = []
        x_insight = []
        x_attachment = []
        # total = 0

        union = (lambda x: x if type(x) != tuple else x[0]+x[1])
        for particle, interaction in self.model.CHAKRA_TEST_HISTORY.items():
            total += union(interaction[0])
            x_survival.append(interaction[1][nnce.EARTH])
            x_pleasure.append(interaction[1][nnce.WATER])
            x_willpower.append(interaction[1][nnce.FIRE])
            x_love.append(interaction[1][nnce.HEART])
            x_truth.append(interaction[1][nnce.SOUND])
            x_insight.append(interaction[1][nnce.LIGHT])
            x_attachment.append(interaction[1][nnce.COSMIC])

        # TODO: Finish Model
        # Maximum likelihood function for each chakra
        # Needs to consider degrees of freedom ... not sure how...

        # llog = x*logarithm(p) + (n-x)*logarithm(1-p)
        # llogp = x/p - ((n-x)/(1-p))
        # llogpp = (-1*x) / (p*p) + ((n-x)/((1-p)*(1-p)))
