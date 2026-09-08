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
    plt.plot(x,Gauss(x,33000,6,4*np.sqrt(1/12)))
    plt.show()


    #Question 2
    def RandomStep(pt,deltat):
        rand = random.random()
        if 0 < rand < 0.25:
            pt[0] += deltat
            return pt
        if 0.25 <= rand < 0.5:
            pt[0] += -deltat
            return pt
        if 0.5 <= rand < 0.75:
            pt[1] += deltat
            return pt
        if 0.75 <= rand < 1:
            pt[1] += -deltat
            return pt
        else:
            print("Failure to step")
            return 0
    def FundSol(x,D0,t):
        return (1/np.sqrt(4*np.pi*D0*t))*np.e**(-(x[0]**2+x[1]**2)/(4*D0*t))
    walkers = np.zeros([10,2])
    for i in range(len(walkers)):
        for k in range(10000):
            walkers[i] = RandomStep(walkers[i],0.1)
    print(walkers)
