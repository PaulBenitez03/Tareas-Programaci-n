calificaciones_103 = {"Paul": 7,"Dario":8,"Ana":9,"Citlalitl":8,"Ernesto":6,
                      "Manuel":9,"Cinthia":7,"Carolina":8,"Estefania":7,"Dhaniel":5}
dic_2 = {}
for i, j in calificaciones_103.items():
    if j not in dic_2.values():
        dic_2[i] = j  
print(dic_2)