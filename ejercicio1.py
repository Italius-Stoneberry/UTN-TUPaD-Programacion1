"""
Requisitos 
1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
2. Pedir cantidad de productos a comprar (número entero positivo, validar con 
.isdigit() en while). 
3. Por cada producto (usar for): 
o Pedir precio (entero, validar .isdigit()). 
o Pedir si tiene descuento S/N (validar con while, aceptar s o n en 
cualquier mayuscula/minuscula). 
o Si tiene descuento: aplicar 10% al precio de ese producto. 
4. Al final mostrar: 
o Total sin descuentos 
o Total con descuentos 
o Ahorro total 
o Promedio por producto (usar float y formatear con :.2f, ejem: 
x = 3.14159 
print(f"{x:.2f}")) 

Cliente: Ana 
Cantidad de productos: 3 
Producto 1 - Precio: 100  Descuento (S/N): s 
Producto 2 - Precio: 50   Descuento (S/N): n 
Producto 3 - Precio: 200  Descuento (S/N): s 
Total sin descuentos: $350 
Total con descuentos: $320.00 
Ahorro: $30.00 
Promedio por producto: $106.67


"""




""""Caja de Kiosko"""
carro=[]
total=0.0
totalcondesc=0.0

while True:
    nom_clien=input("Ingrese el nombre del cliente:").strip()
    if nom_clien.isalpha() and nom_clien != "":
        break
    print("Nombre invalido")
print("Bienvenid@", nom_clien.capitalize())

while True:
        cantidad=input("Ingrese la cantidad de productos: ").strip()
        if cantidad.isdigit() and int(cantidad)>0:
            break
        print("Cantidad invalida")
print("Usted lleva", cantidad, "productos")

for i in range(int(cantidad)):
    carro.append([i+1,0,0])

for i in range(len(carro)):
    print("-"*20)
    print(f"para el producto {carro[i][0]} ingrese el precio")
    print("-"*20)

    while True:
        precio=input("Ingrese el precio: ").strip()
        if precio.isdigit() and int(precio)>0:
            carro[i][1]=int(precio)
            break

        print("Precio invalido")
    while True:
        dest=input("El producto tiene algun descuento?? (S o N)").strip().lower()
        if dest == "s" or dest == "n":
            break
        print("Respuesta invalida")
    if dest == "s":
        print("-"*20)
        print("se aplicara un descuento del 10 porciento")
        print("-"*20)
        carro[i][2]=int(precio)*0.9
    else:
        carro[i][2]=int(precio)
    
    
    total+=carro[i][1]
    totalcondesc+=carro[i][2]

ahorro=total-totalcondesc

print("\n"*5)
print("Resumen de la compra:")
print("-"*20)
for i in range(len(carro)):
    print(f"Producto {carro[i][0]} - Precio: {carro[i][1]}", end="")
    if carro[i][2] != carro[i][1] and carro[i][2] != 0:
        print(f" - Descuento (S/N): {carro[i][2]}")
    else:
        print(" - Descuento (S/N): No")

print(f"El total a pagar es: {totalcondesc}")
print(f"El total sin descuento es: {total}")
print(f"El ahorro es: {ahorro}")
print(f"El promedio por producto es: {totalcondesc/len(carro):.2f}")





