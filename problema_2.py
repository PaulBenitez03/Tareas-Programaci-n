#Se define una funcion para eliminar la clave
def eliminar_clave (diccionario):
#El input lo utilizamos para que el usuario decida que clave eliminar
    clave = input("Ingrese la clave del elemento que desea eliminar: ")
    if clave in diccionario:
        del diccionario[clave]
        print(f"El elemento {clave} fue eliminado con exito")
    else:
        print(f"El elemento {clave} no se encuentra en el diccionario")
#Ejemplo
calificaciones_103 = {"Paul": 7,"Dario":8,"Ana":9,"Citlalitl":8,"Ernesto":6,
                      "Manuel":9,"Cinthia":7,"Carolina":8,"Estefania":7,"Dhaniel":5}
eliminar_clave(calificaciones_103)
#Este ultimo print lo utilizamos para verificar que el programa funciona
print(calificaciones_103)
    