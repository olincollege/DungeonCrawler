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

        # Create Board
        self.board = Board(pygame)
        # Timer for Enemy Projectile
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000)

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

        self.enemy_list = []
        self.ghost_list = []
        self.projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Create Player
        self.player = Player()
        self.all_sprites.add(self.player)
        self.controller = Controller(self.player)

        # Health Bar
        self.health_bar = HealthBar()


    def run(self):
        running = True
        counter = 0
        while running:
            # Exit statement
            for event in self.board.pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.type == QUIT:
                        running = False
                # Enemy Projectile
                if event.type == g.ADDENEMY:
                    enemy_pro = EnemyProjectile()
                    self.projectiles.add(enemy_pro)
                    self.all_sprites.add(enemy_pro)

            # Player Movement
            pressed_keys = self.board.pygame.key.get_pressed()
            self.controller.move_player(pressed_keys)
            self.player.animation()
            self.player.check_invincibility()
            self.player.animate_invincibility()

            ### Need to refactor
            # Enemy Movement
            player_pos = (self.player.rect.x, self.player.rect.y)
            if counter%10 == 0:
                player_pos = (self.player.rect.x, self.player.rect.y)
                for enemy in self.enemy_list:
                    enemy.update(player_pos)
                    enemy.check_collision(self.player, self.health_bar)
                    enemy.animation()
            if counter%20 == 0:
                for ghost in self.ghost_list:
                    ghost.update(player_pos, self.player.direction_check)
                    ghost.check_collision(self.player, self.health_bar)
                    ghost.animation()
            counter += 1

            # Enemy Movement
            self.projectiles.update(self.player, self.health_bar)


            # Check Collision
            if self.board.pygame.sprite.collide_rect(self.player, self.door1) and self.door1 in self.door_list:
                self.board.fade()
                self.board.initialize_new_room(self,1)
            elif pygame.sprite.collide_rect(g.player, g.door2) and self.door2 in self.door_list:
                self.board.fade()
                self.board.initialize_new_room(self,2)
            elif self.board.pygame.sprite.collide_rect(self.player, self.door3) and self.door3 in self.door_list:
                self.board.fade()
                self.board.initialize_new_room(self,3)
            elif self.board.pygame.sprite.collide_rect(self.player, self.return_door) and self.return_door in self.door_list:
                self.board.fade()
                self.room_node = self.room_node.parent
                self.board.return_old_room(self,0)

            for door in self.door_list:
                self.board.screen.blit(door.surf, door.rect)
                    
            # Check Collision with Enemy Projectile
            if self.player.health <= 0:
                self.board.screen.fill((0,0,0))
                running = False

            # Printing things on screen
            self.board.draw_objects(self)









# Initialize 

g = Game(pygame)
g.run()

# Group Creation



