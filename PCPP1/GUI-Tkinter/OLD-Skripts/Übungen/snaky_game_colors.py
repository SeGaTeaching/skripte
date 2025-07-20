import tkinter as tk
from random import randint, choice

colors = [
    "#FFFFFF",  # Weiß
    "#808080",  # Grau
    "#C0C0C0",  # Silber
    "#00FF00",  # Grün
    "#008000",  # Dunkelgrün
    "#00FFFF",  # Cyan
    "#008080",  # Teal
    "#FFFF00",  # Gelb
    "#808000",  # Oliv
    "#0000FF",  # Blau
    "#000080",  # Marineblau
    "#FF00FF",  # Magenta
    "#800080",  # Lila
    "#FFD700",  # Gold
    "#4B0082",  # Indigo
    "#7FFFD4",  # Aquamarin
    "#DC143C",  # Karmesinrot
    "#00CED1",  # Dunkeltürkis
    "#40E0D0",  # Türkis
    "#4682B4",  # Stahlblau
    "#5F9EA0",  # Cadetblau
    "#6A5ACD",  # Schieferblau
    "#7B68EE",  # Mittleres Schieferblau
    "#9370DB",  # Mittelviolettrot
    "#8A2BE2",  # Blauviolett
    "#ADFF2F",  # Gelbgrün
    "#B8860B",  # Dunkler Goldgelb
    "#DAA520",  # Goldenrod
    "#D2691E",  # Schokoladenbraun
    "#CD5C5C",  # Indianerrot
    "#6495ED",  # Kornblumenblau
    "#BC8F8F",  # Rosenholz
    "#4682B4",  # Stahlblau
    "#87CEFA",  # Himmelblau
    "#32CD32",  # Limettengrün
    "#3CB371",  # Mittelmeergrün
    "#66CDAA",  # Mittelmeer-Aquamarin
    "#20B2AA",  # Hellseeblau
    "#778899",  # Helles Schiefergrau
    "#B0C4DE",  # Lichtstahlblau
    "#FAEBD7",  # Antikweiß
    "#F0E68C",  # Khaki
    "#FFE4B5",  # Moccasin
    "#E6E6FA",  # Lavendel
]

root = tk.Tk()
root.title("Classic Snake Game")
root.resizable(False, False)

# Tkinter Variable
skill = tk.StringVar(value="medium")

# Globale Variablen
SPEED = None
SCORE = None
DIRECTION = None
SNAKE_POSITIONS = None
SNAKE_SEGMENTS = None
FOOD = None
FOOD_POSITION = None
button_frame = None

# Canvas erstellen
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack(pady=10, padx=10)

# Schlange erstellen
def create_snake():
    global SNAKE_SEGMENTS
    SNAKE_SEGMENTS.clear()
    for x, y in SNAKE_POSITIONS:
        segment = canvas.create_oval(x, y, x + 20, y + 20, fill=choice(colors))
        SNAKE_SEGMENTS.append(segment)

# Futter erstellen
def create_food():
    global FOOD, FOOD_POSITION
    while True:
        x = randint(0,29) * 20
        y = randint(0,19) * 20
        if (x, y) not in SNAKE_POSITIONS:
            break
    FOOD_POSITION = (x, y)
    FOOD = canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")

