import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):
        # The basic set up for the level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # Loop to place the tiles on the game screen
        for row_index,row in enumerate(layout):
            for column_index,column in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size

                if column == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
        
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200:
            self.world_shift = 8
            player.speed = 0

    def run(self):
        # Drawing the level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Drawing the player tiles
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()