import unittest
import numpy as np

# Function to initialize a 3x3x3 array with numbers 1-27
def init_cube():
    return np.arange(1, 28).reshape(3, 3, 3)

# Revised Function to get a layer from the cube
def _get_layer(cube, side):
    if side == 'front':
        return cube[0, :, :]
    # Invert the back layer horizontally
    elif side == 'back':
        return np.flip(cube[2, :, :], axis=1)
    # Invert the left layer horizontally
    elif side == 'left':
        return np.flip(cube[:, :, 0], axis=1)  # Correcting the axis for left
    elif side == 'right':
        return cube[:, :, 2]  # Correcting the axis for right
    # Invert the up layer vertically
    elif side == 'up':
        return np.flip(cube[:, 0, :], axis=0)  # Correcting the axis for up
    elif side == 'down':
        return cube[:, 2, :]  # Correcting the axis for down
    else:
        raise ValueError("Invalid side specified. Valid options are 'front', 'back', 'left', 'right', 'up', 'down'.")

def rotate_clockwise(layer):
    # Function to rotate a 3x3 layer clockwise
    return np.rot90(layer, k=3)

class TestCubeMethods(unittest.TestCase):

    def setUp(self):
        self.cube = init_cube()

    def test_layer_extraction(self):
        sides = ['front', 'back', 'left', 'right', 'up', 'down']
        expected_first_values = {
            'front': 1,
            'back': 21,
            'left': 7,
            'right': 3,
            'up': 19,
            'down': 7
        }
        for side in sides:
            with self.subTest(side=side):
                layer = _get_layer(self.cube, side)
                self.assertEqual(layer[0, 0], expected_first_values[side],
                                 f"{side.capitalize()} layer first value does not match.")

    def test_rotate_clockwise(self):
        # Test the clockwise rotation of a layer
        original_layer = np.array([
            ['00', '01', '02'],
            ['10', '11', '12'],
            ['20', '21', '22']
        ])
        expected_rotated_layer = np.array([
            ['20', '10', '00'],
            ['21', '11', '01'],
            ['22', '12', '02']
        ])
        rotated_layer = rotate_clockwise(original_layer)
        # Check if the rotated layer matches the expected result
        np.testing.assert_array_equal(rotated_layer, expected_rotated_layer)

# Run the tests
if __name__ == '__main__':
    unittest.main()
