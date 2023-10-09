import numpy as np
import matplotlib.pyplot as plt

# Transmission capacity (R) in bits per second
R = 5

pa = [0.25, 0, 0.5, 0]
pb = [0.25, 0.5, 0, 0]
pc = [0.25, 0.5, 0, 0]
pd = [0.25, 0, 0.5, 1]

# Range of communication probabilities (p) from 0 to 1
p_values = np.linspace(0, 0.99, 101)


def simulate_average_queue_length(p, pa, pb, pc, pd):
    queue_lengths = []
    queue_size = 0
    for prob in p:
        for _ in range(10000):  # Simulate for a large number of time steps
            if np.random.rand() < prob:
                packet_size = np.random.choice([2, 4, 6, 8], p=[pa, pb, pc, pd])
                queue_size = max(0, queue_size + packet_size - R)
            else:
                queue_size = max(0, queue_size - R)
        queue_lengths.append(queue_size)

    return queue_lengths


def simulate_average_packet_delay(p, pa, pb, pc, pd):
    delays = []

    for prob in p:
        total_delay = 0
        packets_transmitted = 0
        for _ in range(10000):
            if np.random.rand() < prob:
                packet_size = np.random.choice([2, 4, 6, 8], p=[pa, pb, pc, pd])
                transmission_time = packet_size / R
                total_delay += transmission_time
                packets_transmitted += 1

        average_delay = (
            total_delay / packets_transmitted if packets_transmitted > 0 else 0
        )
        delays.append(average_delay)

    return delays


for i in range(4):
    # Simulate and plot for Case (i)
    queue_lengths = simulate_average_queue_length(p_values, pa[i], pb[i], pc[i], pd[i])
    # delays = simulate_average_packet_delay(p_values, pa[i], pb[i], pc[i], pd[i])

    # Plot the results
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.plot(p_values, queue_lengths)
    plt.title(f"Average Queue Length vs. p (Case {i+1})")
    plt.xlabel("p")
    plt.ylabel("Average Queue Length")

    # plt.subplot(2, 2, 2)
    # plt.plot(p_values, delays)
    # plt.title(f"Average Packet Delay vs. p (Case {i+1})")
    # plt.xlabel("p")
    # plt.ylabel("Average Packet Delay")

    # plt.tight_layout()
    plt.savefig(f"case{i+1}.png")
