from game_setup import *
from player import Player, HealthBar
from enemy import Enemy, EnemyProjectile
from board import Board
from door import Door
from controller import Controller
from generate_world import WorldGeneration, Room
import pygame

class Game():

    def __init__(self,pyGame):
        self.pygame = pyGame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Initialize starting room background
        background_raw = pygame.image.load("Sprites/Background/cloud_background.jpg")
        self.BACKGROUND = pygame.transform.smoothscale(background_raw, (800, 600)) 

        # Create Board
        self.board = Board(0,0)
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

        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Create Player
        self.player = Player()
        self.all_sprites.add(self.player)
        self.controller = Controller(self.player)
        # Boss creation
        self.boss = Enemy()
        self.all_sprites.add(self.boss)

        # Health Bar
        self.health_bar = HealthBar()


    def run(self):
        running = True
        counter = 0
        while running:
            # Exit statement
            for event in self.pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.type == QUIT:
                        running = False
                # Enemy Projectile
                if event.type == g.ADDENEMY:
                    enemy_pro = EnemyProjectile()
                    self.enemies.add(enemy_pro)
                    self.all_sprites.add(enemy_pro)

            # Player Movement
            pressed_keys = self.pygame.key.get_pressed()
            self.controller.move_player(pressed_keys)
            self.player.animation()
            self.player.check_invincibility()
            self.player.animate_invincibility()

            ### Need to refactor
            # Boss Movement
            if counter%10 == 0:
                player_pos = (self.player.rect.x, self.player.rect.y)
                self.boss.update(player_pos)
                self.boss.check_collision(self.player, self.health_bar)
                self.boss.animation()
            counter += 1

            # Enemy Movement
            self.enemies.update(self.player, self.health_bar)


            # Check Collision
            if self.pygame.sprite.collide_rect(self.player, self.door1) and self.door1 in self.door_list:
                self.board.fade(self)
                self.board.initialize_new_room(self,1)
            elif pygame.sprite.collide_rect(g.player, g.door2) and self.door2 in self.door_list:
                self.board.fade(self)
                self.board.initialize_new_room(self,2)
            elif self.pygame.sprite.collide_rect(self.player, self.door3) and self.door3 in self.door_list:
                self.board.fade(self)
                self.board.initialize_new_room(self,3)
            elif g.pygame.sprite.collide_rect(self.player, self.return_door) and self.return_door in self.door_list:
                self.board.fade(self)
                self.room_node = self.room_node.parent
                self.board.return_old_room(self,0)

            for door in self.door_list:
                self.screen.blit(door.surf, door.rect)
                    
            # Check Collision with Enemy Projectile
            if self.player.health <= 0:
                self.screen.fill((0,0,0))
                running = False

            # Printing things on screen
            self.screen.blit(g.BACKGROUND, (0,0))
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)
            self.screen.blit(self.health_bar.surf, (10,10))
            for door in self.door_list:
                self.screen.blit(door.surf, door.rect)
            self.pygame.display.flip()










# Initialize 

g = Game(pygame)
g.run()

# Group Creation



