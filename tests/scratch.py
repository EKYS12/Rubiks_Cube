import numpy as np

cube = np.arange(1, 28).reshape(3, 3, 3)

layer = cube[:, :, 1].T

print("Cube")
print(cube)
print()
print("Layer")
print(layer)
print()
print("Layer Flipped")
print(np.flip(layer, axis=1))
print()
print("Layer rotated counter clockwise")
print(np.rot90(layer, k=1))
print()
print("Layer rotated clockwise")
print(np.rot90(layer, k=3))
print()
print("Layer flipped and rotated counter clockwise")
print(np.flip(np.rot90(np.flip(layer, axis=1), k=1), axis=1))
print()
print("Layer flipped and rotated clockwise")
print(np.flip(np.rot90(np.flip(layer, axis=1), k=3), axis=1))
print()
