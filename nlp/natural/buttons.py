# Named after the valiant dog always protecting mindy #animaniacs
# Compares two wordmap objects for similarity


class Buttons():
    def __init__(self, brain=None, pinky=None):
        self.brain = brain
        self.pinky = pinky

    def setBrain(self, internal):
        self.brain = internal

    def setPinky(self, external):
        self.pinky = external

    def compare(self, compute=False):
        '''
        Compare the reference model (brain) to the input (pinky)
        IN: compute, bool: Whether this function should run the default
                            computations
        OUT: ???
        '''
        if compute:
            self.brain.generateByDefinitions()
            self.brain.collapse()
            self.pinky.generateByDefinitions()
            self.pinky.collapse()

    def bias(self):
        '''
        Identify whether the data is skewed towards what's known vs. unknown
        OUT: complete, num: measure of how much the brain knows
        OUT: incomplete, num: measure of how much the pinky knows
        '''
        brain_k = set(self.brain.singular.keys())
        pinky_k = set(self.pinky.singular.keys())
        brain_n = len(brain_k)
        pinky_n = len(pinky_k)
        print(brain_n)
        print(pinky_n)

        overlap = brain_k.intersection(pinky_k)
        print(len(overlap))
        complete = len(overlap) / brain_n
        incomplete = len(overlap) / pinky_n

        return complete, incomplete
