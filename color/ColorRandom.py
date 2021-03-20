# imports
from PIL import Image
from random import randint

# map width and height
width = 16
height = 16

# initialize image
image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
pix = image.load()

# for each pixel
for x in range(0, width):
    for y in range(0, height):
        # set pixel to random color
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255), 255)
        pix[x, y] = random_color

# save to file
image.save('./ColorRandom.png')
