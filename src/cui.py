from colorama import Fore


PRE_TITLE_QUEST = 'Podaj rodzaj'
PRE_TITLE_FLOAT = 'Podaj procent'
PRE_TITLE_INT = 'Podaj rozmiar'
PRE_TITLE_SET = 'Podaj zakres zmienych:'
REPRESENT = [
    'reprezentacji',
    ['binarna', 'rzeczywista'],
    'reprezent'
]
SELECT = [
    'selekcji',
    ['najlepsi', 'turniej', 'ruletki', 'najgorsi', 'losowa'],
    'select'
]
CROSS_BIT = [
    'krzyzowania',
    ['1-point', '2-points', 'jednolite'],
    'cross'
]
CROSS_REL = [
    'krzyzowania',
    [''],
    'cross'
]
FUN = [
    'funkcji',
    [
        'BUKIN', 'DROP-WAVE', 'GOLDSTEIN-PRICE',
        'MCCORMICK', 'ACKLEY', 'BEALE',
        'SCHAFFER 2', 'HOLDER TAB'
    ],
    'fun'
]
SORT = [
    'optymalizacji',
    ['min', 'max'],
    'opt'
]
MUTATE_BIT = [
    'mutacji',
    ['1-point', 'indeksowe'],
    'mutate'
]
MUTATE_REL = [
    'mutacji',
    ['Gaussowska'],
    'mutate'
]
BIT = ['długosci cechy', 'bit']
LEN_POPU = ['populacji', 'len_popu']
EPOCH = ['liczby epok', 'epoch']
ELIT = ['osobników elitarych', 'elit']
PROC_CROSS = ['krzyzowania', 'p_cross']
PROC_SELECT = ['selekcji', 'p_select']
PROC_MUTATE = ['mutacji', 'p_mutate']
SET_XY = ['x-min, x-max, y-min, y-max', 'set_xy']
FIRST = 0
SECOND = 1
THIERE = 2
THOUR = 3
IND_TITLE = 0
IND_QUEST = 1
IND_ODP = 2
UP = 1
SEP = ':'
LEN_ARG = 4
SPACE = ' '
SEPAR = ','
GET_IND = 'podaj index: '
GET_VAL = 'podaj wartosc: '
GET_VALS = 'podaj wartosci: '
GET_PROC = 'podaj procent: '
ERR_CHAR = 'Bład wykryto nieznany znak'
ERR_IND = 'Bład niema takiego indeksu'
ERR_NEG = 'Bład ujemny indeks lub zerowy'
ERR_01 = 'Bład wartośc poza zakresem [0-1]'
ERR_NOT_4 = 'Bład zła liczba argumentów'
ERR_ON_1 = 'Bład tylko jedna wartosc'
ERR_MIN_MAX = 'Błąd min >= max'
ZERO = 0
ONE = 1
DOWN = -1
BIT_TYPE = 'binarna'
TYPE_REP = 'reprezent'


