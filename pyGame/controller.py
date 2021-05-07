from game_setup import *

class Controller:
    def __init__(self, player):
        self.player = player

    def move_player(self, pressed_keys):
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
        if self.player.rect.right > SCREEN_WIDTH:
            self.player.rect.right = SCREEN_WIDTH
        if self.player.rect.top <= 0:
            self.player.rect.top = 0
        if self.player.rect.bottom >= SCREEN_HEIGHT:
            self.player.rect.bottom = SCREEN_HEIGHT

    def attack(self, pressed_keys):
        if not self.player.attack:
            if pressed_keys[K_SPACE]:
                self.player.attack = True
                self.player.attack_time = pygame.time.get_ticks()
        if self.player.attack and pygame.time.get_ticks() >= (self.player.attack_time + 600):
            self.player.attack = False