# imports
from PIL import Image
from random import randint

# number of colors
count = 8

# initialize image
palette = Image.new('RGBA', (count, 1), (0, 0, 0, 0))
pix = palette.load()

# get random rgb values
mx = 255 - ((count - 1) * 10)
r = randint(0, mx)
g = randint(0, mx)
b = randint(0, mx)

# generate palette
for x in range(0, count):
    v = x * 10
    pix[x, 0] = (r + v, g + v, b + v, 255)

# save palette
palette.save('./ColorPalette.png')
