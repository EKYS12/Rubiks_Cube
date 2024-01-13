import numpy as np # Used to make 3D array of blocks
from block import Block # Import the block class to populate the cube

class Cube:
    def __init__(self):
        # Colors for each face
        self.face_colors = ['white', 'green', 'blue', 'orange', 'yellow', 'red']
        
        # Initialize the 3x3x3 array of blocks
        self.blocks = np.empty((3, 3, 3), dtype=object)

        # Populate the array with Block objects
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # Simplified color_dict based on position, for a solved cube
                    color_dict = {
                        'front': self.face_colors[0] if i == 0 else None,
                        'left': self.face_colors[1] if k == 0 else None,
                        'right': self.face_colors[2] if k == 2 else None,
                        'down': self.face_colors[3] if j == 2 else None,
                        'back': self.face_colors[4] if i == 2 else None,
                        'up': self.face_colors[5] if j == 0 else None,
                    }
                    # Derive Face Count from number of colored sides
                    face_count = sum(color is not None for color in color_dict.values())
                    self.blocks[i, j, k] = Block(face_count, color_dict)

        self.state = 'solved'

        # Making views of the different layers of the Cube
        # Front layer: All blocks where the first index (i) is 0
        self.front = self.blocks[0, :, :]
        # Back layer: All blocks where the first index (i) is 2
        self.back = self.blocks[2, :, :]
        # Left layer: All blocks where the third index (k) is 0
        self.left = self.blocks[:, :, 0]
        # Right layer: All blocks where the third index (k) is 2
        self.right = self.blocks[:, :, 2]
        # Up layer: All blocks where the second index (j) is 0
        self.up = self.blocks[:, 0, :]
        # Down layer: All blocks where the second index (j) is 2
        self.down = self.blocks[:, 2, :]
        # Center Horizontal layer: All blocks where the second index (j) is 1
        self.c_horizontal = self.blocks[:, 1, :]
        # Center Vertical layer: All blocks where the third index (k) is 1
        self.c_vertical = self.blocks[:, :, 1]
        # Center Slicing layer: All blocks where the third index (i) is 1
        self.c_slicing = self.blocks[1, :, :]

        # Dictionary of segment keys and segment index values
        self.segment_indices = {
            'front': (0, slice(None), slice(None)),
            'back': (2, slice(None), slice(None)),
            'left': (slice(None), slice(None), 0),
            'right': (slice(None), slice(None), 2),
            'up': (slice(None), 0, slice(None)),
            'down': (slice(None), 2, slice(None)),
            'c_horizontal': (slice(None), 1, slice(None)),
            'c_vertical': (1, slice(None), slice(None)),
            'c_slicing': (slice(None), slice(None), 1),
        }

    def _get_face_colors(self, face_key):
        '''
        Helper Method to retrieve colors of a specific face of the cube.

        face_key: side that colors are being pulled from
        '''
        indices = self.segment_indices.get(face_key)
        if not indices:
            raise ValueError(f"Invalid face key: {face_key}")

        # Initialize a 3x3 matrix of None
        colors = np.empty((3, 3), dtype=object)
        colors.fill(None)

        # Accessing the color of each block in the face and storing it
        for i in range(3):
            for j in range(3):
                block = self.blocks[indices[0], indices[1], indices[2]][i, j]
                colors[i][j] = block.color_dict[face_key]

        return colors

    def __str__(self):
        '''
        Return a human-readable string representation of the cube's state.
        '''
        sides = ['front', 'left', 'right', 'up', 'back', 'down']  # Use full names as keys
        cube_str = ''
        for side in sides:
            cube_str += f"{side.capitalize()} Side:\n"
            face_colors = self._get_face_colors(side)

            # If side is left or up, reverse the order of rows to match 2D layout representation of cube.
            if side in sides[1] or side in sides[3]:
                face_colors = np.flip(face_colors, axis=0)

            # if side is the back, flip the matrix so that 
            if side in sides[4]:
                face_colors = np.flip(face_colors, axis=1)

            # If side is left or right, Transpose so that the order is correct upon visual representation.
            if side in sides[1:3]:
                face_colors = face_colors.T

            for row in face_colors:
                cube_str += ''.join(color[0] if color else ' ' for color in row) + '\n'
            cube_str += '\n'
        return cube_str

    def check_state(self):
        '''
        Checks the current state of the cube to determine if it's solved.
        '''
        sides = ['front', 'left', 'right', 'up', 'back', 'down']  # Use full names as keys
        for side in sides:
            face_colors = self._get_face_colors(side)
            # Assuming the first color in each face is representative of that face's color
            first_color = face_colors[0][0]
            if not all(color == first_color for row in face_colors for color in row if color):
                self.state = 'unsolved'
                return 'Unsolved'  # Found a face with inconsistent color
        self.state = 'solved'
        return 'Solved'  # All faces are consistent

    def rotate(self, segment, clockwise=True):
        '''
        Function used to rotate the different layers of the cube.

        segment: Layer to be rotated
        clockwise: Default value is True. Boolean that determines clockwise or counterclockwise rotation.
        '''

        indices = self.segment_indices.get(segment)
        if not indices:
            raise ValueError(f"Invalid segment: {segment}")

        layer = self.blocks[indices].copy()

        TRANSPOSE = False

        # Set Values for Rotation depending on clockwise or counter clockwise 
        if segment in ['front', 'right', 'down', 'c_slicing', 'c_vertical']:
            if clockwise:
                ROTATION = 3
            else:
                ROTATION = 1
        
        if segment in ['left', 'up', 'back', 'c_horizontal']:
            if clockwise:
                ROTATION = 1
            else:
                ROTATION = 3

        # Set tranpose flag for vertical layers
        if segment in ['left', 'right', 'c_vertical']:
            layer = layer.T
            TRANSPOSE = True

        layer_r = np.rot90(layer, k=ROTATION).copy()

        if TRANSPOSE:
            layer_r = layer_r.T

        for i in range(3):
            for j in range(3):
                layer_r[i, j].movement(segment, clockwise)

        self.blocks[indices] = layer_r

        return

