import numpy as np

def softmax(x: np.ndarray)-> np.ndarray:
  e_x = np.exp(x - np.max(x, axis=0))
  return e_x / e_x.sum(axis=0)