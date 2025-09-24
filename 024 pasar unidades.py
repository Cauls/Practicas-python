medida = int(input("¿En que medida estamos? 1:mm 2:cm 3:dm 4:m 5:dam 6:hm 7:km"))
num = int(input("¿Cuantos son?"))
objetivo = int(input("¿A que medida queremos pasar? 1:mm 2:cm 3:dm 4:m 5:dam 6:hm 7:km"))
medida -= objetivo
if medida < 0:
    medida = medida * -1
    num = num * (10*medida)
else:
    num = num / (10*medida)
print(num)
