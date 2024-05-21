#Definimos directamente una funcion para crear el diccionario}
def crear_diccionario (clave,valor):
    if len(clave) == len(valor):
        diccionario = dict(zip(clave,valor))
        return diccionario
    else:
        print("No se puede crear la lista")
        print("Las listas deben tener el mismo tamaño")
#Se ponen dos ejemplos: el primero con listas del mismo tamaño y el segundo con listas de tamaño diferente

l1 = ["Mario","Ramiro","Erendira","Lindoro","Pancracio"]
l2 = [1,2,3,4,5]
l3 = [9,2]
d1 = crear_diccionario(l1,l2)
d2 = crear_diccionario(l1,l3)
print(d1)
print(d2)

