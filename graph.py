
"""
The Class used to construct the Graph for the Problem

"""

""" Variables """
MAX_LENGTH = 100

class Graph(object):

    def __init__(self, size):
        self.size = size
        self.nodes = {}
        self.edges = {}

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

#    def makeWeights(self):
