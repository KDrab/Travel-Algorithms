## Main program environment to run algorithms
##

""" Imports"""
import sys
from graph import Graph


"""Variables"""


def main():

    #Graph
    gSize = input("How big would you like the graph to be?: ")
    graph = Graph(gSize)
    graph.makeGraph()
    print(graph.nodes)

    #Edges
    graph.makeWeights()
    """for edge in graph.edges:
        print(edge, graph.edges[edge])"""

    #Paths
    print(graph.getPath(graph.nodes, 0, [1,2,3,4,5]))

    #Algorithm
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP: ")
    if (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")



main()
