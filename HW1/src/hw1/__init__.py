#import statements
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import random 

def main() ->None:
    #Question 1 
    print("Question 1")
    def GenerateZ():
        z = 0
        for i in range(12):
            z += random.random()
        return z 
    def Gauss(x,a,x0,sigma):
        return a*np.e**(-(x-x0)**2/(2*sigma**2))
    data = []
    for i in range(10**6):
        data.append(GenerateZ())
    x = np.linspace(0,12,100)
    plt.hist(data,bins=100)
    plt.plot(x,Gauss(x,35300,6,1))
    plt.show()


    #Question 2
    print("Question 2")
    def RandomStepQ2(pt,deltat):
        rand = random.random()
        if 0 < rand < 0.25:
            pt[0] += deltat
            return pt
        elif 0.25 <= rand < 0.5:
            pt[0] += -deltat
            return pt
        elif 0.5 <= rand < 0.75:
            pt[1] += deltat
            return pt
        elif 0.75 <= rand < 1:
            pt[1] += -deltat
            return pt
        else:
            print("Failure to step")
            return 0
    NumWalkers = 1000
    Time = 10000
    walkers = np.zeros([NumWalkers,2])
    for i in range(len(walkers[:,0])):
        for k in range(Time):
            walkers[i] = RandomStepQ2(walkers[i],1)
    SumSquares = 0
    for i in range(len(walkers[:,0])):
        SumSquares += walkers[i,0]**2+walkers[i,1]**2
    variance = SumSquares/NumWalkers
    print("Variance:",variance)
    D0 = variance/(2*Time)
    print("D0:",D0)



    #Question 3
    print("Question 3")
    def RandomStepQ3(pt,deltat):
        rand = random.random()
        if rand < 1/6:
            pt[0] += deltat
            return pt
        elif 1/6 <= rand < 1/3:
            pt[0] += -deltat
            return pt
        elif 1/3 <= rand < 1/2:
            pt[1] += deltat
            return pt
        elif 1/2 <= rand < 2/3:
            pt[1] += -deltat
            return pt
        elif 2/3 <= rand < 5/6:
            pt[2] += deltat
            return pt
        elif 5/6 <= rand < 1:
            pt[2] += -deltat
            return pt
        else:
            print("Failure to step")
            return 0
    point = np.zeros(3)
    path = {0:point.copy()}
    for i in range(10):
        point = RandomStepQ3(point,0.1)
        path.update({i+1:point.copy()})
    for i in path.values():
        print(f"{i[0]:.1f}",f"{i[1]:.1f}",f"{i[2]:.1f}")
    