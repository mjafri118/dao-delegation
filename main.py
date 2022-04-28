import numpy as np

from distributions import weight
from distributions import competence
from distributions import perception
from distributions import limit
from distributions import split
from utils import calculate_neighbors, calculate_delegations

np.set_printoptions(precision=2)

def main():
  num_agents = 50
  trials_per_limit = 1000
  limit_list = np.arange(1, num_agents+1, dtype=int)

  binary_results = np.zeros((len(limit_list), trials_per_limit), dtype=int)
  accuracy_results = np.zeros((len(limit_list), trials_per_limit))
  concentration_results = np.zeros((len(limit_list), trials_per_limit))

  for i, limit in enumerate(limit_list):
    for j in range(trials_per_limit):
      print(f'{i * trials_per_limit + j}', end=" ", flush=True)
      binary_results[i, j], accuracy_results[i,j], concentration_results[i,j] = trial(num_agents, limit)
  print()
  
  prefix = "25ennuw"
  np.savetxt(f'results/{prefix}-binary.dat', binary_results, delimiter=",", fmt="%d")
  np.savetxt(f'results/{prefix}-accuracy.dat', accuracy_results, delimiter=",", fmt="%.4f")
  np.savetxt(f'results/{prefix}-concentration.dat', concentration_results, delimiter=",", fmt="%.4f")


def trial(N, K):
  """
  Returns 1 if the correct alternative wins, 0 otherwise.
  """
  dist_weight = weight.exponential
  dist_competence = competence.normal
  dist_perception = perception.normal
  dist_limit = limit.uniform
  dist_split = split.weighted

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

  if correct_vote_share >= 0.25:
    return 1, correct_vote_share, delegations.max()
  else:
    return 0, correct_vote_share, delegations.max()

main()