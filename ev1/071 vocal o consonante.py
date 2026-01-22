letra = input("Inserta una letra").lower()
match letra:
    case "a"|"e"|"i"|"o"|"u":
        print("Vocal")
    case "@"|"|"|"/"|"#":
        print("Caracter especial")
    case default:
        print("Consonante")
