import numpy as np
import matplotlib.pyplot as plt
#globalne------------------------------------------
n = 10
x = 0.5
line = np.arange(n)

#wartosc-funkcji-----------------------------------
funkcja = np.ones(n) * np.log((x + 1))
ciagla_funkcja = np.ones(n) * np.log((np.arange(0,1,0.1) + np.ones(n)))

#rozwinięcie---------------------------------------
def rozwiniecie(x,n):
    wspolczynnik = -1 * np.ones(n)
    rosnace = np.arange(n)

    wspolczynnik = wspolczynnik ** rosnace
#    print(wspolczynnik)
    gora = (x * np.ones(n)) ** np.arange(1, n+1, 1)
    dol = np.arange(1, n+1, 1)
#    print(gora)
    wynik = wspolczynnik * (gora / dol)
#    print(wynik)
    wynik_szeregu = wynik[:].cumsum()
#    print(wynik_szeregu)

    return wynik_szeregu

#rozwinięcie---------------------------------------
def rozwiniecie2(x,n):
    wspolczynnik = -1 * np.ones(n)
    rosnace = np.arange(n)

    wspolczynnik = wspolczynnik ** rosnace
#    print(wspolczynnik)
    gora = (x * np.ones(n)) ** np.arange(1, n+1, 1)
    dol = np.arange(1, n+1, 1)
#    print(gora)
    wynik = wspolczynnik * (gora / dol)
#    print(wynik)
    wynik_szeregu = np.sum(wynik)
#    print(wynik_szeregu)

    return wynik_szeregu

#--------------------------------------------------
#wartość-funkcji-przbylizona-do-n-tego-wyrazu-ciagu
def przyblizona_funkcja(n):
    wartosc_x = np.arange(0, 1, 0.1)

    rozw = []

    for x in range(0, 10):
        rozw.append(rozwiniecie(wartosc_x[x], n))

    return rozw
#--------------------------------------------------

wyniki_rozwiniecia = rozwiniecie(x, n)
blad_bezwzgledny = np.abs(funkcja - wyniki_rozwiniecia)
blad_wzgledny_procentowo = 100 * blad_bezwzgledny / wyniki_rozwiniecia

tabela = []
tabela.append(np.arange(n))
tabela.append(wyniki_rozwiniecia)
tabela.append(blad_bezwzgledny)
tabela.append(blad_wzgledny_procentowo)
tabela = np.transpose(tabela)

print("")
print("                  N | rozwiniecie | blad bezwzgledny | blad_wzgledny_procentowo")
print(tabela)

#----------------------------------------------------
plt.plot(ciagla_funkcja, line,  label = "funkcja")
przyb_fun = np.asmatrix(przyblizona_funkcja(10))
przyb_fun = np.transpose(przyb_fun)

plt.plot(np.transpose(przyb_fun[1][:]), line, label= "n = 1")
plt.plot(np.transpose(przyb_fun[3][:]), line, label = "n = 3")
plt.plot(np.transpose(przyb_fun[9][:]), line, label = "n = 9")

plt.title("Wykres funkcji")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(bbox_to_anchor=(0., -0.2, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
plt.show()
