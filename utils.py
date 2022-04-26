from re import L
import numpy as np

def softmax(x: np.ndarray)-> np.ndarray:
  e_x = np.exp(x - np.max(x, axis=0))
  return e_x / e_x.sum(axis=0)

def is_path(graph, u, v, checked):
  checked[u] = 1
  for child in graph[u]:
    if checked[child] == 1:
      continue
    if child == v:
      return True
    if is_path(graph, child, v, checked):
      return True
  return False

def calculate_neighbors(N, K, weights, competences, perceptions, limits):
  """
  Input:
    N: (int) The number of agents.
    K: (int) The global delegation limit.
    weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
    competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
    perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
    limits: (np.ndarray) A size N array where entry i is the maximum number of out neighbors for agent i. Each entry should be an integer in the set {1,2,...,K}.
  Output:
    in_neighbors: (list[list]) A size N list where entry i is the list of agents to which agent i delegates. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
    out_neighbors: (list[list]) A size N list where entry i is the list of agents that delegate to agent i. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
  """
  in_neighbors = [[] for _ in range(N)]
  out_neighbors = [[] for _ in range(N)]
  for agent, agent_perceptions in enumerate(perceptions):
    num_out_neighbors = 0
    best_out_neighbors = np.argsort(-1 * agent_perceptions)
    for out_neighbor in best_out_neighbors:
      # no zero perception out neighbors
      if perceptions[agent, out_neighbor] == 0:
        break
      # check if adding this agent as a neighbor would cause a cycle
      if not is_path(out_neighbors, out_neighbor, agent, np.zeros(N)):
        out_neighbors[agent].append(out_neighbor)
        in_neighbors[out_neighbor].append(agent)
        num_out_neighbors += 1
        # stop if neighbor limit is reached
        if num_out_neighbors >= limits[agent]:
          break
  return in_neighbors, out_neighbors

def calculate_delegations(N, K, weights, competences, perceptions, limits, in_neighbors, out_neighbors, splits):
  """
  Input:
    N: (int) The number of agents.
    K: (int) The global delegation limit.
    weights: (np.ndarray) A size N array where entry i is the voting share of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
    competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
    perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].
    limits: (np.ndarray) A size N array where entry i is the maximum number of out neighbors for agent i. Each entry should be an integer in the set {1,2,...,K}.
    in_neighbors: (list[list]) A size N list where entry i is the list of agents to which agent i delegates. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
    out_neighbors: (list[list]) A size N list where entry i is the list of agents that delegate to agent i. Each entry in the sub-lists should be an integer in the set {1,2,...,N}
    splits: (list[list]) A size N list that corresponds to out_neighbors but with delegation shares instead of agent indices.
  Output:
    delegations: (np.ndarray) A size N array where entry i is the voting share of agent i after all delegations. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
  """
  intermediate_delegations = np.copy(weights)
  final_delegations = np.zeros(N)

  while(True):
    for agent in range(N):
      weight = intermediate_delegations[agent]
      intermediate_delegations[agent] = 0
      for out_neighbor, split in zip(out_neighbors[agent], splits[agent]):
        if out_neighbor == agent:
          final_delegations[out_neighbor] += weight * split
        else:
          intermediate_delegations[out_neighbor] += weight * split
    if sum(intermediate_delegations) == 0:
      break
  return final_delegations