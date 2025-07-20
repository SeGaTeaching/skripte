
# **Anleitung: Snake Game in Tkinter**

## **Einleitung**
In dieser Anleitung wirst du ein funktionierendes Snake-Spiel mit Python und Tkinter erstellen. 
Das Spiel besteht aus:
- Einer Schlange, die wächst, wenn sie Nahrung frisst.
- Der Möglichkeit, die Schlange mit den Pfeiltasten zu steuern.
- Einem Ende, wenn die Schlange sich selbst oder die Spielfeldränder berührt.

Jeder Schritt enthält eine **Erklärung**, damit du erst selbst versuchen kannst, den Code zu schreiben. Anschließend findest du die Lösung, die du mit deinem Code vergleichen kannst.

---

## **Schritt 1: Ein Fenster und Canvas erstellen**

### **Erklärung**
Beginne damit, ein Fenster (`root`) zu erstellen. Dieses Fenster enthält ein `Canvas`, das als Spielfeld dient. Auf diesem Canvas werden alle Objekte des Spiels gezeichnet.

Denke darüber nach:
1. Wie erstelle ich ein Tkinter-Fenster?
2. Wie füge ich ein Canvas hinzu und setze dessen Größe?

---

### **Code für Schritt 1**
```python
import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# Canvas erstellen (Spielfläche)
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Hauptschleife
root.mainloop()
```

---

## **Schritt 2: Die Schlange erstellen**

### **Erklärung**
Die Schlange besteht aus mehreren Rechtecken, die wir zu Beginn des Spiels zeichnen. Ihre Positionen speichern wir in einer Liste (`snake_positions`), und jedes Rechteck repräsentiert ein Segment der Schlange.

Überlege:
- Wie speichere ich die Position der Schlange?
- Wie zeichne ich Rechtecke auf dem Canvas?

---

### **Code für Schritt 2**
```python
# Schlange initialisieren
snake_positions = [(100, 100), (80, 100), (60, 100)]  # Startposition
snake_segments = []

# Schlange zeichnen
for x, y in snake_positions:
    segment = canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")
    snake_segments.append(segment)
```

---

## **Schritt 3: Nahrung hinzufügen**

### **Erklärung**
Das Essen ist ein kleiner Kreis, der zufällig auf dem Spielfeld erscheint. Die Position des Essens sollte nicht mit der Schlange überlappen.

Überlege:
- Wie wähle ich zufällige Koordinaten für das Essen?
- Wie zeichne ich einen Kreis auf dem Canvas?

---

### **Code für Schritt 3**
```python
from random import randint

# Funktion, um zufällige Position für das Essen zu erstellen
def create_food():
    while True:
        x = randint(0, 29) * 20
        y = randint(0, 19) * 20
        if (x, y) not in snake_positions:
            break
    return canvas.create_oval(x, y, x + 20, y + 20, fill="red"), (x, y)

# Essen erstellen
food, food_position = create_food()
```

---

## **Schritt 4: Bewegung der Schlange**

### **Erklärung**
Die Schlange bewegt sich, indem der Kopf in die Bewegungsrichtung verschoben wird und das letzte Segment entfernt wird. Wir aktualisieren die Positionen und zeichnen die Schlange neu.

Überlege:
- Wie berechne ich die neue Position des Kopfes?
- Wie verschiebe ich die Segmente der Schlange?

---

### **Code für Schritt 4**
```python
# Bewegung der Schlange
def move_snake():
    global food, food_position

    # Neue Position für den Kopf berechnen
    head_x, head_y = snake_positions[0]

    if direction == "Right":
        new_head = (head_x + 20, head_y)
    elif direction == "Left":
        new_head = (head_x - 20, head_y)
    elif direction == "Down":
        new_head = (head_x, head_y + 20)
    elif direction == "Up":
        new_head = (head_x, head_y - 20)

    # Kollision mit dem Essen prüfen
    if new_head == food_position:
        snake_positions.insert(0, new_head)  # Neuer Kopf
        canvas.delete(food)  # Essen entfernen
        food, food_position = create_food()  # Neues Essen erstellen
        segment = canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + 20, new_head[1] + 20, fill="green")
        snake_segments.insert(0, segment)
    else:
        # Bewegung ohne Wachstum
        snake_positions.insert(0, new_head)
        snake_positions.pop()
        for segment, position in zip(snake_segments, snake_positions):
            canvas.coords(segment, position[0], position[1], position[0] + 20, position[1] + 20)
```

---

## **Schritt 5: Steuerung hinzufügen**

### **Erklärung**
Die Richtung der Schlange wird durch die Pfeiltasten gesteuert. Wir speichern die aktuelle Richtung in der Variable `direction` und ändern sie basierend auf der Benutzereingabe.

Überlege:
- Wie fange ich Benutzereingaben in Tkinter ab?
- Wie verhindere ich, dass die Schlange sich in die entgegengesetzte Richtung bewegt?

---

### **Code für Schritt 5**
```python
# Aktuelle Richtung
direction = "Right"

# Funktion, um die Richtung zu ändern
def change_direction(new_direction):
    global direction
    opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_direction != opposites[direction]:  # Keine direkte Umkehr
        direction = new_direction

# Pfeiltasten binden
root.bind("<Up>", lambda event: change_direction("Up"))
root.bind("<Down>", lambda event: change_direction("Down"))
root.bind("<Left>", lambda event: change_direction("Left"))
root.bind("<Right>", lambda event: change_direction("Right"))
```

---

## **Schritt 6: Kollisionen erkennen**

### **Erklärung**
Das Spiel endet, wenn die Schlange gegen die Spielfeldgrenzen oder sich selbst stößt. Diese Bedingungen prüfen wir in jeder Spielschleife.

---

### **Code für Schritt 6**
```python
# Funktion, um Kollisionen zu überprüfen
def check_collisions():
    head_x, head_y = snake_positions[0]

    # Kollision mit den Grenzen
    if head_x < 0 or head_y < 0 or head_x >= 600 or head_y >= 400:
        return True

    # Kollision mit sich selbst
    if (head_x, head_y) in snake_positions[1:]:
        return True

    return False
```

---

## **Schritt 7: Das Spiel zusammenfügen**

### **Erklärung**
Jetzt verbinden wir alle Teile: Bewegung, Steuerung, Nahrung und Kollisionen. Das Spiel läuft in einer Schleife, die regelmäßig die Logik aktualisiert.

---

### **Code für Schritt 7**
```python
# Hauptspielschleife
def game_loop():
    if check_collisions():
        print("Game Over!")
        return

    move_snake()
    root.after(100, game_loop)

# Spiel starten
game_loop()
root.mainloop()
```

---

## **Fertig!**

Herzlichen Glückwunsch! Du hast ein vollständiges Snake-Spiel in Tkinter erstellt. Du kannst es weiter verbessern, indem du:
- Einen Punktestand hinzufügst.
- Die Geschwindigkeit der Schlange mit der Punktzahl erhöhst.
- Soundeffekte einfügst.
