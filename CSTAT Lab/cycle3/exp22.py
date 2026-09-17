import numpy as np
mat = np.array([[1, 2], [2, 1]])
evals, evecs = np.linalg.eig(mat)
print(evals)
print(evecs)
