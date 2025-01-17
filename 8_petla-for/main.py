owoce = ["banan", "jablko", "pomarancza"]

# pętla iterująca po liście
for owoc in owoce:
    print(owoc)
    
k = 0

# pętla iterująca po ciągu znaków
for litera in "jakistekst":
    if litera == "k":
        k=k+1
        
print(f"litera k wystepuje {k} razy w naszym ciągu znakow")

# pętla iterująca 6 razy
for i in range(6):
    print(i)
    
# pętla iterująca od 2 do 6
for i in range(2, 6):
    print(i)

# pętla iterująca od 2 do 30 co 3
for i in range(2, 30, 3):
    print(i)

# pętla iterująca po liście i wykonująca else gdy przeiteruje przez wszystkie elementy
for owoc in owoce:
    print(owoc)
else:
    print("to cała lista owoce")

# continue pomija obrót pętli i idzie do następnego a break wychodzi z pętli
for i in range(10):
    if i % 2 != 0:
        continue
    elif i == 8:
        break
    else:
        print(i)

o_owocach = ["czerwony", "duży", "smaczny"]

# zagnieżdżanie pętli
for x in o_owocach:
    for y in owoce:
        print(x, y)

# argument pass którego używamy aby zadeklarować pętle bez jej ciała
for x in [0, 1, 2]:
    pass