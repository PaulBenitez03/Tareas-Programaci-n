def multiplicar_elementos (diccionario):
    resultado = 1
    for i in diccionario.values():
        resultado = resultado*i

    return resultado

calificaciones_103 = {"Paul": 7,"Dario":8,"Ana":9,"Citlalitl":8,"Ernesto":6,
                      "Manuel":9,"Cinthia":7,"Carolina":8,"Estefania":7,"Dhaniel":5}
l = multiplicar_elementos(calificaciones_103)
print(l)