class Cui:
    """ Klasa słurzy do pobierania opcji podanych
    przez uzytkownika """

    def __init__(self):
        self.__list_opt = {}

    """ Metoda wuwołuje wszystkie zapytania """
    def run(self):
        self.__put_quest(REPRESENT)
        if self.__list_opt[TYPE_REP] == BIT_TYPE:
            self.__put_val(BIT)

        self.__put_quest(FUN)
        self.__put_quest(SORT)
        self.__put_val(LEN_POPU)
        self.__put_val(EPOCH)
        self.__put_quest(SELECT)
        self.__put_proc(PROC_SELECT)

        if 'bit' in self.__list_opt:
            self.__put_quest(CROSS_BIT)
            self.__put_quest(MUTATE_BIT)
        else:
            self.__put_quest(CROSS_REL)
            self.__put_quest(MUTATE_REL)

        self.__put_proc(PROC_CROSS)
        self.__put_proc(PROC_MUTATE)

        self.__put_val(ELIT)
        self.__put_set(SET_XY)

    """ Metoda zwraca pobrana listę """
    def get_result(self) -> {}:
        return self.__list_opt

    """ Metoda do wyswietlania zapytan z opcjami  """
    def __put_quest(self, tab) -> None:
        print(
            Fore.BLUE + PRE_TITLE_QUEST, tab[IND_TITLE],
            Fore.RESET
        )

        self.__print_opt(tab[IND_QUEST])

        self.__list_opt[tab[IND_ODP]] = tab[IND_QUEST][
            self.__get_and_spr_arg(
                len(tab[IND_QUEST])
            )
        ]

    """ Metoda do wyswietlania zapytan 
    od pobrania wartosci naturalnej """
    def __put_val(self, tab):
        print(
            Fore.BLUE + PRE_TITLE_INT, tab[IND_TITLE],
            Fore.RESET
        )

        self.__list_opt[tab[IND_QUEST]] = self.__get_int()

    """ Metoda do wyswietlania zapytan 
        od pobrania procentu """
    def __put_proc(self, tab):
        print(
            Fore.BLUE + PRE_TITLE_FLOAT, tab[IND_TITLE],
            Fore.RESET
        )

        self.__list_opt[tab[IND_QUEST]] = self.__get_float()

    """ Metoda do wyswietlania zapytan 
            od pobrania procentu """
    def __put_set(self, tab):
        print(
            Fore.BLUE + PRE_TITLE_SET,
            tab[IND_TITLE], Fore.RESET
        )

        self.__list_opt[tab[IND_QUEST]] = self.__get_set()

    """ Metoda wyswietla opcje w podany sposob """
    @staticmethod
    def __print_opt(tab):
        for i, val in enumerate(tab):
            print(SPACE, str(i + UP) + SEP, val)

    """ Funkcja pobiera wartosc dopuki 
    nie otrzyma prawidłowego indeksu """
    @staticmethod
    def __get_and_spr_arg(len_opt) -> int:
        while True:
            ind = input(GET_IND)

            try:
                int(ind)
            except ValueError:
                print(Fore.RED + ERR_CHAR, Fore.RESET)
                continue

            if ZERO >= int(ind):
                print(Fore.RED + ERR_NEG, Fore.RESET)
                continue

            if int(ind) > len_opt:
                print(Fore.RED + ERR_IND, Fore.RESET)
                continue

            return int(ind) + DOWN

    """ Funkcja pobiera wartosc dopuki 
    nie otrzyma int """
    @staticmethod
    def __get_int() -> int:
        while True:
            val = input(GET_VAL)

            try:
                int(val)
            except ValueError:
                print(Fore.RED + ERR_CHAR, Fore.RESET)
                continue

            if ZERO > int(val):
                print(Fore.RED + ERR_NEG, Fore.RESET)
                continue

            return int(val)

    """ Funkcja pobiera wartosc dopuki 
    nie otrzyma wartosci [0-1] """
    @staticmethod
    def __get_float() -> float:
        while True:
            val = input(GET_PROC)

            try:
                float(val)
            except ValueError:
                print(Fore.RED + ERR_CHAR, Fore.RESET)
                continue

            if ZERO > float(val) or float(val) > ONE:
                print(Fore.RED + ERR_01, Fore.RESET)
                continue

            return float(val)

    """ Funkcja pobiera wartosc dopuki 
        nie otrzyma poprawnie zdefiniowanych 
        endpointów """
    @staticmethod
    def __get_set() -> []:
        while True:
            val = input(GET_VALS)

            try:
                sets = val.split(SEPAR)
            except ValueError:
                print(Fore.RED + ERR_ON_1, Fore.RESET)
                continue

            if len(sets) != LEN_ARG:
                print(Fore.RED + ERR_NOT_4, Fore.RESET)
                continue

            try:
                for i in sets:
                    float(i)
            except ValueError:
                print(Fore.RED + ERR_CHAR, Fore.RESET)
                continue

            sets = [float(i) for i in sets]

            if (sets[FIRST] >= sets[SECOND]
                    or sets[THIERE] >= sets[THOUR]):
                print(Fore.RED + ERR_MIN_MAX, Fore.RESET)
                continue

            return sets
