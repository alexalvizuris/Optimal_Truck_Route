import math
from csvMethods import *

class tspAlgorithm:
    """
    class for the algorithm I will use to solved the optimal truck route
    """

    def __init__(self, matrix, start):
        """
        constructing the optimal routing solution taking a 2d matrix and starting node as arguments
        :param matrix: distance matrix
        :param start: the starting node aka the HUB
        """
        N = matrix.size
        self.matrix = matrix
        self.start = start
        tour = []
        falsify = False







