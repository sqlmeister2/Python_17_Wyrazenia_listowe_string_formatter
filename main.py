#List comprahesion

lista = list(range(10)) # szybkie stworzenie listy z liczbami, zamiast wpisywania recznego
print(lista)

#wyrazenia listowe pozwalają wykonywac operacje ns pojedycznych elementach listy
#tworzenie nowej listy
nowaLista = [i * 2 for i in lista]
print(nowaLista)

#bardziej złożone wyrażenie z ifem
nowaLista = [i + 1 for i in lista if i % 2 == 0]
print(nowaLista)


#Formatowanie ciągow string
argumenty = ["Adam", 24]
tekst = "Cześć mam na imie {0} i mam {1} lat".format(argumenty[0], argumenty[1])
tekst = "Cześć mam na imie {imie} i mam {wiek} lat".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)
