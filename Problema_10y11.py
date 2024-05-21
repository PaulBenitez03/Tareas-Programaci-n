def valores_asignatura (lista,asignatura):
    l1 = [diccionario[asignatura] for diccionario in lista if asignatura in diccionario] 
    return l1

prueba = [{'Matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 

listaXmateria = valores_asignatura(prueba, 'ciencia')
listaXmateria2 = valores_asignatura(prueba,'Matematicas')
print(f"Las calificaciones de ciencia son {listaXmateria}")
print(f"Las calificaciones de matematicas son {listaXmateria2}")