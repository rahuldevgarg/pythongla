import numpy as np

L = list(map(int, input("Enter space separated value : ").split()))
L.reverse()
a = np.array(L,dtype=float)
print(a)
