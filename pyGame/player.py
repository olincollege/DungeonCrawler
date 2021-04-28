from game_setup import *

class Player(pygame.sprite.Sprite):


    def __init__(self):
        super(Player, self).__init__()
        look_initial = pygame.image.load("Sprites/Yoshi/1.gif").convert()
        self.surf = pygame.transform.smoothscale(look_initial, (40, 40)) 
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_sprites = ["Sprites/Yoshi/1.gif", "Sprites/Yoshi/2.gif", "Sprites/Yoshi/3.gif",
                                "Sprites/Yoshi/4.gif", "Sprites/Yoshi/5.gif", "Sprites/Yoshi/6.gif", 
                                "Sprites/Yoshi/7.gif"]
        self.movement_check = False
        self.direction_check = False

    def move(self, pressed_keys):
        # Arrow-key movement
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
            self.movement_check = True
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
            self.movement_check = True
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
            self.movement_check = True
            self.direction_check = False
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
            self.movement_check = True
            self.direction_check = True

        # WASD movement
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
            self.movement_check = True
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
            self.movement_check = True
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
            self.movement_check = True
            self.direction_check = False
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)
            self.movement_check = True
            self.direction_check = True

        #Boundary
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        

    def animation(self):
        if self.movement_check == True:
            self.image_count = self.image_count + 1
            if self.direction_check == True:
                look_initial = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                self.surf = pygame.transform.smoothscale(look_initial, (40, 40)) 
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            else:
                flip = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                look_initial = pygame.transform.smoothscale(flip, (40, 40)) 
                self.surf = pygame.transform.flip(look_initial, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            # Reset image counter
            if self.image_count > 5:
                self.image_count = 1
        self.movement_check = False
    
    def check_collision(self, sprite):
        if pygame.sprite.spritecollide(self, sprite, True):
            print("hehe")
