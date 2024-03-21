from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable para contar los toques

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def all_tiles_revealed():
    """Check if all tiles have been revealed."""
    return all(not hide[count] for count in range(64))

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count
    tap_count += 1  # Incrementa el contador de toques
    print(f'Número de toques: {tap_count}')  # Muestra el número de toques en la consola

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Ajusta la posición para centrar el dígito en el cuadro
        goto(x + 25, y + 8)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    if all_tiles_revealed():  # Verifica si todos los cuadros han sido destapados
        print("¡Todos los cuadros han sido destapados!")

    up()
    goto(-200, 200)  # Posición para mostrar el número de toques
    write(f'Número de toques: {tap_count}', font=('Arial', 16, 'normal'))  # Muestra el número de toques en la ventana

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(500, 440, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
