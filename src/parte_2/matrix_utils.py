def create_matrix(rows: int, columns: int, fill: int) -> list[list[int]]:
    return [[fill] * columns for _ in range(rows)]


def copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row.copy() for row in matrix]


def rotate_matrix_right(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    columns = len(matrix[0])
    return [[matrix[rows - 1 - j][i] for j in range(0, rows)] for i in range(0, columns)]


def flip_matrix_vertical(matrix: list[list[int]]) -> list[list[int]]:
    return matrix[::-1]
