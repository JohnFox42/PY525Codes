#Dependencies 
import numpy as np
import random
import math
import matplotlib.pyplot as plt 

#(1)
print("Question 1:")
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


#(2)
print("Question 2:")
#Generate all possibilities 
pDic = {}
counter = 0
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                pDic.update({counter:np.array([(-1)**a,(-1)**b,(-1)**c,(-1)**d])})
                counter += 1
#Finding the expected E
ESum = 0
for x in pDic.values():
    E = x[0]*x[1]+x[1]*x[2]+x[2]*x[3]+x[3]*x[0]
    ESum += E*np.e**(-E)
print(ESum)


#Question 3
#For writeup, make sure to cite permutator and talk about same path prevention
print("Question 3")
#Generate the points, do later
Points = {}
for i in range(7):
    Points.update({i:[random.random(),random.random()]})
print("Points:",Points)

#Path permutation generation algorithm
#Source: https://www.geeksforgeeks.org/dsa/print-all-possible-permutations-of-an-array-vector-without-duplicates-using-backtracking/
# Recursive function to find all possible permutations
def permutations(res, arr, idx):
    if idx == len(arr):
        res.append(arr[:])
        return

    # Permutations made by swapping each element starting from index `idx`
    for i in range(idx, len(arr)):
        # Swapping
        arr[idx], arr[i] = arr[i], arr[idx]

        # Recursive call
        permutations(res, arr, idx + 1)

        # Backtracking
        arr[idx], arr[i] = arr[i], arr[idx]

# Function to get the permutations
def permuteDist(arr):
    res = []
    permutations(res, arr, 0)
    return res

arr = [0,1,2,3,4,5,6]
res = permuteDist(arr)

#Minimize the path legnth
MinPath = []
MinPathLength = 99999
ShortestPath = []
SecondShortestPath = []
for x in res:
    PathLength = 0
    #Prevents the same path from being considered as a flipped array will have the same path as its original
    if x[::-1] == ShortestPath:
        continue
    for i in range(len(x)):
        if i == 0:
            continue
        SecondKey = x[i]
        FirstKey = x[i-1]
        SecondPoint = Points[SecondKey]
        FirstPoint = Points[FirstKey]
        PathLength += math.dist(SecondPoint,FirstPoint)
    if PathLength < MinPathLength:
        MinPathLength = PathLength
        SecondShortestPath=ShortestPath
        ShortestPath=x
print("Shortest Path: ",ShortestPath)
print("Second Shortest Path: ",SecondShortestPath)

#Graphing the points
plt.figure(1)
for i in Points.values():
    plt.scatter(i[0],i[1],color="b")
#Graphing the shortest path
for i in range(len(ShortestPath)):
    if i == 0:
        continue
    StartKey = ShortestPath[i-1]
    EndKey = ShortestPath[i]
    StartPoint = Points[StartKey]
    EndPoint = Points[EndKey]
    x = np.linspace(StartPoint[0],EndPoint[0],100)
    y = np.linspace(StartPoint[1],EndPoint[1],100)
    plt.plot(x,y,color="b")
plt.draw()

#Graphing the points
plt.figure(2)
for i in Points.values():
    plt.scatter(i[0],i[1],color="g")
#Graphing the second shortest path
for i in range(len(ShortestPath)):
    if i == 0:
        continue
    StartKey = SecondShortestPath[i-1]
    EndKey = SecondShortestPath[i]
    StartPoint = Points[StartKey]
    EndPoint = Points[EndKey]
    x = np.linspace(StartPoint[0],EndPoint[0],100)
    y = np.linspace(StartPoint[1],EndPoint[1],100)
    plt.plot(x,y,color="g")
plt.draw()
plt.show()


#Question 4
#For writeup, talk about treatment of 0
#Defining the trapezoidal integrator
def TrapIntegrator(f,a,b,N):
    h = (b-a)/N
    x = np.linspace(a,b,N+1)
    Sum = 0
    for i in range(N):
        Sum += (h/2)*(f(x[i])+f(x[i+1]))
    return Sum 

#Defining the Integrand
def g(p):
    return np.sin(p)/np.sqrt(p)

#Defining the Integrator function
def I(t):
    return TrapIntegrator(g,0.000001,t,9999)

#Plotting 
x = np.linspace(0.000001,100,301)
plt.plot(x,I(x))
plt.show()



#Question 5
#Initializing the zero matrix 
N = 10
s = np.zeros([N+1,N+1])
for i in range(N+1):
    for j in range(N+1):
        prob = random.random()
        if prob > 0.33:
            continue
        elif prob <= 0.33:
            s[i,j] = 1

#Printing the empty and filled dots
for i in range(N+1):
    for j in range(N+1):
        if s[i,j] == 1:
            plt.scatter(i,j,color="b")
        elif s[i,j] == 0:
            plt.scatter(i,j,facecolors="none",edgecolors="b")
plt.show()

