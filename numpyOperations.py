import numpy as np

N, M = map(int, input("Enter in N M : ").split(' '))
L = list(map(int, input("Enter space separated value for array : ").split()))
A = np.array(L)
A.shape = (N, M)  # doesn't return
L = list(map(int, input("Enter space separated value for array : ").split()))
B = np.array(L)
B.shape = (N, M)  # doesn't return
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
