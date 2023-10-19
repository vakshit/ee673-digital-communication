def dijkstra(graph, start):
    shortest_path = {}
    predecessor = {}
    unseenNodes = graph.copy()
    infinity = float("inf")

    for node in unseenNodes:
        shortest_path[node] = infinity
    shortest_path[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_path[node] < shortest_path[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_path[minNode] < shortest_path[childNode]:
                shortest_path[childNode] = weight + shortest_path[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    return shortest_path


graph = {
    "A": {"B": 1, "C": 3, "D": 7},
    "B": {"A": 1, "C": 1},
    "C": {"A": 3, "B": 1, "D": 2},
    "D": {"A": 7, "C": 2},
}

for node in graph:
    distances = dijkstra(graph, node)
    print(f"Distances from node {node}: {distances}")
