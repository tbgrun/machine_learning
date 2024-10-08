import numpy as np
from scipy import stats
from scipy.optimize import minimize

def log_likelihood(lmbda, data):
    if lmbda == 0:
        transformed_data = np.log(data)
    else:
        transformed_data = (data**lmbda - 1) / lmbda
    
    mu = np.mean(transformed_data) # calculate mean
    sigma2 = np.var(transformed_data) #calculate variance
    n = len(data) # calculate length
    log_likelihood_value = (-n/2) * np.log(2 * np.pi) - (n/2) * np.log(sigma2) - (1/(2*sigma2)) * np.sum((transformed_data - mu)**2) #calculate log-likelihood
    
    return -log_likelihood_value  # returns negative log-likelyhood for minimalization
best_lambda = result.x[0]
