# Name: Erin Cole
# Description: This module takes a Matlab file and converts it to a numpy array

import numpy as np
import scipy.io as sio

def convertData(inFile):
    matFile = sio.loadmat(inFile)
    
    print(matFile)

