import numpy as np

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The global delegation limit.
#     weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
#     perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
#   Output:
#     limits: (np.ndarray) A size N array where entry i is the maximum number of out neighbors for agent i. Each entry should be an integer in the set {1,2,...,K}.

def uniform(N, K, weights, competences, perceptions):
  return np.random.default_rng().integers(1, K, N, endpoint=True)

def best(N, K, weights, competences, perceptions):
  return np.ones(N)