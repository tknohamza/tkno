# Decomposition LU

import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n)
    U = np.zeros((n, n))
    
    for i in range(n):
        L[i][i] = 1  # Diagonal elements of L are 1
        
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    
    return L, U

# Example usage
A = np.array([[2, -1, 4, 1], 
              [4, -1, 5, 1], 
              [-2, 2, -2, 3], 
              [0, 3, -9, 4]], dtype=float)
L, U = lu_decomposition(A)
print("L:")
print(L)
print("U:")
print(U)

# Écrit par tknohamza
# V1 14-03-2025
