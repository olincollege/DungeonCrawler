from game_setup import *

class Board(pygame.sprite.Sprite):


    def __init__(self, x_cord, y_cord):
        super(Board, self).__init__()
        look_initial = pygame.image.load("Sprites/Door/bottom_door.png").convert()
        self.surf = pygame.transform.smoothscale(look_initial, (40, 40)) 
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord

    def fade(self, game): 
        fade = game.pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            game.pygame.time.delay(8)
            fade.set_alpha(alpha)
            game.screen.blit(fade, (0,0))
            game.pygame.display.update()
            game.pygame.time.delay(1)

    # Move to board.py
    def initialize_new_room(self, game, door_picked):
        game.room_node = game.room_node.children[door_picked-1]
        game.return_door.rect.x = door_picked*200
        game.player.rect.x = door_picked*200
        game.return_door.rect.y = 0
        game.player.rect.y = 80
        game.room = game.room_def[game.room_node.name]
        game.background_raw = game.pygame.image.load(f"Stages/{game.room.sprite}")
        game.BACKGROUND = game.pygame.transform.smoothscale(game.background_raw, (800, 600)) 
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
        print(game.door_list)

    # Move to board.py
    def return_old_room(self, game, door_picked):
        game.return_door.rect.x = door_picked*200
        game.player.rect.x = door_picked*200
        game.return_door.rect.y = 0
        game.player.rect.y = 80
        game.room = game.room_def[game.room_node.name]
        game.background_raw = game.pygame.image.load(f"Stages/{game.room.sprite}")
        game.BACKGROUND = game.pygame.transform.smoothscale(game.background_raw, (800, 600)) 
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
        print(game.door_list)