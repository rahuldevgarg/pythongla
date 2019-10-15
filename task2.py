import numpy as np

L = list(map(int, input("Enter space separated value : ").split()))
a = np.array(L)
a.shape = (3, 3)  # doesn't return
print(a)
a = a.reshape(3, 3)  # returns value 
print(a)
