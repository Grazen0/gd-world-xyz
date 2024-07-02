import geometry_dashworld
import draw_utils
import colors

print('Welcome to the world of Geometry Dash World XYZ')

game = geometry_dashworld.create_game()

initted = False
done = False

while not done:
    commands = input().split()

    redraw = True

    for command in commands:
        if command == 'quit':
            print('Bye bye!')
            redraw = False
            done = True
        elif not initted:
            if command == 'init':
                geometry_dashworld.init_game(game)
                initted = True
            else:
                print('Run "init" before playing')
                redraw = False
        else:
            collision = None

            if command == 'init':
                print('Game is already initialized')
                redraw = False
            elif command == 'right':
                collision = geometry_dashworld.move_player(game, 'right')
            elif command == 'up':
                geometry_dashworld.move_player(game, 'up_begin')

                geometry_dashworld.print_game(game)
                print()

                collision = geometry_dashworld.move_player(game, 'up_end')
            else:
                print('Invalid command')
                redraw = False

            if collision != None:
                # Chocó con una espina. Perder juego
                # Redibujar al obstáculo chocado, pero todo en amarillo
                draw_utils.draw_sprite(
                    draw_utils.mask_sprite(collision['sprite'], colors.YELLOW),
                    collision['pos'][0],
                    collision['pos'][1],
                    game['world']
                )

                geometry_dashworld.print_game(game)
                print('Game over')
                redraw = False
                done = True

        if redraw:
            geometry_dashworld.print_game(game)

        if geometry_dashworld.has_game_won(game):
            print('You win!')
            done = True

        if done:
            break
