# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:39:54 2017

@author: Trunil
"""

import sympy as sp
from fluxpyt.utility import space
import pickle

def get_null_mat(stoich_matrix,model_metabolite):
    space()
    #print(stoich_matrix)
    space()
    S = sp.Matrix(stoich_matrix)
  
    #calculate null space and rreduced row echelon form
    S_null = S.nullspace()
    ref = S.rref()
    
    #calculate free indices
    dep_inds = ref[1]
    V = model_metabolite[0]
    free_ind = [x for x in range(len(V)) if x not in dep_inds]
    free_ind = sp.Matrix(free_ind)
    
    space() 
    #calculate null matrix
    null_mat = sp.zeros(S_null[0].shape[0],1)
    for k in S_null:
       
        null_mat = null_mat.row_join(k)
    
    null_mat.col_del(0)
    
    f = open('null_mat.pckl', 'wb')
    pickle.dump(null_mat, f)
    f.close()
    
    # write free fluxes
    f = open('free_fluxes.csv','w')
    for i in free_ind:
        print(model_metabolite[0][i],model_metabolite[1][i])
        f.write(model_metabolite[0][i])
        f.write(',')
        f.write(model_metabolite[1][i])
        f.write('\n')
    f.close()
    
    
   
    return null_mat,free_ind
 
#    
#def nullspace(A, atol=1e-13, rtol=0):
#    #http://scipy-cookbook.readthedocs.io/items/RankNullspace.html
#    import numpy as np
#    from scipy.linalg import svd
#    A = np.atleast_2d(A)
#    u, s, vh = svd(A)
#    tol = max(atol, rtol * s[0])
#    nnz = (s >= tol).sum()
#    ns = vh[nnz:].conj().T
#    return ns
#        
#    
##    

