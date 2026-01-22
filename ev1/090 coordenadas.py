coord = {
    "A" : (1, 0),
    "B" : (4, 5),
    "C" : (7, 7)
}
maxima = ["O",  0]
for i in coord:
    if sum(coord[i]) > maxima[1]:
        maxima = [i, sum(coord[i])]
print(maxima)
