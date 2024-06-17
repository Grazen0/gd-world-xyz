from colorama import Back

# type World = list[list[int]]

ROWS = 50
COLUMNS = 120

COLOR_NONE = 0
COLOR_BG = 1
COLOR_BLACK = 2
COLOR_GREEN = 3
COLOR_LIGHTBLUE = 4
COLOR_LIGHTWHITE = 5
COLOR_YELLOW = 6

COLOR_CODES = {
    COLOR_BG: Back.WHITE,
    COLOR_BLACK: Back.BLACK,
    COLOR_GREEN: Back.GREEN,
    COLOR_LIGHTBLUE: Back.LIGHTBLUE_EX,
    COLOR_LIGHTWHITE: Back.LIGHTWHITE_EX,
    COLOR_YELLOW: Back.YELLOW
}

FLOOR_HEIGHT = 6

PLAYER_SIZE = 16
PLAYER_I = ROWS - FLOOR_HEIGHT - PLAYER_SIZE
PLAYER_J = 1


def create_world() -> list[list[int]]:
    return [[COLOR_BG] * COLUMNS for _ in range(0, ROWS)]


def player_sprite(size: int):
    pass


def spike_sprite() -> list[list[int]]:

    STAIRS = 8
    SPIK_INF_BASE = 15
    # Matriz inicial
    spike_matrix = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
    
    for fila in range(0, STAIRS):
        for columna in range(0, SPIK_INF_BASE):
                for i in range(0, 2):
                    # Bordes: Amarillo = 6
                    if fila == columna or (fila + columna == 14):
                        spike_matrix[SPIK_INF_BASE - 2*fila - i][columna] = 6
                    # Interior: Negro = 2
                    elif (columna > fila and columna < 8) or (fila + columna < 14 and columna >= 8):
                        spike_matrix[SPIK_INF_BASE - 2*fila - i][columna] = 2
                    # Afueras: Incoloro = 0
                    else: 
                        spike_matrix[SPIK_INF_BASE - 2*fila - i][columna] = 0
    
    return spike_matrix


def poste_sprite():
    # Todo es de color negro: indice = 2
    # Solo para el chupetin será amarillo: indice = 6
    # Igual que en el pincho, lo incoloro será 0

    # Indice en fila de la base inferior:
    BASE_INF = 15
    # Indice en fila de base inferior del chupetin
    BASE_INF_CHU = 6
    # Indice en fila de la base superior del chupetin
    BASE_SUP_CHU = 0
    # Indice en columna del centro del chupetin:
    CENT_CHU = 3
    # No recuerdo qué significa, pero sirve para solo iterar hasta la mitad de lo que será el chupetín :v
    LAMP_TOP_EXT = 3
    poste_matrix = [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ]
    # Laterales de la base: Negro = 2 (Realmente no hace falta usar un for para esto pero igual lo hago :v)
    for k in range(7):
        if k == 2 or k == 4:
            poste_matrix[BASE_INF][k] = 2
    
    #Columna central: 
    for k in range(BASE_INF_CHU, BASE_INF+1):
        poste_matrix[k][CENT_CHU] = 2

    # Chupetin inferior:
    for k in range(0, LAMP_TOP_EXT):
            for l in range(0, k + 2):
                # Mitad de abajo
                poste_matrix[BASE_INF_CHU - k - 1 ][3 + l] = 6
                poste_matrix[BASE_INF_CHU - k - 1][3 - l] = 6

                # Mitad de arriba
                poste_matrix[BASE_INF_CHU -2*LAMP_TOP_EXT + k][3 + l] = 6
                poste_matrix[BASE_INF_CHU -2*LAMP_TOP_EXT + k][3 - l] = 6

    return poste_matrix


