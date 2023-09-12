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

WIN_WIDTH = 800
WIN_HEIGHT = 600
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Raycaster")
clock = pygame.time.Clock()

FPS = 60

# Constants for raycasting
LINE_WIDTH = 2
NUMBER_OF_RAYS = int(WIN_WIDTH / LINE_WIDTH) + 1
FIELD_OF_VIEW = math.radians(60)
ANGLE_BETWEEN_RAYS = FIELD_OF_VIEW / (NUMBER_OF_RAYS + 1)
WALL_SIZE = WIN_HEIGHT * 1.1

MAX_BRIGHTNESS = 200
DIM_FACTOR = -10

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
     
    # Draw background
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 50), (0, 0, WIN_WIDTH, WIN_HEIGHT / 2))
    pygame.draw.rect(screen, (65, 40, 20), (0, WIN_HEIGHT / 2, WIN_WIDTH, WIN_HEIGHT / 2))
    
    # Get user input
    keys = pygame.key.get_pressed()
    
    # Move forwards
    if keys[pygame.K_UP]:
        new_x = player_x + MOVE_SPEED * math.cos(player_direction)
        if world_map[int(player_y)][int(new_x)] == 0:
            player_x = new_x
        new_y = player_y - MOVE_SPEED * math.sin(player_direction)
        if world_map[int(new_y)][int(player_x)] == 0:
            player_y = new_y
    
    # Move backwards
    if keys[pygame.K_DOWN]:
        new_x = player_x - MOVE_SPEED * math.cos(player_direction)
        if world_map[int(player_y)][int(new_x)] == 0:
            player_x = new_x
        new_y = player_y + MOVE_SPEED * math.sin(player_direction)
        if world_map[int(new_y)][int(player_x)] == 0:
            player_y = new_y
                
    # Spin right
    if keys[pygame.K_RIGHT]:
        player_direction -= ROTATION_SPEED
        player_direction %= 2 * math.pi
    
    # Spin left
    if keys[pygame.K_LEFT]:
        player_direction += ROTATION_SPEED
        player_direction %= 2 * math.pi
        
    # The y-position relative to the cell the player is in. (Between 0 and 1)
    cell_y = player_y - math.floor(player_y)
    
    # Set values to calculate the first ray.
    ray_direction = player_direction + FIELD_OF_VIEW / 2
    ray_direction %= 2 * math.pi
    line_screen_x = 0
    
    # Repeat for every ray
    for i in range(NUMBER_OF_RAYS):
        
        # Cell in which the ray is currently in.
        ray_block_column = int(player_x)
        ray_block_row = int(player_y)
        
        ray_direction_degrees = math.degrees(ray_direction)

        if ray_direction_degrees > 0 and ray_direction_degrees < 180: 
            # Ray points up.
            next_horizontal_intersection_x = player_x + cell_y / math.tan(ray_direction)
            delta_x = 1 / math.tan(ray_direction)
            ray_row_movement = -1
        else: 
            # Ray point down.
            next_horizontal_intersection_x = player_x - (1 - cell_y) / math.tan(ray_direction)
            delta_x = -1 / math.tan(ray_direction)
            ray_row_movement = 1
            
        if ray_direction_degrees > 270 or ray_direction_degrees < 90:
            # Ray also point right.
            next_vertical_intersection_x = math.ceil(player_x) 
            ray_column_movement = 1
        else:
            # Ray also point left.
            next_vertical_intersection_x = math.floor(player_x) 
            ray_column_movement = -1
        
        # Send out the ray until it hits a wall.
        # Calculate the x-coordinates of the rays intersections with the grid.
        while True:
            
            distance_horizontal_intersection = abs(player_x - next_horizontal_intersection_x)
            distance_vertical_intersection = abs(player_x - next_vertical_intersection_x)
            
            if distance_horizontal_intersection < distance_vertical_intersection:
                cur_intersection_x = next_horizontal_intersection_x
                next_horizontal_intersection_x += delta_x
                ray_block_row += ray_row_movement
                shadow = False
            else:
                cur_intersection_x = next_vertical_intersection_x
                next_vertical_intersection_x += ray_column_movement
                ray_block_column += ray_column_movement
                shadow = True
            
            # End the loop if the ray hits a wall.
            if world_map[ray_block_row][ray_block_column]:
                break
        
        # Length of ray
        raw_distance = (cur_intersection_x - player_x) / math.cos(ray_direction)
        distance_without_fisheye = raw_distance * math.cos(ray_direction - player_direction)
                
        # Vertical line on screen
        line_height = WALL_SIZE / distance_without_fisheye
        line_start = (WIN_HEIGHT / 2) - (line_height / 2)
        line_start = max(line_start, 0) # Make sure line_start is not smaller than 0.
        line_end = (WIN_HEIGHT / 2) + (line_height / 2)
        line_end = min(line_end, WIN_HEIGHT) # Make sure line_end is not bigger than WIN_HEIGHT.
        
        # Brightness / color of line (walls that are further away are darker.)
        brightness = int(DIM_FACTOR * distance_without_fisheye + MAX_BRIGHTNESS)
        brightness = max(0, brightness) # Make sure brightness is not smaller than 0.
        if shadow: brightness //= 2
        color = (0, brightness, 0)
        
        # Draw line
        pygame.draw.line(screen, color, (line_screen_x, line_start), (line_screen_x, line_end), LINE_WIDTH)
        
        # Set values to calculate the next ray.
        ray_direction -= ANGLE_BETWEEN_RAYS
        ray_direction %= 2 * math.pi
        line_screen_x += LINE_WIDTH
    
    pygame.display.flip()
            
pygame.display.quit()
