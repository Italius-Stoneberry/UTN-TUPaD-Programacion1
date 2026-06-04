def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


##definimos una funcion para mostrar el arbol de directorios que usa el sistema operativo

#suponiendo que partimos de partimos de un sistema de carpetas convencional como el de windows
mi_sistema = {
    "Documentos": {
        "tesis.pdf": "archivo",
        "notas.txt": "archivo"
    },
    "Fotos": {
        "Vacaciones": {
            "playa.jpg": "archivo",
            "montaña.png": "archivo"
        },
        "perfil.jpg": "archivo"
    },
    "configuracion.ini": "archivo"
}
#usamos diccionarios anidados para simular un sistema de carpetas y archivos

"""
Función recursiva para explorar un sistema de carpetas y archivos.
    :param estructura: Diccionario que representa el sistema de carpetas y archivos.
    :param nivel: Nivel de profundidad en la recursión (por defecto 0).
"""

def explorar_directorio(estructura, nivel=0):
    

    # esto genera sangría para que se vea lindo
    sangria = "  " * nivel 
    

    # recorremos los elementos del diccionario actual
    for nombre, contenido in estructura.items(): #clasica funcion k,v in diccionario
        #osea va a ir en orden recorriendo de arriba hacia abajo,



        #CASO RECURSIVO: Si el contenido es un diccionario, es una CARPETA
        if type(contenido) is dict: #la funcion type() nos devuelve el tipo de dato de la variable, en este caso si es un diccionario, va a imprimir una sangria y el nombre de la "carpeta" y luego se va a llamar a si mismo con el contenido de esa carpeta
            print(f"{sangria}📁 Carpeta: {nombre}")
            
            #Se llama a si mismo, para entrar de nuevo en la siguiente carpeta (si es que la hay)    
            # pasándole el contenido de esa carpeta y sumando 1 al nivel.
            explorar_directorio(contenido, nivel + 1)
            
        #CASO BASE: Si no es un diccionario (es un string), es un ARCHIVO
        else:
            print(f"{sangria}📄 Archivo: {nombre}")


            '''en la ejecucion, lo que va a hacer es, agarrar el primer elemento de mi sistema, "Documentos", verifica que tipo de archivo es, "Sos un diccionario ? si/no"
            (SI!) LISTO dibujo una carpetita, y mando todo el contenido a recursividad, dandole al for ahora que recorra el directorio "Documentos"
            ,de vuelta,
            va agarrando archivo por archivo buscando diccionarios, (nada encontro 2 archivos nomas) imprime los archivos de 2do nivel
            Se vuelve al for del contenido del sistema, ya paso por "Documentos", ahora se mete con "Fotos",verifica que tipo de archivo es, "Sos un diccionario ? si/no"
            (SI!) LISTO dibujo una carpetita, y mando todo el contenido a recursividad, dandole al for ahora que recorra el directorio "Fotos"
            resulta que en fotos hay otro diccionario "Vacaciones", verifica que tipo de archivo es, "Sos un diccionario ? si/no"
            (SI!) LISTO dibujo una carpetita en el segundo nivel, y mando todo el contenido a recursividad, dandole al for ahora que recorra el directorio "Vacaciones"
            recorre los archivos de vacacion, y se vuelve al for del contenido del sistema.. y asi sucesivamente con el contenido del sistema, iterando el nivel de profundidad de cada directorio.

            a esto se lo conoce como arbol de directorios y es una estructura de datos que se utiliza para representar un sistema de archivos. 
            '''

# --- Ejecutamos el código --
print("Iniciando exploración del sistema:\n")
explorar_directorio(mi_sistema)