hab=[1,2,3,4,101,102,103,104,201,202,203,204]
estados=[0,0,0,0,0,0,0,0,0,0,0]

opt=""

print("Bienbenido a el hotel pipi")




while True:
    print("1. Ocupar habitacion")
    print("2. Definir el estado de la habitacion")
    print("3. Salir")
    opt=input("Ingrese una opcion: ")
    match opt:
        case "1":
            continue
        case "2":
            for i in hab:
                cant=2
                while cant != 0 or cant != 1:
                    cant=int(input(f"Mi loco la habitacion {i} No tiene estado, por favor ingrese 1 para Ocupada o 0 para Libre: "))
                
                if cant == 0:
                    estados[i] = 0
                else:
                    estados[i] = 1

        case "3":
            continue
        case "4":
            continue
        case "5":
            continue
        case "6":
            continue
        case "7":
            continue
        case "8":
            break
        case _:
            print("Opcion invalida")
            continue