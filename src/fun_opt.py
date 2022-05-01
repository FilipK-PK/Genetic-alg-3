import math

FIRST, SECOND = 0, 1
JUMP_TWO = 2
NEXT = 1
FUN_BUKIN = 'BUKIN'
FUN_DROP_WAVE = 'DROP-WAVE'
FUN_GOLDSTREAM = 'GOLDSTEIN-PRICE'
FUN_MCCORMICK = 'MCCORMICK'
FUN_ACKLEY = 'ACKLEY'
FUN_BEALE = 'BEALE'
FUN_SCHAFFER_2 = 'SCHAFFER 2'
FUN_HOLDER_TABLE = 'HOLDER TAB'


class FunOpt:
    """ Klasa zwraca wartość funkcji
    dla popdanych danych """
    def __init__(self, name_fun, end_points, use_bit=False):
        self.__use_bit = use_bit
        self.__fun = None
        self.__end_p = end_points

        self.__set_use_fun(name_fun)

    def get_val(self, val):
        if self.__use_bit:
            val = self.__bin_to_dec(val)

        val = self.__rescale(val)

        return self.__fun(val),

    def __rescale(self, val):
        res = []
        for i, v in enumerate(val):
            res.append(
                self.__end_p[2*i] +
                (self.__end_p[2*i+1] - self.__end_p[2*i]) * v
            )

        return res

    """ Przekształcanie liczby bit na double """
    def __bin_to_dec(self, val) -> []:
        len_bit = len(val) // 2
        new_val = []

        for i in range(2):
            s = 0
            for el in val[i*len_bit: (i+1)*len_bit]:
                s = s * 2 + el

            new_val.append(s / (2 ** len_bit - 1))

        return new_val

    """ Zapisanie funkcji do zmiennej, czystrzy kod """
    def __set_use_fun(self, name_fun) -> None:
        set_fun = {
            'test': self.__fun_test,
            FUN_ACKLEY: self.__fun_ackley,
            FUN_BEALE: self.__fun_beale,
            FUN_BUKIN: self.__fun_bukin,
            FUN_DROP_WAVE: self.__fun_drop_wawe,
            FUN_GOLDSTREAM: self.__fun_goldstein_price,
            FUN_MCCORMICK: self.__fun_miccormick,
            FUN_SCHAFFER_2: self.__fun_schaffer2,
            FUN_HOLDER_TABLE: self.__fun_holder_table
        }

        self.__fun = set_fun[name_fun]

    def __fun_test(self, val):
        return (val[0] - 2) ** 2 + val[1]

    """ ACKLEY FUNCTION """
    @staticmethod
    def __fun_ackley(p) -> float:
        return (
                -20 * math.exp(-0.2 * math.sqrt(0.5 * (p[0] ** 2 + p[1] ** 2)))
                - math.exp(0.5 * (math.cos(2 * math.pi * p[0]) + math.cos(math.pi * p[1])))
                + 20 + math.exp(1)
        )

    """ BEALE FUNCTION """
    @staticmethod
    def __fun_beale(p) -> float:
        return (
                (1.5 - p[0] + p[0] * p[1]) ** 2 +
                (2.25 - p[0] + p[0] * p[1] ** 2) ** 2 +
                (2.625 - p[0] + p[0] * p[1] ** 3) ** 2
        )

    """ BUKIN """
    @staticmethod
    def __fun_bukin(p) -> float:
        return (
                100.0 * math.sqrt(math.fabs(p[1] - 0.01 * p[0] ** 2))
                + 0.01 * math.fabs(p[0] + 10.0)
        )

    """ DROP-WAVE """
    @staticmethod
    def __fun_drop_wawe(p) -> float:
        return (
            -(1.0 + math.cos(12.0 * math.sqrt(p[0] ** 2 + p[1] ** 2)))
            / (0.5 * (p[0] ** 2 + p[1] ** 2) + 2.0)
        )

    """ GOLDSTEIN-PRICE """
    @staticmethod
    def __fun_goldstein_price(p) -> float:
        return (
            (1.0+(p[0]+p[1]+1.0)**2 * (19.0-14*p[0]+3*p[0]**2-14*p[1]+6*p[0]*p[1]+3*p[1]**2)) *
            (30.0+(2*p[0]-3*p[1])**2 * (18.0-32*p[0]+12*p[0]**2+48*p[1]-36*p[0]*p[1]+27*p[1]**2))
        )

    """ MCCORMICK """
    @staticmethod
    def __fun_miccormick(p) -> float:
        return (
            math.sin(p[0] + p[1]) + (p[0] - p[1])**2 - 1.5 * p[0] + 2.5 * p[1] + 1
        )

    """ SCHAFFER 2 """
    @staticmethod
    def __fun_schaffer2(p) -> float:
        return (
            0.5 + (math.sin(p[0]**2-p[1]**2)**2-0.5) / (1.0 + 0.001*(p[0]**2+p[1]**2))**2
        )

    """ HOLDER TABLE """
    @staticmethod
    def __fun_holder_table(p) -> float:
        return (
            - math.fabs(math.sin(p[0]) * math.cos(p[1]) *
                        math.exp(math.fabs(1-(math.sqrt(p[0]**2+p[1]**2)) / math.pi))
                        )
        )
