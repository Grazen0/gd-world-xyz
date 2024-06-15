from colorama import Back

type World = list[list[int]]

ROWS = 50
COLUMNS = 120

COLOR_BG = 0
COLOR_BLACK = 1
COLOR_GREEN = 2
COLOR_LIGHTBLUE = 3
COLOR_LIGHTWHITE = 4
COLOR_YELLOW = 5

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


def create_world() -> World:
    return [[COLOR_BG] * COLUMNS for _ in range(0, ROWS)]


def draw_world(world: World):
    # Piso
    for i in range(ROWS - FLOOR_HEIGHT, ROWS):
        world[i] = [COLOR_LIGHTWHITE] * COLUMNS

    # Poste
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
            world[LAMP_TOP_BASE - k][LAMP_J + l] = COLOR_YELLOW
            world[LAMP_TOP_BASE - k][LAMP_J - l] = COLOR_YELLOW

            world[LAMP_TOP_BASE - 2 * LAMP_TOP_EXT + 1 + k][LAMP_J + l] \
                = COLOR_YELLOW
            world[LAMP_TOP_BASE - 2 * LAMP_TOP_EXT + 1 + k][LAMP_J - l] \
                = COLOR_YELLOW
    # Pincho 
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
                        world[POS_I_INIC - 2*fila - i][POS_J_INIC+columna] \
                            = COLOR_YELLOW
                    else:
                        if (columna > fila and columna < 8) or (fila + columna < 14 and columna >= 8):
                            world[POS_I_INIC - 2*fila - i][POS_J_INIC+columna] \
                                = COLOR_BLACK   
                            
    # Jugador
    draw_player(world)


def draw_square_contour(i: int, j: int, size: int, color: int, world: World):
    for k in range(0, size):
        world[i + k][j] = color
        world[i + k][j + size - 1] = color
        world[i][j + k] = color
        world[i + size - 1][j + k] = color


def draw_player(world: World):
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


def print_world(world: World):

    for r, row in enumerate(world):
        print(f'{r + 1:2} ', end='')
        last_color = -1

        for i in row:
            if i != last_color:
                last_color = i
                print(COLOR_CODES[i], end='')

            print('  ', end='')

        print(Back.RESET)
