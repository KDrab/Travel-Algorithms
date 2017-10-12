
"""
The Class used to construct the Graph for the Problem
"""

"""Imports"""
import random
from itertools import permutations

""" Variables """
MAX_LENGTH = 100

class Graph(object):

    def __init__(self, size):
        self.size = size
        self.nodes = {}
        self.edges = {}
        self.node_array = []

    # Make Nodes and their edges
    # As: (Node) : Node1, Node2, etc
    def make_graph(self):
        for i in range(0, int(self.size)):
            temps = []
            for j in range(0, int(self.size)):
                if not (i == j):
                    temps.append(j)
            self.nodes[i] = temps
            self.node_array.append(i)


    # Make random weights for each edge in graph
    def make_weights(self):
        random.seed()
        for node in self.nodes:
            for edge in self.nodes[node]:
                e = (node, edge)
                rev_e = (edge, node)
                if (not(e in self.edges or rev_e in self.edges)):
                    self.edges[e] = random.randrange(1, MAX_LENGTH)
                else:
                    self.edges[e] = self.edges[rev_e]

    """ Following three methods use code taken from here:
    https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics
    """

    # Algorithm finds the lowest cost path through the graph, uses O(n!)
    # NEEDS test
    def brute_lowest_cost(self, points, start=None):
        if start is None:
            start = points[0]
        return min([perm for perm in permutations(points) if perm[0] == start], key = self.total_distance)


    # Finds the total cost of a single path of points through the graph
    # MAY need to be fixed
    def total_distance(self, points):
        return sum([self.distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


    # Returns distance between two points
    def distance(self, a, b):
        return self.edges[(a,b)]
