#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:02:03 2020

@author: haishu
"""

import numpy as np
#from numpy.linalg import norm
import dcca # lapjv==1.3.1
import bootstrap as boot#obtained from scikits.bootstrap v1.0.0
from numpy.linalg import norm

def compute_tr_COV_C(Y_1_t, Y_2_t):
#Note: use the global variables r_1, r_2, r_12 and P_mat
    _, _, _, _, _, _, _, _, _, _, _, C_mat_hat, C_mat_neg_hat, _, _, _ = dcca.CDPA(Y_1_t.T, Y_2_t.T, r_1=r_1, r_2=r_2, r_12=r_12, P_mat = P_mat)      
    n = Y_1_t.shape[0]    
    tr_COV_C = norm(C_mat_hat,'fro')**2/n
    tr_COV_C_neg = norm(C_mat_neg_hat,'fro')**2/n    
    return tr_COV_C, tr_COV_C_neg
    

'''''''''''''''''''''''''''
main analysis
'''''''''''''''''''''''''''  
Y_1 = np.load('Y_1.npy')
Y_2 = np.load('Y_2.npy')
n = Y_1.shape[1]
p_1 = Y_1.shape[0]
p_2 = Y_2.shape[0]

X_1_hat, X_2_hat, C_1_hat, C_2_hat, D_1_hat, D_2_hat, r_1_hat, r_2_hat, r_12_hat, \
ccor_hat, ctheta_hat, C_mat_hat, C_mat_neg_hat, pcor_hat, ptheta_hat, P_mat_hat = dcca.CDPA(Y_1, Y_2, method='ED', P_set = 1, assignment=0)   
 
'''''''''
confidence interval for |C|_F^2/n
'''''''''
tr_COV_C = norm(C_mat_hat,'fro')**2/n
tr_COV_C_neg = norm(C_mat_neg_hat,'fro')**2/n

tr_COV_C # |C|_F^2/n for (X_1, X_2)
tr_COV_C_neg # |C|_F^2/n for (X_1, -X_2)

#Note: specify the global variables r_1, r_2, r_12 and P_mat 
#for the function compute_tr_COV_C(Y_1_t, Y_2_t) stated at the lines 15-21
r_1 = r_1_hat
r_2 = r_2_hat
r_12 = r_12_hat
P_mat = P_mat_hat

np.random.seed(0) # seed for the random number geneator of bootstrap
tr_COV_C_interval = boot.ci((Y_1.T, Y_2.T), statfunction=compute_tr_COV_C, alpha=0.05, n_samples=5000, method='bca')

tr_COV_C_interval[0,0],tr_COV_C_interval[1,0] # the 95% bootstrap CI for tr_COV_C
tr_COV_C_interval[0,1],tr_COV_C_interval[1,1] # the 95% bootstrap CI for tr_COV_C_neg


'''''''''
Choose the C of (X_1, X_2) or that of (X_1, -X_2) by the larger one of tr_COV_C and tr_COV_C_neg.
See Remark 2 in the paper for details
'''''''''

#The common-pattern matrix C rescaled with the magnitude of X_k
C_scaled_1_hat = C_mat_hat * norm(X_1_hat,'fro')/np.sqrt(n)
C_scaled_2_hat = C_mat_hat * norm(X_2_hat,'fro')/np.sqrt(n)

#The distinctive-pattern matrix Delta_k
if p_1 > p_2:
    Delta_1_hat = X_1_hat - C_scaled_1_hat
    Delta_2_hat = np.concatenate((X_2_hat, np.zeros([p_1-p_2,n])), axis=0) - C_scaled_2_hat
else:
    Delta_1_hat = np.concatenate((X_1_hat, np.zeros([p_2-p_1,n])), axis=0) - C_scaled_1_hat
    Delta_2_hat = X_2_hat - C_scaled_2_hat

     
