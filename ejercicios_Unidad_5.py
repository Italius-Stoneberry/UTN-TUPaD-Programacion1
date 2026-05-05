from ast import match_case
from sys import setswitchinterval
import random
"""1)
notas=[]
cant_alum=int(input("Ingrese la cantidad de alumnos: "))
for i in range(cant_alum):
    notas.append(random.randint(1,10))
print(notas)
print("La nota mas alta es: ", max(notas))
print("La nota mas baja es: ", min(notas))
print("El promedio es: ", sum(notas)/len(notas))
"""

"""2)
prod=[]
for i in range (5):
    prod.append(input(f"Dame el producto numero {i+1}: "))
print(f"Los productos son: {prod}")
print(f"Los productos ordenados Alfabeticamente son: {sorted(prod)}")
prod_mod=""
while prod_mod not in prod:
    prod_mod=input("que producto de la lista deseas modificar ?")
prod.remove(prod_mod)
print(prod)
"""
"""3)
num=[]
num_par=[]
num_impar=[]
for i in range(100):
    num.append(random.randint(1,100))
print(num)
print(f"la cantidad de numeros en total es: {len(num)}")
for i in num:
    if i % 2 == 0:
        num_par.append(i)
        num.remove(i)
    else:
        num_impar.append(i)
        num.remove(i)
    
print("Los numeros pares (No repetidos) son: ", num_par)
print(f"La cantidad de numeros pares es: {len(num_par)}")
print("Los numeros impares (No repetidos) son: ", num_impar)
print(f"La cantidad de numeros impares es: {len(num_impar)}")
"""
"""4)
datos=[1,3,5,3,7,1,9,5,3]
datos_nw=[]
for i in datos:
    if i not in datos_nw:
        datos_nw.append(i)
print(datos_nw)
"""
"""5)
estudiantes=["Gabriel Gomez","Vero","Lucas Palazzolo","Italo Rocamora","Joaquin Martinez","Luciano Pizarro","Luciano Calella","Roberto Jaimes"]
estudiantes_mod=""
print(estudiantes)
while True:
    opt=input("Deseas Agregar o eliminar estudiantes ? (1 o 2) o 3 para salir")
    match opt:
        case "1":
            estudiantes_mod=input("que estudiante deseas agregar ?")
            estudiantes.append(estudiantes_mod)
            print(estudiantes)
        case "2":
            while estudiantes_mod not in estudiantes:
                estudiantes_mod=input("que estudiante de la lista deseas eliminar ?")
            estudiantes.remove(estudiantes_mod)
            print(estudiantes)
        case "3":
            break
        case _:
            print("Opcion invalida")
"""
"""6)
num=[0,1,2,3,4,5,6]
print(num)  
ultimo=num[-1]
num.remove(ultimo)
num.insert(0,ultimo)
print(num)
"""
"""7)
temp=[]
prom_max=0
prom_min=0
amplitud_max=0
for i in range(7):
    temp.append([random.randint(15,40),random.randint(-5,15)])
print(temp)
for i in range(7):
    prom_max += temp[i][0]
    prom_min += temp[i][1]
print(f"El promedio de temperaturas maximas es: {prom_max/7}")
print(f"El promedio de temperaturas minimas es: {prom_min/7}")
for i in range(len(temp)):
    amplitud=temp[i][0]-temp[i][1]
    print(f"La amplitud termica del dia {i+1} es: {amplitud}")
    if amplitud > amplitud_max:
        amplitud_max=amplitud
print(f"La amplitud termica maxima es: {amplitud_max}")
"""
"""8)
estudiante=[]
materias=["Matenatica","Fisica","Programacion"]
iteracion=1
cant=1

while iteracion <= cant:
    while True:
        cant=input("Cuantos estudiantes son ? ")
        if cant.isdigit():
            cant=int(cant)
            break
        else:
            print("Numero invalido putito")

    for i in range(cant):
        nombre=input(f"Ingrese el nombre del {i+1}º estudiante: ").capitalize()
        nombre.replace(" ","_")
        if nombre == "":
            print("No se ingresaron nombres")
        else:
            estudiante.append([nombre,[]])
            iteracion+=1

for j in range(len(estudiante)):
    print(estudiante)
    for i in range(len(materias)):
        while True:
            nota=float(input(f"Ingrese la nota final de {materias[i]} en {estudiante[j][0]}: "))
            if nota >= 0 and nota <= 10:
                break
            else:
                print("Nota invalida")
        estudiante[j][1].append(nota)

for i in range(len(estudiante)):
    print(f"El estudiante {estudiante[i][0]} tiene las siguiente notas: ")
    for j in range(len(materias)):
        print(f"{materias[j]}: {estudiante[i][1][j]}")
    print(f"El promedio de {estudiante[i][0]} es: {sum(estudiante[i][1])/len(estudiante[i][1])}")
print(f"El promedio de {estudiante[i][0]} es: {sum(estudiante[i][1])/len(estudiante[i][1])}")

"""
"""
#9) aca se empezo a poner complicadito
columnas=["|"]
tablero=["-","-","-","-","-","-","-","-","-"]
aux = 0
turno=0
jugador=["X","O"]
ganador=True

while aux < 3:
        for i in range(len(tablero)):
            print(tablero[i],end="")
            if not (i == 2 or i == 5 or i == 8):
                print(columnas[0],end="")
            aux+=1
            if aux % 3 == 0:
                print("\n")

while ganador:
    
    
    while True:
        ubi_x=int(input(f"Ingrese la fila donde desea colocar la {jugador[turno % 2]}: "))
        ubi_y=int(input(f"Ingrese la columna donde desea colocar la {jugador[turno % 2]}: "))
        if ubi_x > 3 or ubi_x < 1 or ubi_y > 3 or ubi_y < 1:
            print("Posicion invalida")
            continue
        else:
            break
    if tablero[(((ubi_x*3))+(-3+ubi_y))-1] == "-":
        tablero[(((ubi_x*3))+(-3+ubi_y))-1]=jugador[turno % 2]
        aux=0
        turno+=1
        if turno == 9:
            break
    else:
        print("Esa posicion ya esta ocupada")

    while aux < 3:
            for i in range(len(tablero)):
                print(tablero[i],end="")
                if not (i == 2 or i == 5 or i == 8):
                    print(columnas[0],end="")
                aux+=1
                if aux % 3 == 0:
                    print("\n")
    
    if turno >= 5:
        for i in range(3):
            if (tablero[i] == tablero[i+3] == tablero[i+6]) and tablero[i] != "-":
                print("Gano el jugador ", jugador[(turno-1) % 2])
                ganador=False
                break
            elif (tablero[i] == tablero[i+1] == tablero[i+2]) and tablero[i] != "-":
                print("Gano el jugador ", jugador[(turno-1) % 2])
                ganador=False
                break
        if (tablero[0] == tablero[4] == tablero[8]) and tablero[0] != "-":
            print("Gano el jugador ", jugador[(turno-1) % 2])
            ganador=False
            break
        elif (tablero[2] == tablero[4] == tablero[6]) and tablero[2] != "-":
            print("Gano el jugador ", jugador[(turno-1) % 2])
            ganador=False
            break
"""
"""
#10)

productos=[]
semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
maximo=0
maximo_dia=0
prod_max=""
prod_max_dia=""
total_dia=0

cantidad=int(input("Ingrese la cantidad de productos: ")) #supuestamente 4
for i in range(cantidad):
    productos.append([input(f"Ingrese el producto numero {i+1}: "),[]])
print(productos)

for j in range(len(semana)):
    for i in range(len(productos)):
        #venta=float(input(f"Ingrese el monto de la venta del producto {productos[i][0]} del dia {semana[j]}: "))
        #le meto un random por que si no estoy 20 dias probando un error metiendo 7 numeros cada vez
        venta=int(random.randint(1,100))
        print(f"El dia {semana[j]} se vendio: {venta} del producto {productos[i][0]}")
        productos[i][1].append(venta)

#aca no se empieza a entender una goma asique voy a eplicar un poco
#aca lo que se hace es recorrer la lista de productos y sumar las ventas de cada uno
for i in range(len(productos)):
    print(f"El total de ventas del producto {productos[i][0]}: {sum(productos[i][1])}")
    if maximo < sum(productos[i][1]): #aca lo que se hace es comparar el maximo con la suma de las ventas de cada producto
        maximo=sum(productos[i][1])
        prod_max=i #aca se guarda el indice del dia que mas se vendio

for j in range(len(semana)): # esto recorre los dias
    for i in range(len(productos)): # y esto los productos
        total_dia+=productos[i][1][j] # aca se suma el total de ventas de cada dia
    if maximo_dia < total_dia: #aca lo que se hace es comparar el maximo con la suma de las ventas de cada dia
        maximo_dia=total_dia      
        prod_max_dia=j #aca se guarda el indice del dia que mas se vendio
    total_dia=0 #aca se reinicia el total de ventas para que este limpio para el otro dia.

print(f"El producto que mas se vendio fue el {productos[prod_max][0]} con un total de {maximo} ventas")
print(f"El dia {semana[prod_max_dia]} fue el dia que mas se vendio con un total de {maximo_dia} ventas")
"""

