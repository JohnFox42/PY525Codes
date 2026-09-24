import numpy as np
import statistics
import random

def main() -> None:
    #Question 1 
    #Convert our Lattice string into spin up or down
    def LatticeDecoder(str):
        if str == "0":
            return -1
        elif str == "1":
            return 1
        else:
            print("Decoding failure")
            return 0 
    def LatticeHCalculator(fLat):
        if type(fLat) == str:
            Lat = []
            for i in fLat:
                Lat.append(LatticeDecoder(i))
        else:
            Lat = fLat
        H = 0
        for j in range(len(Lat)):
            holder1 = Lat[j]
            if j in {3,7,11,15}:
                holder2 = Lat[j-3]
            else:
                holder2 = Lat[j+1]
            H += -holder2*holder1
            if j in {12,13,14,15}:
                holder2 = Lat[j-12]
            else:
                holder2 = Lat[j+4]
            H += -holder2*holder1
        return H

    #Part a, direct calculation
    HList = []
    #Generating the lattice structure in each loop then calculating H
    #Using binary string idea yoinked from chatgpt    
    for i in range(2**16):
        Lattice = f'{i:016b}'
        H = LatticeHCalculator(Lattice)
        HList.append(H)
    Z = 0
    for i in HList:
        Z += np.e**(-i/5)
    for i in range(len(HList)):
        HList[i] = HList[i]*np.e**(-HList[i]/5)/Z
    print("Brute force <H>/N:",sum(HList)/16)

    #Part b, metropolis algorithm
    #intial guess
    fx0 = random.randint(0,2**16)
    fx0 = f'{fx0:016b}'
    x0 = []
    for i in fx0:
        x0.append(LatticeDecoder(i))
    ListXi = [x0.copy()]
    #Metropolis algorithm
    for i in range(100000):
        xt = x0.copy()
        change = random.randint(0,15)
        xt[change] = -x0[change]
        r = (np.e**(-LatticeHCalculator(xt)/5)/np.e**(-LatticeHCalculator(x0)/5))
        if r >= 1:
            ListXi.append(xt.copy())
            x0 = xt.copy()
        elif random.random() < r:
            ListXi.append(xt.copy())
            x0 = xt.copy()
        else:
            ListXi.append(x0.copy())
            continue
    Htot = 0
    for i in ListXi:
        Htot += LatticeHCalculator(i)
    AvgH = Htot/len(ListXi)
    print("<H>/N:",AvgH/16)

        
            

