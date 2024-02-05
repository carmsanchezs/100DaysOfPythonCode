blocks = int(input("Enter the number of the blocks: "))

blocks_layer = 0
blocks_left = blocks
height = 0

while blocks_left > blocks_layer:
    blocks_layer += 1
    blocks_left -= blocks_layer

height = blocks_layer
print("The height of the pyramid:", height)
