from colorama import Back
import matrix_utils
import draw_utils
import sprites
import colors


WORLD_ROWS = 112
WORLD_COLUMNS = 156

CAMERA_ROWS = 56
CAMERA_COLUMNS = 78
CAMERA_MARGIN = 13

FLOOR_TOP = 44
FLOOR_HEIGHT = 32
FLOOR_WIDTH = 113

PLAYER_SIZE = 16
PLAYER_I = WORLD_ROWS - FLOOR_HEIGHT - PLAYER_SIZE
PLAYER_J = 1


def create_game():
    return {
        'world': create_world(),
        'player_pos': [0, 0],
        'player_direction': 'right',
        'camera_pos': [0, 0],
    }


def init_game(game: dict):
    draw_world(game['world'])
    game['player_pos'] = [FLOOR_TOP - PLAYER_SIZE, 1]


def create_world() -> list[list[int]]:
    return matrix_utils.create_matrix(WORLD_ROWS, WORLD_COLUMNS, colors.BG)


def draw_world(world: list[list[int]]):
    # Piso
    for i in range(0, FLOOR_HEIGHT):
        for j in range(0, FLOOR_WIDTH):
            world[FLOOR_TOP + i][j] = colors.FLOOR

    # Poste
    draw_utils.draw_sprite(sprites.lamp, FLOOR_TOP -
                           len(sprites.lamp), 24, world)

    # Triángulo
    draw_utils.draw_sprite(sprites.spike, FLOOR_TOP -
                           len(sprites.spike), 33, world)
    draw_utils.draw_sprite(sprites.spike, FLOOR_TOP -
                           len(sprites.spike), 97, world)


def draw_player(world: list[list[int]]):
    draw_utils.draw_sprite(sprites.player, WORLD_ROWS -
                           FLOOR_HEIGHT - len(sprites.player), 1, world)


DIRECTION_VECTORS = {
    'down': (1, 0),
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

ROTATIONS = {
    'right': 'down',
    'down': 'left',
    'left': 'up',
    'up': 'right',
}


def rotate_vector_left(vec: tuple[int, int]) -> tuple[int, int]:
    return -vec[1], vec[0]


def rotate_vector_right(vec: tuple[int, int]) -> tuple[int, int]:
    return vec[1], -vec[0]


def move_player(game: dict, direction: str):
    relative_right = DIRECTION_VECTORS[game['player_direction']]
    relative_up = rotate_vector_left(relative_right)

    if direction == 'right':
        game['player_pos'][0] += 16 * relative_right[0]
        game['player_pos'][1] += 16 * relative_right[1]

        update_player_orientation(game)
    elif direction == 'up_begin':
        game['player_pos'][0] += 17 * relative_up[0]
        game['player_pos'][1] += 17 * relative_up[1]
        game['player_pos'][0] += 16 * relative_right[0]
        game['player_pos'][1] += 16 * relative_right[1]
    elif direction == 'up_end':
        game['player_pos'][0] -= 17 * relative_up[0]
        game['player_pos'][1] -= 17 * relative_up[1]
        game['player_pos'][0] += 16 * relative_right[0]
        game['player_pos'][1] += 16 * relative_right[1]

        update_player_orientation(game)

    update_camera_position(game)


def update_player_orientation(game: dict):
    floor_direction = rotate_vector_right(
        DIRECTION_VECTORS[game['player_direction']])

    check_i = game['player_pos'][0] + PLAYER_SIZE * floor_direction[0]
    check_j = game['player_pos'][1] + PLAYER_SIZE * floor_direction[1]

    if game['world'][check_i][check_j] != colors.FLOOR:
        game['player_direction'] = ROTATIONS[game['player_direction']]
        print('New direction:', game['player_direction'])


def update_camera_position(game: dict):
    player_i, player_j = game['player_pos']

    if player_j + PLAYER_SIZE > game['camera_pos'][1] + CAMERA_COLUMNS - CAMERA_MARGIN:
        game['camera_pos'][1] = player_j + \
            PLAYER_SIZE + CAMERA_MARGIN - CAMERA_COLUMNS

    if player_j < game['camera_pos'][1] + CAMERA_MARGIN:
        game['camera_pos'][1] = player_j - CAMERA_MARGIN

    if player_i + PLAYER_SIZE > game['camera_pos'][0] + CAMERA_ROWS - CAMERA_MARGIN:
        game['camera_pos'][0] = player_i + \
            PLAYER_SIZE + CAMERA_MARGIN - CAMERA_ROWS

    if player_i < game['camera_pos'][0] + CAMERA_MARGIN:
        game['camera_pos'][0] = player_i - CAMERA_MARGIN

    if game['camera_pos'][0] < 0:
        game['camera_pos'][0] = 0

    if game['camera_pos'][0] > WORLD_ROWS - CAMERA_ROWS:
        game['camera_pos'][0] = WORLD_ROWS - CAMERA_ROWS

    if game['camera_pos'][1] < 0:
        game['camera_pos'][1] = 0

    if game['camera_pos'][1] > WORLD_COLUMNS - CAMERA_COLUMNS:
        game['camera_pos'][1] = WORLD_COLUMNS - CAMERA_COLUMNS


def print_game(game: dict):
    world_print = matrix_utils.copy_matrix(game['world'])
    player_i, player_j = game['player_pos']
    camera_i, camera_j = game['camera_pos']

    draw_utils.draw_sprite(sprites.player, player_i, player_j, world_print)

    for i in range(0, CAMERA_ROWS):
        last_color = -1

        for j in range(0, CAMERA_COLUMNS):
            pixel = world_print[camera_i + i][camera_j + j]

            if pixel != last_color:
                last_color = pixel
                print(colors.CODES[pixel], end='')

            print('  ', end='')

        print(Back.RESET)
