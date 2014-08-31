__author__ = 'Kevin'

import sys
import pygame
import tmxlib
import TileImageDecoder
from PIL import Image


TILE_SIZE_PIXELS = 32
RESOURCES = 'resources//'

class TileSprite(pygame.sprite.Sprite):
    def __init__(self, image, location):
        super(TileSprite, self).__init__()
        left = location[0]
        top = location[1]
        right = location[0] + TILE_SIZE_PIXELS
        bottom = location[1] + TILE_SIZE_PIXELS

        image = Image.open(RESOURCES + image).crop((left, top, right, bottom))
        self.image = pygame.image.fromstring(image.tostring("raw", "RGB"), image.size, "RGB")
        self.rect = pygame.rect.Rect(location, self.image.get_size())


if __name__ == '__main__':
    pygame.init()
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    map = tmxlib.Map.open(RESOURCES + 'map-blocker-sides.tmx')

    tiles = list(map.layers[0].all_tiles())[:400]

    num_tiles = (width/TILE_SIZE_PIXELS, height/TILE_SIZE_PIXELS)
    visible_tiles = []

    sprite_tile_group = pygame.sprite.Group()

    for x in range(num_tiles[0]):
        for y in range(num_tiles[1]):
            if map.layers[0].__getitem__((x,y)).image is not None:
                image = map.layers[0].__getitem__((x,y)).image.image.source
                sprite_sheet_pos = map.layers[0].__getitem__((x,y))
                location = map.layers[0].__getitem__((x,y))._pos
                sprite_tile_group.add(TileSprite(image, location))

    while True:
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        sprite_tile_group.draw(screen)
        pygame.display.flip()