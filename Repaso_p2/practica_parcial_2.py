'''Desafío Práctico: El Inventario del Club de Lectura
Para seguir afianzando lo que venimos trabajando sobre listas, diccionarios, funciones y manejo de errores, vamos a
armar un pequeño sistema en consola.
Imaginen que estamos organizando nuestro propio club de lectura y necesitamos dejar de anotar todo en papel para
pasar a un registro digital de los libros que tenemos disponibles para prestar.
¿Cómo vamos a guardar la información?
Vamos a usar una única lista principal llamada biblioteca. Cada libro que agreguemos será un diccionario adentro de
esa lista, usando exactamente dos claves: 'titulo' y 'copias'. Ejemplo para que se guíen: biblioteca = [{'titulo': 'Romper
el círculo', 'copias': 3}, {'titulo': 'El arte de ser nosotros', 'copias': 1}]
Las opciones del menú
El programa debe tener un menú interactivo que no se cierre hasta que el usuario elija la opción de salir. Las tareas
que debe poder hacer son:





.
6.
7. Salir de la biblioteca.
Buenas prácticas de programación
Para que el código quede prolijo y a prueba de todo, intenten aplicar lo siguiente:
• Divide y reinarás: No escriban todo de corrido. Creen una función (def) para resolver cada una de las
misiones del menú. El bloque principal solo debería encargarse de mostrar las opciones y llamar a la función
que corresponda.
• El menú: Pueden construirlo usando un ciclo while y la estructura match/case. Recuerden que si en algún
momento del código necesitan evaluar múltiples valores para un mismo caso, la forma correcta de hacerlo es
usando el operador | (por ejemplo: case 'salir' | '7':).
• Atrapando errores (try/except): Si el programa les pide un número (como la cantidad de copias o la opción
del menú) y el usuario escribe texto, eviten que el programa "explote" usando try y except ValueError.
• Protegiendo los datos (raise): Creen sus propias validaciones. Por ejemplo, no deberíamos permitir cargar un
libro sin nombre, registrar copias negativas, o prestar un libro si las copias ya están en cero. Usen raise para
frenar esas acciones, lanzar un mensaje explicando el problema y volver al menú principal sin que se corte la
ejecución.'''



catalogo = []


def mostrar_menu():
    print('--Menu biblioteca--')
    print('1- Carga inicial')
    print('2- Ver catálogo')
    print('3- Buscar libro')
    print('4- Alerta de agotados')
    print('5- Sumar un título nuevo')
    print('6- Prestar o Devolver')
    print('7- Salir')
    opcion = input('Ingrese una opción: ')
    if not opcion.isdigit():
        raise ValueError("Debe ingresar un número.")
    else:
        opcion = int(opcion)
        if opcion < 1 or opcion > 7:
            raise ValueError("Debe ingresar un número entre 1 y 7.")
    return opcion

def cargar_inicial():
    """
    1. Carga inicial: Preguntar cuántos libros se van a registrar por primera vez. Por cada uno, pedir el título y la
    cantidad de copias.
    """
    print("--- Carga Inicial ---")
    try:
        cant_libros = input("¿Cuántos libros vas a registrar por primera vez?: ")
        if not cant_libros.isdigit():
            raise ValueError("Debe ingresar un número.")
        else:
            cant_libros = int(cant_libros)
            if cant_libros <= 0:
                raise ValueError("Debe ingresar un número mayor a 0.")
        
    
        for i in range(cant_libros):
            titulo = input(f"Ingrese el título del libro #{i + 1}: ").capitalize()
            if not titulo:
                raise ValueError("El título no puede estar vacío.")
                
            copias = validar_cantcopias(input(f"Ingrese la cantidad de copias del libro '{titulo}': "))
            catalogo.append({'titulo': titulo, 'copias': copias})
            print("El catálogo ha sido cargado exitosamente.")

    except ValueError as e:
        print(f"Error: {e}")


