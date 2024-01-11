from cube import Cube

new_cube = Cube()

print(new_cube)

print(f"The rubik's cube is: {new_cube.check_state()}")

new_cube.rotate(segment='front')

print(new_cube)

print(f"The rubik's cube is: {new_cube.check_state()}")
