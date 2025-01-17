# tworzenie słownika
auto = {
    "producent": "Toyota",
    "model": "Corolla",
    "rocznik": 2003,
    "bite": False
}

# sprawdzanie ilości elementów słownika
print(len(auto))

# sprawdzanie typu zmiennej auto
print(type(auto))

# tworzenie słownika za pomocą konstruktora
slownikKonstruktor = dict(producent = "BMW", model = "e36", rocznik = 1998, bite = False)

# wyciąganie ze słownika wartości o kluczu model
print(auto["model"])

# wyciąganie ze słownika wartości o kluczu model
print(auto.get("model"))

# wyświetlenie nazw kluczy słownika
print(auto.keys())

# przypisanie do klucza model wartości e36
slownikKonstruktor["model"] = "e46"

# sprawdzenie wartości słownika
print(auto.values())

# wyświetlenie zbiorów wartości klucz : wartość w słowniku
print(auto.items())

# dodanie nowej danej do słownika
auto.update({"kolor": "srebrny"})

# dodanie nowej danej do słownika
auto["przebieg"] = 140000

# usunięcie elementu o kluczu kolor
auto.pop("kolor")

# usunięcie ostatnio dodanego elementu
auto.popitem()

# wyczyszczenie słownika
slownikKonstruktor.clear()

# skopiowanie słoenika do nowej zmiennej
noweAuto = auto.copy()

# skopiowanie słoenika do nowej zmiennej
noweAuto2 = dict(auto)

print(noweAuto2)

# tworzenie słownika wielowartościowego
auta = {
    "auto1": {
        "producent": "Audi",
        "model": "A3",
        "rocznik": 2003
    },
    "auto2": {
        "producent": "BMW",
        "model": "e36",
        "rocznik": 1998
    },
    "auto3": {
        "producent": "Toyota",
        "model": "Yaris",
        "rocznik": 2009
    },
    "auto4": {
        "producent": "Fiat",
        "model": "Punto",
        "rocznik": 2007
    },
}

print(auta["auto4"])