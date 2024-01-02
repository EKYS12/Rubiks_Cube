import numpy as np # Used to make 3D array of blocks
from block import Block # Import the block class to populate the cube

class Cube:
    def __init__(self):
        # Colors for each face in the order front, left, right, down, back, up
        face_colors = ['white', 'green', 'blue', 'orange', 'yellow', 'red']
        
        # Initialize the 3x3x3 array of blocks
        self.blocks = np.empty((3, 3, 3), dtype=object)

        # Populate the array with Block objects
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # Simplified color_dict based on position, for a solved cube
                    color_dict = {
                        'f': face_colors[0] if i == 0 else None,
                        'l': face_colors[1] if j == 0 else None,
                        'r': face_colors[2] if j == 2 else None,
                        'd': face_colors[3] if k == 0 else None,
                        'b': face_colors[4] if i == 2 else None,
                        'u': face_colors[5] if k == 2 else None,
                    }
                    # Derive Face Count from number of colored sides
                    face_count = sum(color is not None for color in color_dict.values())
                    self.blocks[i, j, k] = Block(face_count, color_dict)

        self.state = 'solved'

    def _get_face_colors(self, face_key):
        '''
        Helper Method for both string print outs, and state checker. Gets the information of the colors by side of the cube.
        '''
        # Define the indices for each face
        face_indices = {
            'f': (0, slice(None), slice(None)),
            'b': (2, slice(None), slice(None)),
            'l': (slice(None), 0, slice(None)),
            'r': (slice(None), 2, slice(None)),
            'u': (slice(None), slice(None), 2),
            'd': (slice(None), slice(None), 0),
        }

        indices = face_indices[face_key]
        colors = [[None]*3 for _ in range(3)]  # Initialize a 3x3 matrix of None

        for i in range(3):
            for j in range(3):
                block = self.blocks[indices[0], indices[1], indices[2]][i, j]
                colors[i][j] = block.color_dict[face_key]

        return colors

    def __str__(self):
        '''
        This method is to set up the ability to print out a human readable state of the cube.
        '''
        sides = 'flrubd'  # Front, Left, Right, Up, Back, Down
        cube_str = ''
        for side in sides:
            cube_str += side.upper() + '\n'  # Print the name of the side
            face_colors = self._get_face_colors(side)
            for row in face_colors:
                cube_str += ''.join(color[0] if color else ' ' for color in row) + '\n'
            cube_str += '\n'
        return cube_str

    def check_state(self):
        '''
        Used to check the current state of the cube on whether it is solved or not.
        '''
        sides = 'flrubd'  # Front, Left, Right, Up, Back, Down
        for side in sides:
            face_colors = self._get_face_colors(side)
            first_color = face_colors[0][0]
            if not all(color == first_color for row in face_colors for color in row if color):
                self.state = 'unsolved'
                return self.state # Found a face with inconsistent color
        self.state = 'solved'
        return self.state # All faces are consistent


    '''
    Rotation Logic

    Everthing Below is related to the rotational movements of the cube-segments.
    '''
    def _get_layer(self, segment):
        '''
        Helper method designed to retrieve the layer of a cube.
        '''
        segments = ['front', 'left', 'right', 'up', 'back', 'down', 'c-horizontal', 'c-vertical', 'c-slicing']
        if segment not in segments:
            print(f'Invalid segment. Valid options are {segments}')
            return None
        
        layer = None

        if segment == 'front':
            # Front layer: All blocks where the first index (i) is 0
            layer = self.blocks[0, :, :]
        if segment == 'back':
            # Back layer: All blocks where the first index (i) is 2
            layer = self.blocks[2, :, :]
        if segment == 'left':
            # Left layer: All blocks where the second index (j) is 0
            layer = self.blocks[:, 0, :]
        if segment == 'right':
            # Right layer: All blocks where the second index (j) is 2
            layer = self.blocks[:, 2, :]
        if segment == 'up':
            # Up layer: All blocks where the third index (k) is 2
            layer = self.blocks[:, :, 0]
        if segment == 'down':
            # Down layer: All blocks where the third index (k) is 0
            layer = self.blocks[:, :, 2]
        if segment == 'c-horizontal':
            # Center Horizontal layer: All blocks where the third index (k) is 1
            layer = self.blocks[:, :, 1]
        if segment == 'c-vertical':
            # Center Vertical layer: All blocks where the third index (j) is 1
            layer = self.blocks[:, 1, :]
        if segment == 'c-slicing':
            # Center Slicing layer: All blocks where the third index (i) is 1
            layer = self.blocks[1, :, :]

        return layer

    def _rotate_clockwise(self, segment, layer):
        # Implement clockwise rotation for the specified layer
        if segment == 'front':
            layer = np.rot90(layer, k=3)
        
        if segment == 'left':
            layer = np.rot90(layer.T, k=1).T

        if segment == 'right':
            layer = np.rot90(layer.T, k=3).T

        if segment == 'up':
            layer = np.rot90(layer, k=1)

        if segment == 'down':
            layer = np.rot90(layer, k=3)

        if segment == 'back':
            layer = np.rot90(layer, k=1)
        
        ####
        # The rotations on these are placeholder and need to be corrected
        ####
        if segment == 'c-horizontal':
            layer = np.rot90(layer, k=1)

        if segment == 'c-vertical':
            layer = np.rot90(layer, k=1)

        if segment == 'c-slicing':
            layer = np.rot90(layer, k=1)

        return


    def _rotate_counter_clockwise(self, layer):
        # Implement counter-clockwise rotation for the specified layer
        if segment == 'front':
            layer = np.rot90(layer, k=1)
        
        if segment == 'left':
            layer = np.rot90(layer.T, k=3).T

        if segment == 'right':
            layer = np.rot90(layer.T, k=1).T

        if segment == 'up':
            layer = np.rot90(layer, k=3)

        if segment == 'down':
            layer = np.rot90(layer, k=1)

        if segment == 'back':
            layer = np.rot90(layer, k=3)

        return

    def rotate(self, segment, rotation):
        layer = None

        layer = self._get_layer(segment=segment)
        if layer is None:
            print('Error: No valid layer selected for rotation. Check Args.')
            return

        if rotation == "clockwise":
            self._rotate_clockwise(segment=segment, layer=layer)
        if rotation == "counter-clockwise":
            self._rotate_counter_clockwise(segment=segment, layer=layer)

        return

