agenda = {
    "figue" : 123456789,
    "wassim" : 987654321,
    "hugo" : 456123789
}
contacto = input("Contacto a buscar: ").lower()
if contacto in agenda:
    print(f"{contacto} : {agenda[contacto]}")
else:
    print("Contacto no encontrado")