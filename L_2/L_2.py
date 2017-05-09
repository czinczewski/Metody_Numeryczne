import numpy as np
import matplotlib.pyplot as plt
import math 

x_lin = np.ones(10)
x_lin_2 = np.ones(20)
#----------------------------------------------------wartosc funkcji
y = np.log1p((x_lin))
#----------------------------------------------------wartosc pochodnej
pochodna = np.ones(18) * 1/(1 + 0.5)
#----------------------------------------------------wartosc_przyblizona
a = np.arange(20)
b = 0.2 * np.ones(20)
h = b**a
h = h[2:20]
funkcja = (np.log1p(0.5*np.ones(18) + h) - np.log1p(0.5*np.ones(18) - h))/(2*h)
#----------------------------------------------------oblicznie_bledu
blad = np.abs(pochodna[0:18] - funkcja)
x_lin = np.arange(10)
#----------------------------------------------------tworzenie_tabeli
macierz = []
macierz.append(h)
macierz.append(funkcja)
macierz.append(pochodna)
macierz.append(blad)
macierz = np.asmatrix(macierz)
macierz = np.transpose(macierz)
#----------------------------------------------------wypisywanie
print("Połączone listy: ")
print(" |        h        |     Funkcja    |    Pochodna    |      Blad ")
print(macierz)
#----------------------------------------------------szukanie_minimum
k = np.min(blad)
print("Minimalna wartosc błędu", k)
index = np.where(blad == k)[0][0]
znalezione_h = h[index]
print("Minimalna wartość błędu jest dla h = ", znalezione_h)
#----------------------------------------------------wykres
plt.figure()
plt.plot(h, blad, 'o')
plt.xscale('log')
plt.yscale('log')
plt.title("Wykres")
plt.xlabel("Wartosc h")
plt.ylabel("Błąd bezwzględny")
plt.show()
