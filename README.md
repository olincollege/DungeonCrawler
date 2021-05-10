# DungeonCrawler
By: Merwan Yeditha and Sushmit Dutta

## The Game
You are Yoshi, and you've been trapped in an underground dungeon. The only
way out is to travel to the end and find the treasure room! Traverse through
the randomly generated map and rooms to find the treasure room, but be careful!
Foes await! On the way, you'll find the Shy Guy, an enemy who always runs towards
you, and the dangerous ghost, who won't move when you look at him, but will run
after you when you look away and can't be killed! 

## Instructions
### Dependencies
To run this game, you must have the following dependencies installed
1. pyGame
2. Anytree
3. Git

To install pygame, type `sudo pip install pygame` into the terminal. To install
Anytree, type `sudo pip install pygame`.

Installing git varies based on the platform you are using. Follow [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) webpage for install instructions.

Next, clone this repository.
To do so, type `git clone https://github.com/olincollege/softdes-2021-01.git` into either terminal
or git bash based on your platform.

### Running the game
After cloning the repository, navigate to it inside of the terminal and enter the pyGame folder.
From inside the pyGame folder, run `python run.py` or `python3 run.py` depending on your system.

To exit the game, enter the command window while it is running and hit `Ctrl + C`.

### Project Website
Find our project website at [this link](https://olincollege.github.io/DungeonCrawler/)

*Note: When running pylint, do so from inside the pyGame directory*

## Model View Controller Architecture
This program follows the MVC architecture. Below is a listing of what category each file falls under
### Model
1. game.py
2. generate_world.py
### View
1. board.py
### Controller
1. controller.py
### Sprites (can be considered model)
1. door.py
2. player.py
3. enemy.py
4. yoshiattack.py
