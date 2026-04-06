"""Ejercicio 3 (Alta) — “Agenda de Turnos con
Nombres (sin listas)”
Contexto
Hay 2 días de atención: Lunes y Martes.
Cada día tiene cupos fijos:
• Lunes: 4 turnos
• Martes: 3 turnos
Reglas
1. Pedir nombre del operador (solo letras).
2. Menú repetitivo hasta salir:
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
3. Reservar:
o Elegir día (1=Lunes, 2=Martes).
o Pedir nombre del paciente (solo letras).
o Verificar que no esté repetido en ese día (comparando con las variables
ya cargadas).
o Guardar en el primer espacio libre (ej. lunes1, lunes2...).
4. Cancelar:
o Elegir día.
o Pedir nombre del paciente (solo letras).
o Si existe, cancelar y dejar el espacio vacío ("").
5. Ver agenda del día:

o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
está vacío.

Restricciones
• ❌ No listas, no diccionarios, no sets, no tuplas.
• ✅ Se permite usar "" como “vacío”.
• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except)"""


lunes1=""
lunes2=""
lunes3=""
lunes4=""
L_cupos=4
martes1=""
martes2=""
martes3=""
Mt_cupos=3

while True:




    print("""
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema
    """)

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        
        nombre = input("Ingrese el nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Ingrese el nombre del paciente: ")
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("El paciente ya tiene un turno")
            elif nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("El paciente ya tiene un turno")

        dia = input("Seleccione un día (1=Lunes, 2=Martes): ")
        if dia == "1":

                if lunes1 == "":
                    lunes1 = nombre
                    L_cupos-=1
                elif lunes2 == "":
                    lunes2 = nombre
                    L_cupos-=1
                elif lunes3 == "":
                    lunes3 = nombre
                    L_cupos-=1
                elif lunes4 == "":
                    lunes4 = nombre
                    L_cupos-=1
                else:
                    print("No hay turnos disponibles")
        elif dia == "2":
                if martes1 == "":
                    martes1 = nombre
                    Mt_cupos-=1
                elif martes2 == "":
                    martes2 = nombre
                    Mt_cupos-=1
                elif martes3 == "":
                    martes3 = nombre
                    Mt_cupos-=1
                else:
                    print("No hay turnos disponibles")
        else:
            print("Opción inválida")
    elif opcion == "2":

        nombre = ""
        while not nombre.isalpha():
            nombre = input("Ingrese el nombre del paciente: ")
            if nombre != lunes1 or nombre != lunes2 or nombre != lunes3 or nombre != lunes4:
                print("El paciente no tiene un turno")
            elif nombre != martes1 or nombre != martes2 or nombre != martes3:
                print("El paciente no tiene un turno")

        dia = input("Seleccione un día (1=Lunes, 2=Martes): ")
        if dia == "1":

            if nombre == lunes1:
                lunes1 = ""
                L_cupos+=1
            elif nombre == lunes2:
                lunes2 = ""
                L_cupos+=1
            elif nombre == lunes3:
                lunes3 = ""
                L_cupos+=1
            elif nombre == lunes4:
                lunes4 = ""
                L_cupos+=1

        elif dia == "2":

            if nombre == martes1:
                martes1 = ""
                Mt_cupos+=1
            elif nombre == martes2:
                martes2 = ""
                Mt_cupos+=1
            elif nombre == martes3:
                martes3 = ""
                Mt_cupos+=1
        else:
            print("Opción inválida")

    elif opcion == "3":
        dia = input("Seleccione un día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print("Turnos del lunes:")
            print("1. ", lunes1)
            print("2. ", lunes2)
            print("3. ", lunes3)
            print("4. ", lunes4)
        elif dia == "2":
            print("Turnos del martes:")
            print("1. ", martes1)
            print("2. ", martes2)
            print("3. ", martes3)
        else:
            print("Opción inválida")
    elif opcion == "4":
        print("Resumen general:")
        
        if lunes1=="" and lunes2=="" and lunes3=="" and lunes4=="":
            print("No hay turnos ocupados en lunes")
        else:
            print("Turnos ocupados en lunes: ", lunes1, lunes2, lunes3, lunes4)
        if martes1=="" and martes2=="" and martes3=="":
            print("No hay turnos ocupados en martes")
        else:
            print("Turnos ocupados en martes: ", martes1, martes2, martes3)


        if lunes1=="" and lunes2=="" and lunes3=="" and lunes4=="":
            print("Turnos disponibles en lunes: ", L_cupos)
        else:
            print("Turnos disponibles en lunes: ", L_cupos)
        if martes1=="" and martes2=="" and martes3=="":
            print("No hay turnos disponibles en martes")
        else:
            print("Turnos disponibles en martes: ", Mt_cupos)

            1
        if L_cupos < Mt_cupos:
            print("El dia con mas turnos es el lunes")
        elif Mt_cupos < L_cupos:
            print("El dia con mas turnos es el martes")
        else:
            print("Ambos dias tienen la misma cantidad de turnos")
    
    elif opcion == "5":
        print("Cerrando sistema...")
        break
    else:
        print("Opción inválida")