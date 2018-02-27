## Main program environment to run algorithms
##

""" Imports"""
import sys
import random
from graph import Graph
import greedy
import dynamic

"""Variables"""
s_node = 0

def main():

    #Graph
    gSize = input("How big would you like the graph to be?: ")
    graph = Graph(gSize)
    graph.make_graph()

    #Edges
    graph.make_weights()

    #Total Cost path
    #Save time?
    time = input("Save time?")

    #For now, saving time starts from node 0
    brutes = []
    if (time == "yes"):
        low_path = graph.brute_lowest_cost(graph.node_array, s_node)
        brutes.append(low_path)
    else:
        for node in graph.nodes:
            low_path = graph.brute_lowest_cost(graph.node_array, node)
            brutes.append(low_path)

    #Printing all paths, and best
    for path in brutes:
        print(path, graph.total_distance(path))


    #Algorithm Choice
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP: ")
    while (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")

    #Greedy Choice and parameters
    if (algChoice == "Greedy"):
        to_visit = []
        if (time == "yes"):
            for node in graph.node_array:
                to_visit.append(node)
            path = greedy.greed_triv(graph, s_node, to_visit, [])
            path[::-1]
            print(path, graph.total_distance(path))
        else:
            for i in range(0, len(graph.nodes)):
                for node in graph.node_array:
                    to_visit.append(node)
                first = i
                path = greedy.greed_triv(graph, first, to_visit, [])
                path[::-1]
                print(path, graph.total_distance(path))

    #DP Choice:
    if (algChoice == "DP"):




main()
