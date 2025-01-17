# definicja funkcji wyświetlającej komunikat
def komunikat():
    print("to jest nasz komunikat")
    
komunikat()

# definicja funkcji z argumentem
def nowyUzytkownik(imie):
    print(f"imie nowego użytkownika to: {imie}")
    
nowyUzytkownik("Adam")

# definicja funkcji z dwoma argumentami
def nowyKlient(imie, nazwisko):
    print(f"imie nowego klienta to: {imie} a nazwisko to: {nazwisko}")
    
nowyKlient("Anna", "Nowak")

# definicja funkcji z listą argumentów
def dzieci(*dzieci):
    print(f"dziecko 1: {dzieci[0]} dziecko 2: {dzieci[1]} dziecko 3: {dzieci[2]}")
    
dzieci("Tomek", "Ania", "Kasia")

# przypisywanie wartości do konkretnych argumentów w funkcji
def owoce(owoc3, owoc2, owoc1):
    print(owoc1, owoc2, owoc3)
    
owoce(owoc1="Jablko", owoc2="Pomarańcza", owoc3="banan")

# przekazywanie wartości słownikowych jako argumenty funkcji
def nazwiska(**nazwiska):
    print(f"nazwisko1 to: {nazwiska["nazwisko1"]}")
    
nazwiska(nazwisko1="Nowak", nazwisko2="kowalski")

# ustawienie domyślnej wartości w argumencie 
def kraje(nazwa="Polska"):
    print(f"nazwa kraju to: {nazwa}")

kraje("Niemcy")
kraje()

# funkcja zwracająca wartość
def dodawanie(liczba1, liczba2):
    return liczba1 + liczba2

print(dodawanie(5, 10))

# deklaracja pustej funkcji
def pustaFunkcja():
    pass