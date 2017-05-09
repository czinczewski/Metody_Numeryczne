import numpy as np
import scipy as sc
import scipy.linalg

#GLOBALNE---------------------------------------------
Qa = 200
Qb = 300
Qc = 150
Qd = 350

Ws = 1500
Wg = 2500

ca = 2
cb = 2

E12 = 25
E23 = 50
E34 = 50
E35 = 25
#MATRIX-----------------------------------------------
def matrixA():
    matrix = np.array([[-Qa-E12, E12, 0, 0, 0],
              [E12+Qa,  -Qa-Qb-E12-E23, E23, 0, 0],
              [0, E23+Qa+Qb, -E23-E35-E34-Qc-Qb, E34, E35],
              [0, 0, E34+Qc, -E34-Qc, 0],
              [0, 0, E35+Qd, 0, -E35-Qd]])

    return matrix

#MATRIX-----------------------------------------------
def matrixX():
    matrix = np.array([[c1],
                       [c2],
                       [c3],
                       [c4],
                       [c5]])
    return matrix
#MATRIX-----------------------------------------------
def matrixB():
    matrix = np.array([[Ws+Qa*ca],
                       [Qb*cb],
                       [0],
                       [0],
                       [Wg]])
    return matrix
#------------------------------------------------------

A = matrixA()
#x = matrixX()
B = -1 * matrixB()

P, L, U = sc.linalg.lu(A)

print("P"), print(P)
print("L"), print(L)
print("U"), print(U)

C = np.linalg(A, B)

print("A"), print(A)
print("B"), print(B)
print("C"), print(C)
