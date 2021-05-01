from game_setup import *

class Door(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Door, self).__init__()
        image = pygame.image.load('Sprites/Door/bottom_door.png').convert()
        image.set_colorkey('white', RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (40, 40))
        self.surf.set_colorkey('white', RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y