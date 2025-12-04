aficiones = {
    "Guillermo": ["cine", "fútbol", "música"],
    "Sebas": ["ajedrez", "cine"],
    "Misael": ["música", "lectura"],
    "Hugo": ["fútbol", "música"],
    "Figue": ["lectura", "cine"],
    "Wassim": ["ajedrez", "lectura"]
}
aficionados = {}
for i in aficiones: 
    for j in aficiones[i]:
        if j not in aficionados:
            aficionados.update({j : []})
        aficionados[j].append(i)
print(aficionados)