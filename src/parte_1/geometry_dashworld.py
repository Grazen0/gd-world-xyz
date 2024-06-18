from colorama import Back
import utils
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
    return utils.create_matrix(WORLD_ROWS, WORLD_COLUMNS, colors.BG)


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


def draw_world(world: list[list[int]]):
    # Piso
    for i in range(WORLD_ROWS - FLOOR_HEIGHT, WORLD_ROWS):
        world[i] = [colors.LIGHTWHITE] * WORLD_COLUMNS

    # Poste
    lamp = sprites.lamp_sprite()
    draw_sprite(lamp,  WORLD_ROWS - FLOOR_HEIGHT - len(lamp), 24, world)

    # Triángulo
    spike = sprites.spike_sprite()
    draw_sprite(spike, WORLD_ROWS - FLOOR_HEIGHT - len(spike), 33, world)


def draw_player(world: list[list[int]]):
    player = sprites.player_sprite()
    draw_sprite(player, WORLD_ROWS - FLOOR_HEIGHT - len(player), 1, world)


def move_player(game: dict, direction: str):
    if direction == 'right':
        game['player_pos'][1] += 16
    elif direction == 'up_begin':
        game['player_pos'][0] -= 17
        game['player_pos'][1] += 16
    elif direction == 'up_end':
        game['player_pos'][1] += 16
        game['player_pos'][0] += 17


def print_game(game: dict):
    world_copy = utils.copy_matrix(game['world'])
    player_pos = game['player_pos']

    draw_sprite(sprites.player_sprite(),
                player_pos[0], player_pos[1], world_copy)

    for row in world_copy:
        last_color = -1

        for i in row:
            if i != last_color:
                last_color = i
                print(colors.CODES[i], end='')

            print('  ', end='')

        print(Back.RESET)
