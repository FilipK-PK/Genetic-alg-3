import random

FIRST = 0
SECOND = 1
ONE = 1


def cxArithmetic():
    '''k = random.random()
    len_v = len(ind1)

    new_a = [
        k * ind1[i] + (ONE - k) * ind2[i]
        for i in range(len_v)
    ]

    new_b = [
        k * ind2[i] + (ONE - k) * ind1[i]
        for i in range(len_v)
    ]'''

    return 0.1, 0.2


def cxAveranging():
    pass


def cxA():
    pass


def cxAb():
    pass


def mutTwoPoint(vec, indpb):
    """ Mutacja dwupunktowa """

    if indpb < random.random():
        a = random.randint(0, len(vec)-1)
        b = random.randint(0, len(vec)-1)

        while a == b:
            a = random.randint(0, len(vec)-1)
            b = random.randint(0, len(vec)-1)

        vec[a] = 1 if vec[a] == 0 else 0
        vec[b] = 1 if vec[b] == 0 else 0

    return vec


def mutEvenBit(vec, indpb):
    """ Mutacja jednorodna bitowa """

    if indpb < random.random():
        for i, _ in enumerate(vec):
            if indpb < random.random():
                vec[i] = 1 if vec[i] == 0 else 0

    return vec


def mutIndexing(vec, indpb) -> []:
    """ Mutacja indeksowa """
    if indpb < random.random():
        return [vec[SECOND], vec[FIRST]]

    return vec


def mutEven(vec, indpb) -> []:
    """ Mutacja rownomierna """
    len_vec = len(vec)

    if indpb < random.random():
        return [
            random.random(),
            random.random()
        ]

    return vec
