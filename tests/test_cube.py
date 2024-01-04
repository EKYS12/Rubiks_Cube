import unittest
import numpy as np

# Function to initialize a 3x3x3 array with numbers 1-27
def init_cube():
    return np.arange(1, 28).reshape(3, 3, 3)

def rotate(layer, rotation):
    # Function to rotate a 3x3 layer clockwise
    return np.rot90(layer, k=rotation)

class TestCubeMethods(unittest.TestCase):

    def setUp(self):
        self.cube = init_cube()
# Run the tests
if __name__ == '__main__':
    unittest.main()
