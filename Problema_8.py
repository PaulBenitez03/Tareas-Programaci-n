def diccionario_vacio(diccionario):
    if len(diccionario) == 0:
        print("El diccionario esta vacio")
    else:
        a = len(diccionario)
        print(f"El diccionario tiene {a} elementos")

calificaciones_103 = {"Paul": 7,"Dario":8,"Ana":9,"Citlalitl":8,"Ernesto":6,
                      "Manuel":9,"Cinthia":7,"Carolina":8,"Estefania":7,"Dhaniel":5}
vacio = {}
diccionario_vacio(calificaciones_103)
diccionario_vacio(vacio)