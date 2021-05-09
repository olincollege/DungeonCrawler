"""
File containing the enemy sprite class and Shy Guy and Ghost subclasses
"""
import pygame
import os
import random
from pygame.locals import RLEACCEL

class Enemy(pygame.sprite.Sprite):
    """
    Parent class for all enemy sprites.

    attrs:
        movement_sprites: List of all enemy sprites
        surf: The pygame representation of the sprite object
        rect: The pygame rect object that corresponds to the sprite
        image_count: The index of movement_sprites to set as the
        current surf.
        movement_check: Boolean representing if the sprite is moving
        health: Int representing the total health of an enemy
        direction_check: Boolean, true if the sprite is facing right,
        false if facing left.
        hit: Boolean representing whether the sprite was recently hit
        or not
        hit_time: Int representing the time that the sprite was hit
    """
    def __init__(self, sprite_path, health, spawn, board):
        """
        Initializes the Enemy class.

        args:
            sprite_path: Path to the sprite images
            health: Int representing the total health
            spawn: Two element tuple representing coordinates to spawn at
            board: An instance of the board class
        """
        super(Enemy, self).__init__()
        self.movement_sprites = os.listdir(sprite_path)
        self.surf = pygame.image.load(f"{sprite_path}/{self.movement_sprites[0]}").convert()
        self.surf.set_colorkey('white', RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_check = False
        self.health = health
        self.direction_check = False
        self.hit = False
        self.hit_time = 0
        self.rect.x = spawn[0]
        self.rect.y = spawn[1]
        self.board = board

    def check_collision(self, sprite, health_bar):
        """
        Checks whether the enemy has hit the player, causing damage.

        args:
            sprite: The player sprite
            health_bar: Health bar class
        """
        if pygame.sprite.collide_rect(sprite, self):
            sprite.player_hit(health_bar)

    def enemy_hit(self, sprite, attack):
        """
        Checks whether the player has hit the enemy, damaging the enemy.

        If the enemy has been hit, it will set the hit boolean to true,
        and will begin a countdown. Until the countdown (1200 ticks) is
        elapsed, the enemy cannot be hit again.

        args:
            sprite: The player sprite
            attack: Boolean for whether the player was attacking or not.
        """
        if self.hit_time + 1200 <= pygame.time.get_ticks():
            self.hit = False
        if attack and pygame.sprite.collide_rect(sprite, self):
            if not self.hit:
                self.hit = True
                self.hit_time = pygame.time.get_ticks()
                self.health -= 1

class ShyGuy(Enemy):
    """
    Sub-class of Enemy for the Shy Guy enemy type
    """
    def __init__(self, spawn, board):
        """
        args:
            spawn: A 2 element tuple representing x and y coordinates of spawn
            location.
        """
        super(ShyGuy, self).__init__('Sprites/Shy_Guy', 2, spawn, board)
        self.movement_sprites.remove('damage.png')
        self.movement_sprites.remove('damage1.png')

    def animation(self):
        """
        Function to animate the Shy Guy sprite

        Pulls sprite image from the movement check list, then edits
        it based on the direction the shy guy is moving. After running, it
        increases image_count by one.
        """
        if self.movement_check:
            self.image_count = self.image_count + 1
            look_initial = pygame.image.load(f"Sprites/Shy_Guy/{self.movement_sprites[self.image_count]}")\
            .convert()
            look_initial.set_colorkey('white', RLEACCEL)
            if not self.direction_check:
                self.surf = pygame.transform.smoothscale(look_initial, (51, 57))
                self.surf.set_colorkey('white', RLEACCEL)
            else:
                look_initial = pygame.transform.flip(look_initial, True, False)
                look_initial.set_colorkey('white', RLEACCEL)
                self.surf = pygame.transform.smoothscale(look_initial, (51, 57))
                self.surf.set_colorkey('white', RLEACCEL)

            if self.image_count == len(self.movement_sprites) - 1:
                self.image_count = 0

    def hit_animation(self):
        """
        Function to flash the shy guy when it gets hit.

        During the small period when the shy guy is invincible after
        being hit, this function will flash it black and white to show
        the player that the enemy is invincible. The images representing
        the white and black flashes are 'damage.png' and 'damage1.png'
        """
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
                damage.set_colorkey('white', RLEACCEL)
            elif white:
                # Load the white image
                damage = pygame.image.load('Sprites/Shy_Guy/damage1.png').convert()
                damage.set_colorkey('white', RLEACCEL)
            else:
                return None

            # Orients Yoshi according to what direction the player is moving him
            if self.direction_check:
                damage = pygame.transform.flip(damage, True, False)
                self.surf.set_colorkey('white', RLEACCEL)
            else:
                self.surf.set_colorkey('white', RLEACCEL)
            self.surf = pygame.transform.smoothscale(damage.convert_alpha(), (51, 57))
            self.surf.set_colorkey('white', RLEACCEL)

            # Resume normal sprite animation
            if self.hit_time + 1200 <= pygame.time.get_ticks():
                self.movement_check = True
                self.animation()

    def update(self, pos):
        """
        Updates the position of the shy guy to follow the player.
        """
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

        # Make sure that the sprite always stays in bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.board.screen_width:
            self.rect.right = self.board.screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.board.screen_height:
            self.rect.bottom = self.board.screen_height

class Ghost(Enemy):
    """
    Sub-class of the enemy to represent the ghost enemy type.

    attrs:
        hiding: Boolean representing whether the ghost is 'hiding' from
        the player.
    """
    def __init__(self, spawn, board):
        """
        Initializes the ghost class.

        Health is set to a large number because the ghost is meant to
        not be killed.

        args:
            spawn: Two element tuple containing x and y spawn positions.
        """
        super(Ghost, self).__init__('Sprites/Ghost', 99999999999, spawn, board)
        self.hiding = True
        self.board = board

    def animation(self):
        """
        Function to define ghost animation.

        Ghost only has two sprites. If the ghost is 'hiding', it updates
        the image, and when it stops hiding, it updates again.
        """
        if self.hiding:
            look_initial = pygame.image.load(f"Sprites/Ghost/{self.movement_sprites[1]}").convert()
            if self.direction_check:
                self.surf = pygame.transform.flip(look_initial, True, False)
                self.surf.set_colorkey('white', RLEACCEL)
            else:
                self.surf = look_initial
                self.surf.set_colorkey('white', RLEACCEL)
        else:
            look_initial = pygame.image.load(f"Sprites/Ghost/{self.movement_sprites[0]}").convert()
            if self.direction_check:
                self.surf = pygame.transform.flip(look_initial, True, False)
                self.surf.set_colorkey('white', RLEACCEL)
            else:
                self.surf = look_initial
                self.surf.set_colorkey('white', RLEACCEL)

    def update(self, pos, direction_check):
        """
        Updates the position of the ghost.

        The ghost will alternate between hiding and not hiding based on where
        the player looks. If the player is facing the ghost, it will hide. If not,
        it will not hide. When the ghost is hiding, it stays still. When not
        hiding, it will move towards the player.
        """
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
                self.direction_check = True
            if pos_x < self.rect.x:
                if pos_y > self.rect.y:
                    self.rect.move_ip(-1,1)
                if pos_y < self.rect.y:
                    self.rect.move_ip(-1,-1)
                else:
                    self.rect.move_ip(-1,0)
                self.movement_check = True
                self.direction_check = False
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
        if self.rect.right > self.board.screen_width:
            self.rect.right = self.board.screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.board.screen_height:
            self.rect.bottom = self.board.screen_height

class EnemyProjectile(pygame.sprite.Sprite):
    """
    PyGame sprite class representing the projectiles that fly in the screen.

    attrs:
        surf: PyGame surf object representing the sprite.
        rect: PyGame rect object representing the sprite.
        speed: Random int determining how fast the projectile will fly.
    """
    def __init__(self, board):
        super(EnemyProjectile, self).__init__()
        image = pygame.image.load('Sprites/Mushroom/mushroom_enemy.png')
        image.set_colorkey((247,247,247), RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (50,50))
        self.surf.set_colorkey((247,247,247), RLEACCEL)
        self.board = board
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.board.screen_width + 20, self.board.screen_width + 100),
                random.randint(0, self.board.screen_height),
            )
        )
        self.speed = random.randint(1, 3)

    def update(self, sprite, health_bar):
        """
        Damages player if the projectile hits player.

        args:
            sprite: Player sprite.
            health_bar: Reference to the health_bar class.
        """
        if pygame.sprite.collide_rect(sprite, self):
            self.kill()
            sprite.player_hit(health_bar)
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
