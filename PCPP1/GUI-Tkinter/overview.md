### **2-Tage-Lehrplan: GUI-Programmierung mit Tkinter (PCPP-1 Vorbereitung)**

**Tutor-Projekt (Demonstration):** BMI-Rechner
**Schüler-Projekt (Übungen):** Währungsrechner

---

### **Tag 1: Grundlagen und Interaktivität**

An diesem Tag legen wir das Fundament. Die Schüler lernen, was ein GUI ist, wie man grundlegende Fenster und Bedienelemente (Widgets) erstellt und diese auf dem Bildschirm anordnet. Das Hauptziel ist es, am Ende des Tages eine erste, einfache interaktive Anwendung erstellt zu haben.

**Block 1: Theoretische Grundlagen & Das erste Fenster (ca. 2.5 Stunden)**
* **Lernziele:**
    * Die grundlegenden Konzepte der GUI-Programmierung verstehen (event-driven vs. klassisch, Widgets, Events)[cite: 127, 130, 131, 132].
    * Ein leeres Tkinter-Fenster erstellen, den Titel anpassen und die Größe festlegen[cite: 135, 139].
    * Den Event-Loop (`mainloop`) verstehen und seine entscheidende Rolle in einer GUI-Anwendung erklären können[cite: 135].
* **Themen:**
    1.  **Was ist ein GUI?** (Begriffe, Rationale, Abgrenzung zur Kommandozeile) [cite: 127]
    2.  **Event-Driven-Programming:** Das Kernprinzip jeder GUI.
    3.  **Einführung in Tkinter:** Was ist es, warum ist es in Python Standard?
    4.  **Das Hauptfenster (Root-Window):** Die `Tk()`-Klasse, die `title()`-, `geometry()`-Methoden.
    5.  **Der Mainloop:** Warum die Anwendung ohne ihn nicht "lebt".
* **Tutor-Projekt (BMI-Rechner):** Der Tutor erstellt das leere Hauptfenster für den BMI-Rechner.
* **Übungs-Set 1:** Enthält 5-8 Programmieraufgaben, in denen die Schüler verschiedene Fenster erstellen und anpassen. Die erste Aufgabe für das **Schüler-Projekt** ist hier integriert: "Erstelle das Grundgerüst für den Währungsrechner."

---

**Block 2: Grundlegende Widgets & Layout-Management (ca. 3 Stunden)**
* **Lernziele:**
    * Die wichtigsten "statischen" Widgets kennenlernen und verwenden können: `Label`, `Entry`, `Button`[cite: 144].
    * Widgets in einem Fenster platzieren und organisieren können, unter Verwendung der drei Geometrie-Manager: `pack()`, `grid()` und `place()`[cite: 136, 144, 146].
    * Die Vor- und Nachteile der einzelnen Geometrie-Manager verstehen.
* **Themen:**
    1.  **Widgets als Klassen:** Das Konzept der Widget-Instanziierung.
    2.  **`Label`:** Text und Bilder anzeigen.
    3.  **`Entry`:** Benutzereingaben empfangen.
    4.  **`Button`:** Aktionen auslösen (vorerst ohne Funktion).
    5.  **Geometrie-Management im Detail:**
        * `pack()`: Für einfache, gestapelte Layouts.
        * `grid()`: Für tabellarische, flexible Layouts (der wichtigste Manager).
        * `place()`: Für exakte Pixel-Positionierung (mit Vor- und Nachteilen).
* **Tutor-Projekt (BMI-Rechner):** Der Tutor fügt die Eingabefelder (Entry) für Größe und Gewicht, die entsprechenden Beschriftungen (Label) und einen "Berechnen"-Button hinzu und ordnet alles sauber mit `grid()` an.
* **Übungs-Set 2:** Enthält 5-8 Programmieraufgaben zum Erstellen statischer Layouts. Die Schüler bauen hier die Oberfläche ihres **Währungsrechners** mit allen nötigen Eingabefeldern, Labels und Buttons auf.

---

**Block 3: Event-Handling & grundlegende Interaktivität (ca. 2.5 Stunden)**
* **Lernziele:**
    * Auf Benutzeraktionen (z.B. Button-Klicks) reagieren können[cite: 138].
    * Callback-Funktionen definieren und an Widgets binden[cite: 138, 147].
    * Daten aus `Entry`-Widgets auslesen und in der Anwendung verarbeiten.
    * Den Inhalt von `Label`-Widgets dynamisch zur Laufzeit ändern.
    * Einfache Fehlerbehandlung für Benutzereingaben implementieren[cite: 143].
* **Themen:**
    1.  **Das `command`-Attribut:** Die einfachste Form des Event-Handlings bei Buttons.
    2.  **Callback-Funktionen:** Was sie sind und wie man sie schreibt.
    3.  **Werte aus `Entry`-Widgets holen:** Die `.get()`-Methode.
    4.  **Werte in `Label`-Widgets setzen:** Die `.config()`-Methode.
    5.  **Einfache Datenvalidierung:** Prüfung, ob eine Eingabe eine Zahl ist (`try-except`).
* **Tutor-Projekt (BMI-Rechner):** Der Tutor implementiert die Logik für den "Berechnen"-Button. Die Funktion liest Größe und Gewicht, berechnet den BMI und zeigt das Ergebnis in einem Label an.
* **Übungs-Set 3:** Enthält 5-8 Programmieraufgaben zur Interaktivität. Die Schüler implementieren die Logik für ihren **Währungsrechner**, sodass eine Umrechnung stattfindet, wenn der Button geklickt wird.

---
### **Tag 2: Fortgeschrittene Konzepte und Struktur**

