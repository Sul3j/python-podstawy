# typy zmiennych 
ciag_znakow = "to jest ciąg znaków"
ciag_znakow_liczba = "123"
liczba = 24
zmienna_ulamkowa = 2.4
zmienna_logiczna = True

# typ zmiennej sprawdzamy za pomocą metody type()
print(type(ciag_znakow))
print(type(liczba))
print(type(zmienna_ulamkowa))
print(type(zmienna_logiczna))

# przypisywanie wartości do wielu zmiennych
a, b, c = "pomarancza", 2, True

# przypisywanie tej samej wartości do 2 zmiennych
j = k = "jablko"

# łączenie ciągów znaków
t = "SLI"
i = "MAK"
p = t + i

#konwersja typu
liczba_na_string = str(liczba)
ciag_znakow_na_liczbe = int(ciag_znakow_liczba)
liczba_na_float = float(liczba)
zmienna_logiczna_na_liczbe = int(zmienna_logiczna)

#wycinanie znaku lub fragmentu z ciągu znaków

print(ciag_znakow[0])
print(ciag_znakow[-1])
print(ciag_znakow[-1:-6])
print(ciag_znakow[3:7])