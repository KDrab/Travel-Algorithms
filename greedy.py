# Greedy: A file summarizing varying Greedy algorithms to solve the Traveling
#         Salesman problem



# Trivial Heuristic 1: Start at a random node and choose the smallest edge at each node
# Runs in O(n^2)
def greed_triv(graph, start, to_visit, out):
    # If you have run out of nodes to visit, return
    if not to_visit:
        return out
    to_visit.remove(start)
    out.append(start)
    lowest_cost = 101
    low_node = start
    for node in to_visit:
        if graph.edges[(start, node)] < lowest_cost:
            lowest_cost, low_node = graph.edges[(start, node)], node
    return greed_triv(graph, low_node, to_visit, out)


# Greedy optimization: Algorithm uses repeated greedy runs to output the most frequent
# repeated nodes without and increase by a factor of n

def greed_repeat(graph, start, to_visit, out, attempts):
    runs = []
    for i in range(1, attempts):
        runs.appends(greed_triv(graph, start, to_visit, out))
