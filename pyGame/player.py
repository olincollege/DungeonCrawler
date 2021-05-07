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
        self.attack = False
        self.attack_time = 0
        self.hittable = True
        self.time_hit = 0
        self.up_check = False
        self.down_check = False

    def attack_animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1

    def animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1
            if self.direction_check:
                look_initial = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                look_initial.set_colorkey((252, 254, 252), RLEACCEL)
                if self.up_check:
                    look_initial = pygame.transform.smoothscale(look_initial.convert_alpha(), (40, 40))
                    self.surf = pygame.transform.rotate(look_initial, 90)
                elif self.down_check:
                    look_initial = pygame.transform.smoothscale(look_initial.convert_alpha(), (40, 40))
                    self.surf = pygame.transform.rotate(look_initial, -90)
                else:
                    self.surf = pygame.transform.smoothscale(look_initial.convert_alpha(), (40, 40)) 
                self.surf.set_colorkey((252, 254, 252), RLEACCEL)
            else:
                flip = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                flip.set_colorkey((252, 254, 252), RLEACCEL)
                look_initial = pygame.transform.smoothscale(flip.convert_alpha(), (40, 40))
                if self.up_check:
                    look_initial = pygame.transform.flip(look_initial, True, False)
                    self.surf = pygame.transform.rotate(look_initial, -90)
                elif self.down_check:
                    look_initial = pygame.transform.flip(look_initial, True, False)
                    self.surf = pygame.transform.rotate(look_initial, 90)
                else:
                    self.surf = pygame.transform.flip(look_initial, True, False)
                self.surf.set_colorkey((252, 254, 252), RLEACCEL)
            # Reset image counter
            if self.image_count > 5:
                self.image_count = 1
        self.movement_check = False
    
    def check_invincibility(self):
        if not self.hittable and self.time_hit + 1200 <= pygame.time.get_ticks():
            self.hittable = True

    def animate_invincibility(self):
        white = False
        black = False
        # Function should only occur when Yoshi is invincible after being hit
        if not self.hittable:
            # Based on how much time has passed since the time Yoshi was hit, we will
            # choose whether to flash white or black. This is to make Yoshi appear to be
            # continuously flashing.
            if (self.time_hit - pygame.time.get_ticks())%400 <= 200:
                white = True
                black = False
            else:
                white = False
                black = True
            
            if black:
                # Load the black image
                damage = pygame.image.load('Sprites/Yoshi/damage.png').convert()
                damage.set_colorkey((251, 255, 252), RLEACCEL)
            elif white:
                # Load the white image
                damage = pygame.image.load('Sprites/Yoshi/damage1.png').convert()
                damage.set_colorkey((251, 255, 252), RLEACCEL)
            else:
                return None

            # Orients Yoshi according to what direction the player is moving him
            if self.direction_check:
                if self.up_check:
                    self.surf = pygame.transform.rotate(damage, 90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                if self.down_check:
                    self.surf = pygame.transform.rotate(damage, -90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            else:
                damage = pygame.transform.flip(damage, True, False)
                if self.up_check:
                    self.surf = pygame.transform.rotate(damage, -90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                if self.down_check:
                    self.surf = pygame.transform.rotate(damage, 90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            self.surf = pygame.transform.smoothscale(damage.convert_alpha(), (40, 40))
            self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                        
            # Resume normal sprite animation
            if self.time_hit + 1200 <= pygame.time.get_ticks():
                self.movement_check = True
                self.animation()

    def player_hit(self, health):
        if self.hittable:
            self.hittable = False
            self.time_hit = pygame.time.get_ticks()
            health.surf = health.health_ani[self.health-1]
            self.health = self.health - 1
        

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