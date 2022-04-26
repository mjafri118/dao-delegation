import numpy as np

from utils import softmax

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The global delegation limit.
#   Output:
#     weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.

# Outputs vote shares in an exponential distribution
def exponential(N: int, K: int) -> np.ndarray:
  """
  The exponential distribution. Beta must be greater than 0, and larger values cause increased concentration of voting power
  """
  beta: float = 0.7
  return softmax(np.random.default_rng().exponential(beta, N))

def even(N: int, K: int) -> np.ndarray:
  return np.ones(N, dtype=float) / N