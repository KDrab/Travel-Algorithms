
"""
The Class used to construct the Graph for the Problem
"""

"""Imports"""
import random

""" Variables """
MAX_LENGTH = 100

class Graph(object):

    def __init__(self, size):
        self.size = size
        self.nodes = {}
        self.edges = {}
        self.paths = {}

    # Make Nodes and their edges
    # As: (Node) : Node1, Node2, etc
    def makeGraph(self):
        print(self.size)
        for i in range(0, int(self.size)):
            temps = []
            for j in range(0, int(self.size)):
                if not (i == j):
                    temps.append(j)
            self.nodes[i] = temps


    # Make random weights for each edge in graph
    def makeWeights(self):
        random.seed()
        for node in self.nodes:
            for edge in self.nodes[node]:
                e = (node, edge)
                rev_e = (edge, node)
                if (not(e in self.edges or rev_e in self.edges)):
                    self.edges[e] = random.randrange(1, MAX_LENGTH)


    # Find a single path through the graph
    def getPath(self, g, start, to_visit, path = []):
        path = path + [start]
        if not to_visit:
            return [path]
        if not start in g:
            return []
        paths = []
        for node in g[start]:
            if node not in path:
                print(node)
                print(to_visit)
                if to_visit:
                    to_visit.remove(node)
                newpaths = self.getPath(g, node, to_visit, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
