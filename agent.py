import numpy as np
from typing import Callable


from utils import softmax



class Agent:
  def __init__(self, id: int, weight: float):
    self.id: int = id
    self.weight: float = weight
    self.competence = 0.0
    self.perception = []
    self.subset = []
  
  def set_competence(self, dist_competence: Callable[[float], float]) -> None:
    self.competence: float = dist_competence(self.weight)

  def set_perception(self, perception: list[float]) -> None:
    self.perception: list[tuple[int, float]] = [(i,x) for i, x in enumerate(perception)]

  def pick_subset(self, K: int):
    self.subset: list[tuple[int, float]] = sorted(self.perception, key=lambda x: x[1])[:K]

  def set_split(self, split) -> None:
    