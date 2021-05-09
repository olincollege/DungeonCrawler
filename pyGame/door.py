"""
File containing the door sprite class
"""
import pygame

from pygame.locals import RLEACCEL

class Door(pygame.sprite.Sprite):
    """
    Class representing the door sprite

    attrs:
        surf: The pygame surf representing the sprite image
        rect: The pygame rect representing the bounds of the sprite
    """
    def __init__(self, x, y):
        """
        Initializes the door class

        args:
            x: The x position to set the rect to
            y: The y position to set the rect to
        """
        super(Door, self).__init__()
        image = pygame.image.load('Sprites/Door/bottom_door.png').convert()
        image.set_colorkey('white', RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (60, 30))
        self.surf.set_colorkey('white', RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x # pylint: disable=message
        self.rect.y = y # pylint: disable=message