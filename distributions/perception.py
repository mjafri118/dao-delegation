import numpy as np

# Functions in this file should adhere to the following pattern:
#   Input:
#     N: (int) The number of agents.
#     K: (int) The subset size.
#     weights: (np.ndarray) A size N array where entry i is the weight of agent i. Each entry should be in the interval [0,1]. The sum of the entries should be 1.
#     competences: (np.ndarray) A size N array where entry i is the true competence of agent i. Each entry should be in the interval [0,1].
#   Output:
#     perceptions: (np.ndarray) A size N x N array where entry ij is the perception value agent i has for agent j. Each entry should be in the interval [0,1].

def uniform(N: int, K: int, weights: np.ndarray, competences: np.ndarray) -> np.ndarray:
  return np.random.default_rng().uniform(low=0.0, high=1.0, size=(N,N))


#perception drawn from normal distribution with mean = true competence and variance is a function of your own competence. The more competent you are, the more 
#likely you are to accurately guess the competence of others
def normalPerception(N: int, K: int, weights: np.ndarray, competences: np.ndarray) -> np.ndarray:
  NORNALIZATION = 0.5 
  completePerceptions = []
  for agentC in competences:
    perceptions = []
    for voterC in competences:
      if (agent != voter):
        perceptions.append(np.random.normal(agentC,voterC * NORNALIZATION))
      else:
        perceptions.append(agentC) #if you are guessing about yourself, guess true competence
      completePerceptions.append(perceptions)
    return completePerceptions
    
#perception as true competence
def truePerception(N: int, K: int, weights: np.ndarray, competences: np.ndarray) -> np.ndarray:
    completePerceptions = []  
    for agent in competences:
      completePerceptions.append(competences)
    return completePerceptions
  
  
#perception as a function of personal knowledge about other voters
def knowledgePerception(N: int, K: int, weights: np.ndarray, competences: np.ndarray) -> np.ndarray:
  NORNALIZATION = 0.7 
  THRESHOLD = 0.2
  
  completePerceptions = []
  for agent in competenes:   
    knowledgeVec = []
    for voter in competences:
      if voter != agent: #not yourself
        probKnown = np.random.uniform(0,1)
        if probKnown >= THRESHOLD:
          #if you know them --> get tru competence
          knowledgeVec.append(voter) 
        else:
          #else normal distribution with high variance
          knowledgeVec.append(np.random.normal(agentC,voterC * NORNALIZATION)) 
      else:
        #else it was yourself so get true competence
        knowledgeVec.append(voter) 
      completePerceptions.append(knowledgeVec)
    return completePerceptions
 
  
    
  

