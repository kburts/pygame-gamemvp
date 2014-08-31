__author__ = 'Kevin'

from PIL import Image

def get_tile_image_string(image, location, cols, tile_size):
    rows = location / cols
    position = location % cols - 1

    x,y = rows, position
    left = x * tile_size
    top = y * tile_size
    right = (x + 1) * tile_size
    bottom =(x + 1) * tile_size

    out_image = Image.open(image).crop((left, top, right, bottom))
    out_image = out_image.tostring("raw", "RGB")

    return out_image