# Name: Erin Cole
# Description: This file peforms CSP on data from the BCI Competition IV dataset#               3.
# Attribution: I used the CSP.py file from spolsley/common-spacial-patterns repo# found on GitHub for reference and for general understanding of implementing 
# the algorithm.
import math
import numpy as np
import scipy as sp
import scipy.io as spo

# Input: a 40 x 400 x 10 matrix consisting of one trial of MEG data
# Return: The transformed matrix of CSP data
def CSP(rawFile):
    cspData = None
    leftCovMat, rightCovMat = covMatrices(rawFile)   
    compMatrix = leftCovMat + rightCovMat
    evals, evect = np.linalg.eig(compMatrix)
    
    
    diagEvals = np.dot(evals, np.eye)
    
    print(diagEvals)
    invDiagEvals = np.linalg.inv(diagEvals)
    
    perm = np.sqrt(invDiagEvals) * evect.T
    return cspData


def covMatrices(inFile):
    numTrials = 40
    rCovMatrix = 0
    lCovMatrix = 0

    matFile = spo.loadmat(inFile)
    
    # Get the matrix that contains the trial for desired trial
    rightTrialData = matFile['training_data'][0][0]
    leftTrialData = matFile['training_data'][0][2]
    
    # caluclate mean cov matrix for right trials
    for iRTrial in rightTrialData:
        iRMatrix = np.dot(iRTrial, iRTrial.T)
        iRTrace = np.trace(iRTrial)

        rCovMatrix += (iRMatrix / iRTrace)

    aveRCovMatrix = rCovMatrix / numTrials
    # calculate mean cov matrix for left trials
    for iLTrial in leftTrialData:
        iLMatrix = np.dot(iLTrial, iLTrial.T)
        iLTrace = np.trace(iLTrial)

        lCovMatrix += (iLMatrix / iLTrace)
    aveLCovMatrix = lCovMatrix / numTrials

    return aveLCovMatrix, aveRCovMatrix   

def projMatrix():
    
    return proj


