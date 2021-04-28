from game_setup import *

class Board(pygame.sprite.Sprite):


    def __init__(self, x_cord, y_cord):
        super(Board, self).__init__()
        look_initial = pygame.image.load("Sprites/Door/bottom_door.png").convert()
        self.surf = pygame.transform.smoothscale(look_initial, (40, 40)) 
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord