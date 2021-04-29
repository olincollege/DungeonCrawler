from game_setup import *
from player import Player
from enemy import Enemy
from board import Board
from door import Door
from generate_world import WorldGeneration, Room

class Game():

    def __init__(self, pygame):
# Initlise pyGame w/ Display
        self.pygame = pygame
        self.pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

        # Initialize starting room background
        self.background_raw = self.pygame.image.load("Sprites/Background/cloud_background.jpg")
        self.BACKGROUND = self.pygame.transform.smoothscale(self.background_raw, (800, 600)) 


        # Create self.player
        self.player = Player()

        # Enemy creation
        self.enemy = Enemy()
        self.counter = 0

        # Door creation
        self.door1 = Door(200, 560)
        self.door2 = Door(400, 560)
        self.door3 = Door(600, 560)
        self.return_door = Door(400, 0)

        self.door_list = [self.door1, self.door2, self.door3]
        self.run_game()

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

    def run_game(self):

        counter = 0
        running = True
        while running:

            for event in self.pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.type == QUIT:
                        running = False

            # Movement
            pressed_keys = self.pygame.key.get_pressed()
            self.player.move(pressed_keys)
            self.player.animation()

            # Enemy Movement
            if counter%10 == 0:
                self.player_pos = (self.player.rect.x, self.player.rect.y)
                self.enemy.move(self.player_pos)
                self.enemy.animation()
            counter += 1

            # Screen fill
            self.screen.blit(self.BACKGROUND, (0,0))

            # Creates border
            border = self.pygame.draw.rect(self.screen, self.pygame.Color('black'), self.pygame.Rect(1, 1, 799, 599), width=20)

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
                self.screen.blit(door.surf, door.rect)
            self.screen.blit(self.player.surf, self.player.rect)
            self.screen.blit(self.enemy.surf, self.enemy.rect)
            self.pygame.display.flip()


