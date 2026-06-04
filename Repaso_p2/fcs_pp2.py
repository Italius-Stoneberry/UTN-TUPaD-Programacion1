""""
Desafío Práctico: El Inventario del Club de Lectura
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
1. Carga inicial: Preguntar cuántos libros se van a registrar por primera vez. Por cada uno, pedir el título y la
cantidad de copias.
2. Ver catálogo: Recorrer nuestra lista y mostrar todos los libros con su cantidad de copias actuales.
3. Buscar libro: El usuario escribe un título y le decimos si lo tenemos y cuántas copias quedan. ¡Avisar
amablemente si no lo tenemos!
4. Alerta de agotados: Mostrar solo aquellos libros que tienen 0 copias para saber cuáles hay que reponer.
5. Sumar un título nuevo: Agregar un nuevo diccionario a la lista con su título y cantidad de copias.
6. Prestar o Devolver (Actualizar): Modificar las copias de un libro que ya existe. Si lo prestamos, restamos uno;
si lo devuelven, sumamos uno.
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
ejecución.
"""
import practica_parcial_2 as pp2

while True:
    opcion = pp2.mostrar_menu()
    try:
        match opcion:
            case 1:
                pp2.cargar_inicial()
            case 2:
                pp2.ver_catalogo()
            case 3:
                pp2.buscar_libro()
            case 4:
                pp2.agotados()
            case 5:
                pp2.aniadir_producto()
            case 6:
                pp2.Prestar_productos()
            case 7:
                print('Gracias por usar el programa')
                break
    except ValueError as e:
        print(f'Error: {e}')
