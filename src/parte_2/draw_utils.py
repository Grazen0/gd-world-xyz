import colors
import matrix_utils


def draw_sprite(sprite: list[list[int]], pos_i: int, pos_j: int, target: list[list[int]]):
    for i in range(len(sprite)):
        target_i = pos_i + i

        if target_i < 0:
            continue

        if target_i >= len(target):
            break

        for j in range(len(sprite[i])):
            target_j = pos_j + j

            if target_j < 0:
                continue

            if target_j >= len(target[i]):
                break

            if sprite[i][j] != colors.NONE:
                target[target_i][target_j] = sprite[i][j]


def mask_sprite(sprite: list[list[int]], mask_color: int) -> list[list[int]]:
    result = matrix_utils.copy_matrix(sprite)

    for i in range(0, len(sprite)):
        for j in range(0, len(sprite[i])):
            if sprite[i][j] != colors.NONE:
                result[i][j] = mask_color

    return result


def draw_square_contour(i: int, j: int, size: int, color: int, target: list[list[int]]):
    for k in range(0, size):
        target[i + k][j] = color
        target[i + k][j + size - 1] = color
        target[i][j + k] = color
        target[i + size - 1][j + k] = color
