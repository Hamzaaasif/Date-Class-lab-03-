#*****Min and Max****
import numpy as np
N,M=[int(n) for n in input().strip().split()]
arr=np.array([[int (n) for n in input().strip().split()] for i in range(N)])
print(np.max(np.min(arr,axis=1)))

#***Dot product ****
N=int(input())
A=np.array([[int(n) for n in input().strip().split()] for i in range(N)])
B=np.array([[int(n) for n in input().strip().split()] for i in range(N)])
print(np.dot(A,B))

#****mean,var and std ***
N,M=[int(n) for n in input().strip().split()]
arr=np.array([[int (n) for n in input().strip().split()] for i in range(N)])
np.set_printoptions(legacy='1.13')
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.std(arr))