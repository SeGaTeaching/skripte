
# **Anleitung: Taschenrechner mit Tkinter erstellen**

In dieser Anleitung bauen wir einen einfachen Taschenrechner mit **Tkinter**. Der Fokus liegt darauf, selbstständig die GUI und die grundlegende Rechenlogik zu entwickeln.

---

## **1. Hauptfenster erstellen**
### **Ziel:**
- Ein Hauptfenster für den Taschenrechner erstellen.

### **Schritte:**
1. Importiere das `tkinter`-Modul.
2. Erstelle ein `Tk`-Objekt als Hauptfenster.
3. Stelle eine feste Fenstergröße ein (z. B. 300x400 Pixel).
4. Gib dem Fenster einen passenden Titel (z. B. "Taschenrechner").
5. Starte die Hauptschleife mit `mainloop()`.

---

## **2. Eingabefeld für Zahlen und Ergebnisse hinzufügen**
### **Ziel:**
- Ein Eingabefeld, das Benutzereingaben und Ergebnisse anzeigt.

### **Schritte:**
1. Füge ein Eingabefeld (`Entry`-Widget) hinzu.
2. Platziere das Eingabefeld im oberen Bereich des Fensters.
3. Richte es so ein, dass die Schrift groß genug ist (z. B. `font=("Arial", 24)`) und die Zahlen rechtsbündig angezeigt werden.

### **Hinweise:**
- benütze `columnspan` um die Breite des Entry Feldes anzupassen
---

## **3. Tasten für Zahlen und Operatoren erstellen**
### **Ziel:**
- Eine Liste erstellen, die die Beschriftung und Position jeder Taste beschreibt.

### **Schritte:**
1. Lege eine Liste mit Tupeln an, die die Tasten definieren. Jede Taste besteht aus: `(Beschriftung, Zeile, Spalte)`.
   ```python
   tasten = [
       ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
       ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
       ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
       ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
   ]
   ```

2. Verwende eine `for`-Schleife, um die Tasten zu erstellen und zu positionieren.
3. Nutze den Layout-Manager `grid`, um die Tasten in ein Raster einzufügen.
4. Jede Taste sollte eine feste Schriftgröße (z. B. `font=("Arial", 18)`) und gleichmäßige Abstände (`padx`, `pady`) haben.

### **Hinweise:**
- Durch `if` und `elif` Anweisungen können innerhalb der `for`-Schleife den einzelnen Tasten, individuelle Callbacks zugewiesen werden
---

## **4. Funktionen für Tastenaktionen**
### **Ziel:**
- Implementiere drei grundlegende Funktionen, die mit den Tasten verbunden werden.

### **Funktionen:**
1. **Funktion für Zahlen- und Eingabetasten:**
   - Diese Funktion soll den Text der gedrückten Taste ins Eingabefeld einfügen.

2. **Funktion für Operatoren:**
   - Diese Funktion speichert die erste Zahl und den Operator und leert das Eingabefeld für die zweite Zahl.

3. **Funktion für die Berechnung:**
   - Diese Funktion führt die Berechnung basierend auf der ersten Zahl, dem Operator und der zweiten Zahl durch und zeigt das Ergebnis im Eingabefeld an.

4. **Zusätzliche Clear-Funktion (optional):**
   - Diese Funktion leert das Eingabefeld und setzt gespeicherte Variablen zurück.

### **Hinweise:**
- Um das Eingabefenster zu leeren verwende `eingabefeld.delete(0, tk.END)`
- Um Inhalt in das Eingabefenster zu setzen `eingabefeld.insert(0, '<content>')`
---

## **5. Aktionen mit Tasten verknüpfen**
### **Ziel:**
- Jede Taste soll eine spezifische Funktion ausführen.

### **Schritte:**
1. Nutze den Parameter `command`, um jede Taste mit der entsprechenden Funktion zu verbinden.
2. Für Tasten, die Parameter benötigen (z. B. Zahlen oder Operatoren), verwende **`lambda`**, um die Parameter zu übergeben.
   ```python
   # Beispiel für eine Taste mit Parameter
   command=lambda t='7': button_click(t)
   ```

### **Hinweise:**
- Zahlen und Operatoren sollten an ihre jeweiligen Funktionen übergeben werden.
- Nutze den Text der Taste (z. B. `'7'` oder `'+'`), um die Aktionen dynamisch zu gestalten.

---

## **6. Testen und Anpassen**
### **Ziel:**
- Teste den Taschenrechner mit verschiedenen Eingaben und überprüfe, ob die Grundfunktionen (Addition, Subtraktion, etc.) korrekt arbeiten.

### **Optionale Verbesserungen:**
1. Implementiere zusätzliche Funktionen wie Wurzeln oder Prozentrechnung.
2. Gestalte das Layout ansprechender, indem du Farben oder Rahmen hinzufügst.

---
