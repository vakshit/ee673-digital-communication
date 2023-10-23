from sys import maxsize as INF

NUM_NODES = 4

# Define the nodes
nodes = []


# Define the routing packet class
class rkpkt:
    def __init__(self, source_id, dest_id, min_cost_table):
        self.source_id = source_id
        self.dest_id = dest_id
        self.min_cost_table = min_cost_table


# Define the node class
class Node:
    def __init__(self, _id):
        self.id = _id
        self.distance_table = [INF, INF, INF, INF]
        self.distance_table[self.id] = 0

    def rt_init(self, dist_table):
        for i in range(len(self.distance_table)):
            self.distance_table[i] = min(self.distance_table[i], dist_table[i])
        self.distance_table[self.id] = 0
        self.rt_send()

    def rt_send(self):
        global nodes
        for i in range(NUM_NODES):
            if i != self.id:
                pkt = rkpkt(self.id, i, self.distance_table)
                nodes[i].rt_update(pkt)
        return

    def rt_update(self, pkt: rkpkt):
        global nodes
        source = pkt.source_id
        min_cost_table = pkt.min_cost_table
        updated = False
        for i in range(NUM_NODES):
            # Update if a better distance is offered.
            offered_distance = self.distance_table[i] + min_cost_table[i]
            if self.distance_table[source] > offered_distance:
                self.distance_table[source] = offered_distance
                updated = True
        if updated:
            self.rt_send()
        return


def print_distance_table():
    print("Distance Table:")
    print("Nodes in order 0, 1, 2, 3")
    for i in range(NUM_NODES):
        print(f" {i} -> {nodes[i].distance_table}")


def main():
    global nodes
    nodes = [Node(i) for i in range(NUM_NODES)]

    # Initialise the path costs for each node to the other.
    nodes[0].rt_init([0, 1, 3, 7])
    nodes[1].rt_init([1, 0, 1, INF])
    nodes[2].rt_init([3, 1, 0, 2])
    nodes[3].rt_init([7, INF, 2, 0])
    print_distance_table()


if __name__ == "__main__":
    main()
