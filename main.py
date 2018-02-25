## Main program environment to run algorithms
##

""" Imports"""
import sys
import random
from graph import Graph
import greedy

"""Variables"""


def main():

    #Graph
    gSize = input("How big would you like the graph to be?: ")
    graph = Graph(gSize)
    graph.make_graph()

    #Edges
    graph.make_weights()

    #Total Cost path
    brutes = []
    for node in graph.nodes:
        low_path = graph.brute_lowest_cost(graph.node_array, node)
        brutes.append(low_path)

    #Printing all paths, and best
    for path in brutes:
        print(path, graph.total_distance(path))

    #for e in graph.edges:
    #    print(e, graph.edges[e])

    #Algorithm Choice
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP: ")
    while (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")

    #Greedy Choice and parameters
    random.seed()
    if (algChoice == "Greedy"):
        to_visit = []
        for i in range(0, len(graph.nodes)):
            for node in graph.node_array:
                to_visit.append(node)
            first = i
            path = greedy.greed_triv(graph, first, to_visit, [])
            path[::-1]
            print(path, graph.total_distance(path))



main()
