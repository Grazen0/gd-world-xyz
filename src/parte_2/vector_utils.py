
DIRECTION_VECTORS = {
    'down': (1, 0),
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1),
}


def rotate_vector_left(vec: tuple[int, int]) -> tuple[int, int]:
    return -vec[1], vec[0]


def rotate_vector_right(vec: tuple[int, int]) -> tuple[int, int]:
    return vec[1], -vec[0]
