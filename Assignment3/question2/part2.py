class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor.name] = neighbor
        self.routing_table[neighbor.name] = cost

    def receive_routing_table_from_neighbor(
        self, neighbor_routing_table, neighbor_name
    ):
        updated = False
        for dest, cost in neighbor_routing_table.items():
            if (
                dest not in self.routing_table
                or self.routing_table[dest] > cost + self.routing_table[neighbor_name]
            ):
                self.routing_table[dest] = cost + self.routing_table[neighbor_name]
                updated = True
        return updated

    def __str__(self):
        return f"Node {self.name} {self.routing_table}"


def distance_vector_algorithm(nodes):
    while True:
        updates = False
        for node in nodes:
            for neighbor_name, neighbor_node in node.neighbors.items():
                if node.receive_routing_table_from_neighbor(
                    neighbor_node.routing_table, neighbor_name
                ):
                    updates = True
        if not updates:
            break


# Example
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.add_neighbor(B, 1)
A.add_neighbor(C, 3)
A.add_neighbor(D, 7)

B.add_neighbor(A, 1)
B.add_neighbor(C, 1)

C.add_neighbor(A, 3)
C.add_neighbor(B, 1)
C.add_neighbor(D, 2)

D.add_neighbor(A, 7)
D.add_neighbor(C, 2)

nodes = [A, B, C, D]
distance_vector_algorithm(nodes)

for node in nodes:
    print(node)
