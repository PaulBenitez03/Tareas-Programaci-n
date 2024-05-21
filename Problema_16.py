def filtrar_pares (diccionario):
    diccionario_filtrado = {}
    for clave, valores in diccionario.items():
        numeros_pares = [valor for valor in valores if valor%2 == 0]
        diccionario_filtrado[clave] = numeros_pares
    return diccionario_filtrado

dic1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dic2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
pares_1 = filtrar_pares(dic1)
pares_2 = filtrar_pares(dic2)
print(pares_1)
print(pares_2)