Am zweiten Tag vertiefen wir das Wissen. Die Schüler lernen komplexere Widgets kennen, erfahren, wie man Daten effizienter mit der GUI verknüpft und wie man den Code für größere Anwendungen sauber strukturiert.

**Block 4: Fortgeschrittene Widgets & Datenbindung (ca. 3 Stunden)**
* **Lernziele:**
    * Weitere wichtige Widgets wie `Frame`, `Radiobutton` und `Checkbutton` verwenden können[cite: 144].
    * Das Konzept der Tkinter-Kontrollvariablen (`StringVar`, `IntVar`, `DoubleVar`, `BooleanVar`) verstehen und anwenden können, um Widgets direkt an Programmdaten zu binden[cite: 150].
    * Die Vorteile der Datenbindung (z.B. automatische Aktualisierung der GUI) erkennen.
* **Themen:**
    1.  **Struktur mit `Frame`-Widgets:** Container zur Gruppierung von Widgets.
    2.  **Auswahl-Widgets:** `Radiobutton` (für eine Auswahl aus vielen) und `Checkbutton` (für An/Aus-Optionen).
    3.  **Das Problem der manuellen Synchronisation:** Warum `.get()` und `.config()` umständlich sein können.
    4.  **Tkinter-Kontrollvariablen:** Die elegante Lösung (`StringVar`, `IntVar` etc.).
    5.  **Widgets an Variablen binden:** Die Attribute `textvariable`, `variable`.
* **Tutor-Projekt (BMI-Rechner):** Der Tutor baut den BMI-Rechner um. Das Ergebnis wird nun an eine `StringVar` gebunden. Optional wird eine Auswahl für metrische/imperiale Einheiten mit `Radiobuttons` hinzugefügt.
* **Übungs-Set 4:** Enthält 5-8 Programmieraufgaben. Die Schüler erweitern ihren **Währungsrechner** um `Radiobuttons`, um zwischen verschiedenen Währungspaaren (z.B. EUR->USD, EUR->GBP) umschalten zu können, und binden die Ein- und Ausgabefelder an Kontrollvariablen.

---

**Block 5: Anwendungsstruktur & Dialoge (ca. 2.5 Stunden)**
* **Lernziele:**
    * Eine GUI-Anwendung sauber in einer Klasse strukturieren.
    * Standard-Dialogfenster (Info, Warnung, Fehler) aus dem `tkinter.messagebox`-Modul verwenden können[cite: 138].
    * Ereignisse mit der universellen `bind()`-Methode an beliebige Events (z.B. Tastendrücke, Mausbewegungen) knüpfen können[cite: 144].
* **Themen:**
    1.  **Vom Skript zur Klasse:** Warum OOP für GUIs sinnvoll ist.
    2.  **Aufbau einer GUI-Klasse:** Die Rolle von `__init__`.
    3.  **Interaktion mit dem Benutzer:** `tkinter.messagebox.showinfo()`, `showwarning()`, `showerror()`.
    4.  **Die `bind()`-Methode:** Ein mächtiges Werkzeug für fortgeschrittenes Event-Handling (z.B. "Enter"-Taste im Eingabefeld löst Berechnung aus).
* **Tutor-Projekt (BMI-Rechner):** Der Tutor refaktorisiert den gesamten BMI-Rechner in eine saubere Klasse. Bei ungültiger Eingabe wird nun ein `showerror`-Dialog angezeigt. Die Berechnung wird zusätzlich an die "Enter"-Taste in den Eingabefeldern gebunden.
* **Übungs-Set 5:** Enthält 5-8 Programmieraufgaben. Die Schüler strukturieren ihren **Währungsrechner** ebenfalls in einer Klasse. Sie fügen Fehlerdialoge für ungültige Eingaben hinzu und binden die Umrechnung an die Enter-Taste.

---

**Block 6: Der Canvas-Widget & Abschluss (ca. 2.5 Stunden)**
* **Lernziele:**
    * Den Zweck des `Canvas`-Widgets verstehen[cite: 143].
    * Einfache geometrische Formen (Linien, Rechtecke, Ovale) und Text auf einem `Canvas` zeichnen können.
    * Widget-Eigenschaften wie Farben anpassen können[cite: 146].
* **Themen:**
    1.  **Der `Canvas`:** Eine digitale Leinwand für eigene Zeichnungen.
    2.  **Koordinatensystem:** Wie man auf dem Canvas positioniert.
    3.  **Zeichenmethoden:** `create_line()`, `create_rectangle()`, `create_oval()`, `create_text()`.
    4.  **Farben und Styling:** Vordergrund- (`fg`), Hintergrundfarben (`bg`) und weitere Optionen für alle Widgets.
    5.  **Zusammenfassung und Ausblick:** Wiederholung der Kernkonzepte des GUI-Blocks.
* **Tutor-Projekt (BMI-Rechner):** Der Tutor fügt dem BMI-Rechner eine einfache grafische Anzeige hinzu: Ein `Canvas`, auf dem ein Balken den BMI-Wert farblich (grün, gelb, rot) darstellt.
* **Übungs-Set 6:** Enthält 5-8 Programmieraufgaben rund um das Canvas-Widget. Die Abschlussaufgabe für den **Währungsrechner** könnte lauten: "Stelle die Kursentwicklung der letzten 7 Tage als einfachen Liniengraphen auf einem Canvas dar (mit Dummy-Daten)."

***

Bitte prüfe diesen Plan. Wenn er deinen Vorstellungen entspricht, gib mir einfach den Startbefehl für den ersten Block: **"Block 1: Theoretische Grundlagen & Das erste Fenster"**.