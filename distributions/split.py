import numpy as np

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The subset size.
#     weights: (np.ndarray) A size N array where entry i is the weight of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
#     perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
#     subsets: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1]. In each row, only the largest K values are unmasked.
#   Output:
#     delegations: (np.ndarray) A size N array where entry i is the voting share of agent i after delegation. Each entry should be in the interval [0,1]. The sum of the entries should be 1.

def even(N: int, K: int, weights: np.ndarray, competences: np.ndarray, perceptions: np.ndarray, subsets: np.ndarray) -> np.ndarray:
  delegations = subsets / subsets.sum(axis=1).reshape((N,1))
  delegations *= weights.reshape((N,1))
  return delegations.sum(axis=1).data
