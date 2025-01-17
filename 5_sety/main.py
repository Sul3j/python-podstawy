# tworzenie setów z danymi o różnym typie
owoce = {"jablko", "pomarancza", "sliwka"}
liczby = {3, 4, 6, 9}
logiczne = {True, False}
mieszane = {True, 9, "krzeslo"}
lista = ["monitor", "myszka"]

# towrzenie setu za pomocą konstruktora
setKonstruktor = set(("pomidor", "marchew", "papryka"))

# sprawdzanie typu zmiennej owoce
print(type(owoce))

# sprawdzanie długości setu
print(len(liczby))

# dodawanie danej do setu
owoce.add("kiwi")

# rozszerzanie setu o inny set
mieszane.update(logiczne)
logiczne.update(lista)

# usuwanie danej z setu
logiczne.remove(True)

# usuwanie danej z setu
logiczne.discard("myszka")

# usuwanie losowej danej z setu
liczby.pop()

# czyszczenie setu
logiczne.clear()

# usuwanie setu z pamięci
del logiczne

# łączenie 2 setów
owoceLiczby = owoce.union(liczby)

# łączenie 2 setów
mieszaneLogiczne = mieszane | liczby