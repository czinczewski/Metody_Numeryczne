import numpy as np
from scipy import integrate

# przyklad 10
_a = [- 0.06543, - 0.6341, - 0.7652, - 3.65, 1.543]
function = lambda x: (_a[0] * (x ** 4)) + (_a[1] * (x ** 3)) + (_a[2] * (x ** 2)) + (_a[3] * x) + _a[4]
zakres = [8, -3]


# -----------------------------------
def Analitycznie(a, x_up, x_down):
    x = x_up
    result_up = (a[0] * (1 / 5) * (x ** 5)) + (a[1] * (1 / 4) * (x ** 4)) + (a[2] * (1 / 3) * (x ** 3)) + (a[3] * (1 / 2) * (x ** 2)) + (a[4] * x)

    x = x_down
    result_down = (a[0] * (1 / 5) * (x ** 5)) + (a[1] * (1 / 4) * (x ** 4)) + (a[2] * (1 / 3) * (x ** 3)) + (a[3] * (1 / 2) * (x ** 2)) + (a[4] * x)

    result = result_up - result_down
    return result


# -----------------------------------
def Romberg(function, x_up, x_down):
    result = integrate.romberg(function, x_down, x_up, show=False)
    return result


# -----------------------------------
def Gauss_Quadrature(function, x_up, x_down):
    result, err = integrate.quadrature(function, x_down, x_up)
    return result

# -----------------------------------
wynik_analitycznie = Analitycznie(_a, zakres[0], zakres[1])
wynik_romberg = Romberg(function, zakres[0], zakres[1])
blad = (wynik_analitycznie - wynik_romberg) / wynik_analitycznie

print('\n\nAnalitycznie: \t', wynik_analitycznie, '\n')

print('Romberg: \t\t', wynik_romberg)
print('Blad:\t\t\t\t', np.abs(100*blad), '%\n')

wynik_gauss_quadrature = Gauss_Quadrature(function, zakres[0], zakres[1])
blad2 = (wynik_analitycznie - wynik_gauss_quadrature) / wynik_analitycznie
print('Kwadratura Gaussa: \t', wynik_gauss_quadrature)

print('Blad:\t\t\t\t\t', np.abs(100*blad2), '%')
