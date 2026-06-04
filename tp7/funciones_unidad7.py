import dataclasses
import os


def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

precio_frutas={
        'Banana': 1200,
        'Ananá': 2500,
        'Melón': 3000,
        'Uva': 1450,
    }


import subprocess
def ejercicio1():   
  
    print("Añadiendo frutas solicitadas")
    precio_frutas['Naranja']=1200
    precio_frutas['Pera']=1500
    precio_frutas['Manzana']=2300
    for clave, valor in precio_frutas.items():
        print(clave, valor)
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio2():
    print("Actualizando el precio de las frutas solicitadas")
    precio_frutas['Banana']=1330
    precio_frutas['Melón']=2800
    precio_frutas['Manzana']=1700
    for clave, valor in precio_frutas.items():
        print(clave, valor)
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio3():
    lista_frutas=[]
    for clave in precio_frutas.keys():
           lista_frutas.append(clave) 
    print(lista_frutas)
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio4():
    agenda_telefonica = {}

    print("---Carga de Contactos---")
    print("Por favor, ingresá los datos de 5 contactos.")
    for i in range(1, 6):
        print(f"\nContacto {i}:")
        nombre = input("Nombre: ").strip()
        
        # Bucle de validación para el teléfono
        while True:
            telefono_input = input("Teléfono: ").strip()
            try:
                int(telefono_input)
                telefono = telefono_input 
                break 
            except ValueError:
                print("Error: El teléfono debe contener solo números, sin letras ni espacios. Intentá de nuevo.")

        agenda_telefonica[nombre] = telefono

    print("\n---Consulta de Agenda---")
    while True:
        busqueda = input("Ingresá el nombre del contacto que querés consultar: ").strip()
        if busqueda in agenda_telefonica:
            print(f"El número de {busqueda} es: {agenda_telefonica[busqueda]}")
        else:
            print(f"El contacto '{busqueda}' no se encuentra en la agenda.")
        continuar=input("¿Desea consultar otro contacto? (s/n): ").strip().lower()
        if continuar == 'n':
            break

    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio5():
    frase = input("Ingresá una frase: ").strip()

    palabras = frase.lower().split()
    palabras_unicas = set(palabras)

    #diccionario con la cantidad de veces que aparece cada palabra
    frecuencia_palabras = {}

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1  # Si ya existe, le sumamos 1 al contador
        else:
            frecuencia_palabras[palabra] = 1  

    print("Resultados")

    print("palabras unicas encontradas:")
    print(palabras_unicas)

    print("\nConteo de palabras:")
    print(frecuencia_palabras)
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio6():

    alumnos={}
    print("ingresando alumnos")
    for i in range(3):
        nombre=input("ingrese el nombre del alumno {}: ".format(i+1)).strip()
        alumnos[nombre]=()
    for nombre in alumnos.keys():
        for i in range(3):     
            while True:
                nota=input(f"ingrese la nota {i+1} de {nombre}: ").strip()
                if not nota.isdigit():
                    print("Error: La nota debe ser un número.")
                    continue
                else:
                    nota=int(nota)
                    if not 1 <= nota <= 10:
                        print("Error: La nota debe estar entre 1 y 10.")
                        continue
                    else:
                        alumnos[nombre]+=(nota,)
                        break

    promedio_alumnos = {}

    # Calcular promedio para cada alumno
    for nombre, notas in alumnos.items():
        suma_notas = 0
        for nota in notas:
            suma_notas += nota
        promedio_alumnos[nombre] = suma_notas / len(notas)

    print("\n---Alumnos ordenados por promedio ---")
    print("Nombre\t\tPromedio")
    for nombre, promedio in promedio_alumnos.items():
        print(f"{nombre}\t\t{promedio:.2f}")
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()
        
def ejercicio7():

    asistencias = []
    print("--- Sistema de Ingreso de Asistencias ---")

    while True:
        nombre = input("Ingrese el nombre del trabajador: ").strip().title()
        if not nombre:
            print("Error: El nombre no puede estar vacío. Intente de nuevo.\n")
            continue
        asistencias.append(nombre)
        while True:
            continuar = input("¿Desea agregar otro trabajador? (s/n): ").strip().lower()
            if continuar in ['s', 'n']:
                break # Sale del bucle de pregunta si respondió bien
            else:
                print("Error: Por favor, ingrese 's' para sí o 'n' para no.")
    
        if continuar == 'n':
            break

    print("\n--- Registro finalizado ---")
    print("Asistencias de la capacitacion:", asistencias)
    
    lista_trabajadores=set(asistencias)
    print("--- Empleados que asistieron (al menos una vez) ---")
    print(lista_trabajadores)
    
    print("--- Cantidad de asistencias por empleado ---")
    for empleado in lista_trabajadores:
        cantidad = asistencias.count(empleado)
        print(f"{empleado} asistió {cantidad} vez/veces.")
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()

