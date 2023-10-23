import numpy as np

# Define the transition matrix
P = np.array(
    [
        [0.5, 0.25, 0.25, 0],
        [0.25, 0.25, 0.25, 0.25],
        [0.25, 0.25, 0.25, 0.25],
        [0.0, 0.25, 0.25, 0.5],
    ]
)

# Compute the stationary distribution
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary_vector = eigenvectors[:, np.isclose(eigenvalues, 1)]
stationary_vector = stationary_vector[:, 0]
stationary_distribution = stationary_vector / stationary_vector.sum()

print(stationary_distribution)
