nombres_prod = ["arroz","zapallo","papa"] 
stock_prod = ["1","2","3"] 
precios_prod = ["1200","123","1234"]



print("Buenos dias cliente")
while True:
    print('''Menu:
          1. Cargar Individual de productos.
          2. Carga Masiva de productos.
          3. Borrar producto.
          4. Buscar producto.
          5. Mov de stock
          6.
          7.
          8. Salir.
        ''')
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            
            stock = int(input("Ingrese el stock del producto: "))
            while not stock.isdigit():
                stock =int(input("Ingrese numero valido de stock del producto: "))
            
            precio = float(input("Ingrese el precio del producto: "))
            while not precio.isdigit():
                precio =float(input("Ingrese precio valido del producto: "))

            nombres_prod.append(nombre)
            stock_prod.append(stock)
            precios_prod.append(precio)
        
        case "2":
            cantidad=int(input("Deme la cantidad de productos a aniadir"))
            
            for i in range(cantidad):
                nombre = input("Ingrese el nombre del producto: ").strip()
                
                stock = int(input("Ingrese el stock del producto: "))
                while not stock.isdigit():
                    stock =int(input("Ingrese numero valido de stock del producto: "))
            
                precio = float(input("Ingrese el precio del producto: "))
                while not precio.isdigit():
                    precio =float(input("Ingrese precio valido del producto: "))

                nombres_prod.append(nombre)
                stock_prod.append(stock)
                precios_prod.append(precio)        

        case "3":
             
            nombre = input("Ingrese el producto a eliminar: ").strip()
            if nombre == "":
                print("No puede estar vacío.")
            else:

                """"borrado con indice"""
                encontrado = False
                for i in range(len(nombres_prod)):
                    if nombres_prod[i].lower() == nombre.lower():

                        nombres_prod.pop(i)
                        stock_prod.pop(i)
                        precios_prod.pop(i)
                        print("Producto eliminado.")
                        encontrado = True
                        break
                
                if not encontrado:
                    print("Producto no encontrado.") 


        case "4":
            nombre = input("Ingrese el producto a buscar: ").strip()
            if nombre == "":
                print("No puede estar vacío.")
            else:
                encontrado = False
                for i in range(len(nombres_prod)):
                    if nombres_prod[i].lower() == nombre.lower():
                        
                        opcion2=int(input("Producto encontrado ! , desea ver stock o precio (1 o 2)"))

                        if opcion2 == 1:
                            print(f"El stock del producto {nombre} Es :{stock_prod[i]}")
                        elif opcion2 == 2:
                            print(f"El precio del producto {nombre} Es :{precios_prod[i]}")
                        else:
                            print("Opcion invalida")
                        opcion2 = 0
                        encontrado = True
                        break
                
                if not encontrado:
                    print("Producto no encontrado.") 


        case "5":
            nombre = input("Ingrese el producto a modificar: ").strip()
            if nombre == "":
                print("No puede estar vacío.")
            else:
                encontrado = False
                for i in range(len(nombres_prod)):
                    if nombres_prod[i].lower() == nombre.lower():
                        indice=i
                        encontrado = True
                        break
                if not encontrado:
                    print("Producto no encontrado.")

            opcion2=int(input("Que operacion desea realizar, \n 1 para vender o 2 para reponer"))
            match opcion2:
                case 1:
                    cantidad=int(input("Cuanta cantidad de stock desea remover"))
                    while cantidad < 0:
                        cantidad=int(input("Deme una cantidad a remover valida"))
                    if stock[indice] < cantidad:
                        print("Error cantidad invalida")
                    else:
                        stock[indice] -= cantidad
                case 2:
                    cantidad=int(input("Cuanta cantidad de stock desea sumar"))
                    while cantidad < 0:
                        cantidad=int(input("Deme una cantidad a sumar valida"))
                    stock[indice] += cantidad   

        case "6":
            hay = False
            for i in range(len(stock_prod)):
                if stock_prod[i] == 0:
                    print(nombres_prod[i])
                    hay = True
            if not hay:
                print("No hay productos agotados.")
        case "7":
            if len(nombres_prod) == 0:
                print("No hay productos cargados.")
            else:
                print("NOMBRE | STOCK | PRECIO")
                print("------------------------")
                for i in range(len(nombres_prod)):
                    print(
                        f"{nombres_prod[i]} | {stock_prod[i]} | ${precios_prod[i]}")
        case _:
            print("Opción incorrecta, por favor ingrese una opción válida: ")