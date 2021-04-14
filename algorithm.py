import math
from csvMethods import *
from array import *

class tspAlgorithm:
    """
    class for the algorithm I will use to solved the optimal truck route
    """

    falsify = False
    memo = [[]]

    def __init__(self, matrix, start):
        """
        constructing the optimal routing solution taking a 2d matrix and starting node as arguments
        :param matrix: distance matrix
        :param start: the starting node aka the HUB
        """
        nodes = matrix.size
        self.matrix = matrix
        self.start = start
        tour = []
        self.memo = [[0 for x in range(nodes)] for y in range(2 ** nodes)]




    def setup_memo(self, matrix, memo, start, nodes):
        self.matrix = matrix
        self.memo = memo
        self.start = start
        nodes = matrix.size

        for i in range(nodes):
            if i == start:
                continue
            memo[i][1 << start | 1 << i] = matrix[start][i]




    def solve(self, matrix, memo, start, nodes):
        self.start = start
        self.matrix = matrix
        self.memo = memo
        nodes = matrix.size

        # for r in range(3, nodes): finish from here


























