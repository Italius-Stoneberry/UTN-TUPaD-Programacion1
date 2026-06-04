import tp8fn as fun

while True:
    print("1. lista de errores")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3 4 y 5 combinado")
    print("4. Ejercicio 6y7 ejemplo de funcionamiento propio")
    print("5. Salir")
    opcion = input("Elija una opción: ")
    
    match(opcion):
        case '1':
            fun.limpiar_pantalla()
            fun.ejercicio1()
        case '2':
            fun.limpiar_pantalla()
            fun.ejercicio2()
        case '3':
            fun.limpiar_pantalla()
            fun.ejercicio3()
        case '4':
            fun.limpiar_pantalla()
            fun.ejercicio4()
        case'5':
            fun.limpiar_pantalla()
            print("Gracias por usar el programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
            