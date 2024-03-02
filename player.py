import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6

    def get_input(self):
        keys = pygame.key.get_pressed()

        # Checks to see if keys were pressed and assign movement to them
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed