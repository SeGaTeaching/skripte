cimport tkinter as tk
from random import randint, choice

# Hauptfenster
root = tk.Tk()
root.title('Snake Game')
root.resizable(False, False)

# Variablen
DIRECTION = 'Right'
SPEED = None
SCORE = 0

# Canvas erstellen
canvas = tk.Canvas(root, width=600, height=400, bg='darkgreen')
canvas.pack()

# Globale Variablen für Schlange und Food
snake_positions = []
snake_segments = []
food = None
food_position = None
# start_button = None
# restart_button = None
# quit_button = None
button_frame = None
skill = tk.IntVar(value=500)

# Schlange initialisieren
def create_snake():
    global snake_positions, snake_segments
    snake_positions = [(100, 100), (80, 100), (60, 100)]
    snake_segments.clear()

    # Schlange zeichnen
    for x, y in snake_positions:
        segment = canvas.create_rectangle(x, y, x + 20, y + 20, fill='#2F4F4F')
        snake_segments.append(segment)

# Funktion für Futter, welches zufällig auf dem Canvas platziert wird
def create_food():
    global food, food_position
    while True:
        x = randint(0, 29) * 20
        y = randint(0, 19) * 20
        if (x, y) not in snake_positions:
            break
    food, food_position = (canvas.create_oval(x, y, x + 20, y + 20, fill='#2F4F4F'), (x, y))

# Schlange in Bewegung setzen
def move_snake():
    global food, food_position, SPEED, SCORE, DIRECTION
    
    # Neue Position für den Kopf
    head_x, head_y = snake_positions[0]
    if DIRECTION == 'Right':
        new_head = (head_x + 20, head_y)
    elif DIRECTION == 'Left':
        new_head = (head_x - 20, head_y)
    elif DIRECTION == 'Down':
        new_head = (head_x, head_y +20)
    elif DIRECTION == 'Up':
        new_head = (head_x, head_y - 20)
    
    # Kollision mit Futter
    if new_head == food_position:
        SCORE += 1
        snake_positions.insert(0, new_head) # Neuer Kopf
        canvas.delete(food) # Entfernen des Foods
        create_food()
        segment = canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + 20, new_head[1] + 20, fill="#2F4F4F")
        snake_segments.insert(0, segment)
        if SPEED >= 150:
            SPEED -= 50
        
    # Bewegung
    else: 
        snake_positions.insert(0, new_head)
        snake_positions.pop()
        for segment, position in zip(snake_segments, snake_positions):
            canvas.coords(segment, position[0], position[1], position[0] + 20, position[1] + 20)

# Funktion um Richtung zu ändern
def change_DIRECTION(new_DIRECTION):
    global DIRECTION, SPEED
    opposition = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
    if new_DIRECTION != opposition[DIRECTION]:
        DIRECTION = new_DIRECTION
    if new_DIRECTION == DIRECTION and SPEED >= 150:
        SPEED -= 50
        
    
# Pfeiltasten klicken
root.bind("<Up>", lambda event: change_DIRECTION('Up'))
root.bind("<Down>", lambda event: change_DIRECTION('Down'))
root.bind("<Left>", lambda event: change_DIRECTION('Left'))
root.bind("<Right>", lambda event: change_DIRECTION('Right'))

# Funktion um Kollision zu überprüfen
def is_collision():
    head_x, head_y = snake_positions[0]
    
    # Kollision mit Fenster Grenze
    if head_x < 0 or head_y < 0 or head_x >= 600 or head_y >= 400:
        return True
    
    # Kollision der Schlange mit sich selbst
    if (head_x, head_y) in snake_positions[1:]:
        return True
    
    return False

def restart_game():
    global DIRECTION, SCORE, SPEED, button_frame
    SPEED = skill.get()
    canvas.delete('all')
    if button_frame:
        button_frame.destroy()
    DIRECTION = 'Right'
    SCORE = 0
    create_snake()
    create_food()
    game_loop()

def start_game():
    global button_frame, SPEED
    SPEED = skill.get()
    if button_frame:
        button_frame.destroy()
    create_snake()
    create_food()
    game_loop()

def game_loop():
    global button_frame
    if is_collision():
        canvas.create_text(
            600 / 2,
            400 / 2,
            text=f'Game Over! Score: {SCORE}\n{SPEED} ',
            fill='red',
            font=("TkDefaultFont", 24),
            justify='center'
        )
        button_frame = tk.Frame(root)
        button_frame.pack(fill='both', expand=True)
        easy_rb = tk.Radiobutton(button_frame, text="Easy", variable=skill, value=800)
        medium_rb = tk.Radiobutton(button_frame, text="Medium", variable=skill, value=400)
        hard_rb = tk.Radiobutton(button_frame, text="Hard", variable=skill, value=200)
        easy_rb.pack(anchor="w")
        medium_rb.pack(anchor="w")
        hard_rb.pack(anchor="w")
        restart_button = tk.Button(button_frame, text='Play again', command=restart_game)
        restart_button.pack(pady=20)
        quit_button = tk.Button(button_frame, text='Quit Game', command=root.destroy)
        quit_button.pack(pady=10)
        return
    
    move_snake()
    root.after(SPEED, game_loop)

# Spiel laufen lassen
button_frame = tk.Frame(root)
button_frame.pack(fill='both', expand=True)
easy_rb = tk.Radiobutton(button_frame, text="Easy", variable=skill, value=500)
medium_rb = tk.Radiobutton(button_frame, text="Medium", variable=skill, value=300)
hard_rb = tk.Radiobutton(button_frame, text="Hard", variable=skill, value=200)
easy_rb.pack(anchor="w")
medium_rb.pack(anchor="w")
hard_rb.pack(anchor="w")

start_button = tk.Button(button_frame, text='Start', command=start_game)
start_button.pack(pady=20)

root.mainloop()