from game_setup import *
from player import Player

# Initlise pyGame w/ Display
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Group Creation
doors = pygame.sprite.Group()

# Create player
player = Player()

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


    # Screen fill
    screen.fill(BACKGROUND_COLOR)

    # Creates border
    border = pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(1, 1, 799, 599), width=10)
    left_door = pygame.draw.line(screen, pygame.Color('red'), [0, 250], [0,350], width=15)
    right_door = pygame.draw.line(screen, pygame.Color('red'), [799, 250], [799,350], width=15)
    bottom_door = pygame.draw.line(screen, pygame.Color('red'), [350, 599], [450,599], width=15)

    doors.add(left_door)

    # Check Collision
    player.check_collision(doors)

    screen.blit(player.surf, player.rect)
    pygame.display.flip()
