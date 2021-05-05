from game_setup import *

class Controller:
    def __init__(self, player):
        self.player = player

    def move_player(self, pressed_keys):
    # Arrow-key movement
        if pressed_keys[K_UP]:
            self.player.rect.move_ip(0, -1)
            self.player.movement_check = True
        if pressed_keys[K_DOWN]:
            self.player.rect.move_ip(0, 1)
            self.player.movement_check = True
        if pressed_keys[K_LEFT]:
            self.player.rect.move_ip(-1, 0)
            self.player.movement_check = True
            self.player.direction_check = False
        if pressed_keys[K_RIGHT]:
            self.player.rect.move_ip(1, 0)
            self.player.movement_check = True
            self.player.direction_check = True

        # WASD movement
        if pressed_keys[K_w]:
            self.player.rect.move_ip(0, -1)
            self.player.movement_check = True
        if pressed_keys[K_s]:
            self.player.rect.move_ip(0, 1)
            self.player.movement_check = True
        if pressed_keys[K_a]:
            self.player.rect.move_ip(-1, 0)
            self.player.movement_check = True
            self.player.direction_check = False
        if pressed_keys[K_d]:
            self.player.rect.move_ip(1, 0)
            self.player.movement_check = True
            self.player.direction_check = True

        #Boundary
        if self.player.rect.left < 0:
            self.player.rect.left = 0
        if self.player.rect.right > SCREEN_WIDTH:
            self.player.rect.right = SCREEN_WIDTH
        if self.player.rect.top <= 0:
            self.player.rect.top = 0
        if self.player.rect.bottom >= SCREEN_HEIGHT:
            self.player.rect.bottom = SCREEN_HEIGHT