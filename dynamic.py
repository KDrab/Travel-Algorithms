# Dynamic: A file using a dynamic programming method to solve the traveling Salesman
#          Problem


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

Speed up: Eliminate function calls for subpaths that have already been evaluated

"""
def dynamic_p(graph, start, to_visit, out):
    
