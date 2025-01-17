lista1 = ["jablko", "banan", "pomarancza"]
lista2 = list((1, 2, 3))
lista3 = ["pomidor", "marchew"]
lista4 = [6, 2, 8, 4, 2, 1, 9, 2]

# wybieranie 2 elementu listy
print(lista1[1])
# wybieranie ostatniego elementu listy
print(lista2[-1])
# wybieranie elementów od 2 do 4
print(lista2[1:3])
# wybieranie elementów do 3
print(lista1[:2])
# wybieranie elementów od 3
print(lista1[2:])
# zamiana pierwszego elementu listy na arbuz
lista1[0] = "arbuz"
print(lista1)
# zamiana elementu pierwszego i drugiego na 8 i 9
lista2[0:2] = [8, 9]
print(lista2)
# dodanie mandarynki na koniec listy
lista1.append("mandarynka")
print(lista1)
# dodanie śliwki na 2 pozycje
lista1.insert(1, "sliwka")
print(lista1)
# rozszrzenie listy1 o liste2
lista1.extend(lista3)
print(lista1)
# usunięcie arbuza z listy1
lista1.remove("arbuz")
print(lista1)
# usunięcie pierwszego elementu listy
lista1.pop(0)
print(lista1)
# usunięcie ostatniego elementu listy
lista1.pop()
print(lista1)
# usunięcie pierwszego elementu listy za pomocą del
del lista1[0]
print(lista1)
# wyczyszczenie całej listy
lista2.clear()
print(lista2)
# sortowanie listy z cyframi
lista4.sort()
print(lista4)
# sortowanie listy z ciągami znaków
lista1.sort()
print(lista1)
# sortowanie listy z cyframi w odwrotnej kolejności
lista4.sort(reverse = True)
print(lista4)
# kopiowanie listy do nowej zmiennej
lista5 = lista4.copy()
print(lista5)
# zliczenie ile jest wrtości 2 w liście
print(lista5.count(2))