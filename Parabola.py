import turtle

# Función para dibujar ejes coordenados xy
def dibujar_ejes():
    # Crear ventana
    ventana = turtle.Screen()
    ventana.setup(width=600, height=600)
    ventana.title("Trayectoria Parabólica")

    # Crear tortuga para dibujar ejes
    ejes = turtle.Turtle()
    ejes.speed(0)  # Máxima velocidad

    # Dibujar eje x
    ejes.penup()
    ejes.goto(-300, 0)
    ejes.pendown()
    ejes.forward(600)
    ejes.stamp()
    ejes.write("X", align="center")
    ejes.penup()

    # Dibujar eje y
    ejes.goto(0, -300)
    ejes.setheading(90)
    ejes.pendown()
    ejes.forward(600)
    ejes.stamp()
    ejes.write("Y", align="center")

    ejes.hideturtle()

# Función para dibujar trayectoria parabólica
def dibujar_parabola():
    tortuga = turtle.Turtle()
    tortuga.speed(0)  # Máxima velocidad

    # Dibujar la parábola
    tortuga.penup()
    for x in range(-300, 301, 10):
        y = (x ** 2) / 100  # La ecuación de la parábola: y = x^2 / 100
        tortuga.goto(x, y)
        tortuga.pendown()

    tortuga.hideturtle()

# Función principal
def main():
    dibujar_ejes()
    dibujar_parabola()
    turtle.done()

if __name__ == "__main__":
    main()
