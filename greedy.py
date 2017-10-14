# Greedy: A file summarizing varying Greedy algorithms to solve the Traveling
#         Salesman problem



# Trivial Heuristic 1: Start at a random node and choose the smallest edge at each node

def greed_triv(graph, start, to_visit, out):
    if not to_visit:
        return out
    next_set = to_visit
    next_set.remove(start)
    out.append(start)
    lowest_cost = 101
    low_node = start
    for node in next_set:
        if graph.edges[(start, node)] < lowest_cost:
            lowest_cost, low_node = graph.edges[(start, node)], node
    return greed_triv(graph, low_node, to_visit, out)
