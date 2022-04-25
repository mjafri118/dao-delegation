import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from math import log2

from distributions import weight
from distributions import competence
from distributions import perception
from distributions import limit
from distributions import split
from utils import calculate_neighbors, calculate_delegations

np.set_printoptions(precision=2)

def main():
  num_agents = 10
  num_limits = 5
  trials_per_limit = 100000
  limit_list = np.arange(1, num_agents, num_agents / num_limits, dtype=int)

  results = np.zeros((len(limit_list), trials_per_limit))

  for i, limit in enumerate(limit_list):
    for j in range(trials_per_limit):
      print(f'{i * trials_per_limit + j}', end=" ", flush=True)
      results[i, j] = trial(num_agents, limit)

  results = results.sum(axis=1) / trials_per_limit

  plt.plot(limit_list, results)
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
  dist_limit = limit.uniform
  dist_split = split.even

  weights = dist_weight(N, K)
  competences = dist_competence(N, K, weights)
  perceptions = dist_perception(N, K, weights, competences)
  limits = dist_limit(N, K, weights, competences, perceptions)

  in_neighbors, out_neighbors = calculate_neighbors(N, K, weights, competences, perceptions, limits)
  splits = dist_split(N, K, weights, competences, perceptions, limits, in_neighbors, out_neighbors)

  delegations = calculate_delegations(N, K, weights, competences, perceptions, limits, in_neighbors, out_neighbors, splits)

  correct_vote_share = 0
  flags = np.random.rand(N)
  for vote, comp, flag in zip(delegations, competences, flags):
    if (flag < comp):
      correct_vote_share += vote

  if correct_vote_share >= 0.5:
    return 1.0
  else:
    return 0.0

main()