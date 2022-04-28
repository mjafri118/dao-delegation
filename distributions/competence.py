import numpy as np
import scipy.stats as stats

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The global delegation limit.
#     weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#   Output:
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].

def normal(N, K, weights):
  mu, sigma, lower, upper = 0.6, 0.1, 0, 1
  return np.array(stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma).rvs(N))

def weighted(N, K, weights):
  competences = np.zeros(N)
  for i in range(N):
    competences[i] = weights[i] / np.sum(weights)
  competences = competences / (np.max(competences)) / 2
  return competences
  
def tiered(N, K, weights):
  competences = np.zeros(N)
  one_q = np.quantile(weights, 0.25)
  two_q = np.quantile(weights, 0.5)
  three_q = np.quantile(weights, 0.75)
  for i in range(N):
    if weights[i] < one_q:
        competences[i] = 0.1    # can pick whatever values
    elif weights[i] < two_q:
        competences[i] = 0.3
    elif weights[i] < three_q:
        competences[i] = 0.5
    else:
        competences[i] = 0.7
  return competences
