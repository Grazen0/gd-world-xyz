import colors


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


def draw_square_contour(i: int, j: int, size: int, color: int, world: list[list[int]]):
    for k in range(0, size):
        world[i + k][j] = color
        world[i + k][j + size - 1] = color
        world[i][j + k] = color
        world[i + size - 1][j + k] = color
