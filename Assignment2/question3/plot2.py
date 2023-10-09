import random
import matplotlib.pyplot as plt

# Constants
R = 5  # Transmission capacity
TIME_INSTANTS = 10000  # Number of time instants for the simulation

# Packet sizes
a, b, c, d = 2, 4, 6, 8

# Probabilities for the different cases
cases = [[0.25, 0.25, 0.25, 0.25], [0, 0.5, 0.5, 0], [0.5, 0, 0, 0.5], [0, 0, 0, 1]]


def generate_packet_size(probabilities):
    rand_val = random.random()
    if rand_val < probabilities[0]:
        return a
    elif rand_val < sum(probabilities[:2]):
        return b
    elif rand_val < sum(probabilities[:3]):
        return c
    else:
        return d


def simulate_queue(p, probabilities):
    queue_length = 0
    total_delay = 0
    total_packets = 0

    for t in range(TIME_INSTANTS):
        if random.random() < p:  # User communicates
            packet_size = generate_packet_size(probabilities)
            queue_length += packet_size
            if queue_length > R:
                delay = (queue_length - R) / R
                total_delay += delay
            total_packets += 1
        queue_length -= R  # Transmission capacity
        if queue_length < 0:
            queue_length = 0

    average_queue_length = queue_length
    average_delay = total_delay / total_packets if total_packets > 0 else 0

    return average_queue_length, average_delay


# Main simulation
p_values = [i / 100 for i in range(99)]
for case in cases:
    avg_queue_lengths = []
    avg_delays = []
    for p in p_values:
        avg_ql, avg_d = simulate_queue(p, case)
        avg_queue_lengths.append(avg_ql)
        avg_delays.append(avg_d)

    # plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, cases.index(case) + 1)
    plt.plot(
        p_values, avg_queue_lengths, label=f"Case {cases.index(case) + 1} Queue Length"
    )
    plt.subplot(2, 2, cases.index(case) + 1)
    plt.plot(
        p_values,
        avg_delays,
        label=f"Case {cases.index(case) + 1} Delay",
        linestyle="--",
    )
    plt.legend()

    plt.xlabel("p")
    plt.ylabel("Value")
plt.title("Network Queuing Simulation")
plt.show()
