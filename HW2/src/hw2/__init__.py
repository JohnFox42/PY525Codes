import numpy as np
import random

def main() -> None:
    #Functions used throughout
    #Convert our Lattice string into spin up or down
    def LatticeDecoder(str):
        if str == "0":
            return -1
        elif str == "1":
            return 1
        else:
            print("Decoding failure")
            return 0     
    #Question 1 
    print("Question 1:")
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
        Z += np.e**(-i/0.2)
    for i in range(len(HList)):
        HList[i] = HList[i]*np.e**(-HList[i]/0.2)/Z
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
        r = (np.e**(-LatticeHCalculator(xt)/0.2)/np.e**(-LatticeHCalculator(x0)/0.2))
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
    print("Metropolis <H>/N:",AvgH/16)

    #Question 2
    print("Question 2:")
    #Metropolis Algorithm
    #H Calculator
    def TenLatticeHCalculator(fLat):
        if type(fLat) == str:
            Lat = []
            for i in fLat:
                Lat.append(LatticeDecoder(i))
        else:
            Lat = fLat
        H = 0
        for j in range(len(Lat)):
            holder1 = Lat[j]
            if j in {9,19,29,39,49,59,69,79,89,99}:
                holder2 = Lat[j-9]
            else:
                holder2 = Lat[j+1]
            H += -holder2*holder1
            if j in {90,91,92,93,94,95,96,97,98,99}:
                holder2 = Lat[j-90]
            else:
                holder2 = Lat[j+10]
            H += -holder2*holder1
        return H
    def TwentyLatticeHCalculator(fLat):
        if type(fLat) == str:
            Lat = []
            for i in fLat:
                Lat.append(LatticeDecoder(i))
        else:
            Lat = fLat
        H = 0
        for j in range(len(Lat)):
            holder1 = Lat[j]
            if j in {19,39,59,79,99,119,139,159,179,199,219,239,259,279,299,319,339,359,379,399}:
                holder2 = Lat[j-19]
            else:
                holder2 = Lat[j+1]
            H += -holder2*holder1
            if j in {380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399}:
                holder2 = Lat[j-380]
            else:
                holder2 = Lat[j+20]
            H += -holder2*holder1
        return H
    def TenMetroAlgorithm(T):
        #initial guess
        fx0 = random.randint(0,2**100)
        fx0 = f'{fx0:0100b}'
        x0 = []
        for i in fx0:
            x0.append(LatticeDecoder(i))
        ListXi = [x0.copy()]
        #Metropolis algorithm
        for i in range(100000):
            xt = x0.copy()
            change = random.randint(0,99)
            xt[change] = -x0[change]
            r = (np.e**(-TenLatticeHCalculator(xt)/T)/np.e**(-TenLatticeHCalculator(x0)/T))
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
            Htot += TenLatticeHCalculator(i)
        AvgH = Htot/len(ListXi)
        return AvgH
    print("Metropolis <H>/N:",TenMetroAlgorithm(0.3)/100)

