def imprimir_hola_mundo():
    print("Hola mundo")

#programaa principal
imprimir_hola_mundo()

#ejercicio 2

def saludar_usuario(nombre):
    print("hola, " + nombre +  "!")

saludar_usuario("itiro")

#ejercicio 3

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

informacion_personal("itiro","bonzatto",20,"quilmes")

#ejercicio 4

def calc_perimetro_circulo(radio):
    return 3.14 * (radio * 2)
def calc_area_circulo(radio):
    return 3.14 * (radio ** 2)

print(f"El area del circulo es {calc_area_circulo(5)} y el perimetro es {calc_perimetro_circulo(5)}")

#ejercicio 5

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas
print(segundos_a_horas(3600))

#ejercicio 6

def tabla_de_multiplicar(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

tabla_de_multiplicar(5)

#ejercicio 7

def operaciones_basicas(num1,num2):
    print(f"La suma es {num1 + num2}")
    print(f"La resta es {num1 - num2}")
    print(f"La multiplicacion es {num1 * num2}")
    print(f"La division es {num1 / num2}")

operaciones_basicas(5,3)

#ejercicio 8

def calcular_imc(peso,altura):
    return peso / (altura ** 2)

def estado_imc(imc):
    if imc < 18.5:
        return "bajo peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

while True:
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: ")) 

print(f"tu IMC es {calcular_imc(peso,altura)} y tu estado es {estado_imc(calcular_imc(peso,altura))}")


#ejercicio 9

def celcius_fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

while True:
    temperatura = (input("Ingrese la temperatura en grados celcius: "))
    if not temperatura.isdigit():
        print("Error: La temperatura debe ser un numero")
        continue
    else:
        break
temperatura = float(temperatura)
print(f"La temperatura en grados fahrenheit es {celcius_fahrenheit(temperatura)}")

#ejercicio 10

def calcular_promedio(a,b,c):
    return (a + b + c) / 3

while True:
    numero1 = (input("Ingrese el primer numero: "))
    numero2 = (input("Ingrese el segundo numero: "))
    numero3 = (input("Ingrese el tercer numero: "))
    if not numero1.isdigit() or not numero2.isdigit() or not numero3.isdigit():
        print("Error: Todos los valores deben ser numeros")
        continue
    else:
        break
numero1 = float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)
print(f"El promedio de los numeros es {calcular_promedio(numero1,numero2,numero3)}")   

    