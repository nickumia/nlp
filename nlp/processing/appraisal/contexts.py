
import nlp.processing.corpus.representativeness as npcr
import nlp.processing.corpus.identity as npci

def generate(groups, full_text):
    '''
    IN: groups, dict(list), a dictionary of identity groups
    IN: full_text, str, full input text
    OUT: contexts, dict(list), a dictionary of 
            {word: [(context, type(context), position in full_text)]}
    '''
    contexts = {}

    # Only count words once
    tokens = npcr.unique(groups[npci.WORDS])

    for word in tokens:
        for id_group, results in groups.items():
            if id_group == npci.WORDS:
                continue
            for context in results:
                if word.strip() in context:
                    position = locate(full_text, context)
                    if word in contexts:
                        contexts[word] += [(context,
                                            id_group,
                                            position)]
                    else:
                        contexts[word] = [(context, id_group, position)]

    return contexts


def locate(full_text, key):
    '''
    IN: full_text, str, full input text
    IN: key, str, phrase to find in text
    '''
    return full_text.find(key)
