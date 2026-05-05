def calcular_promedio(lista):
    return sum(lista)/len(lista)

def filtrar_aprobados(lista):
    aprobados=[]
    for i in lista:
        if i >= 6:
            aprobados.append(i)
    return aprobados

def max_notas(lista):
    max_nota=lista[0]
    for i in lista:
        if i > max_nota:
            max_nota=i
    return max_nota

def min_notas(lista):
    min_nota=lista[0]
    for i in lista:
        if i < min_nota:
            min_nota=i
    return min_nota

def analizar_notas(lista):
    return max_notas(lista),min_notas(lista),calcular_promedio(lista)