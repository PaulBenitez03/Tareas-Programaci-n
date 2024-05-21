def prf_diccionarios (diccionario):
    if not isinstance(diccionario,dict):
        return 0
    profundidades = [prf_diccionarios(valores) for valores in diccionario.values()]
    return 1 +(max(profundidades) if profundidades else 0)

l ={'a':{'g':{'f':{'m':1}}}}
l2 = {'mama':40,'pepe':{'mama de pepe':51}}
l3 = {'w':0}
prueba1 = prf_diccionarios(l)
prueba2 = prf_diccionarios(l2)
prueba3= prf_diccionarios(l3)
print(f"La profundidad es: {prueba1}")
print(f"La profundidad es: {prueba2}")
print(f"La profundidad es: {prueba3}")
