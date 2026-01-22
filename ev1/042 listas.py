lista=["pera","manzana","platano",["perro","gato","castor"]]
frutas=[]
animales=[]
for i in range(len(lista)-1):
    print(lista[i], end=" ")
print("")
for j in range(len(lista[3])):
    print(lista[-1][j], end=" ")