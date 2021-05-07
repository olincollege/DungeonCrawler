from game_setup import *
from player import Player, HealthBar
from enemy import Enemy, EnemyProjectile
from board import Board
from door import Door
from controller import Controller
from yoshiattack import YoshiAttack
from generate_world import WorldGeneration, Room
import pygame

class Game():
    """ 
    Main model class to run the Dungeon Crawler.

    attrs:
        board: Instance of the board class
        ADDENEMY: pygame event to show when to add a projectile
        wgen: Instance of WorldGeneration class
        tree: Generated tree from the WorldGeneration class
        room_def: Dictionary mapping tree node names to room objects
        room_node: Node of the tree that the player is in
        room: Room object that the player is currently in
        door1: Far left door sprite
        door2: Middle door sprite
        door3: Far right door sprite
        return_door: Door that leads to the previous room
        door_list: List of doors that should be rendered
        enemy_list: List of Shy_Guy enemies that should be rendered
        ghost_list: List of ghost enemies that should be rendered
        projectiles: PyGame sprite group containing all projectiles.
    """
    def __init__(self,pyGame):
        """
        Initializes the Game class.

        attrs:
            pyGame: The pyGame library
        """
        # Create Board
        self.board = Board(pygame)
        # Timer for Enemy Projectile
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 4000)

        self.wgen = WorldGeneration()
        self.wgen.generate_world()
        self.tree = self.wgen.tree
        self.room_def = self.wgen.dict
        self.room_node = self.tree
        self.room_def['Spawn'] = Room('cloud_background.jpg', 0, 0)
        self.room = self.room_def['Spawn']

        # Door creation
        self.door1 = Door(200, 560)
        self.door2 = Door(400, 560)
        self.door3 = Door(600, 560)
        self.return_door = Door(400, 0)

        self.door_list = [self.door1, self.door2, self.door3]

        self.enemy_list = []
        self.ghost_list = []
        self.projectiles = pygame.sprite.Group()

        # Create Player
        self.player = Player()
        self.controller = Controller(self.player)

        # Attack Sprite
        self.attack = YoshiAttack(self.player)

        # Health Bar
        self.health_bar = HealthBar()

    @property
    def num_children(self):
        """
        Property representing the number of children a certain node has.
        """
        self.num_children = len(self.room_node.children)

    def run(self):
        """
        Method to run the game.

        Runs a while loop to run all checks and processes necessary for the
        game to run.
        """
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

            # Player Movement
            pressed_keys = self.board.pygame.key.get_pressed()
            self.controller.move_player(pressed_keys)
            self.controller.attack(pressed_keys)
            self.player.animation()
            self.player.check_invincibility()
            self.player.animate_invincibility()
            self.attack.animate()

            ### Need to refactor
            # Enemy Movement
            player_pos = (self.player.rect.x, self.player.rect.y)
            if counter%10 == 0:
                player_pos = (self.player.rect.x, self.player.rect.y)
                for enemy in self.enemy_list:
                    enemy.update(player_pos)
                    enemy.check_collision(self.player, self.health_bar)
                    enemy.enemy_hit(self.attack, self.player.attack)
                    enemy.animation()
                    enemy.hit_animation()
                    if enemy.health == 0:
                        self.enemy_list.remove(enemy)
            if counter%5 == 0:
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
                self.projectiles.empty()
            elif pygame.sprite.collide_rect(g.player, g.door2) and self.door2 in self.door_list:
                self.board.fade()
                self.board.initialize_new_room(self,2)
                self.projectiles.empty()
            elif self.board.pygame.sprite.collide_rect(self.player, self.door3) and self.door3 in self.door_list:
                self.board.fade()
                self.board.initialize_new_room(self,3)
                self.projectiles.empty()
            elif self.board.pygame.sprite.collide_rect(self.player, self.return_door) and self.return_door in self.door_list:
                self.board.fade()
                self.room_node = self.room_node.parent
                self.board.return_old_room(self)
                self.projectiles.empty()

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



