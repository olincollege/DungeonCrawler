import pytest
import pygame
#from game import Game
from anytree import Node, LevelOrderGroupIter
from anytree.search import findall_by_attr
from generate_world import WorldGeneration

w = WorldGeneration()
w.generate_world()

# Tests for tree
num_levels = len([[node.name for node in children] for children in LevelOrderGroupIter(w.tree)])

@pytest.mark.parametrize("actual, expected", [
    # Test that the tree has at most 7 levels
    (num_levels, 7)])

def test_levels(actual, expected):
    assert actual <= expected

boss_room = findall_by_attr(w.tree, 'Boss Room')[0]
parent = boss_room.parent.name

@pytest.mark.parametrize("actual, expected", [
    # Test that the boss room has no children
    (len(boss_room.children),
    0),
    # Test that the boss room is on the last level
    # This is based on the fact that node names are based on their level
    (len(parent), 5+(num_levels-2)*2)])

def test_tree(actual, expected):
    assert actual == expected

from game import Game
g = Game(pygame)
# g.QUIT()

# Tests for game state and ability to traverse the tree in game
g = Game(pygame)
g.board.initialize_new_room(g, 1)
name = g.room_node.name

# Test that the first door leads to the child room with name 0
@pytest.mark.parametrize("actual, expected", [
    (name[len(name)-1:len(name)], '0')
    ])

def test_room_one(actual, expected):
    assert actual == expected

# Resetting to original room
g.room_node = g.tree
g.board.initialize_new_room(g, 2)
name = g.room_node.name

# Test that the second door leads to the child room with name 1
@pytest.mark.parametrize("actual, expected", [
    (name[len(name)-1:len(name)], '1')
    ])

def test_room_two(actual, expected):
    assert actual == expected

# Resetting to original room
g.room_node = g.tree
g.board.initialize_new_room(g, 3)
name = g.room_node.name

# Test that the third door leads to the child room with name 2
@pytest.mark.parametrize("actual, expected", [
    (name[len(name)-1:len(name)], '2')
    ])

def test_room_three(actual, expected):
    assert actual == expected

# Test that when the player is hit, they are invincible for a
# short period and their health is lowered.
g.player.player_hit(g.health_bar)

@pytest.mark.parametrize("actual, expected", [
    (g.player.health, 4),
    (g.player.hittable, False)
    ])

def test_player_hit(actual, expected):
    actual == expected
