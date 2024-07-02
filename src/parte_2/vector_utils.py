def rotate_vector_left(vec: tuple[int, int]) -> tuple[int, int]:
    return -vec[1], vec[0]


def rotate_vector_right(vec: tuple[int, int]) -> tuple[int, int]:
    return vec[1], -vec[0]
