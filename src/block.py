'''
This is the class for the blocks that build up the Rubiks Cube

Face count determines if the piece is a center face piece, an edge piece, or a corner piece.

Color dictionary determines the initial placement of the colors on the block.

Example Color Dictionary:
    color_dict = {f: white, l: green, r: null, d: null, b: red, u: null}

Example Movement Log:
    movement_log = [(f, b), (b, d), (l, f)]
'''

class Block:
    def __init__(self, face_count, color_dict):
        self.face_count = face_count
        self.color_dict = color_dict

    def __str__(self):
        # Dynamically create a string representation, filtering out None values
        color_str = {face: color for face, color in self.color_dict.items() if color is not None}
        return str(color_str)

    def movement(self, movement_log):
        for movement in movement_log:
            face1, face2 = movement
            self.color_dict[face1], self.color_dict[face2] = self.color_dict[face1], self.color_dict[face2]
        return self.color_dict
