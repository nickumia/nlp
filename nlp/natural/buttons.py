# Named after the valiant dog always protecting mindy #animaniacs
# Compares two wordmap objects for similarity


class Buttons():
    def __init__(self, brain=None, pinky=None):
        self.brain = brain
        self.pinky = pinky
        self.overlap = None
        self.brain_n = 0
        self.pinky_n = 0

    def setBrain(self, internal):
        self.brain = internal

    def setPinky(self, external):
        self.pinky = external

    def intersect(self):
        brain_k = set(self.brain.ranking.keys())
        pinky_k = set(self.pinky.ranking.keys())
        self.brain_n = len(brain_k)
        self.pinky_n = len(pinky_k)

        self.overlap = brain_k.intersection(pinky_k)

    def match(self, compute=False):
        '''
        Compare the reference model (brain) to the input (pinky)
        IN: compute, bool: Whether this function should run the default
                            computations
        OUT: total, num: percent of perfect match (total & subset)
        '''
        total = 0
        subset = 0
        # reference = sum(self.brain.singular.values())
        for word in self.overlap:
            brain_occur = len(self.brain.ranking[word])
            pinky_occur = len(self.pinky.ranking[word])
            if brain_occur > pinky_occur:
                weight = pinky_occur / brain_occur
            else:
                weight = brain_occur / pinky_occur
            total += abs(weight) * self.brain.singular[word]
            subset += self.brain.singular[word]

        return total / subset  # , total / reference

    def bias(self):
        '''
        Identify whether the data is skewed towards what's known vs. unknown
        OUT: complete, num: measure of how much the brain knows
        OUT: incomplete, num: measure of how much the pinky knows
        '''
        complete = len(self.overlap) / self.brain_n
        incomplete = len(self.overlap) / self.pinky_n

        return complete, incomplete
