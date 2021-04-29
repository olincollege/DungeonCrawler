from game_setup import *

class Door(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Door, self).__init__()
        image = pygame.image.load('Sprites/Door/bottom_door.png')
        self.surf = pygame.transform.smoothscale(image, (40, 40))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y