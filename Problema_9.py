def lista_valores (diccionario):
    lista = [valor for dic in diccionario for valor in dic.values()]
    return lista
calificaciones = {'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88} 
l = lista_valores(calificaciones)
print(l)