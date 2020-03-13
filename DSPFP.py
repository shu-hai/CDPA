import numpy as np
from sys import float_info
#code based on https://github.com/emanuele/graph_matching_tractograms
#from scipy.optimize import linear_sum_assignment
from lapjv import lapjv

def DSPFP(A, B, C, D, lam=0.5, alpha=0.5, threshold1=1.0e-6,
                 threshold2=1.0e-6, X=None, Y=None, #verbose=True,
                 max_iter1=100, max_iter2=100):        
    #Note: in the paper A, B, C and D are called A, A', B and B'.    
    size = A.shape[0]
    if X is None:
        X = np.eye(size)#np.ones((size, size)) / (size * size)

    if Y is None:
        Y = np.zeros((size, size))

    K = C[:,None] @ D[:,None].T

    float_max = float_info.max
    epsilon1 = epsilon2 = float_max
    iter1 = 0
    while epsilon1 > threshold1 and iter1 < max_iter1:
        Y = A @ X @ B + lam * K
        epsilon2 = float_max
        iter2 = 0
        while epsilon2 > threshold2 and iter2 < max_iter2:
            tmp = (1.0 + Y.sum() / size - Y.sum(1)) / size
            Y_new = Y + tmp[:, None] - Y.sum(0) / size
            Y_new = np.clip(Y_new, 0.0, float_max)
            epsilon2 = np.abs(Y_new - Y).max()
            Y = Y_new
            iter2 += 1

        #if verbose:
        #    print("epsilon2 = %s \t (iter2=%s)" % (epsilon2, iter2))

        X_new = (1.0 - alpha) * X + alpha * Y
        X_new = X_new / X_new.max()
        epsilon1 = np.abs(X_new - X).max()
        X = X_new
        #if verbose:
        #    print("epsilon1 = %s \t (iter1=%s)" % (epsilon1, iter1))

        iter1 += 1

    return X


def greedy_assignment(X):
    """A simple greedy algorithm for the assignment problem as
    proposed in the paper of DSPFP. It creates a proper partial
    permutation matrix (P) from the result (X) of the optimization
    algorithm DSPFP.
    """
    XX = np.nan_to_num(X.copy())
    min = XX.min() - 1.0
    P = np.zeros(X.shape)
    while (XX > min).any():
        row, col = np.unravel_index(XX.argmax(), XX.shape)
        P[row, col] = 1.0
        XX[row, :] = min
        XX[:, col] = min

    return P


def lapjv_assignment(X):
    #Jonker-Volgenant algorithm
    
    cost_M = np.max(X)-X
    
    row_ind, col_ind, _ = lapjv(cost_M)#row_ind, col_ind = linear_sum_assignment(cost_M)
     
    P = np.zeros(X.shape)
    P[range(P.shape[0]), row_ind] = 1#P[row_ind, col_ind] = 1
    
    return P

    