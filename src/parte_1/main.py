import geometry_dashworld

print('Welcome to the world of Geometry Dash World XYZ')

game = geometry_dashworld.create_game()

initted = False
done = False

while not done:
    commands = input().split()

    redraw = True

    for command in commands:
        if not initted:
            if command == 'init':
                geometry_dashworld.init_game(game)
                initted = True
            else:
                print('Run "init" before playing')
                redraw = False
        else:
            if command == 'init':
                print('Game is already initialized')
                redraw = False
            elif command == 'right':
                geometry_dashworld.move_player(game, 'right')
            elif command == 'up':
                geometry_dashworld.move_player(game, 'up_begin')

                geometry_dashworld.print_game(game)
                print()

                geometry_dashworld.move_player(game, 'up_end')
            elif command == 'quit':
                print('Bye bye!')
                redraw = False
                done = True
            else:
                print('Comando incorrecto')
                redraw = False

        if redraw:
            geometry_dashworld.print_game(game)
