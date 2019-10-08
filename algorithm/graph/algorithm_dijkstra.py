graph = {}
""" Create graph table """
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

""" Create costs table """
costs = {}
infinity = float("inf")

costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

""" Create parents table """
parents = {}

parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

""" Create list complete check nodes """
processed = []


def find_lowest_cost_node(_costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for _node in costs:
        _cost = costs[_node]
        if _cost < lowest_cost and _node not in processed:
            lowest_cost = _cost
            lowest_cost_node = _node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(parents)
