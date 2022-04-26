import numpy as np

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The global delegation limit.
#     weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
#     perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
#     limits: (np.ndarray) A size N array where entry i is the maximum number of out neighbors for agent i. Each entry should be an integer in the set {1,2,...,K}.
#     in_neighbors: (list[list]) A size N list where entry i is the list of agents to which agent i delegates. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
#     out_neighbors: (list[list]) A size N list where entry i is the list of agents that delegate to agent i. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
#   Output:
#     splits: (list[list]) A size N list that corresponds to out_neighbors but with delegation shares instead of agent indices.

def even(N, K, weights, competences, perceptions, limits, in_neighbors, out_neighbors):
  splits = [[] for _ in range(N)]
  for agent, agent_out_neighbors in enumerate(out_neighbors):
    for neighbor in agent_out_neighbors:
      splits[agent].append(perceptions[agent, neighbor])
    normalization = sum(splits[agent])
    splits[agent] = [x / normalization for x in splits[agent]]
  return splits