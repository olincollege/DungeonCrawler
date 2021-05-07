"""
WorldGeneration and Room class.
"""
import random
import os
import cv2, csv, os, statistics
import numpy as np
from anytree import Node, LevelOrderGroupIter
from anytree.exporter import DotExporter
from anytree.search import findall_by_attr

class Room:
    def __init__(self, room_sprite, num_enemies, num_ghosts):
        self.sprite = room_sprite
        self.num_enemies = num_enemies
        self.num_ghosts = num_ghosts

class WorldGeneration:
    """
    Class to randomly generate a tree representing room hierarchy.

    attrs:
        spawn: The top node of the world-generation map.
        obj_list: List of room objects.
    """
    RAND_LEVEL = {
        1: [3],
        2: [3,3,3,3,2,2,1],
        3: [3,3,2,2,2,1,1,0,0],
        4: [2,2,1,1,1,1,0,0,0],
        5: [2,1,0,0,0],
        6: [0]
    }
    # replace this dir with whatever we name the folder that we put backgrounds in
    # If we have time, we sort room backgrounds based on what type of room it is, so
    # then we'd create a dictionary where the key is the room type and value is a list
    # of the names of background images for that type.'
    # SAMPLE LINE: ROOM_SPRITES = os.listdir('assets/backgrounds')
    ROOM_SPRITES = os.listdir('Stages/levels') # Placeholder

    def __init__(self):
        """
        Initializes the tree with spawn room
        """
        self.spawn = Node("Spawn")
        self.obj_dict = {}

    def generate_world(self):
        """
        Runs the initial recursive call and then generates the 'boss' room.
        """
        self.generate_rooms(self.spawn, 1)
        self.generate_end()

    def generate_rooms(self,parent_room, level):
        """
        Recursive function to generate rooms.

        Takes in the parent room and the level of the tree and generates sub-rooms.
        Using the RAND_LEVEL lists, the function chooses a number of 'sub-rooms' and
        generates that number of children nodes to the parent passed. Then, for
        each child node, the function calls itself again. The recursion terminates
        once 6 levels have been reached.

        args:
            parent_room: A string (CHANGE TO NODE OBJECT) representing the parent
            node to generate child nodes for.
            level: An int representing the level of the tree the child nodes will exist on.
        """
        # spawn = self.spawn

        # Finding the number of children based on random frequencies
        num_children = random.choice(self.RAND_LEVEL[level])

        # Generating child rooms
        for i in range(0,num_children):
            next_room = Node(f"{parent_room.name}_{i}", parent=parent_room)
            # Creating object for the room
            self.create_rooms(next_room.name, level)
            # Generating sub-children
            self.generate_rooms(next_room, level + 1)

    def generate_end(self):
        """
        Adds a 'boss' room to the tree.

        Takes the elements of the tree and finds those that are furthest from the
        spawn room (highest level). Then, chooses a random room among those on the
        highest level and makes the boss room a sub-node.
        """
        items = [[node.name for node in children] for children in LevelOrderGroupIter(self.spawn)]
        end_nodes = items[len(items)-1]
        node_name = random.choice(end_nodes)
        node_ref = list(findall_by_attr(self.spawn, node_name))[0]
        Node("Boss Room", parent=node_ref)
        self.obj_dict['Boss Room'] = Room('boss_room/boss.png', 0,0)
        DotExporter(self.spawn).to_picture('game_map.png')

    def create_rooms(self, name, level):
        """
        Instantiates a room object with random parameters for a single item in the
        generated map.
        """
        sprite = random.choice(self.ROOM_SPRITES)
        # DEBUG LINE
        num_enemies = (random.randint(1,3)*level)//2
        num_ghosts = random.randint(1,2)*(level-2)//2
        self.obj_dict[name] = Room(sprite, num_enemies, num_ghosts)

    @property
    def tree(self):
        """
        Accessor for the tree
        """
        return self.spawn

    @property
    def dict(self):
        """
        Accessor for dictionary of room objects
        """
        return self.obj_dict

t = WorldGeneration()
t.generate_world()
