def create_matrix(rows: int, columns: int, fill: int) -> list[list[int]]:
    return [[fill] * columns for _ in range(rows)]


def copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [row.copy() for row in matrix]
