import numpy as np
import itertools as it

A = np.array([
  [2,1],
  [4,5,6],
  [7,8,9,3]
], dtype=object)

print(A)

for i, row in enumerate(A):
  print(i, row)