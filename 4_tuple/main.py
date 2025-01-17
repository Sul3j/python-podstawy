# tupla zawierająca wartości tekstowe
owoce = ("jablko", "pomarancza", "sliwka")
# tupla zawierająca liczby
liczby = (5, 8, 2, 6, 9)
# tupla zawierająca wartości logiczne
logiczne = (True, False, True)
# tupla zawierająca wartoci mieszane
mieszane = (True, "jablko", 5,)
# tworzenie tupli za pomocą konstruktora
tuplaKonstruktor = tuple(("krzeslo", "stolik", "monitor"))

# sprawdzenie typu zmiennej tuplaKonstruktor
print(type(tuplaKonstruktor))

# dostęp do danych tupli za pomocą indexów i do przedziału danych
print(owoce[0])
print(owoce[-1])
print(liczby[2:4])
print(liczby[:3])
print(liczby[2:])

# zamiana wartości tupli za pomocą konwersji do listy ponieważ tupla nie jest modyfikowalna
x = list(owoce)
x[0] = "kiwi"
owoce = tuple(x)

# dodawanie danej do tupli za pomocą konwersji do listy ponieważ tupla nie jest modyfikowalna
y = list(owoce)
y.append("jablko")
owoce = tuple(y)

# łączenie tupli mieszane z tuplą tuplaKonstruktor
mieszane += tuplaKonstruktor

# usuwanie danej z tupli za pomocą konwersji do listy ponieważ tupla nie jest modyfikowalna
z = list(mieszane)
z.remove("monitor")
mieszane = tuple(z)

# usuwanie tupli mieszane z pamięci
del mieszane

# destrukturyzacja tupli czyli przypisywanie wartości tupli do zmiennych
(kiwi, pomarancza, sliwka, jablko) = owoce

# destrukturyzacja tupli czyli przypisywanie wartości tupli do zmiennych a reszty do tablicy reszta
(pierwsza, druga, *reszta) = liczby

# łączenie 2 tupli w jedną nową tuple
liczbyLogiczne = liczby + logiczne

# zapisanie do nowej tupli zdwojonej tupli
logiczne2 = logiczne * 2

# metoda count umożliwia zliczenie wystąpień danej wartości
print(logiczne.count(True))

# metoda index umożliwia uzyskanie informacji na którym indeksie tupli znajduje się dana wartość
print(liczby.index(8))