# Importaciones
from random import randrange
from turtle import *
from freegames import vector

# Inicialización de variables
ball = vector(-200, -200)  # Posición inicial del proyectil
speed = vector(0, 0)  # Velocidad inicial del proyectil
targets = []  

# Función para responder al clic en la pantalla
def tap(x, y):
    """Responde al clic en la pantalla."""
    if not inside(ball): 
        # Si el proyectil no está dentro de la pantalla
        
        ball.x = -199  
        ball.y = -199
        speed.x = (x + 200) / 17  
        speed.y = (y + 200) / 17  

# Función para verificar si un punto está dentro de la pantalla
def inside(xy):
    """Devuelve True si xy está dentro de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Función para dibujar el proyectil y los balones
def draw():
    """Dibuja el proyectil y los objetivos."""
    clear()

    for target in targets:  
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):  
        goto(ball.x, ball.y)
        dot(6, 'red')  

    update()

# Función para mover el proyectil y los objetivos
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # cambia su posicion si sale de la pantalla
    if ball.x < -200:
        ball.x = 200 

    draw()

    #cambia la velocidad del proyectil
    ontimer(move, 20)  

# Configuración inicial de la pantalla y ejecución del juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()