def ver_catalogo():
    """Ver catálogo: Recorrer nuestra lista y mostrar todos los libros con su cantidad de copias actuales."""
    print("--- Catálogo Actual ---")
    try:   
        validar_catalogo()
        for libro in catalogo:
            print(f"Título: {libro['titulo']}, Copias: {libro['copias']}")
    except ValueError as e:
        print(f"Error: {e}")

def buscar_libro():
    """Buscar libro: El usuario escribe un título y le decimos si lo tenemos y cuántas copias quedan. ¡Avisar
amablemente si no lo tenemos!"""
    print("--- Buscar Libro ---")
    try:    
        titulo = validar_titulo()
        for libro in catalogo:
            if libro['titulo'] == titulo:
                print(f"El libro '{titulo}' está disponible con {libro['copias']} copias.")
                return
        raise ValueError(f"El libro '{titulo}' no se encuentra en el catálogo.")
    except ValueError as e:
        print(f"Error: {e}")

def agotados():
    """Alerta de agotados: Mostrar solo aquellos libros que tienen 0 copias para saber cuáles hay que reponer."""
    print("--- Libros Agotados ---")
    try:
        validar_catalogo()
        libros_agotados = [libro['titulo'] for libro in catalogo if libro['copias'] == 0]
        if not libros_agotados:
            raise ValueError("No hay libros agotados.")
        for libro in libros_agotados:
            print(f"Título: {libro}, Copias: 0")
    except ValueError as e:
        print(f"Error: {e}")
    


def aniadir_producto():
    """5. Sumar un título nuevo: Agregar un nuevo diccionario a la lista con su título y cantidad de copias"""
    print("--- Añadir Libro ---")
    try:
        titulo = validar_titulo()

        copias = validar_cantcopias(input(f"Ingrese la cantidad de copias del libro '{titulo}': "))
        catalogo.append({'titulo': titulo, 'copias': copias})
        print("El libro ha sido agregado exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")

def Prestar_productos():
    """ Prestar o Devolver (Actualizar): Modificar las copias de un libro que ya existe. Si lo prestamos, restamos uno;
si lo devuelven, sumamos uno."""
    try:
        validar_catalogo()
        opcion = validar_cantcopias(input("¿Qué desea hacer? 1- Pedir 2- Devolver: "))
        if opcion == 1:
                titulo = validar_titulo()

                """libros_agotados = [libro['titulo'] for libro in catalogo if libro['copias'] == 0]"esto de abajo es esto mismo pero escrito diferente"""
                for libro in catalogo:
                    if libro['titulo'] == titulo:
                        if libro['copias'] == 0:
                            raise ValueError("No hay copias disponibles para prestar.")

                        libro['copias'] -= 1
                        print(f"El libro '{titulo}' ha sido prestado exitosamente.")
                        return
                raise ValueError(f"El libro '{titulo}' no se encuentra en el catálogo.")
        elif opcion == 2:
                titulo = validar_titulo()
                for libro in catalogo:
                    if libro['titulo'] == titulo:
                        libro['copias'] += 1
                        print(f"El libro '{titulo}' ha sido devuelto exitosamente.")
                        return
                raise ValueError(f"El libro '{titulo}' no se encuentra en el catálogo.")
        else:
            raise ValueError("Opción no válida.")
    except ValueError as e:
        print(f"Error: {e}")

def validar_catalogo():
    """pequenia verificacion para no repetir en busqueda y en mostrar catalogo"""
    if not catalogo:
        raise ValueError("El catálogo está vacío. No se puede realizar la operación.")

def validar_cantcopias(cant_copias):
    
    """valida que la cantidad de copias sea un numero y mayor a 0 (ni tampoco 0)"""
    if not cant_copias.isdigit():
        raise ValueError("Se debe ingresar un numero valido.")
    else:
        cant_copias = int(cant_copias)
        if cant_copias <= 0:
            raise ValueError("Se debe ingresar un numero mayor a 0.")
    return cant_copias

def validar_titulo():
    titulo_val = input("Ingrese el título del libro: ").capitalize()
    if not titulo_val:
        raise ValueError("El título no puede estar vacío.")
    return titulo_val
    