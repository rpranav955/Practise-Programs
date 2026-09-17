import numpy as np
n = np.arange(1, 11)
phi = (1 + np.sqrt(5)) / 2
fib = (phi**n - (-phi)**(-n)) / np.sqrt(5)
print(np.round(fib).astype(int))
