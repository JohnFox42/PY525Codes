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
                print("x:",x)
                print("i:",i)
                dist = MinDist(x,i)
                distMag = np.linalg.norm(dist)
                print("distMag:",distMag)
                #truncating the force term
                if distMag > 3:
                    continue
                ForceMag = 4*((-12/distMag**13+6/distMag**7))
                print("ForceMag:",ForceMag)
                if dist[1] == 0:
                    if dist[0] > 0:
                        theta = 0
                    elif dist[0] < 0:
                        theta = np.pi
                    else:
                        print("Two Particles on top of one another")
                else:
                    theta = np.arctan(dist[1]/dist[0])
                TotalForce += [ForceMag*np.cos(theta),ForceMag*np.sin(theta)]
                print("theta:",theta)
                print("Total Force",TotalForce)
        return TotalForce
    #Setting intial positions and velocities 
    r = np.array([[4,5],[6,5]])
    v = np.array([[0.001,0],[-0.001,0]])

    #Evolving the system
    delrminus = np.zeros([2,2])
    for i in range(len(r)):
        delrminus[i] = r[i] - v[i]*(0.005)
    delrplus = np.zeros([16,2])

    print(delrminus)

    for i in range(3):
        for j in range(len(r)):
            delrplus[j] = 2*r[j]-(0.005)*v[j]+(0.005)**2/2*Flj(r[j],r,j)
            v[j] = v[j] + (0.005)/2*(Flj(r[j],r,j)+Flj(delrplus[j],r,j))
            #Check periodic boundaries
            if 0 <= delrplus[j][0] <= 10 and 0 <= delrplus[j][1] <= 10:
                pass
            elif delrplus[j][0] > 10:
                delrplus[j][0] = delrplus[j][0] - 10
            elif delrplus[j][0] < 0:
                delrplus[j][0] = delrplus[j][0] + 10 
            elif delrplus[j][1] > 10:
                delrplus[j][1] = delrplus[j][1] - 10
            elif delrplus[j][1] < 0:
                delrplus[j][1] = delrplus[j][1] + 10 
        r = delrplus
        print(r)
    
