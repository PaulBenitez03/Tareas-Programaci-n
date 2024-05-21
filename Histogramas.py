import turtle
import random

# Función para generar números aleatorios en un rango dado
def generar_numeros_aleatorios(n, rango):
    return [random.randint(*rango) for _ in range(n)]

# Función para calcular la frecuencia de cada número
def calcular_frecuencia(numeros):
    frecuencia = {}
    for num in numeros:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    return frecuencia

# Función para dibujar el histograma
def dibujar_histograma(frecuencias):
    ventana = turtle.Screen()
    ventana.setup(width=800, height=600)
    ventana.title("Histograma")

    tortuga = turtle.Turtle()
    tortuga.speed(0)

    # Definir tamaño máximo del histograma
    max_frecuencia = max(frecuencias.values())
    max_altura = 400
    ancho_barra = 20

    # Dibujar cada barra del histograma
    for numero, frecuencia in frecuencias.items():
        altura = (frecuencia / max_frecuencia) * max_altura
        tortuga.penup()
        tortuga.goto(numero * 30 - 300, -200)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.left(90)
        tortuga.forward(altura)
        tortuga.write(str(frecuencia), align="center")
        tortuga.right(90)
        tortuga.forward(ancho_barra)
        tortuga.right(90)
        tortuga.forward(altura)
        tortuga.left(90)
        tortuga.end_fill()

    tortuga.hideturtle()
    ventana.mainloop()

# Definir rango y cantidad de números aleatorios a generar
rango = (1, 100)  # Por ejemplo, del 1 al 10
cantidad_numeros = 100

# Generar números aleatorios y calcular frecuencia
numeros_aleatorios = generar_numeros_aleatorios(cantidad_numeros, rango)
frecuencias = calcular_frecuencia(numeros_aleatorios)

# Dibujar histograma
dibujar_histograma(frecuencias)

rango1 = (1,1000)
cantidad_numeros1 = 1000

numeros_aleatorios2 = generar_numeros_aleatorios(cantidad_numeros1,rango1)
frecuencias1 = calcular_frecuencia(numeros_aleatorios2)
dibujar_histograma(frecuencias1)