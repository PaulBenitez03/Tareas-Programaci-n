def maximo_y_minimo (diccionario):
    maximo = max(diccionario.values())
    print(f"El valor maximo es: {maximo}")
    minimo = min(diccionario.values())
    print(f"El valor minimo es: {minimo}")

calificaciones_103 = {"Paul": 7,"Dario":8.3,"Ana":9.4,"Citlalitl":8.9,"Ernesto":6,
                      "Manuel":9.1,"Cinthia":7.3,"Carolina":8.5,"Estefania":7.7,"Dhaniel":5}
maximo_y_minimo(calificaciones_103)