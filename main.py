import pygame, sys

# Main game setup
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# Loop for checking if you quit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # When quitting the game, fill the screen black
    screen.fill('black')

    # Sets the framerate for the gakme
    pygame.display.update()
    clock.tick(60)