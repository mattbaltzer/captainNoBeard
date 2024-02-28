import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

    # Updates how much you want to move the camera on the X axis
    def update(self,x_shift):
        self.rect.x += x_shift
