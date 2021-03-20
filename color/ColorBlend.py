# imports
from PIL import Image
from random import randint

# blend interval
interval = 8

# initialize image
blend = Image.new('RGBA', (interval, 1), (0, 0, 0, 0))
pix = blend.load()

# get random colors
r_a = randint(0, 255)
g_a = randint(0, 255)
b_a = randint(0, 255)
color_a = (r_a, g_a, b_a)

r_b = randint(0, 255)
g_b = randint(0, 255)
b_b = randint(0, 255)
color_b = (r_b, g_b, b_b)

# generate blend
n = interval - 1
for x in range(0, interval):
    v = (n - x) / n
    r = int((r_a * v) + (r_b * (1 - v)))
    g = int((g_a * v) + (g_b * (1 - v)))
    b = int((b_a * v) + (b_b * (1 - v)))
    pix[x, 0] = (r, g, b)

# save blend
blend.save('./ColorBlend.png')
