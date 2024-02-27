import pygame, sys
from settings import *
from tiles import Tile

# Main game setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# Sprite group
test_tile = pygame.sprite.Group(Tile(100,100),200)

# Loop for checking if you quit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # When quitting the game, fill the screen black
    screen.fill('black')
    test_tile.draw(screen)
    # Sets the framerate for the gakme
    pygame.display.update()
    clock.tick(60)