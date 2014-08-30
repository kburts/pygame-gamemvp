__author__ = 'Kevin'

import sys
import pygame
import tmxlib
from PIL import Image
"""
filename = 'map-blocker-sides.tmx'
map = tmxlib.Map.open(filename)

print map
allTiles = map.layers[0].all_tiles()
print map.layers[0].type
while True:
    try:
        print allTiles.next()
    except:
        break

print map.layers[0].to_dict()
print vars(map)
"""

class TileSprite(pygame.sprite.Sprite):
    def __init__(self, image, location, tilesize, spritesheet_num):
        super(TileSprite, self).__init__()
        location = (location[0] * tilesize, location[1] * tilesize)
        left = location[0]
        top = location[1]
        right = location[0] + 32
        bottom = location[1] + 32

        im = Image.open(image).crop((left, top, right, bottom))#.tostring("raw", "RGB")
        self.image = pygame.image.fromstring(im.tostring("raw", "RGB"), im.size, "RGB")
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        print self.rect

if __name__ == '__main__':
    pygame.init()
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)

    map = tmxlib.Map.open('map-blocker-sides.tmx')
    tiles = list(map.layers[0].all_tiles())[:400]
    print vars(tiles[0])
    print tiles[0], tiles[-1]

    tilesize = 32
    num_tiles = (width/tilesize, height/tilesize)
    visible_tiles = []

    sprite_tile_group = pygame.sprite.Group()

    for x in range(num_tiles[0]):
        #visible_tiles.append([]);
        for y in range(num_tiles[1]):
            if map.layers[0].__getitem__((x,y)).image is not None:
                image = map.layers[0].__getitem__((x,y)).image.image.source
                spritesheet_pos = map.layers[0].__getitem__((x,y))
                location = map.layers[0].__getitem__((x,y))._pos
                #location = map.layers[0].__getitem__((x,y)).image.top_left
                sprite_tile_group.add(TileSprite(image, location, tilesize, spritesheet_pos))

            #visible_tiles[-1].append(map.layers[0].__getitem__([x, y]))
            #sprite_tile_group.add(TileSprite())
    print sprite_tile_group
    while 1:
        sprite_tile_group.draw(screen)
        pygame.display.flip()

    print 'done'