from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a simple maze layout
maze = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1],
    [1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]

# Create wall and floor textures
wall_texture = load_texture('brick')
floor_texture = load_texture('grass')

# Create walls and floor
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            wall = Entity(model='cube', texture=wall_texture,
                          position=(j,0.5,i), scale=(1,1,1), collider='box')
        else:
            floor = Entity(model='plane', texture=floor_texture,
                           position=(j,0,i), scale=(1,1), collider='mesh')

# Create player
player = FirstPersonController(position=(1,1,1), speed=3)

# Run the game
app.run()
