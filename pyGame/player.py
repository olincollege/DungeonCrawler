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
        self.hittable = True
        self.time_hit = 0

    def attack_animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1

    def animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1
            if self.direction_check:
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
    
    def check_invincibility(self):
        if not self.hittable and self.time_hit + 600 <= pygame.time.get_ticks():
            self.hittable = True
            print('Invincibility over')

    def animate_invincibility(self):

        time_hit = pygame.time.get_ticks()
        damage_1 = pygame.image.load('Sprites/Yoshi/damage.png').convert()
        damage_1 = pygame.transform.smoothscale(damage_1.convert_alpha(), (40, 40))
        damage_2 = pygame.image.load('Sprites/Yoshi/damage1.png').convert()
        damage_2 = pygame.transform.smoothscale(damage_2.convert_alpha(), (40, 40))
        resting = pygame.image.load('Sprites/Yoshi/1.png').convert()
        resting = pygame.transform.smoothscale(resting.convert_alpha(), (40, 40))

        if not self.hittable:
            damage_2.set_colorkey((255, 255, 255), RLEACCEL)
            # self.surf = pygame.transform.flip(damage_2, True, False)
            if self.direction_check:
                self.surf = pygame.transform.smoothscale(damage_2, (40,40))
            else:
                self.surf = pygame.transform.flip(damage_2, True, False)
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 100 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_1, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_1, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 200 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_2, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_2, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 300 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_1, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_1, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 400 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_1, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_1, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 500 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_2, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_2, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

            if self.time_hit + 600 <= pygame.time.get_ticks():
                if self.direction_check:
                    self.surf = pygame.transform.smoothscale(damage_1, (40,40))
                else:
                    self.surf = pygame.transform.flip(damage_1, True, False)
                self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    def player_hit(self, health):
        if self.hittable:
            print('hit')
            self.hittable = False
            self.time_hit = pygame.time.get_ticks()
            health.surf = health.health_ani[self.health]
            self.hittable = False
            self.health = self.health - 1
            # Now show the other color.
        """
        self.surf = pygame.transform.smoothscale(damage_2.convert_alpha(), (40, 40))
        self.surf = pygame.transform.flip(damage_2, True, False)
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)

        self.surf = pygame.transform.smoothscale(damage_1.convert_alpha(), (40, 40))
        self.surf = pygame.transform.flip(damage_1, True, False)
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)

        self.surf = pygame.transform.smoothscale(damage_2.convert_alpha(), (40, 40))
        self.surf = pygame.transform.flip(damage_2, True, False)
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)
        """
        """
        self.surf = pygame.transform.smoothscale(resting.convert_alpha(), (40, 40))
        self.surf = pygame.transform.flip(resting, True, False)
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)
        """
        

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