#11 y aca paso a ser facil de nuevo
"""
estudiantes=["Gabriel","Vero","Lucas","Italo","Joaquin","Luciano","Luciano","Roberto","Lucas","Martin","Mateo"]
estudiantes_mod=""
print(estudiantes)
while True:
        estudiantes_mod=input("que estudiante de la lista deseas buscar ?('Salir' para salir): ").capitalize()
        if estudiantes_mod == "Salir":
            break
        if estudiantes_mod in estudiantes:
            print(f"El estudiante {estudiantes_mod} se encuentra en la posicion {estudiantes.index(estudiantes_mod)+1}")
            print(estudiantes)
        else:
            print("Estudiante no encontrado")
"""

#12
"""
lista=[]
for i in range(8):
    num=input(f"Dame el numero {i+1} de 8: ")
    while not num.isdigit():
        print("Numero invalido")
        num=input()
    num=int(num)
    lista.append(num)

print(f"Asi es la lista original: {lista}")
print(f"Asi es la lista ordenada: {sorted(lista)}")
print(f"Asi es la lista invertida: {reversed(lista)}")
"""
#13
"""
lista=[450,1200,875,990,300,1500,640]
print(f"El puntaje mas alto es {max(lista)}")
print(f"El puntaje mas bajo es {sorted(lista)}")
print(f"El la posicion del puntaje 990 es: {lista.index(990)+1}")
"""

