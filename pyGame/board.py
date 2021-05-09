"""
File containing the Board Viewer class.
"""
import random
import pygame

from enemy import (
    ShyGuy,
    Ghost
)

from pygame.locals import RLEACCEL

class Board(pygame.sprite.Sprite):
    """
    Viewer class for the Dungeon Crawler game

    attrs:
        pygame: Instance of pygame
        screen: Pygame screen object, defines the actual window
        background: Pygame background image
    """
    def __init__(self, pygame):
        """
        Initializes the Board class

        args:
            pyGame: Instance of pygame
        """
        self.pygame = pygame
        pygame.init()

        # Initialize starting room background
        background_raw = pygame.image.load("Stages/spawn/spawn.png")
        self.background = pygame.transform.smoothscale(background_raw, (800, 600))
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def fade(self):
        """
        Creates a fade to black effect when switching rooms
        """
        fade = self.pygame.Surface((self.screen_width, self.screen_height))
        fade.fill((0,0,0))
        for alpha in range(0, 100):
            self.pygame.time.delay(8)
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0,0))
            self.pygame.display.update()
            self.pygame.time.delay(1)

    # Move to board.py
    def initialize_new_room(self, game, door_picked):
        """
        Sets up new rooms

        When the player hits a door, this function sets up a new room
        based on the door chosen. This involves updating the game class'
        definition of the current room node, updating the player position
        in the new room based on the door entered, and adding the relevant
        enemies and doors to the game lists based on the data given by the
        Room object.

        args:
            game: Instance of the game object
            door_picked: The number that the door was hit.
        """
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
        if game.room_node.name == "Boss Room":
            self.background_raw = self.pygame.image.load("Stages/boss/stage_6.png")
        else:
            self.background_raw = self.pygame.image.load(f"Stages/levels/{game.room.sprite}")
        self.background = self.pygame.transform.smoothscale(self.background_raw, (800, 600))

        # Creating enemies based on num_enemies
        for _ in range(0,game.room.num_enemies):
            # Test to make sure enemy doesn't spawn right where the player enters the door
            if door_picked == 1:
                x_pos = random.randint(50, 500)
            elif door_picked == 2:
                x_pos = random.choice([random.randint(50, 300),random.randint(450, 750)])
            else:
                x_pos = random.randint(250, 750)
            spawn = (x_pos, random.randint(150, 550))
            game.enemy_list.append(ShyGuy(spawn, self))

        for _ in range(0, game.room.num_ghosts):
            if door_picked == 1:
                x_pos = random.randint(50, 500)
            elif door_picked == 2:
                x_pos = random.choice([random.randint(50, 300),random.randint(450, 750)])
            else:
                x_pos = random.randint(250, 750)
            spawn = (x_pos, random.randint(150, 550))
            game.ghost_list.append(Ghost(spawn, self))

        # Creating doors based on the number of children a room has in the tree
        if len(game.room_node.children) == 1:
            game.door_list = [game.return_door, game.door1]
        elif len(game.room_node.children) == 2:
            game.door_list = [game.return_door, game.door1, game.door2]
        elif len(game.room_node.children) == 3:
            game.door_list = [game.return_door, game.door1, game.door2, game.door3]
        else:
            game.door_list = [game.return_door]

    def return_old_room(self, game):
        """
        Sets up old room when the player hits the return door.

        Very similar behavior to the initialize_new_room function,
        but does not edit the game node variable.

        attrs:
            game: Instance of the Game class
        """
        # Resetting enemies and ghosts that should be displayed
        game.enemy_list = []
        game.ghost_list = []

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
        game.room = game.room_def[game.room_node.name]
        for _ in range(0,game.room.num_enemies):
            # Test to make sure enemy doesn't spawn right where the player enters the door
            spawn = (random.randint(100, 500), random.randint(200, 500))
            game.enemy_list.append(ShyGuy(spawn, self))

        for i in range(0, game.room.num_ghosts):
            spawn = (random.randint(100, 500), random.randint(150, 550))
            game.ghost_list.append(Ghost(spawn, self))

        game.return_door.rect.y = 0

        game.room = game.room_def[game.room_node.name]
        if name == "Spawn":
            self.background_raw = self.pygame.image.load("Stages/spawn/spawn.png")
        else:
            self.background_raw = self.pygame.image.load(f"Stages/levels/{game.room.sprite}")

        self.background = self.pygame.transform.smoothscale(self.background_raw, (800, 600))
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

    def draw_objects(self, game):
        """
        Draws all of the required sprites on screen.

        game: Instance of the Game class
        """
        self.screen.blit(self.background, (0,0))

        # Drawing projectiles as they are generated
        for entity in game.projectiles:
            self.screen.blit(entity.surf, entity.rect)

        self.screen.blit(game.player.surf, game.player.rect)
        self.screen.blit(game.health_bar.surf, (10,10))

        # Drawing only doors that the room contains
        for door in game.door_list:
            self.screen.blit(door.surf, door.rect)

        # Drawing only enemies that the room contains
        for enemy in game.enemy_list:
            self.screen.blit(enemy.surf, enemy.rect)
        for ghost in game.ghost_list:
            self.screen.blit(ghost.surf, ghost.rect)

        # Drawing the attack sprite at the right time
        if game.player.attack:
            self.screen.blit(game.attack.surf, game.attack.rect)
        self.pygame.display.flip()
