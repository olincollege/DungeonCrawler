from game_setup import *

class Player(pygame.sprite.Sprite):


    def __init__(self):
        super(Player, self).__init__()
        image = pygame.image.load("Sprites/Yoshi/1.png").convert()
        image.set_colorkey((252, 254, 252), RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (40, 40))
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_sprites = ["Sprites/Yoshi/1.png", "Sprites/Yoshi/2.png", "Sprites/Yoshi/3.png",
                                "Sprites/Yoshi/4.png", "Sprites/Yoshi/5.png", "Sprites/Yoshi/6.png", 
                                "Sprites/Yoshi/7.png"]
        self.movement_check = False
        self.direction_check = False
        self.rect.x = 100
        self.rect.y = 300
        self.health = 5

    def update(self, pressed_keys):
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
                look_initial.set_colorkey((252, 254, 252), RLEACCEL)
                self.surf = pygame.transform.smoothscale(look_initial.convert_alpha(), (40, 40)) 
                self.surf.set_colorkey((252, 254, 252), RLEACCEL)
            else:
                flip = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                flip.set_colorkey((252, 254, 252), RLEACCEL)
                look_initial = pygame.transform.smoothscale(flip.convert_alpha(), (40, 40))
                self.surf = pygame.transform.flip(look_initial, True, False)
                self.surf.set_colorkey((252, 254, 252), RLEACCEL)
            # Reset image counter
            if self.image_count > 5:
                self.image_count = 1
        self.movement_check = False
    
    def player_hit(self, health):
        self.health = self.health - 1
        health.surf = health.health_ani[self.health]

class HealthBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.surf = pygame.image.load("Sprites/Heart/heart5.png")
            self.health_ani = [
                pygame.image.load("Sprites/Heart/heart0.png"), 
                pygame.image.load("Sprites/Heart/heart.png"),
                pygame.image.load("Sprites/Heart/heart2.png"), 
                pygame.image.load("Sprites/Heart/heart3.png"),
                pygame.image.load("Sprites/Heart/heart4.png"), 
                pygame.image.load("Sprites/Heart/heart5.png")]