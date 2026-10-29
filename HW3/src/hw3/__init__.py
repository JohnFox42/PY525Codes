#Import Statements
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from scipy.optimize import brentq
from scipy.special import erf


def main() -> None:
    #Function Definitions
    #Defining the periodic boundary conditions
    def MinDist(x,i):
        mindist = [10,10]
        #Center
        disthold = np.sqrt((x[0]-i[0])**2+(x[1]-i[1])**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [i[0]-x[0],i[1]-x[1]]
        #Left
        disthold = np.sqrt((x[0]-(i[0]-10))**2+(x[1]-i[1])**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]-10)-x[0],i[1]-x[1]]
        #Up
        disthold = np.sqrt((x[0]-i[0])**2+(x[1]-(i[1]+10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [i[0]-x[0],(i[1]+10)-x[1]]
        #Right
        disthold = np.sqrt((x[0]-(i[0]+10))**2+(x[1]-i[1])**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]+10)-x[0],i[1]-x[1]]
        #Down
        disthold = np.sqrt((x[0]-i[0])**2+(x[1]-(i[1]-10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [i[0]-x[0],(i[1]-10)-x[1]]
        #LeftUp
        disthold = np.sqrt((x[0]-(i[0]-10))**2+(x[1]-(i[1]+10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]-10)-x[0],(i[1]+10)-x[1]]
        #RightUp
        disthold = np.sqrt((x[0]-(i[0]+10))**2+(x[1]-(i[1]+10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]+10)-x[0],(i[1]+10)-x[1]]
        #LeftDown
        disthold = np.sqrt((x[0]-(i[0]-10))**2+(x[1]-(i[1]-10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]-10)-x[0],(i[1]-10)-x[1]]
        #RightDown
        disthold = np.sqrt((x[0]-(i[0]+10))**2+(x[1]-(i[1]-10))**2)
        if disthold < np.linalg.norm(mindist):
            mindist = [(i[0]+10)-x[0],(i[1]-10)-x[1]]
        return mindist
    #Defining the Lennard-Jones Force
    def Flj(x,array,index):
        TotalForce = np.zeros(2)
        ind = -1
        for i in array:
            ind += 1 
            if ind == index:
                continue
            else:
                dist = np.array(MinDist(x,i))
                distMag = np.linalg.norm(dist)
                #truncating the force term
                if distMag > 3:
                    continue
                elif distMag == 0:
                    raise ValueError("Two particles occupy the same position")
                ForceMag = 24*((-2/distMag**13+1/distMag**7))
                TotalForce += ForceMag*dist/distMag
        return TotalForce
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
    for i in range(2000):
        for j in range(len(r)):
            delr = r[j] + (0.01)*v[j] + (0.01)**2/(2)*Flj(r[j],r,j)
            v[j] = v[j] + (0.01/2)*(Flj(r[j],r,j)+Flj(delr,r,j))
            r[j] = delr
        if i % 200 == 0:
            plt.scatter(r[:,0],r[:,1])
    plt.scatter(r[:,0],r[:,1])
    plt.show()
        

                
        
    