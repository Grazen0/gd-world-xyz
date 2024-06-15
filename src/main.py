import geometry_dashworld

print('Welcome to the world of Geometry Dash World XYZ')

command = input()
while command != 'init':
    command = input()

world = geometry_dashworld.create_world()

geometry_dashworld.draw_world(world)
geometry_dashworld.draw_player(world)

geometry_dashworld.print_world(world)
