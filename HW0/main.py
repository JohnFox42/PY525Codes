#Dependencies 
import numpy as np

#(1)
def MatrixMult(A,B):
    if len(A) != len(B):
        print("lengths of A and B don't match")
        return 0
    n = len(A)
    #initialize C

    C = np.zeros((n,n))
    Sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Sum += (-1)**(i+j+k)*A[i,k]*B[k,j]
            C[i,j] = Sum
            Sum = 0
    return C 

#Initializing two matricies of nxn
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

#Testing matrix mult. function
print(MatrixMult(A,B))
