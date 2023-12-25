# Rubik's Cube Project

## Cube Maker
Make a 3D Array that is a solved Rubik's Cube

Composed of 4 types of blocks
- Core (Unseen, cannot move)
- Face (Seen, cannot move)
- Edge (Seen, can move)
- Corner (Seen, can move)

## Cube Rotation Functions
Functions for each legal rotation/movement

Rotation can be clockwise or counter clockwise centering around a face block

Rotations are to target the movements of specific corner or edge blocks

The Functions arguements must be movement and face block. These will be determined by algorithm functions

## Cube Randomizer
Function that takes a solved cube and randomly picks a sequence of *200* movements to perform on the cube to randomize it.

## Cube Solver
Create Functions for different Cube solving Algorithms that use the movement functions to perform it's steps.

Attach a timer function and a movement counting function to each algorithm. Store the time and step count in a dataframe.

# Data Collection
Data frame that stores step count and time for each algorithm for each random cube variation. 
