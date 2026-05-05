import funciones

notas=[]
for i in range(10):
    notas.append(int(input(f"Ingrese la nota {i+1}: ")))
print(f"El promedio es: {funciones.calcular_promedio(notas)}")

print(f"Los aprobados son: {funciones.filtrar_aprobados(notas)}")
print(f"La cantidad de aprobados es: {len(funciones.filtrar_aprobados(notas))}")
print(f"El porcentaje de los aprobados es: {(len(funciones.filtrar_aprobados(notas))/len(notas))*100}")