def draw_world(world: list[list[int]]):
    # Piso
    for i in range(ROWS - FLOOR_HEIGHT, ROWS):
        world[i] = [COLOR_LIGHTWHITE] * COLUMNS


    # Poste:

    LAMP_TOP_EXT = 3
    LAMP_I = ROWS - FLOOR_HEIGHT - 1
    LAMP_J = 24
    LAMP_TOP_BASE = LAMP_I - 10

    # Laterales de la base inferior del poste
    world[LAMP_I][LAMP_J - 1] = COLOR_BLACK
    world[LAMP_I][LAMP_J + 1] = COLOR_BLACK
    
    # Columna central del poste
    for k in range(LAMP_TOP_BASE + 1, LAMP_I + 1):
        world[k][LAMP_J] = COLOR_BLACK

    # Chupetin :v
    for k in range(0, LAMP_TOP_EXT):
        for l in range(0, k + 2):
            # Mitad de abajo
            world[LAMP_TOP_BASE - k][LAMP_J + l] = COLOR_YELLOW
            world[LAMP_TOP_BASE - k][LAMP_J - l] = COLOR_YELLOW

            # Mitad de arriba
            world[LAMP_TOP_BASE - 2 * LAMP_TOP_EXT + 1 + k][LAMP_J + l] = COLOR_YELLOW
            world[LAMP_TOP_BASE - 2 * LAMP_TOP_EXT + 1 + k][LAMP_J - l] = COLOR_YELLOW


    # Pincho:

    # Filas "únicas" = 8
    STAIRS = 8
    # Logitud inicial de la base del pincho
    SPIK_INF_BASE = 15
    # Posición en Y donde inicia
    POS_I_INIC = ROWS - FLOOR_HEIGHT - 1
    # Posiciión en X donde inicia
    POS_J_INIC = 30

    # For para iterar sobre la cantidad de escaleras/escalones
    for fila in range(0, STAIRS):
        # For para iterar sobre las columnas
        for columna in range(0, SPIK_INF_BASE):
                # Este for es para que se imprima otra fila :v
                for i in range(0, 2):
                    if fila == columna or (fila + columna == 14):
                        world[POS_I_INIC - 2*fila - i][POS_J_INIC+columna] = COLOR_YELLOW
                    elif (columna > fila and columna < 8) or (fila + columna < 14 and columna >= 8):
                        world[POS_I_INIC - 2*fila - i][POS_J_INIC+columna] = COLOR_BLACK   


def draw_square_contour(i: int, j: int, size: int, color: int, world: list[list[int]]):
    for k in range(0, size):
        world[i + k][j] = color
        world[i + k][j + size - 1] = color
        world[i][j + k] = color
        world[i + size - 1][j + k] = color


def draw_player(world: list[list[int]]):
    draw_square_contour(PLAYER_I, PLAYER_J, PLAYER_SIZE, COLOR_BLACK, world)

    draw_square_contour(PLAYER_I + 1, PLAYER_J + 1,
                        PLAYER_SIZE - 2, COLOR_GREEN, world)
    draw_square_contour(PLAYER_I + 2, PLAYER_J + 2,
                        PLAYER_SIZE - 4, COLOR_GREEN, world)

    draw_square_contour(PLAYER_I + 3, PLAYER_J + 3,
                        PLAYER_SIZE - 6, COLOR_BLACK, world)

    draw_square_contour(PLAYER_I + 4, PLAYER_J + 4,
                        PLAYER_SIZE - 8, COLOR_LIGHTBLUE, world)
    draw_square_contour(PLAYER_I + 5, PLAYER_J + 5,
                        PLAYER_SIZE - 10, COLOR_LIGHTBLUE, world)

    draw_square_contour(PLAYER_I + 6, PLAYER_J + 6,
                        PLAYER_SIZE - 12, COLOR_BLACK, world)

    draw_square_contour(PLAYER_I + 7, PLAYER_J + 7,
                        PLAYER_SIZE - 14, COLOR_GREEN, world)


def move_player():
    pass


def print_world(world: list[list[int]]):
    for row in world:
        last_color = -1

        for i in row:
            if i != last_color:
                last_color = i
                print(COLOR_CODES[i], end='')

            print('  ', end='')

        print(Back.RESET)
