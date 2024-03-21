# Importaciones 
from random import choice, randrange
from turtle import *
from freegames import square, vector

# Posiciones iniciales y dirección de la serpiente
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores disponibles para la serpiente y la comida
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar color aleatorio 
snake_color = choice(colors)
food_color = choice(colors)

def change(x, y):
    """Cambiar la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Mover la comida aleatoriamente un paso a la vez."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    direction = choice(directions)
    new_food = food + direction

    if inside(new_food):
        food.move(direction)


def move():
    """Mover la serpiente hacia adelante un segmento."""
    head = snake[-1].copy()
    head.move(aim)

    # Verificar colisiones
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Dibujar la cabeza de la serpiente en rojo
        update()
        return

    snake.append(head)  

    clear()  

    # Dibujar el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, 'black')

    move_food()  # Mover la comida aleatoriamente en cada paso
    
    # Si la serpiente alcanza la comida
    if head == food:  
        print('Snake:', len(snake))  
        food.x = randrange(-15, 15) * 10  
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  

    clear()  # Limpiar la pantalla

    # Dibujar la serpiente y la comida con colores aleatorios
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)  # Temporizador para el movimiento continuo

# Configuración inicial de la pantalla y controles
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')  
onkey(lambda: change(-10, 0), 'Left') 
onkey(lambda: change(0, 10), 'Up') 
onkey(lambda: change(0, -10), 'Down') 
move_food() 
move() 
done()
