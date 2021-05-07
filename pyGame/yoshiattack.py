from game_setup import *

class YoshiAttack(pygame.sprite.Sprite):

    def __init__(self, player):
        super(YoshiAttack, self).__init__()
        self.player = player
        self.tongue = pygame.image.load('Sprites/Tongue/tongue.png')
        self.tongue.set_colorkey((251,255,252), RLEACCEL)
        self.surf = pygame.transform.smoothscale(self.tongue.convert_alpha(), (40, 40))
        self.surf.set_colorkey((251, 255, 252), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.pos_x = 0
        self.pos_y = 0
        
    def animate(self):
        tongue = self.tongue
        tongue.set_colorkey((251, 255, 252))
        tongue = pygame.transform.smoothscale(tongue.convert_alpha(), (20,5))
        if self.player.direction_check:
            if self.player.up_check:
                self.rect.x = self.player.rect.x + 12
                self.rect.y = self.player.rect.y - 15
                self.surf = pygame.transform.rotate(tongue, 90)
            elif self.player.down_check:
                self.rect.x = self.player.rect.x + 22
                self.rect.y = self.player.rect.y + 35
                self.surf = pygame.transform.rotate(tongue, -90)
            else:
                self.rect.x = self.player.rect.x + 35
                self.rect.y = self.player.rect.y + 15
                self.surf = pygame.transform.smoothscale(tongue.convert_alpha(), (20,5))
            self.surf.set_colorkey((251,255,252), RLEACCEL) 
        else:
            if self.player.up_check:
                self.rect.x = self.player.rect.x + 22
                self.rect.y = self.player.rect.y - 15
                self.surf = pygame.transform.smoothscale(tongue.convert_alpha(), (20,5))
                self.surf = pygame.transform.rotate(tongue, 90)
            elif self.player.down_check:
                self.rect.x = self.player.rect.x + 12
                self.rect.y = self.player.rect.y + 35
                self.surf = pygame.transform.smoothscale(tongue.convert_alpha(), (20,5))
                self.surf = pygame.transform.rotate(tongue, -90)
            else:
                self.rect.x = self.player.rect.x - 15
                self.rect.y = self.player.rect.y + 15
                self.surf = pygame.transform.smoothscale(tongue.convert_alpha(), (20,5))
                self.surf = pygame.transform.flip(tongue, True, False)
            self.surf.set_colorkey((251,255,252), RLEACCEL) 