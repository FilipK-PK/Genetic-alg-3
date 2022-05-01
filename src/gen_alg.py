from deap import creator, base, tools
from src.fun_opt import FunOpt
from src.statistic import Statistic
import random


MATE = {
    '1-point': tools.cxOnePoint,
    '2-points': tools.cxTwoPoint,
    'jednolite': tools.cxUniform,
    #'': tools.cxPartialyMatched,
    #'': tools.cxOrdered,
    #'': tools.cxBlend,
    #'': tools.cxESBlend,
    #'': tools.cxESTwoPoint,
    #'': tools.cxSimulatedBinary,
    #'': tools.cxSimulatedBinaryBounded,
    #'': tools.cxMessyOnePoint
}
MUTATE = {
    '1-point': tools.mutFlipBit,
    'Gaussowska': tools.mutGaussian,
    'sekfencja indeksu': tools.mutShuffleIndexes,
    #'': tools.mutPolynomialBounded,
    #'': tools.mutUniformInt,
    #'': tools.mutESLogNormal,
}
SELECT = {
    'turniej': tools.selTournament,
    'ruletki': tools.selRoulette,
    #'': tools.selNSGA2,
    #'': tools.selNSGA3,
    #'': tools.selSPEA2,
    'losowa': tools.selRandom,
    'najlepsi': tools.selBest,
    'najgorsi': tools.selWorst,
    #'': tools.selTournamentDCD,
    #'': tools.selDoubleTournament,
    #'': tools.selStochasticUniversalSampling,
    #'': tools.selLexicase,
    #'': tools.selEpsilonLexicase,
    #'': tools.selAutomaticEpsilonLexicase,
}


class GenAlg:
    """ Klasa przeprowadza proces genetyczny """

    def __init__(self, param):
        self.__param = param
        self.__is_bit = True if 'bit' in self.__param else False
        self.__toolbox = base.Toolbox()
        self.__popu = []
        self.__statistic = Statistic()
        self.__fun = FunOpt(
            param['fun'],
            param['set_xy'],
            'bit' in self.__param
        )

    def run(self) -> None:
        """ Metoda wywołuje poszczegulne moduły """

        self.__set_opt()
        self.__rand_popu()
        self.__set_select()
        self.__set_cross()
        self.__set_mutable()

        self.__start_find()

    def __rand_popu(self) -> None:
        """ Metoda tworzy populację """

        self.__toolbox.register(
            'individual', self.__rand_gen,
            creator.Individual
        )

        self.__toolbox.register(
            "population", tools.initRepeat,
            list, self.__toolbox.individual
        )

        self.__toolbox.register("evaluate", self.__fun.get_val)

        self.__popu = self.__toolbox.population(
            n=self.__param['len_popu']
        )

    def __set_opt(self) -> None:
        """ Metoda okresla czy ma zostac
        wyszukiwane min czy max"""

        if self.__param['opt'] == 'min':
            creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
            creator.create("Individual", list, fitness=creator.FitnessMin)
        else:
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))
            creator.create("Individual", list, fitness=creator.FitnessMax)

    def __set_select(self) -> None:
        """ Metoda ustawia rodzja selekcji """

        if self.__param['select'] == 'turniej':
            self.__toolbox.register(
                "select", tools.selTournament,
                tournsize=int(
                    self.__param['len_popu']
                    * self.__param['p_select']
                )
            )
        else:
            self.__toolbox.register(
                "select",
                SELECT[self.__param['select']]
            )

    def __set_cross(self) -> None:
        """ Metoda ustawia rodzaj krzyrzowania """

        self.__toolbox.register(
            "mate", MATE[self.__param['mutate']]
        )

    def __set_mutable(self) -> None:
        """ Metoda ustawia rodzaj mutacji """

        if self.__param['mutate'] == 'Gausowska':
            self.__toolbox.register(
                "mutate", tools.mutGaussian,
                sigma=1, mu=0,
                indpb=self.__param['p_mutate']
            )
        else:
            self.__toolbox.register(
                "mutate", MUTATE[self.__param['mutate']],
                indpb=self.__param['p_mutate']
            )

    def __start_find(self) -> None:
        """ Metoda przeprowadza proces genetyczny
        okresloną liczbe epok """

        fitnesses = list(map(self.__toolbox.evaluate, self.__popu))
        for ind, fit in zip(self.__popu, fitnesses):
            ind.fitness.values = fit

        for _ in range(self.__param['epoch']):
            offspring = self.__toolbox.select(self.__popu, len(self.__popu))
            offspring = list(map(self.__toolbox.clone, offspring))

            listElitism = []
            for x in range(self.__param['elit']):
                listElitism.append(tools.selBest(self.__popu, 1)[0])

            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < self.__param['p_cross']:
                    self.__toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < self.__param['p_mutate']:
                    self.__toolbox.mutate(mutant)
                    del mutant.fitness.values

            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(self.__toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            self.__popu[:] = offspring + listElitism

            fits = [ind.fitness.values[0] for ind in self.__popu]
            self.__statistic.put_epoch(fits, self.__popu)

        self.__print_result()

    def __rand_gen(self, icls) -> []:
        """ Metoda losuje pojedynczego osobnika  """

        if 'bit' in self.__param:
            return icls(
                [
                    random.randint(0, 1)
                    for _ in range(self.__param['bit'])
                ]
            )

        return icls(
            [random.random() for _ in range(2)]
        )

    def __print_result(self):
        data = self.__statistic.get_statistic()

        if self.__param['opt'] == 'min':
            print('min end', data['min'][-1])
            print('best end', data['best'][-1])
            print('min global ', min(data['min']))
            print('best end', min(data['best'][-1]))
        else:
            print('max end', data['max'][-1])
            print('best end', data['best'][-1])
            print('max global', max(data['max']))
            print('best global', max(data['best'][-1]))

        self.__statistic.draw_graphs()

