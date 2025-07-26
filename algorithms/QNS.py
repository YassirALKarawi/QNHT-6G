# Quantum Neural Synchronization (QNS)
import numpy as np

def quantum_neural_synchronization(gradients, theta, eta=0.1):
    """
    Apply synchronization rule to QNN parameters across distributed units.
    Parameters:
        gradients: list of np.array, gradients ∇θJ_i from all DUs
        theta: list of np.array, current parameters of each DU
        eta: learning rate
    Returns:
        updated_theta: list of np.array, updated parameters
    """
    N = len(theta)
    updated_theta = []
    for i in range(N):
        avg_grad_diff = sum([gradients[i] - gradients[j] for j in range(N) if j != i]) / (N - 1)
        updated_theta.append(theta[i] - eta * avg_grad_diff)
    return updated_theta
