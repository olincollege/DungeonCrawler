from game_setup import *
from player import Player

# Initlise pyGame w/ Display
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    screen.blit(player.surf, player.rect)
    pygame.display.flip()