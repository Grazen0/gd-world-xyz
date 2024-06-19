from colorama import Back
import matrix_utils
import draw_utils
import sprites
import colors


WORLD_ROWS = 50
WORLD_COLUMNS = 120

FLOOR_HEIGHT = 6

PLAYER_SIZE = 16
PLAYER_I = WORLD_ROWS - FLOOR_HEIGHT - PLAYER_SIZE
PLAYER_J = 1


def create_game():
    return {
        'world': create_world(),
        'player_pos': [0, 0],
    }


def init_game(game: dict):
    draw_world(game['world'])
    game['player_pos'] = [WORLD_ROWS - FLOOR_HEIGHT - 16, 1]


def create_world() -> list[list[int]]:
    return matrix_utils.create_matrix(WORLD_ROWS, WORLD_COLUMNS, colors.BG)


def draw_world(world: list[list[int]]):
    # Piso
    for i in range(WORLD_ROWS - FLOOR_HEIGHT, WORLD_ROWS):
        world[i] = [colors.LIGHTWHITE] * WORLD_COLUMNS

    # Poste
    lamp = sprites.lamp_sprite()
    draw_utils.draw_sprite(lamp,  WORLD_ROWS -
                           FLOOR_HEIGHT - len(lamp), 24, world)

    # Triángulo
    spike = sprites.spike_sprite()
    draw_utils.draw_sprite(spike, WORLD_ROWS -
                           FLOOR_HEIGHT - len(spike), 33, world)


def draw_player(world: list[list[int]]):
    player = sprites.player_sprite()
    draw_utils.draw_sprite(player, WORLD_ROWS -
                           FLOOR_HEIGHT - len(player), 1, world)


def move_player(game: dict, direction: str):
    if direction == 'right':
        game['player_pos'][1] += 16
    elif direction == 'up_begin':
        game['player_pos'][0] -= 17
        game['player_pos'][1] += 16
    elif direction == 'up_end':
        game['player_pos'][0] += 17
        game['player_pos'][1] += 16


def print_game(game: dict):
    world_print = matrix_utils.copy_matrix(game['world'])
    player_pos = game['player_pos']

    draw_utils.draw_sprite(sprites.player_sprite(),
                           player_pos[0], player_pos[1], world_print)

    for row in world_print:
        last_color = -1

        for i in row:
            if i != last_color:
                last_color = i
                print(colors.CODES[i], end='')

            print('  ', end='')

        print(Back.RESET)
