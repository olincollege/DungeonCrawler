from game_setup import *
from player import Player
from enemy import Enemy
from board import Board

# Initlise pyGame w/ Display
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Group Creation
doors = pygame.sprite.Group()

# Create player
player = Player()

# Enemy creation
enemy = Enemy()
counter = 0

# Door creation
door = Board(200, 560)
door1 = Board(400, 560)
door2 = Board(600, 560)
doors.add(door)
doors.add(door1)
doors.add(door2)

# Fade
def fade(): 
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        pygame.time.delay(8)
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.type == QUIT:
                running = False

    # Movement
    pressed_keys = pygame.key.get_pressed()
    player.move(pressed_keys)
    player.animation()

    # Enemy Movement
    if counter%10 == 0:
        player_pos = (player.rect.x, player.rect.y)
        enemy.move(player_pos)
        enemy.animation()
    counter += 1

    # Screen fill
    screen.blit(BACKGROUND, (0,0))

    # Creates border
    border = pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(1, 1, 799, 599), width=20)

    # Check Collision
    if player.check_collision(doors):
        fade()

    screen.blit(player.surf, player.rect)
    screen.blit(enemy.surf, enemy.rect)
    screen.blit(door.surf, door.rect)
    screen.blit(door1.surf, door1.rect)
    screen.blit(door2.surf, door2.rect)
    pygame.display.flip()


