i, x, y = 1, 1, 0

# pętla while iterująca do 6
while i < 6:
    print(i)
    i += 1

# pętla while iterująca do 6 do czasu aż x przyjmie liczbe 6
while x < 6:
    print(x)
    if x == 3:
        break
    x += 1

# pętla while iterująca do 6 przerywana gdy y przyjmie liczbe 3 i po całej iteracji wyświetlany jest komunikat "koniec iteracji"
while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)
else:
    print("koniec iteracji")