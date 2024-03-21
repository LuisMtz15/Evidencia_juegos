from random import choice, randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores disponibles para la serpiente y la comida
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar color aleatorio a la serpiente
snake_color = choice(colors)
# Asignar color aleatorio a la comida
food_color = choice(colors)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Move food randomly one step at a time."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    direction = choice(directions)
    new_food = food + direction

    if inside(new_food):
        food.move(direction)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    move_food()  # Move food randomly in each step

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        
        
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move_food()  # Initialize food movement
move()
done()
