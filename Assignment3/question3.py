import numpy as np

# Define the transition matrix
P = np.array([[0, 0.5, 0.5, 0], [0.5, 0, 0, 0.5], [0.5, 0, 0, 0.5], [0, 0.5, 0.5, 0]])

# Compute the stationary distribution
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary_vector = eigenvectors[:, np.isclose(eigenvalues, 1)]
stationary_vector = stationary_vector[:, 0]
stationary_distribution = stationary_vector / stationary_vector.sum()

print(stationary_distribution)

# The throughput for each input can be calculated as follows:

# For input 1:

# When the system is in state 11 or 12, input 1 can send its packet to output 1.
# When the system is in state 21 or 22, input 1 is blocked by input 2 (due to HOL blocking) and cannot send its packet.
# For input 2:

# When the system is in state 21 or 22, input 2 can send its packet to output 2.
# When the system is in state 11 or 12, input 2 is blocked by input 1 and cannot send its packet.
# Given the stationary distribution π (which we previously computed using the transition matrix), the throughput T for each input is:
# t1 = pi(11) + pi(12)
# t2 = pi(21) + pi(22)
# where both of them is a stationary distribution of the Markov chain.
