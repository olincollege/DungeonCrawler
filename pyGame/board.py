import random
from game_setup import *
from enemy import *

class Board(pygame.sprite.Sprite):

    def __init__(self, pyGame):
        self.pygame = pyGame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Initialize starting room background
        background_raw = pygame.image.load("Sprites/Background/cloud_background.jpg")
        self.BACKGROUND = pygame.transform.smoothscale(background_raw, (800, 600)) 

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
    def initialize_new_room(self, game, door_picked):
        # Resetting enemies and ghosts that should be displayed
        game.enemy_list = []
        game.ghost_list = []

        # Going to the next node on the tree based on the door the player
        # collides with
        game.room_node = game.room_node.children[door_picked-1]

        # Defining where the return door should be
        game.return_door.rect.x = door_picked*200
        game.return_door.rect.y = 0

        # Defining where the player should be after entering the room
        game.player.rect.x = door_picked*200
        game.player.rect.y = 80

        # Finding the corresponding room object and pulling info
        game.room = game.room_def[game.room_node.name]
        self.background_raw = self.pygame.image.load(f"Stages/{game.room.sprite}")
        self.BACKGROUND = self.pygame.transform.smoothscale(self.background_raw, (800, 600))

        # Creating enemies based on num_enemies
        for i in range(0,game.room.num_enemies):
            # Test to make sure enemy doesn't spawn right where the player enters the door
            if door_picked == 1:
                x_pos = random.randint(50, 500)
            if door_picked == 2:
                x_pos = random.choice([random.randint(50, 300),random.randint(450, 750)])
            if door_picked == 3:
                x_pos = random.randint(250, 750)
            spawn = (x_pos, random.randint(150, 550))
            game.enemy_list.append(ShyGuy(spawn))
        
        for i in range(0, game.room.num_ghosts):
            if door_picked == 1:
                x_pos = random.randint(50, 500)
            if door_picked == 2:
                x_pos = random.choice([random.randint(50, 300),random.randint(450, 750)])
            if door_picked == 3:
                x_pos = random.randint(250, 750)
            spawn = (x_pos, random.randint(150, 550))
            game.ghost_list.append(Ghost(spawn))

        # Statement to make sure we're in the right room
        print(game.room_node)
        print(f"num children: {len(list(game.room_node.children))}")
        print(game.enemy_list)
        print(game.ghost_list)

        # Creating doors based on the number of children a room has in the tree
        if len(game.room_node.children) == 1:
            game.door_list = [game.return_door, game.door1]
        if len(game.room_node.children) == 2:
            game.door_list = [game.return_door, game.door1, game.door2]
        if len(game.room_node.children) == 3:
            game.door_list = [game.return_door, game.door1, game.door2, game.door3]
        if len(game.room_node.children) == 0:
            game.door_list = [game.return_door]
        print(game.door_list)

    def return_old_room(self, game):

        # Defining player position after returning to previous room.
        # Y is constant x depends on the position of the return door
        game.player.rect.x = game.return_door.rect.x
        game.player.rect.y = 500

        # Defining where the previous room's return door should be.
        # Will be based on the name of the room
        name = game.room_node.name
        if name != "Spawn":
            game.return_door.rect.x = (int(name[len(name)-1:len(name)])+1)*200
        else: 
            game.return_door.rect.x = 10000
        
        game.return_door.rect.y = 0
        
        game.room = game.room_def[game.room_node.name]
        self.background_raw = self.pygame.image.load(f"Stages/{game.room.sprite}")
        self.BACKGROUND = self.pygame.transform.smoothscale(self.background_raw, (800, 600)) 
        print(game.room_node)
        print(f"num children: {len(list(game.room_node.children))}")
        if len(game.room_node.children) == 1:
            game.door_list = [game.return_door, game.door1]
        if len(game.room_node.children) == 2:
            game.door_list = [game.return_door, game.door1, game.door2]
        if len(game.room_node.children) == 3:
            game.door_list = [game.return_door, game.door1, game.door2, game.door3]
        if len(game.room_node.children) == 0:
            game.door_list = [game.return_door]
        if game.room_node.name == 'Spawn':
            game.door_list.remove(game.return_door)
        print(game.door_list)

    def draw_objects(self, game):
        self.screen.blit(self.BACKGROUND, (0,0))
        for entity in game.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        self.screen.blit(game.health_bar.surf, (10,10))
        for door in game.door_list:
            self.screen.blit(door.surf, door.rect)

        for enemy in game.enemy_list:
            self.screen.blit(enemy.surf, enemy.rect)
        for ghost in game.ghost_list:
            self.screen.blit(ghost.surf, ghost.rect)

        if game.player.attack:
            self.screen.blit(game.attack.surf, game.attack.rect)
        self.pygame.display.flip()