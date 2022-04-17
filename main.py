import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from math import log2

from distributions import weight
from distributions import competence
from distributions import perception
from distributions import split
from utils import softmax


def calculate_subsets(N: int, K: int, perceptions: np.ndarray) -> np.ndarray:
  """
  Input:
    N: (int) The number of agents.
    K: (int) The subset size.
    perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
  Output:
    subsets: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1]. In each row, only the largest K values are unmasked.
  """
  subset_indices = np.concatenate((np.indices((N,N-K))[0], np.argsort(perceptions, axis=1)[:,:N-K]), axis=0).reshape(2,N*(N-K))
  perceptions_mask = np.zeros(N * N)
  perceptions_mask[np.ravel_multi_index(subset_indices, (N,N))] = 1
  return np.ma.masked_array(perceptions, mask=perceptions_mask)

def main():
  trials_per_K = 100
  N = 1000 # keep as a multiple of 100
  K = np.linspace(1, N, num=100, dtype=int)

  results = np.zeros((len(K), trials_per_K))

  for i, k in enumerate(K):
    for j in range(trials_per_K):
      print(f'{i*trials_per_K + j}', end=" ", flush=True)
      results[i, j] = trial(N, k)

  results = results.sum(axis=1) / trials_per_K

  plt.plot(K, results)
  plt.title("Results")
  plt.xlabel("K")
  plt.ylabel("Correct Outcomes / Total Outcomes")
  plt.savefig("results.png")



def trial(N: int, K: int) -> int:
  """
  Returns 1 if the correct alternative wins, 0 otherwise.
  """
  dist_weight = weight.exponential
  dist_competence = competence.normal
  dist_perception = perception.uniform
  dist_split = split.even

  weights = dist_weight(N, K)
  competences = dist_competence(N, K, weights)
  perceptions = dist_perception(N, K, weights, competences)
  subsets = calculate_subsets(N, K, perceptions)
  delegations = dist_split(N, K, weights, competences, perceptions, subsets)

  correct_vote_share = 0
  flags = np.random.rand(N)
  for vote, comp, flag in zip(delegations, competences, flags):
    if (flag > comp):
      correct_vote_share += vote

  if correct_vote_share >= 0.5:
    return 1.0
  else:
    return 0.0





main()


