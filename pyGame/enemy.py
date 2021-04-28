import os
from game_setup import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('Sprites/Shy_Guy/shy_guy_1.png').convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_sprites = ['Sprites/Shy_Guy/shy_guy_0.png', 'Sprites/Shy_Guy/shy_guy_1.png', 'Sprites/Shy_Guy/shy_guy_2.png']
        self.movement_check = False
        self.rect.x = 500
        self.rect.y = 300

    def move(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]

        # Moving towards the player
        
        if pos_x > self.rect.x:
            if pos_y > self.rect.y:
                self.rect.move_ip(1,1)
            if pos_y < self.rect.y:
                self.rect.move_ip(1,-1)
            else:
                self.rect.move_ip(1,0)
            self.movement_check = True
        if pos_x < self.rect.x:
            if pos_y > self.rect.y:
                self.rect.move_ip(-1,1)
            if pos_y < self.rect.y:
                self.rect.move_ip(-1,-1)
            else:
                self.rect.move_ip(-1,0)
            self.movement_check = True
        if pos_x == self.rect.x:
            if pos_y > self.rect.y:
                self.rect.move_ip(0,1)
            if pos_y < self.rect.y:
                self.rect.move_ip(0,-1)
            self.movement_check = True
        
        self.movement_check = True
        # Boundary
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1
            self.surf = pygame.image.load(self.movement_sprites[self.image_count]).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.image_count == 2:
                self.image_count = 0
        self.movement_check = False

