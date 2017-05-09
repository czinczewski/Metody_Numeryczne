import numpy as np
from matplotlib import pyplot as plt


# funkcja 10
#rozwiazujemy rownanie dx(t)/dt=f(t,x)
# rozwiązywanie równań różniczkowych
t0 = 0
y0 = 2
n = 10
# n = 100
def f(t):
    return ((3*(t**2) + 2*(t**3) + 2*np.sqrt(2))**2)/4

# analitycznie (rozdzielając zmienne)
def analitycznie ():
    time = np.linspace(t0, n)
    # function y = ((3*(t**2) + 2*(t**3) + 2*np.sqrt(2))**2)/4
    y = []
    for t in range(len(time)):
        y.append(((3*(t**2) + 2*(t**3) + 2*np.sqrt(2))**2)/4)

    plt.plot(y, time, 'b')
    plt.show()


# metodą Eulera - metoda Explicit Euler
def EE(f,x0,t0,tk,h):
    # f - funkcja f z rownania, x0 - wartosc poczatkowa, t0-czas poczatkowy
    # tk-czas koncowy, h-krok czasowy
    t = np.arange(t0,tk,h) # generujemy wektor czasow
    N = len(t) #liczba krokow czasowych
    #wektor wynikowy
    if hasattr(x0, "__len__"):
        x=np.zeros((N,len(x0))) # gdy mamy do czynienia w równaniem wektorowym

    else:
        x=np.zeros(N) # dla przypadku skalarnego

    x = np.array(x0) # wpisujemy wartosc poczatkowa
    i=1 # index
    while (i<N): # petla glowna
        x[i]=np.array(x[i-1]+h*f(t[i-1],x[i-1]))
        i+=1
    return t,x


# metodą Heuna (bez iteracji)
def Heun(f,x0,t0,tk,h):
    t = np.arange(t0, tk, h) # generujemy wektor czasow
    N = len(t) #liczba krokow czasowych
    # wektor wynikowy
    if hasattr(x0, "__len__"):
        x = np.zeros((N, len(x0)))
    else:
        x = np.zeros(N)
    # wpisujemy wartosc poczatkowa
    x = np.array(x0)
    # index
    i = 1
    # petla glowna
    while (i < N):
        k1 = f(t[i - 1], x[i - 1])

    k2 = f(t[i - 1] + h * 0.5, x[i - 1] + 0.5 * h * k1)
    x[i] = np.array(x[i - 1] + h * 0.5 * (k1 + k2))
    i += 1
    return t, x


# metodą punktu środkowego


# --------------------------------------------------------------
analitycznie()
tk = 10
EE(f, y0, t0, tk, 1)
