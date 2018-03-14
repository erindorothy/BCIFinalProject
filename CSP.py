# Name: Erin Cole
# Description: This file peforms CSP on data from the BCI Competition IV dataset#               3.
# Attribution: I used the CSP.py file from spolsley/common-spacial-patterns repo# found on GitHub for reference and for general understanding of implementing 
# the algorithm.

import numpy as np
import scipy as sp
import scipy.io as spo

# Input: a 40 x 400 x 10 matrix consisting of one trial of MEG data
# Return: The transformed matrix of CSP data
def CSP(rawFile):
    leftCovMat, rightCovMat = convertData(rawFile)   
    
    compMatrix = leftCovMat + rightCovMat
    
    
    return cspData


def convertData(inFile, trialIndex):
    numTrials = 40
    matFile = spo.loadmat(rawFile)
    
    # Get the matrix that contains the trial for desired trial
    rightTrialData = matFile[0][0]
    leftTrialData = matFile[0][2]
    
    # caluclate mean cov matrix for right trials
    for iRTrial in rightTrialData:
        iRMatrix = np.dot(iTrial, iTrial.T)
        iLTrace = np.trace(iTrial)

        rCovMatrix += iRMatrix / iRTrace

    aveRCovMatrix = rCovMatrix / numTrials
    for iLTrial in leftTrialData:
        iLMatrix = np.dot(iLTrial, iLTrial.T)
        iLTrace = np.trace(iLTrial)

        lCovMatrix += iLMatrix / iLTrace
    aveLCovMatrix = lCovMatrix / numTrials

    return aveLCovMatrix, aveRCovMatrix   

def projMatrix():
    
    return proj


