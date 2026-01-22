lista = [ 1, 2, 3, 3]
usados = []
actual = 0
contador = 0
for indice, valor in enumerate(lista):
    if valor == actual:
        contador += 1
    else:
        print(f"{actual}:{contador}")
        actual = valor
        contador += 1