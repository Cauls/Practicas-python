dia = int(input("Inserta tu dia de nacimiento"))
mes = int(input("Inserta tu mes de nacimiento"))
match mes:
    case 1:
        if dia <21:
            print("Capricornio")
        else:
            print("Acuario")
    case 2:
        if dia <20:
            print("Acuario")
        else:
            print("Piscis")
    case 3:
        if dia <21:
            print("Aries")
        else:
            print("Piscis")
    case 4:
        if dia <21:
            print("Aries")
        else:
            print("Tauro")
    case 5:
        if dia <21:
            print("Tauro")
        else:
            print("Geminis")
    case 6:
        if dia <22:
            print("Geminis")
        else:
            print("Cancer")
    case 7:
        if dia <23:
            print("Cancer")
        else:
            print("Leo")
    case 8:
        if dia <23:
            print("Leo")
        else:
            print("Virgo")
    case 9:
        if dia <22:
            print("Virgo")
        else:
            print("Libra")
    case 10:
        if dia <24:
            print("Libra")
        else:
            print("Escorpio")
    case 11:
        if dia <23:
            print("Escorpio")
        else:
            print("Sagitario")
    case 12:
        if dia <22:
            print("Sagitario")
        else:
            print("Capricornio")