"""Ejercicio 2 — “Acceso al Campus y Menú Seguro”
Objetivo: Login con intentos + menú de acciones con validación estricta.
"""

"""Pequeña base de datos de alumnos"""
alumnos = [
    ["alumno", "python123"],
    ["matias", "1223456"],
    ["ana", "ana123"],
    ["juan", "juan123"],
    ["pedro", "pedro123"]
]

"""login"""
intentos=0
posicion_alumno = -1 # Para recordar qué alumno inició sesión
print("\n"*5)
print("Bienvenido al sistema de acceso al campus")
while True:
    alumno=input("Ingrese su usuario: ").strip()
    clave=input("Ingrese su clave: ").strip()

    acceso_concedido = False

    print("\n")

    for i in range(len(alumnos)):
        if alumnos[i][0] == alumno and alumnos[i][1] == clave:
            acceso_concedido = True
            posicion_alumno = i
            break

    if acceso_concedido:
        print("Acceso concedido")
        intentos=4
        break
    else:
        print("Error: credenciales invalidas")
        print("\n")
        print(f"Intento {intentos+1}/3")
        print("\n")
        if intentos==3:
            print("Cuenta bloqueada")
            break

"""menu"""
while intentos==4:
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")
    opcion=input("Ingrese una opcion: ").strip()
    if opcion.isdigit() and int(opcion)>=1 and int(opcion)<=4:
        if opcion=="1":
            print("\n")
            print("Inscripto")
            print("\n")
        elif opcion=="2":
            nueva_clave=input("Ingrese la nueva clave: ").strip()
            if len(nueva_clave)>=6:
                print("Repetir clave")
                nueva_clave2=input("Ingrese la nueva clave de nuevo: ").strip()
                if nueva_clave==nueva_clave2:
                    alumnos[posicion_alumno][1]=nueva_clave
                    print("\n")
                    print("Clave cambiada exitosamente")
                    print("\n")
                else:
                    print("\n")
                    print("Error: las claves no coinciden")
                    print("\n")
            else:
                print("\n")
                print("Error: la clave debe tener al menos 6 caracteres")
                print("\n")
        elif opcion=="3":
            print("\n")
            print("Nunca te rindas")
            print("\n")
        elif opcion=="4":
            print("\n")
            print("Hasta luego")
            print("\n")
            break
    else:
        print("\n")
        print("Error: opcion invalida")
        print("\n")
