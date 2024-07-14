import pygame
import random
from pygame.math import Vector3

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_pos = Vector3(1.5, 1.5, 0)
player_angle = 0

# Maze settings
maze_size = 10
maze = [[1 for _ in range(maze_size)] for _ in range(maze_size)]

# Generate maze (simple random maze)
for i in range(1, maze_size - 1):
    for j in range(1, maze_size - 1):
        if random.random() > 0.3:
            maze[i][j] = 0

# Set start and end points
maze[1][1] = 0
maze[maze_size - 2][maze_size - 2] = 0

# Raycasting settings
FOV = 60
num_rays = width // 2

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 0.1
    if keys[pygame.K_RIGHT]:
        player_angle += 0.1
    if keys[pygame.K_UP]:
        new_pos = player_pos + Vector3(0.1, 0, 0).rotate_z(player_angle)
        if maze[int(new_pos.x)][int(new_pos.y)] == 0:
            player_pos = new_pos
    if keys[pygame.K_DOWN]:
        new_pos = player_pos - Vector3(0.1, 0, 0).rotate_z(player_angle)
        if maze[int(new_pos.x)][int(new_pos.y)] == 0:
            player_pos = new_pos

    # Clear the screen
    display.fill(BLACK)

    # Raycasting
    for x in range(num_rays):
        ray_angle = player_angle - FOV / 2 + FOV * x / num_rays
        ray_dir = Vector3(1, 0, 0).rotate_z(ray_angle)
        
        distance = 0
        hit_wall = False
        
        while not hit_wall and distance < 20:
            distance += 0.1
            test_point = player_pos + ray_dir * distance
            test_x, test_y = int(test_point.x), int(test_point.y)
            
            if test_x < 0 or test_x >= maze_size or test_y < 0 or test_y >= maze_size:
                hit_wall = True
                distance = 20
            elif maze[test_x][test_y] == 1:
                hit_wall = True

        # Calculate wall height
        wall_height = min(height, height / distance)
        
        # Draw wall slice
        pygame.draw.line(display, WHITE, (x * 2, (height - wall_height) / 2),
                         (x * 2, (height + wall_height) / 2), 2)

    # Draw player position on 2D map
    map_scale = 5
    for y in range(maze_size):
        for x in range(maze_size):
            if maze[x][y] == 1:
                pygame.draw.rect(display, WHITE, (x * map_scale, y * map_scale, map_scale - 1, map_scale - 1))
    
    pygame.draw.circle(display, RED, (int(player_pos.x * map_scale), int(player_pos.y * map_scale)), 2)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
