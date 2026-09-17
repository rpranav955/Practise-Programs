import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
res = np.einsum('ij,jk->ik', a, b)
print(res)
