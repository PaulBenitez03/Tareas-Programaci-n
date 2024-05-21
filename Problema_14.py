def claveXvalor (diccionario):
    dic1 = {}
    key = input("Introduzca una calificacion: ")
    for clave, valor in diccionario.items():
        if valor == key:
            dic1[clave] = valor
    return dic1

sd = {'l':2,'s':2,'f':1}
sfs = claveXvalor(sd)
print(sfs)

        