from deap import tools
import matplotlib.pyplot as plt
import numpy as np


TITLE_BEST_MENS = 'Wykres najlepszej i sredniej wartosci dla epoki'
TITLE_STD = 'Wykres odchylenia standardowego dla epoki'
LEGEND_BEST = 'Najlepszy'
LEGEND_STR = 'Średnia'
COORD_LEGEND = 'upper right'
PADDING = 0.5
COLUMN = 1
ROW_1 = 1
ROW_2 = 2
ALL_EL = 2


class Statistic:
    def __init__(self):
        self.__min = []
        self.__max = []
        self.__mean = []
        self.__best = []
        self.__std = []

    def put_epoch(self, fit, popu):
        self.__min.append(min(fit))
        self.__max.append(max(fit))
        self.__mean.append(np.array(fit).mean())
        self.__std.append(np.array(fit).std())
        best = tools.selBest(popu, 1)[0]
        self.__best.append(best.fitness.values)

    def get_statistic(self):
        return {
            'min': self.__min,
            'max': self.__max,
            'std': self.__std,
            'mean': self.__mean,
            'best': self.__best
        }

    """ Rysowanie wykresu """

    def draw_graphs(self) -> None:
        epoch = np.arange(len(self.__best))

        plt.subplot(ALL_EL, COLUMN, ROW_1)
        plt.title(TITLE_BEST_MENS)
        plt.plot(epoch, self.__best, label=LEGEND_BEST)
        plt.plot(epoch, self.__mean, label=LEGEND_STR)
        plt.legend(loc=COORD_LEGEND)

        plt.subplot(ALL_EL, COLUMN, ROW_2)
        plt.title(TITLE_STD)
        plt.plot(epoch, self.__std)

        plt.subplots_adjust(hspace=PADDING)
        plt.show()
