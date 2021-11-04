import numpy as np

def rmslog(ytrue, yhat):
    logerror = np.square(np.log(yhat+1)-np.log(ytrue-1))
    return np.sqrt(np.mean(logerror))