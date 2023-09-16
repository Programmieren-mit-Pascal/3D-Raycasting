import pygame
import math
pygame.init()

# The world map is represented by a 2D-Array. 
# A one represents a wall-tile and a zero represents a floor tile.
world_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

WIN_WIDTH = 600
WIN_HEIGHT = 600
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Raycaster")
clock = pygame.time.Clock()

FPS = 60
BLOCK_SIZE = WIN_HEIGHT / len(world_map)

# Constants for player movement
MOVE_SPEED = 0.06
ROTATION_SPEED = math.radians(1.7)

# Starting position and direction of player
player_x = 1.5
player_y = 5.2
player_direction = math.radians(350)

# We do not want the player to be on an exact integer position or have a direction of exactly 0.
# Occurrences of these events could result in glitches or division-by-zero errors.
# By adding a little starting offset to the values, we make
# these events extremely unlikely (practically impossible) to occur.
player_x += 0.0000001
player_y += 0.0000001
player_direction += 0.0000001

run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    screen.fill((0, 0, 0))
    
    # Draw 2D world map
    for row in range(len(world_map)):
        for column in range(len(world_map[0])):
            block_x = column * BLOCK_SIZE
            block_y = row * BLOCK_SIZE
            color = (0, 200, 0) if world_map[row][column] == 1 else (200, 200, 200)
            pygame.draw.rect(screen, color, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, (100, 100, 100), (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE), 2)
            
    # Draw player
    player_screen_x = player_x * BLOCK_SIZE
    player_screen_y = player_y * BLOCK_SIZE
    pygame.draw.circle(screen, (255, 0, 0), (player_screen_x, player_screen_y), 6)

    pygame.display.flip()
            
pygame.display.quit()
