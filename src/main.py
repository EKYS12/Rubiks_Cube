from lib.utils import home
from lib.cube import Cube

'''
Outline for new code:

Ask User to make a new code or exit.

New cube is made.

Ask to preform move, scramble, help, or back.

Preforming move asks user to input move and returns user to previous screen, but locks scrambles.

Preforming scramble will scramble the cube, save the seed, and return user to the previous screen.

Preforming help will give user information about rotations and scramble.

Preforming back will take them back to first screen.
'''

make_cube = home()

if make_cube:
    cube = Cube()