def ejercicio8():

    productos={}

    while True:
        print("1. Cargar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                while True:
                    cantidad=input("Ingrese la cantidad de productos: ")
                    if not cantidad.isdigit():
                        print("Error: La cantidad debe ser un número.")
                        continue
                    else:
                        cantidad=int(cantidad)
                        break

                for i in range(cantidad):
                    while True:
                        nombre=input(f"Ingrese el nombre del producto {i+1}: ").strip().title()
                        if not nombre:
                            print("Error: El nombre no puede estar vacío. Intente de nuevo.\n")
                            continue
                        else:
                            break
                            
                    while True:
                        stock=input(f"Ingrese el stock del producto {i+1}: ").strip()
                        if not stock.isdigit():
                            print("Error: El stock debe ser un número.")
                            continue
                        else:
                            stock=int(stock)
                            break
                            
                    productos[nombre]=stock
            case "2":
                print(f"productos: {', '.join(f'{key} : {value}' for key, value in productos.items())}") #80 horas para aprender a hacer esto en una linea
            case "3":
                nombre=input("Ingrese el nombre del producto que desea buscar: ").strip().title()
                if nombre in productos:
                    print(f"El producto {nombre} tiene un stock de {productos[nombre]}")
                else:
                    print(f"El producto {nombre} no se encuentra en la lista")
            case "4":
                nombre=input("Ingrese el nombre del producto que desea modificar: ").strip().title()
                if nombre in productos:
                    while True:
                        stock=input(f"Ingrese el stock a añadir del producto {nombre}: ").strip()
                        if not stock.isdigit():
                            print("Error: El stock debe ser un número.")
                            continue
                        else:
                            stock=int(stock)
                            break
                    productos[nombre]+=stock
                    print(f"Se agregaron {stock} unidades al producto {nombre}")
                else:
                    print(f"El producto {nombre} no se encuentra en la lista")
            case "5":
                nombre=input("Ingrese el nombre del producto que desea eliminar: ").strip().title()
                if nombre in productos:
                    del productos[nombre]
                else:
                    print(f"El producto {nombre} no se encuentra en la lista")
            case "6":
                break

    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()
    
def ejercicio9():
    agenda={}

    while True:
        print("1. Cargar eventos")
        print("2. Mostrar agenda")

        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                while True:
                    dia=input("Ingrese el dia de la semana del evento: ").strip().title()
                    if dia not in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]:
                        print("Error: No existe ese dia de la semana.")
                        continue
                    else:
                        while True:
                            hora=input(f"Ingrese la hora de inicio del evento del dia (formato 24hras) {dia}: ").strip()
                            if not hora:
                                print("Error: La hora no puede estar vacía. Intente de nuevo.\n")
                                continue
                            elif not hora.isdigit():
                                print("Error: La hora debe ser un número.")
                                continue
                            else:
                                hora=int(hora)
                                if 0 <= hora <=23:
                                    break
                                else:
                                    print("Error: La hora debe estar entre 0 y 23.")
                                    continue
                        while True:
                            minutos=input(f"Ingrese los minutos de inicio del evento del dia (formato 60min) {hora}: ").strip()
                            if not minutos:
                                print("Error: Los minutos no puede estar vacía. Intente de nuevo.\n")
                                continue
                            elif not minutos.isdigit():
                                print("Error: Los minutos debe ser un número.")
                                continue
                            else:
                                minutos=int(minutos)
                                if 0 <= minutos <=59:
                                    break
                                else:
                                    print("Error: Los minutos debe estar entre 0 y 59.")
                                    continue
                    while True:
                        evento=input(f"Ingrese el nombre del evento del dia {dia} a las {hora}:{minutos}: ").strip().title()
                        if not evento:
                            print("Error: El evento no puede estar vacío. Intente de nuevo.\n")
                            continue
                        else:
                            break
                    agenda[(dia,hora,minutos)]=evento
                    break
            case "2":
                for key,value in agenda.items():
                    print(f"El dia {key[0]} a las {key[1]}:{key[2]}, hay un evento llamado {value}")
    


    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()


def ejercicio10():
    original={"argentina":"buenos aires","brasil":"brasilia","chile":"santiago"}
    invertido={}    
    for key,value in original.items():
        invertido[value]=key
    print(f" Diccionario original: {original}")
    print(f" Diccionario invertido: {invertido}")
    
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()





class Color:
    VERDE = '\033[92m'
    CYAN = '\033[96m'
    ROJO = '\033[91m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'

def limpiar_pantalla():
    # Detecta si estás en Windows ('nt') o Linux/Mac y limpia la consola
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    opciones = ["Crear nuevo usuario", "Ver base de datos", "Configuraciones", "Salir"]
    
    while True:
        limpiar_pantalla()
        print(f"{Color.CYAN}{Color.NEGRITA}=== MENÚ PRINCIPAL ==={Color.RESET}\n")
        
        # Imprime las opciones automáticamente con su número
        for i, opcion in enumerate(opciones):
            print(f"{Color.VERDE}[{i + 1}]{Color.RESET} {opcion}")
            
        print("\n" + "-" * 22)
        seleccion = input(f"Elegí una opción (1-{len(opciones)}): ")

        # Validamos qué eligió el usuario
        if seleccion == '1':
            print(f"\n{Color.CYAN}>> Elegiste crear un usuario...{Color.RESET}")
            input("Apretá Enter para volver al menú...")
            
        elif seleccion == '2':
            print(f"\n{Color.CYAN}>> Mostrando base de datos...{Color.RESET}")
            input("Apretá Enter para volver al menú...")
            
        elif seleccion == '3':
            print(f"\n{Color.CYAN}>> Abriendo configuraciones...{Color.RESET}")
            input("Apretá Enter para volver al menú...")
            
        elif seleccion == str(len(opciones)): # Opción Salir (la última)
            print(f"\n{Color.VERDE}¡Nos vemos! Saliendo del programa...{Color.RESET}")
            break
            
        else:
            print(f"\n{Color.ROJO}❌ Opción incorrecta. Por favor, ingresá un número válido.{Color.RESET}")
            input("Apretá Enter para intentar de nuevo...")























if __name__ == "__main__":
    mostrar_menu()

