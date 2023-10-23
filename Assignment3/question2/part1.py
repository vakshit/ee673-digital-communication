# Graph of the network in the format {(node1, node2): weight, ...}
nodes = {(0, 1): 1, (0, 2): 3, (0, 3): 7, (1, 2): 1, (2, 3): 2}


# Find the node with the nearest distance
def min_distance(distances, vis):
    min_dist = float("inf")
    min_node = None
    for node in range(len(distances)):
        if distances[node] < min_dist and not vis[node]:
            min_dist = distances[node]
            min_node = node
    return min_node


# Function to print the routing table
def routing_table(node, distances, previous_nodes):
    print(f" Routing table for node: {node}")
    print("-" * 30)
    print(" Destination | Cost | Path")
    print("-" * 30)

    for i in range(len(distances)):
        if i != node:
            path = []
            curr_node = i
            while curr_node is not None:
                path.insert(0, curr_node)
                curr_node = previous_nodes[curr_node]
            print(f"   {node} -> {i}    |   {distances[i]}  |  {path}")
    print()


# Dijkstra's algorithm
def dijkstra(nodes, start_node):
    num_nodes = len(set(sum(nodes.keys(), ())))

    distances = [float("inf")] * num_nodes
    previous_nodes = [None] * num_nodes
    vis = [False] * num_nodes

    distances[start_node] = 0

    for _ in range(num_nodes):
        current_node = min_distance(distances, vis)
        vis[current_node] = True

        for edge, weight in nodes.items():
            if current_node in edge:
                neighbor = edge[0] if edge[1] == current_node else edge[1]
                if (
                    not vis[neighbor]
                    and distances[neighbor] > distances[current_node] + weight
                ):
                    distances[neighbor] = distances[current_node] + weight
                    previous_nodes[neighbor] = current_node
    return distances, previous_nodes


# Run the routing algorithm for each node
for node in range(4):
    distances, previous_nodes = dijkstra(nodes, node)

    routing_table(node, distances, previous_nodes)
