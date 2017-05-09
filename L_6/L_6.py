import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy.optimize


# -------------------------------------------------------------------------------------
def read_data(x):
    if x == 1:
        lines = [line.rstrip('\n') for line in open('./lab6_dane/data1.txt')]
    if x == 2:
        lines = [line.rstrip('\n') for line in open('./lab6_dane/data2.txt')]

    wartosci = []
    czas = []
    odp_skok = []

    for i in range(len(lines)):
        wartosci = np.append(wartosci, lines[i].split())

    for i in range(len(wartosci)):
        if i % 2 == 0:
            czas = np.append(czas, wartosci[i])
        else:
            odp_skok = np.append(odp_skok, wartosci[i])

    plt.plot(czas, odp_skok, 'bx')
    plt.plot(czas, odp_skok, 'b')
    return wartosci, czas, odp_skok


# -------------------------------------------------------------------------------------
def odpSkok(t, tau, tauz, k, dzeta):
    h = k * (
        tauz * 1 / (tau * m.sqrt(1 - dzeta ** 2)) * m.exp(-dzeta * t / tau) * m.sin(t * m.sqrt(1 - dzeta ** 2) / tau) + (
        1 - m.exp(-dzeta * t / tau) / m.sqrt(1 - dzeta ** 2) * m.sin(t * m.sqrt(1 - dzeta ** 2) / tau + m.acos(dzeta))))

    return h


# -------------------------------------------------------------------------------------
def funk(odp_skok, parm):
    k = 0
    for i in range(len(odp_skok)):
        k += (float(odp_skok[i]) - odpSkok(float(wartosci[i]), parm[0], parm[1], parm[2], parm[3])) ** 2
    return k


# -------------------------------------------------------------------------------------
def odpUkladu():
    odp = []
    pod = []
    for i in range(120):
        odp.append(odpSkok(float(i)/10, 1, -1, 1, 0.75))
        pod.append(float(i)/10)

    plt.plot(pod, odp, 'r')



# -------------------------------------------------------------------------------------
wartosci, czas, odp_skok = read_data(1)
funk(odp_skok, [1, -1, 1, 0.75])
odpUkladu()
plt.show()
param = scipy.optimize.fmin(funk, [1, 1, 1, 1])
print(param)
