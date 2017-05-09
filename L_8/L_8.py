import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------------------
def read_data():
    lines = [line.rstrip('\n') for line in open('./lab8_dane/data10.txt')]
    wartosci = []
    X = []
    Y = []

    for i in range(len(lines)):
        wartosci = np.append(wartosci, lines[i].split())

    for i in range(len(wartosci)):
        if i % 2 == 0:
            X = np.append(X, float(wartosci[i]))
        else:
            Y = np.append(Y, float(wartosci[i]))

    plt.plot(X, Y, 'xr')
    plt.show()

    return X, Y


# ----------------------------------------------------------------------------------
def NewtonInterpol():
    pass


# ----------------------------------------------------------------------------------
X, Y = read_data()
points = [X, Y]
