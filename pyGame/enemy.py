import os
import random
from game_setup import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, sprite_path, health, spawn):
        """
        Sprite is the path to the sprite, spawn is a 2 element tuple    
        """
        super(Enemy, self).__init__()
        self.movement_sprites = os.listdir(sprite_path)
        self.surf = pygame.image.load(f"{sprite_path}/{self.movement_sprites[0]}").convert()
        self.surf.set_colorkey('white', RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_check = False
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.health = health
        self.direction_check = False
        self.hit = False
        self.hit_time = 0
    
    def check_collision(self, sprite, health_bar):
        if pygame.sprite.collide_rect(sprite, self):
            sprite.player_hit(health_bar)

    def enemy_hit(self, sprite, attack):
        print(self.hit)
        if self.hit_time + 1200 >= pygame.time.get_ticks():
            self.hit = False
        if attack and pygame.sprite.collide_rect(sprite, self):
            if not self.hit:
                self.hit = True
                self.hit_time = pygame.time.get_ticks()
                self.health -= 1
                print('hit enemy!')

class ShyGuy(Enemy):

    def __init__(self, spawn):
        super(ShyGuy, self).__init__('Sprites/Shy_Guy', 4, spawn)
        self.movement_sprites.remove('damage.png')
        self.movement_sprites.remove('damage1.png')

    def animation(self):
        if self.movement_check:
            self.image_count = self.image_count + 1
            look_initial = pygame.image.load(f"Sprites/Shy_Guy/{self.movement_sprites[self.image_count]}").convert()
            look_initial.set_colorkey((251, 255, 252), RLEACCEL)
            if self.direction_check:
                self.surf = pygame.transform.smoothscale(look_initial, (50, 50))
            else:
                look_initial = pygame.transform.flip(look_initial, True, False)
                self.surf = pygame.transform.smoothscale(look_initial, (50, 50))

            if self.image_count == len(self.movement_sprites) - 1:
                self.image_count = 0
        self.movement_check = False

    def hit_animation():
        white = False
        black = False

        if self.hit:
            if (self.hit_time - pygame.time.get_ticks())%400 <= 200:
                white = True
                black = False
            else:
                white = False
                black = True
            
            if black:
                # Load the black image
                damage = pygame.image.load('Sprites/Shy_Guy/damage.png').convert()
                damage.set_colorkey((251, 255, 252), RLEACCEL)
            elif white:
                # Load the white image
                damage = pygame.image.load('Sprites/Shy_Guy/damage1.png').convert()
                damage.set_colorkey((251, 255, 252), RLEACCEL)
            else:
                return None

            # Orients Yoshi according to what direction the player is moving him
            if self.direction_check:
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            else:
                damage = pygame.transform.flip(damage, True, False)
                self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            self.surf = pygame.transform.smoothscale(damage.convert_alpha(), (40, 40))
            self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                        
            # Resume normal sprite animation
            if self.time_hit + 1200 <= pygame.time.get_ticks():
                self.movement_check = True
                self.animation()

    def update(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]

        # Moving towards the player
        if pos_x > self.rect.x:
            self.direction_check = True
            if pos_y > self.rect.y:
                self.rect.move_ip(1,1)
            if pos_y < self.rect.y:
                self.rect.move_ip(1,-1)
            else:
                self.rect.move_ip(1,0)
            self.movement_check = True
        if pos_x < self.rect.x:
            self.direction_check = False
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

class Ghost(Enemy):

    def __init__(self, spawn):
        super(Ghost, self).__init__('Sprites/Ghost', 99999999999, spawn)
        self.hiding = True

    def animation(self):
        if self.hiding:
            self.surf = pygame.image.load(f"Sprites/Ghost/{self.movement_sprites[1]}").convert()
            self.surf.set_colorkey('white', RLEACCEL)
        else:
            self.surf = pygame.image.load(f"Sprites/Ghost/{self.movement_sprites[0]}").convert()
            self.surf.set_colorkey('white', RLEACCEL)

    def update(self, pos, direction_check):
        pos_x = pos[0]
        pos_y = pos[1]

        if direction_check and pos_x < self.rect.x:
            self.hiding = True
        elif not direction_check and pos_x > self.rect.x:
            self.hiding = True
        else:
            self.hiding = False
        # Moving towards the player
        if not self.hiding:
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

class Boss(Enemy):
    def __init__(self, spawn):
        super()._init__('Shy_Guy/shy_guy_0.png', 2, spawn)


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyProjectile, self).__init__()
        image = pygame.image.load('Sprites/Mushroom/mushroom_enemy.png')
        image.set_colorkey((247,247,247), RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (50,50))
        self.surf.set_colorkey((247,247,247), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 3)

    def update(self, sprite, health_bar):
        if pygame.sprite.collide_rect(sprite, self):
            self.kill()
            sprite.player_hit(health_bar)
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()