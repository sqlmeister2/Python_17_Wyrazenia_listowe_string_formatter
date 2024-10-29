#List comprehension

# funkcja range zwroci nam obiekt typu range i wtedy trzeba ja przecastowac na liste
lista = list(range(10)) # szybkie stworzenie listy z liczbami, zamiast wpisywania recznego
print(lista)

#wyrazenia listowe pozwalają wykonywac operacje ns pojedycznych elementach listy
#tworzenie nowej listy
lista = list(range(10))
print(lista)
nowaLista = [i * 2 for i in lista]
print(nowaLista)

#bardziej złożone wyrażenie z ifem
lista = list(range(10))
nowaLista = [i + 1 for i in lista if i % 2 == 0]
print(nowaLista)

#STRING FORMATTER
#Formatowanie ciągow string
argumenty = ["Adam", 24]
tekst = "Cześć mam na imie {0} i mam {1} lat".format(argumenty[0], argumenty[1])
tekst = "Cześć mam na imie {imie} i mam {wiek} lat".format(imie = argumenty[0], wiek = argumenty[1])
print(tekst)

#Albo w bardziej czytelny sposob:
tekst = f'jestem {argumenty[0]} i mam {argumenty[1]} lat'
print(tekst)

#Dodanie listy do string formatera
lista_znakow = ['c', 'b', 'd']
print(f'Lista znakow {lista_znakow}')