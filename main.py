import matplotlib.pyplot as plt
import numpy as np

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
  N = 5
  K = 2

  dist_weight = weight.exponential
  dist_competence = competence.normal
  dist_perception = perception.uniform
  dist_split = split.even

  weights = dist_weight(N, K)
  print(weights)
  print()
  competences = dist_competence(N, K, weights)
  print(competences)
  print()

  perceptions = dist_perception(N, K, weights, competences)
  print(perceptions)
  print()

  subsets = calculate_subsets(N, K, perceptions)
  print(subsets)
  print()

  delegations = dist_split(N, K, weights, competences, perceptions, subsets)
  print(delegations)
  print()

  correct_vote_share = 0
  flags = np.random.rand(N)
  for vote, comp, flag in zip(delegations, competences, flags):
    if (flag > comp):
      correct_vote_share += vote
  
  print(correct_vote_share)
  print()

  if correct_vote_share >= 0.5:
    print("Correct Alternative Wins!")
  else:
    print("Incorrect Alternative Wins :(")
    





main()

# W = weight.exponential(1000,0.7)