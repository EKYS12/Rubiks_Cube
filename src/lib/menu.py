import sys
from lib.cube import Cube

def _cube_scramble(cube):
    '''
    Used to Call the cube scrambler method on the cube object.

    cube: cube that is instantiated.
    '''

    user_scramble_seed = int(input(f'\nInput Seed for scramble: '))
    user_scramble_rotations = int(input(f'\nInput number of rotations: '))

    print('\nPrint the list of moves in scramble?')
    print('\n1. Yes')
    print('\n2. No')

    valid_input = False

    while not valid_input:
        user_print_moves = int(input('\n'))

        if user_print_moves not in [1, 2]:
            print('\nInvalid Input, try again')
        else:
            valid_input = True

    if user_print_moves == 1:
        print_moves = True
    else:
        print_moves = False

    cube.scramble(seed=user_scramble_seed, rotations=user_scramble_rotations, print_moves=print_moves)
   
    return

def _rotation_menu(cube):
    '''
    Menu for the User to input a manual rotation.
    '''
    print('\nWhich side would you like to rotate?')
    print()
    print(cube.sides)
    print()

    valid_input = False
    
    while not valid_input:
        user_rotation_side = input('\n')

        if user_rotation_side not in cube.sides:
            print('\nInvalid Input, try again')
        else:
            valid_input = True

    print('\nFor a clockwise rotation type "True". For counter-clockwise rotation, type "False"')
    valid_input = False

    user_rotation_clockwise = bool(input('\n'))

    cube.rotate(segment=user_rotation_side, clockwise=user_rotation_clockwise)

    return cube_menu(cube)

def cube_menu(cube):
    '''
    Menu for when a cube is instantiated

    cube: cube that is instantiated
    '''
    print(cube)

    if cube.solved:
        solved_status = 'solved'
    else:
        solved_status = 'not solved'

    print(f"\nThe Rubik's Cube is {solved_status}")

    print('\nWhat would you like to do with the cube?')
    print('\n0. Scramble Cube')
    print('\n1. Perform Rotation')
    print('\n2. Go Back to Home Menu')

    valid_input = False

    while not valid_input:
        user_input_cube = int(input('\n'))

        if user_input_cube not in [0, 1, 2]:
            print('\nInvalid Input, try again')
        else:
            valid_input = True

    if user_input_cube == 0:
        _cube_scramble(cube)
        cube_menu(cube)

    if user_input_cube == 1:
        _rotation_menu(cube)

    if user_input_cube == 2:
        home()

def home():
    '''
    Home menu for the program
    '''

    rubiks_cube_3d_ascii = """
        +----+----+----+
       /    /    /    / |
      +----+----+----+  +
     /    /    /    /| /|
    +----+----+----+  + +
    |    |    |    |/| /|
    +----+----+----+  + +
    |    |    |    |/| / 
    +----+----+----+  +
    |    |    |    | /  
    +----+----+----+
    """

    print(rubiks_cube_3d_ascii)

    print("\nHello User, would you like to make a new rubik's cube?")
    print("\n1. New Cube")
    print("\n2. Exit")

    valid_input = False


    while not valid_input:
        user_input_home = int(input('\n'))

        if user_input_home not in [1, 2]:
            print('\nInvalid Input, try again')
        else:
            valid_input = True

    if user_input_home == 1:
        cube = Cube()
        return cube_menu(cube)

    if user_input_home == 2:
        sys.exit()

