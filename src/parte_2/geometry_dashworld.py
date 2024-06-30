from colorama import Back
import extra_math
import matrix_utils
import draw_utils
import vector_utils
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
        'player_direction': vector_utils.DIRECTION_VECTORS['right'],
        'camera_pos': [0, 0],
        'spikes': []
    }


def init_game(game: dict):
    draw_world(game)
    game['player_pos'] = [FLOOR_TOP - PLAYER_SIZE, 1]


def create_world() -> list[list[int]]:
    return matrix_utils.create_matrix(WORLD_ROWS, WORLD_COLUMNS, colors.BG)


def insert_spike(sprite: list[list[int]], pos_i: int, pos_j: int, game: dict):
    draw_utils.draw_sprite(sprite, pos_i, pos_j, game['world'])
    game['spikes'].append({
        'pos': (pos_i, pos_j),
        'sprite': sprite,
    })


def draw_world(game: dict):
    world = game['world']

    # Piso
    for i in range(0, FLOOR_HEIGHT):
        for j in range(0, FLOOR_WIDTH):
            world[FLOOR_TOP + i][j] = colors.FLOOR

    # Postes
    lamp_up = sprites.lamp
    lamp_right = matrix_utils.rotate_matrix_right(sprites.lamp)
    lamp_down = matrix_utils.flip_matrix_vertical(sprites.lamp)

    draw_utils.draw_sprite(lamp_up,
                           FLOOR_TOP - len(sprites.lamp), 24, world)
    draw_utils.draw_sprite(lamp_right, FLOOR_TOP + 8, FLOOR_WIDTH, world)
    draw_utils.draw_sprite(lamp_down, FLOOR_TOP + FLOOR_HEIGHT, 50, world)
    draw_utils.draw_sprite(lamp_down, FLOOR_TOP + FLOOR_HEIGHT, 3, world)

    # Espinas
    spike_up = sprites.spike
    spike_right = matrix_utils.rotate_matrix_right(sprites.spike)
    spike_down = matrix_utils.flip_matrix_vertical(sprites.spike)

    insert_spike(spike_up, FLOOR_TOP - len(spike_up), 33, game)
    insert_spike(spike_up, FLOOR_TOP - len(spike_up), 97, game)
    insert_spike(spike_right, FLOOR_TOP + FLOOR_HEIGHT -
                 len(spike_right), FLOOR_WIDTH, game)
    insert_spike(spike_down, FLOOR_TOP + FLOOR_HEIGHT, 81, game)
    insert_spike(spike_down, FLOOR_TOP + FLOOR_HEIGHT, 17, game)


def draw_player(world: list[list[int]]):
    draw_utils.draw_sprite(sprites.player, WORLD_ROWS -
                           FLOOR_HEIGHT - len(sprites.player), 1, world)


# Retorna None si el jugador sigue vivo
# Caso contrario, retorna el spike al que chocó
def move_player(game: dict, direction: str) -> dict | None:
    relative_right = game['player_direction']
    relative_up = vector_utils.rotate_vector_left(relative_right)
    new_i, new_j = game['player_pos']

    if direction == 'right':
        new_i += 16 * relative_right[0]
        new_j += 16 * relative_right[1]
    elif direction == 'up_begin':
        new_i += 17 * relative_up[0]
        new_j += 17 * relative_up[1]
        new_i += 16 * relative_right[0]
        new_j += 16 * relative_right[1]
    elif direction == 'up_end':
        new_i -= 17 * relative_up[0]
        new_j -= 17 * relative_up[1]
        new_i += 16 * relative_right[0]
        new_j += 16 * relative_right[1]

    # Comprobar colisiones
    player_left = new_i
    player_right = new_i + PLAYER_SIZE
    player_top = new_j
    player_bottom = new_j + PLAYER_SIZE

    for spike in game['spikes']:
        spike_left = spike['pos'][0]
        spike_right = spike['pos'][0] + len(spike['sprite'])
        spike_top = spike['pos'][1]
        spike_bottom = spike['pos'][1] + len(spike['sprite'][0])

        if player_left < spike_right and player_right > spike_left \
                and player_top < spike_bottom and player_bottom > spike_top:
            # Colisión detectada
            return spike

    game['player_pos'] = [new_i, new_j]

    if direction != 'up_begin':
        update_player_orientation(game)

    update_camera_position(game)
    return None


def update_player_orientation(game: dict):
    floor_direction = vector_utils.rotate_vector_right(
        game['player_direction']
    )

    check_i = game['player_pos'][0] + PLAYER_SIZE * floor_direction[0]
    check_j = game['player_pos'][1] + PLAYER_SIZE * floor_direction[1]

    if game['world'][check_i][check_j] != colors.FLOOR:
        # Rotar dirección del jugador
        game['player_direction'] = floor_direction


def update_camera_position(game: dict):
    player_i, player_j = game['player_pos']

    # Adaptar al jugador
    game['camera_pos'][0] = extra_math.clamp(
        game['camera_pos'][0],
        player_i + PLAYER_SIZE - CAMERA_ROWS + CAMERA_MARGIN,
        player_i - CAMERA_MARGIN
    )
    game['camera_pos'][1] = extra_math.clamp(
        game['camera_pos'][1],
        player_j + PLAYER_SIZE - CAMERA_COLUMNS + CAMERA_MARGIN,
        player_j - CAMERA_MARGIN
    )

    # Evitar que salga del mundo
    game['camera_pos'][0] = extra_math.clamp(
        game['camera_pos'][0],
        0,
        WORLD_ROWS - CAMERA_ROWS
    )
    game['camera_pos'][1] = extra_math.clamp(
        game['camera_pos'][1],
        0,
        WORLD_COLUMNS - CAMERA_COLUMNS
    )


def has_game_won(game: dict) -> bool:
    return game['player_pos'][1] <= 1 - PLAYER_SIZE


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
