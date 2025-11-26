notas = {
    "Figue":10,
    "Wassim":8,
    "Hugo":9,
    "Misael":6
}
alta = ["", 0]
for alumno, nota in notas.items():
    if nota > alta[1]:
        alta = [alumno, nota]
print(alta)