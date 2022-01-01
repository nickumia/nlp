import timeit


class Time():

    def __init__(self, setup, func, iterations):
        self.setup_code = setup
        self.test_function = func
        self.iterations = iterations

    def run(self):
        return timeit.timeit(setup=self.setup_code,
                             stmt=self.test_function,
                             number=self.iterations)


def ttr1(body):
    return len(set(body))/len(body)


def ttr2(body):
    a = {}
    for word in body:
        if word not in a.keys():
            a[word] = 1
        else:
            a[word] += 1
    return len(a.keys())/len(body)


def dictmax(dm):
    return max(dm.values())


def listmax(lm):
    return max(lm)
