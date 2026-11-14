import numpy as np
arr3d = np.arange(27).reshape(3, 3, 3)
diags = np.diagonal(arr3d, axis1=1, axis2=2)
print(diags)
