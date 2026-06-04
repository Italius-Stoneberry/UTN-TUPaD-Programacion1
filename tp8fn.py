import os

'''
Esta funcion limpia la pantalla.
Se usa en todos los ejercicios para que el codigo se vea mas ordenado.
'''
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

'''
Esta funcion es del ejercicio 1.
Lo que hace es tirar dos errores a proposito.
El primero es un TypeError, porque se intenta dividir un entero con un string.
El segundo es un IndexError, porque se intenta acceder a un indice que no existe en la lista.
'''
def ejercicio1():
    print("""
    a = 10
    b = input("Introduce un número: ")  # aca tiraria error por que el tipo de dato de b es string y no un entero. Type Error
    result = a / b
    print(f"Resultado: {result}")
    numbers = [1, 2, 3]
    print(numbers[5])   # y aca tiraria error por que la lista solo tiene 3 elementos, y se esta intentando acceder al 6to Index Error""")
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()


'''
Esta funcion es del ejercicio 2.
Lo que hace es al ejercicio 1 le agrega validaciones basicas para que el codigo no se rompa sin usar Try/Except.
'''
def ejercicio2():
    #ejercicio 2: (sin Try except)
    a = 10
    while True:
        b = input("Introduce un número: ") 
        if b.isdigit():
            b=int(b)
            if b == 0:
                print("Error: No se puede dividir por cero.")
                continue
            else:
                result = a / b 
                break
        else:
            print("Error: Debe ingresar un número.")

    print(f"Resultado: {result}")
    numbers = [1, 2, 3]
    while True:
        n = input("Introduce un número (0-2): ") 
        if n.isdigit():
            n=int(n)
            if n < 0 or n > 2:
                print("Error: El indice esta fuera de rango.")
                continue
            else:
                print(f"El número en la posición {n} es: {numbers[n]}")
                break
        else:
            print("Error: Debe ingresar un número.")
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla()


'''
Esta funcion combina el ejercicio 3, 4 y 5., lo que hace es el ejercicio 1 le agrega los Try y los Excepts multiples, ademas de uno extra
por si surge otro error inesperado. Tambien le agrega un FINALLY.
'''
def ejercicio3 ():
    #ejercicio 3: (con Try except)

    a = 10
    numbers = [1, 2, 3]
    while True:         #este while es para que el programa no se cierre si hay un error ejercicio 3
        try:
            b = input("Introduce un número: ")
            b=int(b)
            result = a / b
        #multiples excepts para diferentes tipos de errores (ejercicio 4)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
            continue
        except ValueError:
            print("Error: Debe ingresar un número.")
            continue
        except IndexError:
            print("Error: El índice está fuera de rango.")
            continue
        except TypeError:
            print("Error: Se esta utilizando un dato erroneo.")
            continue
        except Exception as e:
            print("Ocurrió el siguiente error: ", type(e).__name__)
            continue
        #se incoporo bloques else y finaly para que el codigo sea mas profecional y muestre mensaje al finalizar la operacion (ejercicio 5)
        else:
            print(f"Resultado de la operacion: {result}")
            break
    
    while True:
        try:
            n=input("Introduce un número indice del (0-2): ")
            n=int(n)
        #multiples excepts para diferentes tipos de errores (ejercicio 4)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
            continue
        except ValueError:
            print("Error: Debe ingresar un número.")
            continue
        except IndexError:
            print("Error: El índice está fuera de rango.")
            continue
        except TypeError:
            print("Error: Se esta utilizando un dato erroneo.")
            continue
        #este except atrapa cualquier otro error que no se haya mencionado anteriormente
        except Exception as e:
            print("Ocurrió el siguiente error: ", type(e).__name__)
            continue    
        #se incoporo bloques else y finaly para que el codigo sea mas profecional y muestre mensaje al finalizar la operacion (ejercicio 5)
        else:
            print(f"numero elegido: {numbers[n]}")
            break
    print("\n")
    input("presiona enter para continuar")
    limpiar_pantalla() 

'''
Esta funcion es del ejercicio 6 y 7.
Lo que hace es usar Try Except y While para que el programa no se cierre si hay un error. Ademas de usar RAISE para lanzar errores personalizados.
'''
def ejercicio4():
    while True:         #este while es para que el programa no se cierre si hay un error ejercicio 3
        try:
            numerito= input("Introduce un número: ")
            numero=int(numerito)
            print(f"El número ingresado fue el: {numero}")
        except ValueError:
            print("Error: Debe ingresar un número válido")
        except Exception as e:
            print("Ocurrió el siguiente error: ", type(e).__name__)
        else:
            print("Operacion realizada exitosamente.")
            break
        finally:    
            print("\n")
            input("presiona enter para continuar")
            limpiar_pantalla()