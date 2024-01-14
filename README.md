# Rubik's Cube Project

This is a personal project with the intention of making a digital rubik's cube. Using just base python 3.10 along with the addition of the powerful library `NumPy`, a functioning rubik's cube can be made in your vary own terminal.

## Cube
Using NumPy we can create a 3D Array that is a representation of a Rubik's Cube. Each element of the 3x3x3 array contain a Block object, where the orientation of the block and it's colors are shown in dictionary for sides and colors. The cube gets printed out as seperate 3x3 matrices of each of it's sides layed out in 2D.

## Cube Rotation Functions
The cube object also contains methods for rotating it's different segments. These methods will both rotate the segment of the cube selected in the direction chosen, but will also update the blocks within the segment with their new orientations as they move around the cube.

## Cube Randomizer
The cube when first initialized is created in a solved state. Using the scramble function we can randomize the layout of the cube and begin solving it.
