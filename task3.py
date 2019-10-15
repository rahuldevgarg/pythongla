import numpy as np
N, M = map(int, input("Enter in NxM : ").split('x'))
A = np.eye(N, M, dtype=float)
print(A)
