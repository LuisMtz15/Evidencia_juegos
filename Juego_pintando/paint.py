from turtle import *
from freegames import vector

# Función para dibujar una línea recta entre dor puntos
def line(start, end):
    """Dibuja una línea desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado de distancia decidida por el usuario
def square(start, end):
    """Dibuja un cuadrado desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90) #Rota 90 grados cada que hace una linea

    end_fill()

# Función para dibujar un círculo 
def circle(start, end):
    """Dibuja un círculo desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    
    for count in range(360): #Cada vez gira 1 grado y lo hace 360 veces
        
        #Calcular su radio para que sea de ese tamaño
        forward(3.1416 * end.x / 360 - 3.1416 * start.x / 360) 
        left(1)
        
    end_fill()

# Función para dibujar un rectángulo 
def rectangle(start, end):
    """Dibuja un rectángulo desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        #Gira 90° cada que acaba con una linea y lo hace 4 veces
        forward(end.x - start.x)
        left(90) 
        forward(end.y - start.y)
        left(90)

    end_fill()

# Función para dibujar un triángulo 
def triangle(start, end):
    """Dibuja un triángulo desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        #Forma un trianguloo equilatero
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    """Almacena el punto de inicio o dibuja la forma."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Almacena el valor en el estado en la clave especificada."""
    state[key] = value

# Estado inicial con punto de inicio nulo y forma de línea
state = {'start': None, 'shape': line}

# Configuración inicial de la pantalla y configuración de controles
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
