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
    print(graph.node_array)
    low_path = graph.brute_lowest_cost(graph.node_array)
    print(low_path, graph.total_distance(low_path))

    #Algorithm Choice
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP: ")
    while (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")

    #Greedy Choice and parameters
    random.seed()
    if (algChoice == "Greedy"):
        num_iters = int(input("From how many nodes would you like to run the trivial algorithm?: "))
        to_visit = []
        for i in range(0, num_iters):
            for node in graph.node_array:
                to_visit.append(node)
            first = random.randrange(0, num_iters)
            path = greedy.greed_triv(graph, first, to_visit, [])
            print(path, graph.total_distance(path))



main()