# Schlange bewegen
def move_snake():
    global DIRECTION, SCORE, SPEED

    # Aktueller Schlangenkopfkoordinate
    head_x, head_y = SNAKE_POSITIONS[0]

    # Neue Kopfposition anhand der Richtung bestimmen
    if DIRECTION == "Right":
        new_head = (head_x + 20, head_y)
    elif DIRECTION == "Down":
        new_head = (head_x, head_y + 20)
    elif DIRECTION == "Up":
        new_head = (head_x, head_y - 20)
    elif DIRECTION == "Left":
        new_head = (head_x - 20, head_y)

    # Prüfen ob Schlange das Futter frisst
    if new_head == FOOD_POSITION:
        SCORE += 1

        # Geschwindigkeit des Game Loops bzw. der Schlange erhöhen
        if skill.get() == "easy":
            if SPEED > 400:
                SPEED -= 50
        elif skill.get() == "medium":
            if SPEED > 250:
                SPEED -= 50
        else:
            if SPEED > 100:
                SPEED -= 50

        canvas.delete(FOOD)  # Altes Futter löschen
        create_food()  # Neues Futter erstellen
        SNAKE_POSITIONS.insert(0, new_head)

        # Neues Kopfsegment erstellen
        x, y = new_head
        new_segment = canvas.create_oval(x, y, x + 20, y + 20, fill=choice(colors))
        SNAKE_SEGMENTS.insert(0, new_segment)

    else:
        # Entferne letztes Schlangen Element bzw. Koordinate
        SNAKE_POSITIONS.pop()

        # Füge neue Kopf-Koordinate in die Liste ein
        SNAKE_POSITIONS.insert(0, new_head)

        # Schlange neu zeichnen
        for segment, position in zip(SNAKE_SEGMENTS, SNAKE_POSITIONS):
            x, y = position
            canvas.coords(segment, x, y, x + 20, y + 20)

# Richtung der Schlange ändern
def change_direction(event):
    global DIRECTION
    opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if event.keysym != opposite[DIRECTION]:
        DIRECTION = event.keysym

# Kollision überprüfen
def check_collision():
    head_x, head_y = SNAKE_POSITIONS[0]

    # Kollision mit dem Körper der Schlange
    if (head_x, head_y) in SNAKE_POSITIONS[1:]:
        return True

    # Kollison mit Canvas Rändern selber
    if head_x < 0 or head_y < 0 or head_x >= 600 or head_y >= 400:
        return True

# Buttons aktivieren/deaktivieren
def toggle_controls(state):
    global button_frame
    if button_frame:
        for child in button_frame.winfo_children():
            child.config(state=state)

# Spielschleife
def game_loop():
    if check_collision():
        canvas.delete("all")
        canvas.create_text(300, 200, text=f'Game Over!\n\nScore: {SCORE}', fill='red', font=('TkDefaultFont', 24))
        toggle_controls("normal")  # Buttons aktivieren
        return
    move_snake()
    root.after(SPEED, game_loop)

# Spiel starten
def start_game():
    reset_game()
    toggle_controls("disabled")  # Buttons deaktivieren
    game_loop()

# Spiel neu starten
def reset_game():
    global DIRECTION, SCORE, SNAKE_POSITIONS, SNAKE_SEGMENTS, SPEED

    if skill.get() == "easy":
        SPEED = 600
    elif skill.get() == "medium":
        SPEED = 400
    else:
        SPEED = 250
    DIRECTION = "Right"
    SCORE = 0
    SNAKE_POSITIONS = [(100, 100), (80, 100), (60, 100)]
    SNAKE_SEGMENTS = []
    canvas.delete("all")
    create_snake()
    create_food()

# Steuerung mit Pfeiltasten
root.bind("<Up>", change_direction)
root.bind("<Down>", change_direction)
root.bind("<Left>", change_direction)
root.bind("<Right>", change_direction)

# UI erstellen
def create_controls():
    global button_frame
    button_frame = tk.Frame(root, pady=15, padx=15)
    button_frame.pack(fill='both', expand=True)

    # Start Button
    start_button = tk.Button(button_frame, text='Start Game', command=start_game)
    start_button.grid(row=0, column=0, columnspan=3, pady=10)

    # Radiobuttons in einer Reihe
    tk.Radiobutton(button_frame, text="Easy", variable=skill, value="easy").grid(row=1, column=0, padx=5)
    tk.Radiobutton(button_frame, text="Medium", variable=skill, value="medium").grid(row=1, column=1, padx=5)
    tk.Radiobutton(button_frame, text="Hard", variable=skill, value="hard").grid(row=1, column=2, padx=5)

    button_frame.columnconfigure((0,1,2), weight=1)
    
create_controls()

root.mainloop()

# ---------------------------------------------

# Snake Game Expotieren als eigenständige App

## Voraussetzung:
## - pyinstaller
## - pillow, wenn Du ein App-Logo haben möchtest

## Kommandozeile Code
## $ pyinstaller --onefile --noconsole --icon="images/snake.jpg" snaky_game.py
