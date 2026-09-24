import numpy as np
import statistics

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

    #Part a, direct calculation
    HList = []
    #Generating the lattice structure in each loop then calculating H
    #Using binary string idea yoinked from chatgpt    
    for i in range(2**16):
        Lattice = f'{i:016b}'
        H = 0
        #Caculating the only the interactions to the right and down to prevent double counting.
        for j in range(len(Lattice)):
            holder1 = LatticeDecoder(Lattice[j])
            if j in {3,7,11,15}:
                holder2 = LatticeDecoder(Lattice[j-3])
            else:
                holder2 = LatticeDecoder(Lattice[j+1])
            H += -holder2*holder1
            if j in {12,13,14,15}:
                holder2 = LatticeDecoder(Lattice[j-12])
            else:
                holder2 = LatticeDecoder(Lattice[j+4])
            H += -holder2*holder1
        HList.append(H)
    print(statistics.mean(HList)/16)
        
            

