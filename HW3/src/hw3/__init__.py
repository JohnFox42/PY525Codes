#Import Statements
import numpy as np
import random
import matplotlib.pyplot as plt


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
    #Setting intial positions and velocities 
    r = np.array([[4,5],[6,5]])
    v = np.array([[1,0],[-1,0]])

    #Evolving the system
    delrminus = np.zeros([2,2])
    for i in range(len(r)):
        delrminus[i] = r[i] - v[i]*(0.005)
    delrplus = np.zeros([2,2])

    for i in range(200):
        if i % 20 == 0:
            plt.scatter(r[:,0],r[:,1])
        for j in range(len(r)):
            delrplus[j] = 2*r[j]-delrminus[j]+(0.005)**2*Flj(r[j],r,j)
            v[j] = delrplus[j]-delrminus[j]/(2*(0.005))
            #Apply periodic boundaries
            delrplus[j] %= 10
        delrminus = np.copy(r) 
        r = np.copy(delrplus)
    plt.scatter(r[:,0],r[:,1])
    plt.show()
    
