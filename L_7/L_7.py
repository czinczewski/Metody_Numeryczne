import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt


def read_data():
    X = []
    Y = []

    for lines in open("./lab7_dane/measurements19.txt", 'r'):
        x, y = lines.split()
        X.append(x)
        Y.append(y)

    X = np.array(X, 'float64')
    Y = np.array(Y, 'float64')
    return X, Y


def create_matrix(T, X, Y):
    F = np.matrix([[1, 0, T, 0],
                   [0, 1, 0, T],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    G = np.matrix([[0, 0],
                   [0, 0],
                   [1, 0],
                   [0, 1]])
    H = np.matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0]])
    s0 = np.transpose(np.matrix([X[0],
                                 Y[0],
                                 0,
                                 0]))
    P0 = np.asmatrix(5.0 * np.identity(4))
    Q = np.asmatrix(0.025 * np.identity(2))
    R = np.asmatrix(2.0 * np.identity(2))
    return F, G, H, s0, P0, Q, R


def pred(F, G, H, s0, P0, Q, R):
    vec_spx = []
    vec_spy = []
    vec_zpx = []
    vec_zpy = []

    for i in range(len(X)):
        s_ = F * s0
        P = F * P0 * np.transpose(F) + G * Q * np.transpose(G)
        z_ = H * s_
        z = np.transpose(np.matrix([X[i], Y[i]]))
        e = z - z_
        S = H * P * np.transpose(H) + R
        K = P * np.transpose(H) * (lin.inv(S))
        s_new = s_ + K * e
        I = np.asmatrix(np.identity(4))
        P_new = (I - K * H) * P

        s0 = s_new
        P0 = P_new
        s_arr = np.squeeze(np.asarray(s0))
        z_arr = np.squeeze(np.asarray(z_))
        vec_spx.append(s_arr[0])
        vec_spy.append(s_arr[1])
        vec_zpx.append(z_arr[0])
        vec_zpy.append(z_arr[1])

    return s_arr, s0, vec_spx, vec_spy


def pred5(s_arr, F, s0):
    s_predx = [s_arr[0]]
    s_predy = [s_arr[1]]

    for i in range(5):
        s = F * s0
        s_arr = np.squeeze(np.asarray(s))
        s_predx.append(s_arr[0])
        s_predy.append(s_arr[1])
        s0 = s

    return s_predx, s_predy


def draw(X, Y, vec_spx, vec_spy, s_predx, s_predy):
    plt.plot(X, Y, 'r^')
    plt.plot(vec_spx, vec_spy, 'r--')
    plt.plot(s_predx, s_predy, 'g--')
    plt.plot(s_predx[-1], s_predy[-1], 'gx')
    plt.show()

X, Y = read_data()
F, G, H, s0, P0, Q, R = create_matrix(1, X, Y)
s_arr, s0, vec_spx, vec_spy = pred(F, G, H, s0, P0, Q, R)
s_predx, s_predy = pred5(s_arr, F, s0)

draw(X, Y, vec_spx, vec_spy, s_predx, s_predy)
