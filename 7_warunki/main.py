a = 10
b = 2

# struktura warunków w Pythonie
if a > b:
    print("a jest większe od b")
elif a < b:
    print("a jest mniejsze od b")
else:
    print("a i b są równe")

# warunek jednoliniowy
print("a i b są równe") if a == b else print("a i b nie są równe")

# warunek z łącznikiem and gdy oba zwracają True to wyświetli się komunikat
if a <= 10 and b >= 5:
    print("a jest mniejsze lub równe 10 a b jest więsze lub równe 5")

# warunek z łącznikiem or gdy jeden zwraca True to wyświetli się komunikat
if a != 10 or b > 3:
    print("a nie jest równe 10 lub b jest większe od 3")
    
# warunek z argumentem pass używany jest gdy deklarujemy warunek bez jego ciała
if b > a:
    pass

owoce = ["jablko", "pomarancza", 'sliwka']

# sprawdzenie za pomocą warunku czy dany element istnieje w liście
if "jablko" in owoce:
    print("jablko znajduje się w liście owoce")

auto = {
    "producent": "BMW",
    "model": "e46"
}

# sprawdzenie za pomocą warunku czy dany klucz istnieje w słowniku i czy zawiera wartość e36
if "model" in auto:
    print("w słowniku określony jest model")
    if auto["model"] == "e36":
        print("modelem auta jest e36")