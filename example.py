__author__ = 'Travis Moy'

import random
import rpas


# Map generation parameters
prob_is_obstructed = .1
map_size = 20

# False values are obstructed; True are unobstructed.
map = [[(lambda: prob_is_obstructed < random.uniform(0.0, 1.0))() for _ in range(map_size)] for _ in range(map_size)]


# Normally this would be some class' function, accessing that class' data.
def is_unobstructed(x, y):
    try:
        return map[x][y]
    except IndexError:
        return False

center_x = map_size / 2
center_y = map_size / 2
radius = 10


def print_row(row, cells):
    print_str = ''
    for col in range(map_size):
        if col == center_x and row == center_y:
            print_str += '@'
        elif (col, row) in cells:
            if is_unobstructed(col, row):
                print_str += '.'
            else:
                print_str += 'X'
        else:
            print_str += ' '
    print print_str


def print_map_vision(cells):
    for row in range(map_size):
        print_row(row, cells)

fov = rpas.FOVCalc()

# FOV settings parameters; most restrictive
fov.NOT_VISIBLE_BLOCKS_VISION = True
fov.RESTRICTIVENESS = 2
fov.VISIBLE_ON_EQUAL = False

cells = fov.calc_visible_cells_from(center_x, center_y, radius, is_unobstructed)
print "Most restrictive settings:"
print_map_vision(cells)

# FOV settings parameters; least restrictive
fov.NOT_VISIBLE_BLOCKS_VISION = False
fov.RESTRICTIVENESS = 0
fov.VISIBLE_ON_EQUAL = True

cells = fov.calc_visible_cells_from(center_x, center_y, radius, is_unobstructed)
print "Least restrictive settings:"
print_map_vision(cells)