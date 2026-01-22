frutas = ["manzana", "pera", "polla", "polla", "polla", "pera", "platano"]
bien = []
for i in frutas:
    tiene = False
    for j in bien:
        if i == j:
            tiene = True
    if tiene == False:
        bien.append(i)
print(bien)