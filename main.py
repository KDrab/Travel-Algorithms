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
    print(graph.nodes)

    #Edges
    print(graph.make_weights())
    for edge in graph.edges:
        print(edge, graph.edges[edge])

    #Total Cost path
    print(graph.node_array)
    print(graph.brute_lowest_cost(graph.node_array))

    #Algorithm Choice
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP: ")
    while (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")

    #Greedy Choice and parameters
    random.seed()
    if (algChoice == "Greedy"):
        num_iters = int(input("From how many nodes would you like to run the trivial algorithm?: "))
        for i in range(1, num_iters):
            to_visit = []
            to_visit = graph.node_array
            print(to_visit)
            first = random.randrange(0, len(graph.node_array))
            print(greedy.greed_triv(graph, first, to_visit, []))



main()
