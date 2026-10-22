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
    def Flj(r):
        return 4*(-12/r**13+6/r**7)
    def MinR(element,array):
        minr = 9999
        for i in array:
            if element == i:
                pass
            else:
                holder = np.sqrt((element[0]-i[0])**2+(element[1]-i[1])**2)
                if holder < minr:
                    minr = holder
                holder = np.sqrt((element[0]-(10-i[0]))**2+(element[1]-i[1])**2)
                if holder < minr:
                    minr = holder
                holder = np.sqrt((element[0]-i[0])**2+(element[1]-(10-i[1]))**2)
                if holder < minr:
                    minr = holder
                
    for i in r:
        minr = MinR(i,r)
    