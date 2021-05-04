from game_setup import *
from player import Player, HealthBar
from enemy import Enemy, EnemyProjectile
from board import Board
from door import Door
from generate_world import WorldGeneration, Room
import pygame

class Game():

    def __init__(self,pyGame):

        # Initialize starting room background
        background_raw = pygame.image.load("Sprites/Background/cloud_background.jpg")
        self.BACKGROUND = pygame.transform.smoothscale(background_raw, (800, 600)) 

        # Timer for Enemy Projectile
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000)


        ####### Need to refactor 
        # Set room variable equal to spawn room to initialize
        # Should probably put this in init when we make it into a class
        self.wgen = WorldGeneration()
        self.wgen.generate_world()
        self.tree = self.wgen.tree
        self.room_def = self.wgen.dict
        self.room_node = self.tree
        self.room_def['Spawn'] = Room('cloud_background.jpg', 0, 0)
        self.room = self.room_def['Spawn']
        self.num_children = len(self.room_node.children)

        # Door creation
        self.door1 = Door(200, 560)
        self.door2 = Door(400, 560)
        self.door3 = Door(600, 560)
        self.return_door = Door(400, 0)

        self.door_list = [self.door1, self.door2, self.door3]

# Fade
    def fade(self): 
        fade = self.pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            self.pygame.time.delay(8)
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0,0))
            self.pygame.display.update()
            self.pygame.time.delay(1)

    # Move to board.py
    def initialize_new_room(self, door_picked):
        self.room_node = self.room_node.children[door_picked-1]
        self.return_door.rect.x = door_picked*200
        self.player.rect.x = door_picked*200
        self.return_door.rect.y = 0
        self.player.rect.y = 80
        self.room = self.room_def[self.room_node.name]
        self.background_raw = self.pygame.image.load(f"Stages/{self.room.sprite}")
        self.BACKGROUND = self.pygame.transform.smoothscale(self.background_raw, (800, 600)) 
        print(self.room_node)
        print(f"num children: {len(list(self.room_node.children))}")
        if len(self.room_node.children) == 1:
            self.door_list = [self.return_door, self.door1]
        if len(self.room_node.children) == 2:
            self.door_list = [self.return_door, self.door1, self.door2]
        if len(self.room_node.children) == 3:
            self.door_list = [self.return_door, self.door1, self.door2, self.door3]
        if len(self.room_node.children) == 0:
            self.door_list = [self.return_door]
        print(self.door_list)

    # Move to board.py
    def return_old_room(self, door_picked):
        self.return_door.rect.x = door_picked*200
        self.player.rect.x = door_picked*200
        self.return_door.rect.y = 0
        self.player.rect.y = 80
        self.room = self.room_def[self.room_node.name]
        self.background_raw = self.pygame.image.load(f"Stages/{self.room.sprite}")
        self.BACKGROUND = self.pygame.transform.smoothscale(self.background_raw, (800, 600)) 
        print(self.room_node)
        print(f"num children: {len(list(self.room_node.children))}")
        if len(self.room_node.children) == 1:
            self.door_list = [self.return_door, self.door1]
        if len(self.room_node.children) == 2:
            self.door_list = [self.return_door, self.door1, self.door2]
        if len(self.room_node.children) == 3:
            self.door_list = [self.return_door, self.door1, self.door2, self.door3]
        if len(self.room_node.children) == 0:
            self.door_list = [self.return_door]
        print(self.door_list)


# Initialize 
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
G = Game(pygame)

# Group Creation
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create Player
player = Player()
all_sprites.add(player)

# Boss creation
boss = Enemy()
all_sprites.add(boss)
counter = 0

# Health Bar
health_bar = HealthBar()

running = True
while running:

    # Exit statement
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.type == QUIT:
                running = False
         # Enemy Projectile
        if event.type == G.ADDENEMY:
            enemy_pro = EnemyProjectile()
            enemies.add(enemy_pro)
            all_sprites.add(enemy_pro)

    # Player Movement
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    player.animation()

    ### Need to refactor
    # Boss Movement
    if counter%10 == 0:
        player_pos = (player.rect.x, player.rect.y)
        boss.update(player_pos)
        boss.check_collision(player, health_bar)
        boss.animation()
    counter += 1

    # Enemy Movement
    enemies.update(player, health_bar)

    """
    # Need to refactor 
    # Check Collision
    if self.pygame.sprite.collide_rect(self.player, self.door1) and self.door1 in self.door_list:
        self.fade()
        self.initialize_new_room(1)
    elif self.pygame.sprite.collide_rect(self.player, self.door2) and self.door2 in self.door_list:
        self.fade()
        self.initialize_new_room(2)
    elif self.pygame.sprite.collide_rect(self.player, self.door3) and self.door3 in self.door_list:
        self.fade()
        self.initialize_new_room(3)
    elif self.pygame.sprite.collide_rect(self.player, self.return_door) and self.return_door in self.door_list:
        self.fade()
        self.room_node = self.room_node.parent
        self.return_old_room(0)

    for door in self.door_list:
        screen.blit(door.surf, door.rect)
    """
            
    # Check Collision with Enemy Projectile
    if player.health <= 0:
        screen.fill((0,0,0))
        running = False

    # Printing things on screen
    screen.blit(G.BACKGROUND, (0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    screen.blit(health_bar.surf, (10,10))

    pygame.display.flip()


