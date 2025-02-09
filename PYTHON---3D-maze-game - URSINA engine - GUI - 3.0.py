from ursina import *

# Initialize Ursina
app = Ursina()

# Game variables
player_speed = 3
player_color = color.orange

# --- SETTINGS MENU ---
def start_game():
    global player, walls
    
    # Hide settings UI
    menu.visible = False

    # Maze grid (1 = wall, 0 = path)
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    # Create walls based on the maze grid
    walls = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                walls.append(Entity(model="cube", color=color.gray, scale=(1,1,1), position=(x,0,y)))
    
    # Create player
    global player
    player = Entity(model="cube", color=player_color, position=(1, 0, 1), scale=(0.8, 0.8, 0.8))

# --- UPDATE PLAYER MOVEMENT ---
def update():
    global player_speed
    speed = player_speed * time.dt
    if held_keys['w']: player.z -= speed
    if held_keys['s']: player.z += speed
    if held_keys['a']: player.x -= speed
    if held_keys['d']: player.x += speed

# --- GUI ELEMENTS ---
menu = Entity(parent=camera.ui)  # UI container

# Title
Text("3D Maze Game", scale=2, y=0.3, parent=menu)

# Speed slider
speed_label = Text("Speed: 3", scale=1.5, y=0.15, parent=menu)
speed_slider = Slider(min=1, max=10, default=3, step=0.5, y=0.1, parent=menu)
def change_speed():
    global player_speed
    player_speed = speed_slider.value
    speed_label.text = f"Speed: {round(player_speed,1)}"
speed_slider.on_value_changed = change_speed

# Color selection buttons
def change_color(new_color):
    global player_color
    player_color = new_color
color_label = Text("Select Player Color:", scale=1.5, y=0, parent=menu)
color_buttons = [
    Button(text="Red", color=color.red, position=(-0.3, -0.05), scale=(0.2,0.1), parent=menu, on_click=lambda: change_color(color.red)),
    Button(text="Green", color=color.green, position=(0, -0.05), scale=(0.2,0.1), parent=menu, on_click=lambda: change_color(color.green)),
    Button(text="Blue", color=color.blue, position=(0.3, -0.05), scale=(0.2,0.1), parent=menu, on_click=lambda: change_color(color.blue))
]

# Start button
start_button = Button(text="Start Game", scale=(0.4,0.1), y=-0.2, parent=menu, on_click=start_game)

# Run the game
app.run()
