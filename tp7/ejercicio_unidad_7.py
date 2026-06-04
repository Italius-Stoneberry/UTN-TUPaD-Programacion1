import funciones_unidad7 as fun

while True:
    print("1. Cargar frutas")
    print("2. Modificar frutas (parte 2)")
    print("3. Mostrar frutas (parte 3)")
    print("4. Agenda telefonica")
    print("5. Analisis de frase")
    print("6. Promedio alumnos")
    print("7. Asistencias")
    print("8. Productos")
    print("9. Agenda")
    print("10. Paises y capitales")
    print("11. Salir")
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
        case '5':
            fun.limpiar_pantalla()
            fun.ejercicio5()
        case'6':
            fun.limpiar_pantalla()
            fun.ejercicio6()
        case '7':
            fun.limpiar_pantalla()
            fun.ejercicio7()
        case '8':
            fun.limpiar_pantalla()
            fun.ejercicio8()
        case '9':
            fun.limpiar_pantalla()
            fun.ejercicio9()
        case'10':
            fun.limpiar_pantalla()
            fun.ejercicio10()
        case'11':
            fun.limpiar_pantalla()
            print("Gracias por usar el programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
        
