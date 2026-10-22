#Import Statements
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from scipy.optimize import brentq
from scipy.special import erf


def main() -> None:
    #Question 1
    print("Question 1")
    #Creating the positions and velocities 
    r = np.zeros([16,2])
    v = np.zeros([16,2])
    #Randomly placing the points
    for i in r:
        i[0] = 10*random.random()
        i[1] = 10*random.random()
    #Setting the velocities based on the Maxwell-Boltzmann Distribution with help from chatgpt
    a = np.sqrt(1/120)
    def MaxCDF(x):
        return erf(x/(np.sqrt(2)*a))-np.sqrt(2/np.pi)*(x/a)*np.exp(-x**2/(2*a**2))
    for i in v:
        y = random.random()
        vmax = brentq(lambda x:MaxCDF(x)-y,0,10*a)
        theta = 2*np.pi*random.random()
        i[0] = vmax*np.cos(theta)
        i[1] = vmax*np.sin(theta)
    #Defining the Lennard-Jones Force
    def Flj(x,array,index):
        TotalForce = np.array([0,0])
        ind = -1
        for i in array:
            ind += 1 
            if ind == index:
                continue
            else:
                dist = np.sqrt((x[0]-i[0])**2+(x[1]-i[1])**2)
                ForceMag = 4*((-12/dist**13+6/dist**7))
                theta = np.arctan((i[1]-x[1])/(i[0]-x[0]))
                np.add(TotalForce,np.array([ForceMag*np.cos(theta),ForceMag*np.sin(theta)]))
        return TotalForce
    for i in range(2000):
        for j in range(len(r)):
            delr = r[j] + (0.01)*v[j] + (0.01)**2/(2)*Flj(r[j],r,j)
            v[j] = v[j] + (0.01/2)*(Flj(r[j],r,j)+Flj(delr,r,j))
            r[j] = delr
        if i % 200 == 0:
            plt.scatter(r[:,0],r[:,1])
    plt.scatter(r[:,0],r[:,1])
    plt.show()
        

                
        
    