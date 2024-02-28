import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self,level_data,surface):
        # The basic set up for the level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        # Loop to place the tiles on the game screen
        for row_index,row in enumerate(layout):
            for column_index,column in enumerate(row):
                if column == 'X':
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)