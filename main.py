## Main program environment to run algorithms
##


#VARS

#IMPORTS
import sys
from graph import Graph

def main():

    #Graph
    gSize = input("How big would you like the graph to be?:")
    graph = Graph(gSize)
    graph.makeGraph()
    print(graph.nodes)

    #Algorithm
    algChoice = input("What algorithm would you like to run? Please enter Greedy, or DP:" )
    if (not (algChoice == "Greedy" or algChoice == "DP")):
        algChoice = input("Please enter Greedy or DP:")









main()
