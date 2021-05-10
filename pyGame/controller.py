"""
File containing the user input class.
"""
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE,
)

class Controller:
    """
    Controller class for the dungeon crawler game

    attrs:
        player: An instance of the player class
    """
    def __init__(self, player, board):
        """
        Initializes the player class.

        args:
            player: An instance of the player class.
            board: An instance of the board class
        """
        self.player = player
        self.board = board

    def move_player(self, pressed_keys):
        """
        Function responsible for moving the player according to key presses.

        This function takes key presses as an input and moves the pygame
        rect of the player sprite. In addition, this function changes
        the up_check, down_check, and movement_check booleans in the player
        class so that they can be accesse by other methods with updated
        information regarding the player's position and movement.

        args:
            pressed_keys: A series of booleans representing the keys pressed.
            This boolean list is aquired by the pygame.key.get_pressed function.
        """
    # Arrow-key movement
        if pressed_keys[K_UP]:
            self.player.rect.move_ip(0, -2)
            self.player.movement_check = True
            self.player.up_check = True
            self.player.down_check = False
        if pressed_keys[K_DOWN]:
            self.player.rect.move_ip(0, 2)
            self.player.movement_check = True
            self.player.up_check = False
            self.player.down_check = True
        if pressed_keys[K_LEFT]:
            self.player.rect.move_ip(-2, 0)
            self.player.movement_check = True
            self.player.direction_check = False
            self.player.up_check = False
            self.player.down_check = False
        if pressed_keys[K_RIGHT]:
            self.player.rect.move_ip(2, 0)
            self.player.movement_check = True
            self.player.direction_check = True
            self.player.up_check = False
            self.player.down_check = False
        # WASD movement
        if pressed_keys[K_w]:
            self.player.rect.move_ip(0, -2)
            self.player.movement_check = True
            self.player.up_check = True
            self.player.down_check = False
        if pressed_keys[K_s]:
            self.player.rect.move_ip(0, 2)
            self.player.movement_check = True
            self.player.up_check = False
            self.player.down_check = True
        if pressed_keys[K_a]:
            self.player.rect.move_ip(-2, 0)
            self.player.movement_check = True
            self.player.direction_check = False
            self.player.up_check = False
            self.player.down_check = False
        if pressed_keys[K_d]:
            self.player.rect.move_ip(2, 0)
            self.player.movement_check = True
            self.player.direction_check = True
            self.player.up_check = False
            self.player.down_check = False
        #Boundary
        if self.player.rect.left < 0:
            self.player.rect.left = 0
        if self.player.rect.right > self.board.screen_width:
            self.player.rect.right = self.board.screen_width
        if self.player.rect.top <= 0:
            self.player.rect.top = 0
        if self.player.rect.bottom >= self.board.screen_height:
            self.player.rect.bottom = self.board.screen_height

    def attack(self, pressed_keys):
        """
        Initiates player attack sequence based on key presses.

        args:
            pressed_keys: A series of booleans representing the keys pressed.
            This boolean list is aquired by the pygame.key.get_pressed function.
        """
        if not self.player.attack:
            if pressed_keys[K_SPACE]:
                self.player.attack = True
                self.player.attack_time = pygame.time.get_ticks()
        if self.player.attack and pygame.time.get_ticks() >= (self.player.attack_time + 600):
            self.player.attack = False
