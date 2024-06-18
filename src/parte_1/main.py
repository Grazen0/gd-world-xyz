import geometry_dashworld

print('Welcome to the world of Geometry Dash World XYZ')

game = geometry_dashworld.create_game()

# command = input()
# while command != 'init':
#     command = input()


initted = False

while True:
    commands = input().split()

    redraw = True

    for command in commands:
        if command == 'init':
            if not initted:
                initted = True
                geometry_dashworld.init_game(game)
            else:
                print('Game already initialized')
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
            exit()
        else:
            print('Comando incorrecto')
            redraw = False

    if redraw:
        geometry_dashworld.print_game(game)
