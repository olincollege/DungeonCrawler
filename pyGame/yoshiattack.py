"""
Model file containing Yoshi Attack file.
"""
import pygame
from pygame.locals import RLEACCEL

class YoshiAttack(pygame.sprite.Sprite):
    """
    Class to represent the tongue sprite for yoshi's attack animation

    attrs:
        player: An instance of the player class.
        tongue: The sprite image of yoshi's tongue
        surf: The pygame representation of the sprite image
        rect: The pygame rectangle representing the bounds of the sprite
        pos_x:
    """
    def __init__(self, player):
        """
        Initializes the YoshiAttack class

        args:
            player: An instance of the player class
        """
        super(YoshiAttack, self).__init__()
        self.player = player
        self.tongue = pygame.image.load('Sprites/Tongue/tongue.png')
        self.tongue.set_colorkey((251,255,252), RLEACCEL)
        self.surf = pygame.transform.smoothscale(self.tongue.convert_alpha(), (40, 40))
        self.surf.set_colorkey((251, 255, 252), RLEACCEL)
        self.rect = self.surf.get_rect()

    def animate(self):
        """
        Function to define animation of the attack sprite

        This function controls the offset and rotation of the tongue sprite
        in relation to the player's position and direction.
        """
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
