import keyboard
import mouse
import time
import random

# Constantes
DELAY_MIN = 0.08
DELAY_MAX = 0.09
RIGHT_CLICK = "right_click"
RELEASE_RIGHT_CLICK = "release_right_click"
SHIFT = "shift"

# Variables globales
boton_a_detectar = "q"

# Lista de jutsus
jutsus = [
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("y", 0.0), (SHIFT, 0.0), ("space", 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 15, 0], # RAIKYUU
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("h", 0.0), (SHIFT, 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 7, 0], # MIZURAPPA
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("c", 0.0), (SHIFT, 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 10, 0], # HANACHI
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("c", 0.0), (SHIFT, 0.0), ("c", 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 10, 0], # GOUKAKYUU
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("c", 0.0), (SHIFT, 0.0), ("n", 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 15, 0], # KARYUUENDAN
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("c", 0.0), (SHIFT, 0.0), ("space", 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 15, 0], # HOUSENKA
    [[(RIGHT_CLICK, 0.05), (SHIFT, 0.0), ("space", 0.0), (SHIFT, 0.0), ("c", 0.0), (RELEASE_RIGHT_CLICK, 0.05)], 15, 0] # SHINKUHA
]

def ordenar_jutsus(jutsu):
    """Ordena los jutsus, dejando el primer jutsu en la primera posición y los demás al azar."""
    return 0 if jutsu == jutsus[0] else random.random()

def check_timer(jutsu):
    """Revisa si el temporizador del jutsu ha terminado."""
    remaining_time = jutsu[1] - (int(time.time()) - jutsu[2])
    return max(remaining_time, 0)

def ejecutar_sucesion(sucesion):
    """Ejecuta una sucesión de teclas y clics de ratón."""
    for tecla, delay in sucesion:
        if not keyboard.is_pressed(boton_a_detectar):
            if tecla != RELEASE_RIGHT_CLICK:
                mouse.release(mouse.RIGHT)
            return False

        delay = delay or random.uniform(DELAY_MIN, DELAY_MAX)

        if tecla == RIGHT_CLICK:
            mouse.press(mouse.RIGHT)
            time.sleep(delay)
        elif tecla == RELEASE_RIGHT_CLICK:
            mouse.release(mouse.RIGHT)
            time.sleep(delay)
        else:
            keyboard.press(tecla)
            time.sleep(delay)
            keyboard.release(tecla)

    return True

def macro(jutsus):
    """Ejecuta los jutsus en secuencia si el temporizador ha expirado."""
    for jutsu in jutsus:
        if check_timer(jutsu) > 0:
            continue
        if ejecutar_sucesion(jutsu[0]):
            jutsu[2] = int(time.time())

def on_key_event(event):
    """Evento que se dispara al presionar una tecla."""
    if event.name == boton_a_detectar:
        global jutsus
        jutsus = sorted(jutsus, key=ordenar_jutsus)
        macro(jutsus)

# Asigna el evento al presionar la tecla
keyboard.on_press_key(boton_a_detectar, on_key_event)

# Espera hasta que se presione la tecla 'esc' para salir
keyboard.wait('}')
