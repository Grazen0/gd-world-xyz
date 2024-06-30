import geometry_dashworld

print('Welcome to the world of Geometry Dash World XYZ')

game = geometry_dashworld.create_game()

initted = False
done = False

while not done:
    commands = input().split()

    redraw = True

    for command in commands:
        if command == 'quit' or command == 'q':
            print('Bye bye!')
            done = True
            break

        if not initted:
            if command == 'init' or command == 'i':
                geometry_dashworld.init_game(game)
                initted = True
            else:
                print('Run "init" before playing')
                redraw = False
        else:
            if command == 'init' or command == 'i':
                print('Game is already initialized')
                redraw = False
            elif command == 'right' or command == 'r':
                geometry_dashworld.move_player(game, 'right')
            elif command == 'up' or command == 'u':
                geometry_dashworld.move_player(game, 'up_begin')

                geometry_dashworld.print_game(game)
                print()

                geometry_dashworld.move_player(game, 'up_end')
            else:
                print('Invalid command')
                redraw = False

        if redraw:
            geometry_dashworld.print_game(game)

        if geometry_dashworld.has_game_won(game):
            print('You win!')
            done = True
            break
