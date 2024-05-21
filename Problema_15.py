def elementos_por_valor(diccionario):
    diccionario_nuevo = []
    valor_buscado = int(input("Introduce el valor a buscar: "))
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            diccionario_nuevo.append(clave)
    return diccionario_nuevo

calificaciones = {'Ingles':7,'Español':6,'Matematicas':10,'Fisica':10,'Quimica':10,'Programacion':5}
elementos_encontrados = elementos_por_valor(calificaciones)
print("Elementos encontrados:", elementos_encontrados)
