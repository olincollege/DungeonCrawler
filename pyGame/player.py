"""
File containing Player class
"""
import pygame
from pygame.locals import RLEACCEL

class Player(pygame.sprite.Sprite):
    """
    Class representing the pygame player sprite.

    attrs:
        surf: The pygame surf object for the Yoshi sprite
        rect: The pygame rect defining the bounds of the Yoshi sprite
        image_count: Int representing the current frame of animation
        movement_sprites: List of paths to the images in Yoshi's animation
        movement_check: Boolean defining whether Yoshi is moving or not
        direction_check: Boolean defining whether Yoshi is moving right
        or left. Right is defined as true, left as false.
        health: The health of the player
        attack: Boolean defining whether Yoshi is attacking or not
        attack_time: Int representing the time in ticks at which Yoshi
        began attacking.
        hittable: Boolean defining whether Yoshi can be hit or not
        up_check: Boolean defining whether Yoshi is moving up or not
        down_check: Boolean defining whether Yoshi is moving down or not.
    """
    def __init__(self):
        """
        Initializes the player class.
        """
        super(Player, self).__init__()
        image = pygame.image.load("Sprites/Yoshi/1.png").convert()
        image.set_colorkey((252, 254, 252), RLEACCEL)
        self.surf = pygame.transform.smoothscale(image.convert_alpha(), (40, 40))
        self.surf.set_colorkey((252, 254, 252), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.image_count = 0
        self.movement_sprites = ["Sprites/Yoshi/1.png", "Sprites/Yoshi/2.png", "Sprites/Yoshi/3.png"
                                ,"Sprites/Yoshi/4.png", "Sprites/Yoshi/5.png", "Sprites/Yoshi/6.png"
                                ,"Sprites/Yoshi/7.png"]
        self.movement_check = False
        self.direction_check = False
        self.rect.x = 100
        self.rect.y = 300
        self._health = 5
        self.attack_time = 0
        self.time_hit = 0
        self.up_check = False
        self.down_check = False
        self.hittable = True
        self.attack = False

    def animation(self):
        """
        Function defining animation for Yoshi's movement.

        Based on the values of direction_check, up_check, and down_check,
        this function will rotate or flip the player sprite and run through the
        list of frames of animation.
        """
        if self.movement_check:
            self.image_count = self.image_count + 1
            if self.direction_check:
                look_initial = pygame.image.load(self.movement_sprites[self.image_count]).convert()
                look_initial.set_colorkey((252, 254, 252), RLEACCEL)
                if self.up_check:
                    look_initial = pygame.transform.smoothscale(look_initial.convert_alpha(), \
                    (40, 40))
                    self.surf = pygame.transform.rotate(look_initial, 90)
                elif self.down_check:
                    look_initial = pygame.transform.smoothscale(look_initial.convert_alpha(), \
                    (40, 40))
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
        """
        Function to see if Yoshi's temporary invincibility has expired.

        For a short time after being hit, Yoshi is invincible to prevent him from
        instantly dying after hitting one enemy.
        """
        if not self.hittable and self.time_hit + 1200 <= pygame.time.get_ticks():
            self.hittable = True
        else:
            pass

    def animate_invincibility(self):
        """
        Flashes Yoshi black and white to show the player Yoshi is invincible.

        This function switches Yoshi's sprite to be an all-white and all-black
        animation during the time when Yoshi is invincible.
        """
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
                pass

            # Orients Yoshi according to what direction the player is moving him
            if self.direction_check:
                if self.up_check:
                    self.surf = pygame.transform.rotate(damage, 90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                elif self.down_check:
                    self.surf = pygame.transform.rotate(damage, -90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            else:
                damage = pygame.transform.flip(damage, True, False)
                if self.up_check:
                    self.surf = pygame.transform.rotate(damage, -90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
                elif self.down_check:
                    self.surf = pygame.transform.rotate(damage, 90)
                    self.surf.set_colorkey((251, 255, 252), RLEACCEL)
            self.surf = pygame.transform.smoothscale(damage.convert_alpha(), (40, 40))
            self.surf.set_colorkey((251, 255, 252), RLEACCEL)

            # Resume normal sprite animation
            if self.time_hit + 1200 <= pygame.time.get_ticks():
                self.movement_check = True
                self.animation()

    def player_hit(self, health):
        """
        Changes health and initiates invincibility period when Yoshi is hit

        args:
            health: An int representing Yoshi's health
        """
        if self.hittable:
            self.hittable = False
            self.time_hit = pygame.time.get_ticks()
            health.surf = health.health_ani[self._health-1]
            self._health = self._health - 1

    @property
    def health(self):
        """
        Accessor for the player health.
        """
        return self._health


class HealthBar(pygame.sprite.Sprite):
    """
    Sprite representing the health bar

    attrs:
        surf: The pygame surf object defining the sprite image
        health_ani: List of paths to the animation frame images
    """
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
