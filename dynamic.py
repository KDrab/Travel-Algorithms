# Dynamic: A file using a dynamic programming method to solve the traveling Salesman
#          Problem


"""Imports"""
from graph import Graph

#Memoization: evalutaing the cost of a sub_path will be stored and accessed
#instead of being reevaluated

""" Example using 4 cities:

A----------B
|  \    /  |
|    /\    |
| /      \ |
C----------D

A->B = 10
A->C = 20
A->D = 40

B->C = 30
B->D = 50

C->D = 15

max_length = size of the set of cities = 4
current_cost = cost of the path so far

--IDEA--

while cities is NOT empty:
    choose a city
    add cost of subpath to path
    add the subpath created to a dictionary of subpaths for speedup

Speed up:
    Eliminate function calls for subpaths that have already been evaluated
    Function calls to be reduced always occur at least halfway through the Graph
    We shall say: If the # of nodes is odd, reduction will occur for subpaths
        of length n - 1 /2
        If the # of nodes is even, reduction will occur for subpaths
        of length n/2 - 1

    Thus, we want to store subpaths that are approximately occupying the 2nd half
    of our decision tree and access those without evaluating whole new paths
"""

def dynamic_p(graph, start, to_visit, out):
