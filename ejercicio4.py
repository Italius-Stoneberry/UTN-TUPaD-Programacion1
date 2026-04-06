
""""Ejercicio 4 — “Escape Room: La Bóveda”
Historia
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.


Variables iniciales (NO se piden por teclado)
• energia = 100
• tiempo = 12
• cerraduras_abiertas = 0
• alarma = False
• codigo_parcial = ""
Validaciones obligatorias



• Pedir nombre del agente y validar con .isalpha() en un while.


• Validar opciones del menú y cualquier número pedido con .isdigit() en un
while.

Regla anti-spam (muy importante)
Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al
iniciar:
✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
• se cobra el costo normal (-20 energía, -2 tiempo),
• NO abre cerradura, y
• se activa la alarma automáticamente (alarma = True) porque “la cerradura se
trabó”.
Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
Menú de acciones (se repite mientras el juego siga)


El juego continúa mientras:
• energia > 0, tiempo > 0, cerraduras_abiertas < 3
• y no esté bloqueado por alarma.
En cada turno mostrar el estado y el siguiente menú:

1. Forzar cerradura (costo: -20 energía, -2 tiempo)
o Si la energía está por debajo de 40, hay “riesgo de alarma”:
▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
o Si no hay alarma, abre 1 cerradura.
o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y
no abre.

2. Hackear panel (costo: -10 energía, -3 tiempo)
o Debe usar un for de 4 pasos mostrando progreso.
o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si
todavía faltan.


3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
energía extra)
Regla de bloqueo por alarma
• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
se bloquea y se pierde.
Condiciones de fin


• Si cerraduras_abiertas == 3 → VICTORIA
• Si energia <= 0 o tiempo <= 0 → DERROTA
• Si se bloquea por alarma → DERROTA (bloqueo)"""

import random

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
antspam = 0
cod=False

nombre = ""
while not nombre.isalpha():
    nombre = input("Ingrese el nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("~"*20)
    print("Energía: ", energia)
    print("Tiempo: ", tiempo)
    print("Cerraduras abiertas: ", cerraduras_abiertas)
    print("Alarma: ", alarma)
    print("Código parcial: ", codigo_parcial)
    print("~"*20 + "\n")
    print("~"*20)
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    print("~"*20 + "\n")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        antspam += 1
        if antspam == 3:
            alarma = True
            print("Alarma activada")
        if energia < 40:
            print("riesgo de alarma")
            while not num.isdigit() or num < 1 or num > 3:
                num=input("inserte un numero del 1 al 3")
                if num.isdigit() and num < 1 or num > 3:
                    print("Perdiste tiempo pulsando un numero equivocado -1 segundo \n`Por que hiciste eso ?`")
                    tiempo -= 1 
            if num == random.randint(1, 3):
                alarma = True
                print("Alarma activada")
            else:
                cerraduras_abiertas += 1
                print("Cerradura forzada")
        else:
            cerraduras_abiertas += 1
            print("Cerradura forzada")

    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        if len(codigo_parcial) >= 8 and cod==False:
            cerraduras_abiertas += 1
            print("Cerradura abierta")
            cod=True
        elif cod==True:
            print("Codigo ya ingresado")
            tiempo +=2 
            continue
        else:
            for i in range(4):
                codigo_parcial += chr(random.randint(65,90))
                print("Código parcial: ", codigo_parcial)
        antspam = 0
    elif opcion == "3":
        energia += 15
        tiempo -= 1
        antspam = 0
        if alarma:
            energia -= 10
    elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        break
    
    else:
        print("Tic tac tic tac")
        tiempo -= 1

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
elif alarma:
    print("DERROTA (bloqueo)")