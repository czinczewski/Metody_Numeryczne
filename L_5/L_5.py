import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------
A = np.matrix([[3.8, -2.55, 0.45], [1, 0, 0], [0, 1, 0]])
print("A: \n", A)

B = np.matrix([[1], [0], [0]])
print("B: \n", B)

C = np.matrix([1, 1, 1])
print("C: \n", C)

D = [0]
print("D: \n", D)

x0 = np.matrix([[0], [0], [0]])
u = 1
#--------------------------------------
def odpowiedz_skokowa(A, B, C, D, x0, u):
    x = []
    y = []
    for i in range(20):
        xk = np.dot(A, x0) + np.dot(B, u)
        yk = np.dot(C, xk) + np.dot(D, u)
        x0 = xk
        x.append(xk)
        y.append(yk.item(0))
    return y
#--------------------------------------
def Riccati(A, B, Q, R):
    Pp = 0*np.identity(3)
    P = Pp
    for i in range(10):
        P = Q + np.transpose(A)*(Pp - Pp*B*(R + np.transpose(B)*P*B)**(-1)*np.transpose(B)*P)*A
        Pp = P

    return P
#--------------------------------------
def sterownik(c1, c2, A, B):
    Q = c1*np.identity(3)
    R = c2
    P = Riccati(A, B, Q, R)

    F = (R + np.transpose(B)*P*B)**(-1)*np.transpose(B)*P*A
    return F
#--------------------------------------
def uk(A, B, C, D, F, x0, u):
    x = []
    y = []
    uk = []
    print(F)
    for i in range(20):
        xk = np.dot(A, x0) + np.dot(B, u)
        x0 = xk
        uk_buf = -np.dot(F, xk)
        uk = np.append(uk, uk_buf)
    print(uk)
    return uk

#WYWOLANIE-----------------------------
y = odpowiedz_skokowa(A, B, C, D, x0, u)
#niestabilny rozbiega się

F = sterownik(1, 1, A, B)
print("F\n", F)

Anowe = A - np.dot(B, F)
print("\n nowe A\n", Anowe)
ynowe = odpowiedz_skokowa(Anowe, B, C, D, 0, 1)

uk1 = uk(Anowe, B, C, D, F, x0, 1)

plt.figure(1)

plt.subplot(131)
plt.plot(y)
plt.title("Odpowiedź skokowa")

plt.subplot(132)
plt.stem(ynowe)
plt.title("c1 = 1 c2 = 1")

plt.subplot(133)
plt.stem(uk1)
plt.title("uk")

plt.show()
