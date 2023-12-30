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

    def _get_layer(self, side):
        '''
        Helper function designed to retrieve the layer of a cube surrounding one of the side faces.
        '''
        sides = ['front', 'left', 'right', 'up', 'back', 'down']
        if side not in sides:
            print(f'Invalid side. Valid options are {sides}')
            return None
        
        layer = np.empty((3, 3), dtype=object)  # Placeholder for the 3x3 layer

        if side == 'f':
            # Front layer: All blocks where the first index (i) is 0
            layer = self.blocks[0, :, :]
        elif side == 'b':
            # Back layer: All blocks where the first index (i) is 2
            layer = self.blocks[2, :, :]
        elif side == 'l':
            # Left layer: All blocks where the second index (j) is 0
            layer = self.blocks[:, 0, :]
        elif side == 'r':
            # Right layer: All blocks where the second index (j) is 2
            layer = self.blocks[:, 2, :]
        elif side == 'u':
            # Up layer: All blocks where the third index (k) is 2
            layer = self.blocks[:, :, 2]
        elif side == 'd':
            # Down layer: All blocks where the third index (k) is 0
            layer = self.blocks[:, :, 0]

        return layer

    def _center_horizontal_layer(self):
        # Helper function designed to retrieve the center layer of the cube on the X axis, or k.
        layer = self.blocks[:, :, 1]
        return layer

    def _center_vertical_layer(self):
        # Helper function designed to retrieve the center layer of the cube on the Y axis, or j.
        layer = self.blocks[:, 1, :]
        return layer

    def _center_slicing_layer(self):
        # Helper function designed to retrieve the center layer of the cube on the Z axis, or i.
        layer = self.blocks[1, :, :]
        return layer

    def _rotate_clockwise(self, side, layer):
        # Implement clockwise rotation for the specified layer
        if side == 'front':
            cube[0, :, :] = np.rot90(cube[0, :, :], k=3)
        
        elif side == 'left':
            cube[2, :, :] = np.rot90(cube[2, :, :].T, k=1).T

        if side == 'right':
            cube[0, :, :] = np.rot90(cube[0, :, :].T, k=3).T

        elif side == 'up':
            cube[2, :, :] = np.rot90(cube[2, :, :], k=1)

        if side == 'down':
            cube[0, :, :] = np.rot90(cube[0, :, :], k=3)

        elif side == 'back':
            cube[2, :, :] = np.rot90(cube[2, :, :], k=1)

        return

    def _rotate_counter_clockwise(self, layer):
        # Implement counter-clockwise rotation for the specified layer
        if side == 'front':
            cube[0, :, :] = np.rot90(cube[0, :, :], k=1)
        
        elif side == 'left':
            cube[2, :, :] = np.rot90(cube[2, :, :].T, k=3).T

        if side == 'right':
            cube[0, :, :] = np.rot90(cube[0, :, :].T, k=1).T

        elif side == 'up':
            cube[2, :, :] = np.rot90(cube[2, :, :], k=3)

        if side == 'down':
            cube[0, :, :] = np.rot90(cube[0, :, :], k=1)

        elif side == 'back':
            cube[2, :, :] = np.rot90(cube[2, :, :], k=3)

        return

    def rotate(self, side, rotation, center_horizontal=False, center_vertical=False, center_slicing=False):
        layer = None
        if side=='center':
            if center_horizontal:
                layer = self._center_horizontal_layer()
            if center_vertical:
                layer = self._center_vertical_layer()
            if center_slicing:
                layer = self._center_slicing_layer()
            else:
                print ('Error: Core of cube selected as center of rotation but layer unspecified. Check Args')
                return
        else:
            layer = self._get_layer(side=side)
            if layer is None:
                print('Error: No valid layer selected for rotation. Check Args.')
                return

        if rotation == "clockwise":
            self._rotate_clockwise(side=side, layer=layer)
        elif rotation == "counter-clockwise":
            self._rotate_counter_clockwise(side=side, layer=layer)

        return

