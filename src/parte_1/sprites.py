import matrix_utils
import colors
import draw_utils


def player_sprite() -> list[list[int]]:
    sprite = matrix_utils.create_matrix(16, 16, colors.NONE)

    draw_utils.draw_square_contour(0, 0, 16, colors.BLACK, sprite)
    draw_utils.draw_square_contour(1, 1, 14, colors.GREEN, sprite)
    draw_utils.draw_square_contour(2, 2, 12, colors.GREEN, sprite)
    draw_utils.draw_square_contour(3, 3, 10, colors.BLACK, sprite)
    draw_utils.draw_square_contour(4, 4, 8, colors.LIGHTBLUE, sprite)
    draw_utils.draw_square_contour(5, 5, 6, colors.LIGHTBLUE, sprite)
    draw_utils.draw_square_contour(6, 6, 4, colors.BLACK, sprite)
    draw_utils.draw_square_contour(7, 7, 2, colors.GREEN, sprite)

    return sprite


def spike_sprite() -> list[list[int]]:
    STAIRS = 8
    SPIK_INF_BASE = 15
    sprite = matrix_utils.create_matrix(16, 15, 0)

    for fila in range(0, STAIRS):
        for columna in range(0, SPIK_INF_BASE):
            for i in range(0, 2):
                if fila == columna or (fila + columna == 14):
                    sprite[SPIK_INF_BASE - 2 *
                           fila - i][columna] = colors.YELLOW
                elif (columna > fila and columna < 8) or (fila + columna < 14 and columna >= 8):
                    sprite[SPIK_INF_BASE - 2 *
                           fila - i][columna] = colors.BLACK

    return sprite


def lamp_sprite():
    # Todo es de color negro: indice = 2
    # Solo para el chupetin será amarillo: indice = 6
    # Igual que en el pincho, lo incoloro será 0

    # Indice en fila de la base inferior:
    BASE_INF = 15
    # Indice en fila de base inferior del chupetin
    BASE_INF_CHU = 6
    # Indice en columna del centro del chupetin:
    CENT_CHU = 3
    # No recuerdo qué significa, pero sirve para solo iterar hasta la mitad de lo que será el chupetín :v
    LAMP_TOP_EXT = 3

    sprite = matrix_utils.create_matrix(16, 7, colors.NONE)

    # Laterales de la base: Negro = 2 (Realmente no hace falta usar un for para esto pero igual lo hago :v)
    for k in range(7):
        if k == 2 or k == 4:
            sprite[BASE_INF][k] = colors.BLACK

    # Columna central:
    for k in range(BASE_INF_CHU, BASE_INF+1):
        sprite[k][CENT_CHU] = colors.BLACK

    # Chupetin
    for k in range(0, LAMP_TOP_EXT):
        for l in range(0, k + 2):
            # Mitad de abajo
            sprite[BASE_INF_CHU - k - 1][3 + l] = colors.YELLOW
            sprite[BASE_INF_CHU - k - 1][3 - l] = colors.YELLOW

            # Mitad de arriba
            sprite[BASE_INF_CHU - 2 *
                   LAMP_TOP_EXT + k][3 + l] = colors.YELLOW
            sprite[BASE_INF_CHU - 2 *
                   LAMP_TOP_EXT + k][3 - l] = colors.YELLOW

    return sprite
