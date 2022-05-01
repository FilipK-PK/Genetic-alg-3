"""
@article{DEAP_JMLR2012,
    author = " F\'elix-Antoine Fortin and Fran\c{c}ois-Michel {De Rainville} and Marc-Andr\'e Gardner and Marc Parizeau and Christian Gagn\'e ",
    title = { {DEAP}: Evolutionary Algorithms Made Easy },
    pages = { 2171--2175 },
    volume = { 13 },
    month = { jul },
    year = { 2012 },
    journal = { Journal of Machine Learning Research }
}
"""

from src.cui import Cui
from src.gen_alg import GenAlg


if __name__ == '__main__':
    app = Cui()
    app.run()
    vec = app.get_result()

    app = GenAlg(vec)
    app.run()
