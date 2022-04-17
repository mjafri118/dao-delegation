import numpy as np

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The subset size.
#     weights: (np.ndarray) A size N array where entry i is the weight of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#   Output:
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].

def normal(N: int, K: int, weights: np.ndarray) -> np.ndarray:
  competences = [0] * N
  for i in range(N):
    while True:
      competences[i] = np.random.default_rng().normal(loc=0.5, scale=0.15, size=1).item()
      if (competences[i] >= 0 and competences[i] <= 1):
        break
  return competences