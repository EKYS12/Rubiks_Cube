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
                return print(self.state) # Found a face with inconsistent color
        self.state = 'solved'
        return print(self.state) # All faces are consistent

    def _face_layer(self, face):
        '''
        Helper function designed to retrieve the layer of a cube surrounding one of the side faces.
        '''
        pass

    def _middle_horizontal_layer(self):
        '''
        Helper function designed to retrieve the middle layer of the cube on the X axis.
        '''
        pass

    def _middle_vertical_layer(self):
        '''
        Helper function designed to retrieve the middle layer of the cube on the Y axis.
        '''
        pass

    def _middle_slicing_layer(self):
        '''
        Helper function designed to retrieve the middle layer of the cube on the Z axis.
        '''
       pass

    def _rotate_clockwise(self, layer):
        # Implement clockwise rotation around the specified face block
        # Update cube state
        pass

    def _rotate_counter_clockwise(self, layer):
        # Implement counter-clockwise rotation around the specified face block
        # Update cube state
        pass

    def rotate(self, center, rotation):
        if center==cube_center_placeholder: 
            if middle_horizontal==True:
                layer = self._middle_horizontal_layer()
            if middle_vertical==True:
                layer = self._middle_vertical_layer()
            if middle_slicing==True:
                layer = self._middle_slicing_layer()
        else:
            layer = self._face_layer(face=center)

        if rotation == "clockwise":
            self._rotate_clockwise(layer=layer)
        elif rotation == "counter-clockwise":
            self._rotate_counter_clockwise(layer=layer)

        return

