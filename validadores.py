def validadores_enteros(numero):
    while True:
        if not numero.isdigit():
            print("Error: El numero debe ser un numero entero")
            continue
        else:
            break
    return numero
def validadores_nombres_apellidos(nombre):
    while True:
        if not nombre.isalpha():
            print("Error: El nombre debe ser una palabra")
            continue
        else:
            break
    return nombre 