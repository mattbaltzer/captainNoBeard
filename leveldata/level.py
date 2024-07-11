import pygame
import random
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height
from tiles import Tile, StaticTile, Crate, Coin, Palm
from enemy import Enemy
from decoration import Sky, Water, Clouds

class Level:
    def __init__(self,level_data,surface):
        # Generates the surface and controls the level scroll
        self.display_surface = surface
        self.world_shift = -2

        # Player setup
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # Creates the terrain by seleting values from the terrain csv
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        # Creates the grass by seleting values from the grass csv
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout,'grass')
        
        # Creates the crates setup
        crate_layout = import_csv_layout(level_data['crates'])
        self.crate_sprites = self.create_tile_group(crate_layout,'crates')

        # Creates the animated coins setup
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout,'coins') 

        # Creates the animated foreground palm trees
        fg_palm_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprites = self.create_tile_group(fg_palm_layout,'fg palms')

        # Creates the animated background palm trees
        bg_palm_layout = import_csv_layout(level_data['bg palms'])
        self.bg_palm_sprites = self.create_tile_group(bg_palm_layout,'bg palms')
        
        # Enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout,'enemies')

        # Constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout,'constraints')

        # Skybox/Decorations
        self.sky = Sky(8)
        level_width = len(terrain_layout[0]) * tile_size
        self.water = Water(screen_height - 30,level_width)
        self.clouds = Clouds(400,level_width,30)
    
    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('./graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)

                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('./graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                    
                    if type == 'crates':
                        sprite = Crate(tile_size,x,y)

                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size,x,y,'./graphics/coins/gold')
                        elif val == '1':
                            sprite = Coin(tile_size,x,y,'./graphics/coins/silver')
                    
                    if type == 'fg palms':
                        if val == '0':
                            sprite = Palm(tile_size,x,y,'./graphics/terrain/palm_small',random.randint(30,38))
                        elif val == '1':
                            sprite = Palm(tile_size,x,y,'./graphics/terrain/palm_large',random.randint(55,64))
                    
                    if type == 'bg palms':
                        sprite = Palm(tile_size,x,y,'./graphics/terrain/palm_bg',random.randint(55,64))

                    if type == 'enemies':
                        sprite = Enemy(tile_size,x,y)

                    if type == 'constraints':
                        sprite = Tile(tile_size,x,y)

                    sprite_group.add(sprite)

        return sprite_group
    
    def player_setup(self,layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print('player goes here')
                elif val == '1':
                    hat_surface = pygame.image.load('./graphics/character/hat.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,hat_surface)
                    self.goal.add(sprite)


    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            # The false prevents the enemy from being killed when a collision happens
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()

    def run(self):
        # skybox/decorations
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface, self.world_shift)

        # background palms
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)

        # runs the entire level
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # enemy
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        # crates
        self.crate_sprites.update(self.world_shift)
        self.crate_sprites.draw(self.display_surface)
        
        # grass
        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        #coins
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        # foreground palms
        self.fg_palm_sprites.update(self.world_shift)
        self.fg_palm_sprites.draw(self.display_surface)

        # player sprites
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        # water sprites
        self.water.draw(self.display_surface,self.world_shift)

