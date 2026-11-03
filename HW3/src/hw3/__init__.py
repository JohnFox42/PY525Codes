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
    OGr = r 
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

    #Evolving the system
    delrminus = np.zeros([16,2])
    for i in range(len(r)):
        delrminus[i] = r[i] - v[i]*(0.01)
    delrplus = np.zeros([16,2])

    for i in range(100):
        for j in range(len(r)):
            delrplus[j] = 2*r[j]-delrminus[j]+(0.01)**2*Flj(r[j],r,j)
            v[j] = delrplus[j]-delrminus[j]/(2*(0.01))
            #Apply periodic boundaries
            delrplus[j] %= 10
        delrminus = np.copy(r) 
        r = np.copy(delrplus)
    for i in v:
        print(np.linalg.norm(i))
    for i in range(len(r)):
        Totdisp = np.linalg.norm(r[i]-OGr[i])**2
        AvgDisp = Totdisp/16
    D0 = AvgDisp/(4*1)
    print("Dispersion Constant D0:",D0)

    #Question 2
    print("Question 2")
    #Placing the initial lattice with small initial velocities
    r = np.zeros([16,2])
    v = np.zeros([16,2])
    hozcount = -1
    for i in range(len(r)):
        if i % 4 == 0:
            hozcount += 1
        r[i] = [(hozcount)*2+2,(i%4)*2+2]
    for i in range(len(v)):
        theta = random.random()*2*np.pi
        v[i] = [(0.00001)*np.cos(theta),(0.00001)*np.sin(theta)]

    #Evolving the system
    delrminus = np.zeros([16,2])
    for i in range(len(r)):
        delrminus[i] = r[i] - v[i]*(0.005)
    delrplus = np.zeros([16,2])

    plt.scatter(r[:,0],r[:,1])

    for i in range(3000):
        for j in range(len(r)):
            delrplus[j] = 2*r[j]-delrminus[j]+(0.005)**2*Flj(r[j],r,j)
            v[j] = delrplus[j]-delrminus[j]/(2*(0.005))
            #Apply periodic boundaries
            delrplus[j] %= 10
        delrminus = np.copy(r) 
        r = np.copy(delrplus)

    keys = np.linspace(1,15,15)
    CorrCount = dict.fromkeys(keys,0)
    for i in range(1,len(r)):
        dist = np.linalg.norm(r[0]-r[i])
        formKey = 0 
        for j in CorrCount.keys():
            if formKey < dist <= j:
                CorrCount[j] += 1
                formKey = j
    print(CorrCount)   
    AvgV = 0 
    for i in v:
        AvgV += np.linalg.norm(i)/16
    T = AvgV**2*np.pi/8
    print("Temperature",T) 
    plt.scatter(r[:,0],r[:,1])
    plt.show()

    #Question 3
    print("Question 3")
    AddedTemp = 0 
    for i in range(30):
        #Heating the system 
        for i in range(len(v)):
            theta = np.arctan(v[i][1]/v[i][0])
            v[i] += [np.sqrt(0.2)*np.cos(theta),np.sqrt(0.2)*np.sin(theta)]
        AddedTemp += 16*np.sqrt(0.2)

        #Evolving the system
        for i in range(200):
            for j in range(len(r)):
                delrplus[j] = 2*r[j]-delrminus[j]+(0.005)**2*Flj(r[j],r,j)
                v[j] = delrplus[j]-delrminus[j]/(2*(0.005))
                #Apply periodic boundaries
                delrplus[j] %= 10
            delrminus = np.copy(r) 
            r = np.copy(delrplus)
        print("AddedTemp: ",AddedTemp)
        plt.scatter(r[:,0],r[:,1])
        plt.show()
    
