'''
This is the class for the blocks that build up the Rubiks Cube

Face count determines if the piece is a center face piece, an edge piece, or a corner piece.

Color dictionary determines the initial placement of the colors on the block.
'''

class Block:
    def __init__(self, face_count, color_dict):
        self.face_count = face_count
        self.color_dict = color_dict

    def __str__(self):
        # Dynamically create a string representation, filtering out None values
        color_str = {face: color for face, color in self.color_dict.items() if color is not None}
        return str(color_str)

    def _log_maker(self, segment, clockwise=True):
        '''
        Function that creates the movement log as a list of tuples to determine how sides will shift during a rotation.

        segment: Side of the cube that is being rotated.
        clockwise: Default=True. Direction of rotation being done.
        '''
        if (segment in ['front', 'c_slicing'] and clockwise) or (segment in ['back'] and not clockwise):
            movement_log = [
                ('front', 'front'),
                ('back', 'back'),
                ('up', 'left'),
                ('left', 'down'),
                ('down', 'right'),
                ('right', 'up')
            ]
        if (segment in ['front', 'c_slicing'] and not clockwise) or (segment in ['back'] and clockwise):
            movement_log = [
                ('front', 'front'),
                ('back', 'back'),
                ('up', 'right'),
                ('right', 'down'),
                ('down', 'left'),
                ('left', 'up')
            ]
        if (segment in ['right', 'c_vertical'] and clockwise) or (segment in ['left'] and not clockwise):
            movement_log = [
                ('right', 'right'),
                ('left', 'left'),
                ('up', 'front'),
                ('front', 'down'),
                ('down', 'back'),
                ('back', 'up')
            ]
        if (segment in ['right', 'c_vertical'] and not clockwise) or (segment in ['left'] and clockwise):
            movement_log = [
                ('right', 'right'),
                ('left', 'left'),
                ('up', 'back'),
                ('back', 'down'),
                ('down', 'front'),
                ('front', 'up')
            ]
        if (segment in ['down'] and clockwise) or (segment in ['up', 'c_horizontal'] and not clockwise):
            movement_log = [
                ('down', 'down'),
                ('up', 'up'),
                ('front', 'left'),
                ('left', 'back'),
                ('back', 'right'),
                ('right', 'front')
            ]
        if (segment in ['down'] and not clockwise) or (segment in ['up', 'c_horizontal'] and clockwise):
            movement_log = [
                ('down', 'down'),
                ('up', 'up'),
                ('front', 'right'),
                ('right', 'back'),
                ('back', 'left'),
                ('left', 'front')
            ]

        return movement_log

    def movement(self, segment, clockwise=True):
        '''
        Function that reworks the block's color dictionary as a movement along the cube takes place.

        segment: Side on the cube that is being rotated.

        clockwise: Default=True. Direction of rotation.
        '''
        movement_log = self._log_maker(segment=segment, clockwise=clockwise)
        color_copy = self.color_dict.copy()
        for movement in movement_log:
            face1, face2 = movement
            self.color_dict[face1] = color_copy[face2]

        new_face_count = sum(color is not None for color in self.color_dict.values())
        if new_face_count != self.face_count:
            raise ValueError(f'Face Count Error. Initial Face Count: {self.face_count}. New Face Count: {new_face_count}. \n {self.color_dict}')
