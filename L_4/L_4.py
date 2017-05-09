import numpy as np
from matplotlib import pyplot as plt
#f(x)-----------------------------------------
def fun_1(x):
    return 3*(x**2)-x-1

def fun_2(x):
    return -2*(x**2)/(4+3*x)
#---------------------------------------------
#elementy dominujące
def iter_1(x, y):
    return (x-1-y)/3

def iter_2(x, y):
    return ((-2)*(x**2) -1*3*x*y)/4
#---------------------------------------------
def fun_3(x):
    return ((-14*x/3) + (4/3) + (4/(3*x)))
#ROZW-GRAFICZNE-------------------------------
def wykres(Rx1, Ry1, Rx2, Ry2, Rx3, Ry3, xi, yi):
    x = np.linspace(-2, 2, 1000)
    fun_1_wyk = fun_1(x)
    fun_2_wyk = fun_2(x)

    plt.plot(x, fun_1_wyk, 'r')
    plt.plot(x, fun_2_wyk, 'g')

    plt.plot(Rx1, Ry1, 'bo')
    plt.plot(Rx2, Ry2, 'bo')
    plt.plot(Rx3, Ry3, 'bo')

    plt.plot(xi, yi, 'rx') #iteracyjne
    plt.show()
#WYNIKI-GRAFICZNE-----------------------------
# trzy pierwiasteki
# 1) x1 = -1.54     y1 = -0.11
# 2) x2 =  0.72     y2 = -0.16
# 3) x3 = -1.54     y3 =  7.63
#METODA-ITERACYJNA----------------------------
def Metoda_Iter():
    xstart = -1
    ystart = -1

    for i in range(100):
        #print(i, ")", "X: ", xstart, " Y: ", ystart)
        x_step = iter_1(xstart, ystart)
        y_step = iter_2(xstart, ystart)
        xstart = x_step
        ystart = y_step

    print("Metoda Iteracyjna(x, y)=: ", xstart, ystart)
    return xstart, ystart
#---------------------------------------------
def NewtonRaphson(startX, startY):
    f1 =    lambda x, y: -2*(x**2)-3*x*y-4*y
    f2 =    lambda x, y: 3*(x**2) - x - y - 1

    dX1 =   lambda x, y: -4*x-3*y
    dY1 =   lambda x, y: -3*x-4

    dX2 =   lambda x, y: 6*x-1
    dY2 =   lambda x, y: -1

    for i in range(1000):
        derX1 = dX1(startX, startY)
        derX2 = dX2(startX, startY)
        derY1 = dY1(startX, startY)
        derY2 = dY2(startX, startY)
        jakobian = derX1*derY2 - derY1*derX2
        startX = startX - (f1(startX,startY)*derY2 - f2(startX,startY)*derY1)/jakobian
        startY = startY - (f2(startX,startY)*derX1 - f1(startX,startY)*derX2)/jakobian

    print("Newton-Raphson(x,y)=: ", startX, startY)
    return startX, startY
#---------------------------------------------
#wywołanie
xi, yi = Metoda_Iter()
print("")
x1, y1 = NewtonRaphson(-2, -2)
x2, y2 = NewtonRaphson(2, 2)
x3, y3 = NewtonRaphson(-2, 5)
wykres(x1, y1, x2, y2, x3, y3, xi, yi)
#---------------------------------------------
