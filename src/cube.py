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

        # Making views of the different layers of the Cube
        # Front layer: All blocks where the first index (i) is 0
        self.front = self.blocks[0, :, :]
        # Back layer: All blocks where the first index (i) is 2
        self.back = self.blocks[2, :, :]
        # Left layer: All blocks where the second index (j) is 0
        self.left = self.blocks[:, :, 0]
        # Right layer: All blocks where the second index (j) is 2
        self.right = self.blocks[:, :, 2]
        # Up layer: All blocks where the third index (k) is 2
        self.up = self.blocks[:, 0, :]
        # Down layer: All blocks where the third index (k) is 0
        self.down = self.blocks[:, 2, :]
        # Center Horizontal layer: All blocks where the third index (k) is 1
        self.c_horizontal = self.blocks[:, 1, :]
        # Center Vertical layer: All blocks where the third index (j) is 1
        self.c_vertical = self.blocks[:, :, 1]
        # Center Slicing layer: All blocks where the third index (i) is 1
        self.c_slicing = self.blocks[1, :, :]


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
        segment_map = {
            'front': self.front,
            'back': self.back,
            'left': self.left,
            'right': self.right,
            'up': self.up,
            'down': self.down,
            'c_horizontal': self.c_horizontal,
            'c_vertical': self.c_vertical,
            'c_slicing': self.c_slicing
        }

        # Validate segment
        if segment not in segment_map:
            raise ValueError(f'Invalid segment. Valid options are {list(segment_map.keys())}')

        # Return the corresponding layer
        layer = segment_map[segment]
        return layer

    def rotate(self, segment, clockwise=True):
        '''
        Function used to rotate the different layers of the cube.
        '''
        
        # Get Layer to be rotated
        layer = self._get_layer(segment=segment)
        
        # Create a copy of the layer to work on, incase the layer needs to be transposed
        layer_r = layer.copy()

        TRANSPOSE = False

        # LAYERS WERE POSSIBLY INCORRECT HAVE TO RECHECK WHAT GOES WHERE

        # Set Values for Rotation depending on clockwise or counter clockwise 
        if segment in ['front', 'right', 'down', 'c_slicing']:
            if clockwise:
                ROTATION = 3
            else:
                ROTATION = 1
        
        if segment in ['left', 'up', 'back']:
            if clockwise:
                ROTATION = 1
            else:
                ROTATION = 3

        # Set tranpose flag for left and right
        if segment in ['left', 'right']:
            layer_r = layer_r.T
            TRANSPOSE = True
       
        ####
        # The ROTATIONs on these are placeholder and need to be corrected
        ####
        '''
        if segment == 'c_horizontal':
            ROTATION = 1

        if segment == 'c_vertical':
            ROTATION = 1
            TRANSPOSE = False

        '''

        layer = np.rot90(layer_r, k=ROTATION)

        if TRANSPOSE:
            layer = layer.T

        del layer_r

        return

