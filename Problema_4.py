def ordenar_diccionario (diccionario):
    lista = sorted(diccionario.items())

    diccionario_ordenado = dict(lista)
    return diccionario_ordenado
calificaciones_103 = {"Paul": 7,"Dario":8,"Ana":9,"Citlalitl":8,"Ernesto":6,
                      "Manuel":9,"Cinthia":7,"Carolina":8,"Estefania":7,"Dhaniel":5}
diccionario_nuevo = ordenar_diccionario(calificaciones_103)
print(diccionario_nuevo)



