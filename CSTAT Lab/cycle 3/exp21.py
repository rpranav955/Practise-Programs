import numpy as np
mat = np.array([[1, 2], [3, 4]])
q, r = np.linalg.qr(mat)
print(q)
print(r)
