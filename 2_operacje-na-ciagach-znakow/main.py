ciag_znakow1 = "Jakis tekst"
ciag_znakow2 = 'j'
ciag_znakow3 = "   Jakis tekst   "
ciag_znakow4 = "jeden: dwa: trzy"
ciag_znakow5 = "akas"

# wybiera pierwszy element z ciągu znaków
print(ciag_znakow1[0])
# wybiera elementy od 1 do 5
print(ciag_znakow1[0:5])
# wybiera ostatni element
print(ciag_znakow1[-1])
# wybiera elementy od 2 do końca
print(ciag_znakow1[2:])
# wybiera elementy od początku do 2
print(ciag_znakow1[:2])
# zwraca nam długość ciągu znaków
print(len(ciag_znakow1))
# zmienia nam ciąg na duże litery
print(ciag_znakow1.upper())
# zmienia nam ciąg na małe litery
print(ciag_znakow1.lower())
# usuwa białe znaki (spacje, entery)
print(ciag_znakow3.strip())
# zamienia litery
print(ciag_znakow1.replace("t", "J"))
# dzieli ciąg znaków (podajemy seperator)
print(ciag_znakow4.split(":"))
# + łączy ciągi znaków
print(ciag_znakow2 + ciag_znakow5)

# formatowany ciąg znaków pozwala na umiesczanie w środku wartości zmiennej
wiek = 36
ciag_znakow6 = f"Tomek ma {wiek} lat"
print(ciag_znakow6)

# w formatowanym ciągu znaków możemy wykonywać operacje na danych
ciag_znakow7 = f"Kasia ma {wiek + 2} lat"
print(ciag_znakow7)