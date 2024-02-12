import time
import VarGlobal
from BruteForce import *

def DisplayResult():
    
    print("Processing Result")
    print("-----------------\033[0;34;40m")

    start = time.time()    
    brute(len(VarGlobal.matriks), len(VarGlobal.matriks[0]))

    print("MAX VALUE             =", VarGlobal.MAX_VALUE)

    N = len(VarGlobal.BUFFER_MAX_VALUE_TOKEN)
    print("TOKEN                 =", end=" ")
    if len(VarGlobal.BUFFER_MAX_VALUE_TOKEN) == 0:
        print("\033[0;31;40mTidak ada solusi yang menghasilkan value bernilai positif\033[0;34;40m")
    else:
        for i in range(0, N):
            print(VarGlobal.BUFFER_MAX_VALUE_TOKEN[i],end=" ")

        print()
    
    print("COORDINATE (col,row)  =", end=" ")
    if len(VarGlobal.BUFFER_MAX_VALUE_COORDINATE) == 0:
        print("\033[0;31;40mTidak ada solusi yang menghasilkan value bernilai positif\033[0;34;40m")
    else:
        for i in range(0, N):
            print("("+str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[i][1]+1)+","+str(VarGlobal.BUFFER_MAX_VALUE_COORDINATE[i][0]+1)+")",end=" ")

    end = time.time()

    VarGlobal.time_processing = int((end-start)*1000)

    print()
    print("\033[0;32;40m")
    print("Finished in", VarGlobal.time_processing," ms")
    print()