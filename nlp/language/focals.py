
import nlp.processing.appraisal.dictionary as npad
import nlp.processing.corpus.identity as npci
import nlp.processing.corpus.representativeness as npcr
import nlp.processing.filters as npf
import nlp.processing.storage as nps
import nlp.language.fuzzy as nlf
import nlp.language.constants as nlc


class WordMap(nps.S3Storage):
    def __init__(self, focal):
        '''
        focal, list: list of words as focal point
        map, dict(priority, words): priority of word associations
        ranking, dict(words, ranking): the order in which the word showed
                                        up in the definition (i.e. the first
                                        definition, the second definition...)
        singular, dict(word, weight): the combination of priority and rank to
                                        form a weight of association
        '''
        # super().__init__()
        super().__init__('nlpdev', 'nlpdev')
        self.focal = focal
        self.map = {0: focal}
        self.ranking = {}
        self.singular = {}

    def generateByDefinitions(self, layers=2):
        '''
        layers, int: the number of recursive word associations to create
        map, dict{layer, words}: priority-ranked word associations
            (0 -> highest priority; n -> lowest priority
        '''

        ranking = {}
        for layer in range(layers):
            all_words = []
            for word in self.map[layer]:
                entry = npad.DICTIONARY.lookup(word)['entry']
                # print(layer, word, len(entry.getDefinitions()))
                for key, sense in entry.getDefinitions().items():
                    # print(word, sense['definition'])
                    if sense['definition'] is not None:
                        temp_words = npci.group(sense['definition'],
                                                specific=npci.char_word)
                        pos = nlf.posTag(temp_words, whole=True)
                        for item in pos:
                            if item[1] in nlc.CONTENT_WORDS:
                                filtered = npf.pre_sanitize(item[0])
                                all_words += [filtered]
                                if filtered in ranking:
                                    ranking[filtered] += [key + 1]
                                else:
                                    ranking[filtered] = [key + 1]
                    else:
                        # TODO: what should happen if the word cannot be
                        # looked up?
                        pass

            word_freq = npcr.occurences(all_words)
            self.map[layer+1] = word_freq
        self.ranking = ranking

    def collapse(self):
        '''
        Calculate a weight associated with each word given the map
        OUT: singular, dict{word, value}: weight of each word
                                            association
        '''
        print(self.map)
        for priority in self.map:
            if priority == 0:
                for word in self.map[priority]:
                    self.singular[word] = len(self.map[priority+1])
            else:
                for word in self.map[priority].keys():
                    rank = sum(self.ranking[word]) / \
                            float(len(self.ranking[word]))
                    if word in self.map[priority - 1]:
                        coefficient = 1
                    else:
                        coefficient = (1 / (rank * rank * priority * priority))
                    if word not in self.singular:
                        self.singular[word] = coefficient * \
                            self.map[priority][word]
                    else:
                        self.singular[word] += coefficient * \
                            self.map[priority][word]
        # print(self.singular['thing'])
        # print(self.ranking)
        return self.singular

    def backup(self, filename):
        self.save = self.map
        super().backup(filename)

    def restore(self, filename):
        super().restore(filename)
        self.map = self.save

    def getMap(self):
        return self.map


def combineMaps(A, B):
    ''' Combine focals '''
    new_focal = A.focal + B.focal
    C = WordMap(new_focal)

    ''' Combine maps '''
    big_map = A.map if len(A.map.keys()) > len(B.map.keys()) else B.map
    new_map = A.map if big_map == B.map else B.map
    for priority in big_map:
        if priority == 0:
            new_map[priority] += big_map[priority]
        elif priority not in new_map.keys():
            new_map[priority] = big_map[priority]
        else:
            new_map[priority].update(big_map[priority])
    C.map = new_map

    ''' Combine rankings '''
    new_ranking = A.ranking
    for word in B.ranking:
        if word not in new_ranking:
            new_ranking[word] = B.ranking[word]
        else:
            new_ranking[word] += B.ranking[word]
    C.ranking = new_ranking

    ''' Combine singulars '''
    new_singular = A.singular
    for word in B.singular:
        if word not in new_singular:
            new_singular[word] = B.singular[word]
        else:
            new_singular[word] += B.singular[word]
    C.singular = new_singular

    return C
