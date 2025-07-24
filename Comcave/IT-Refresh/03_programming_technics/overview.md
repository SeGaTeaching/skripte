## **Detaillierter Plan: Block 3 (Angepasst auf 7 Tage / 50 UE)**

#### **Tag 1: Was ist ein Algorithmus? (Theoretische Grundlagen)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Eine formale Definition von Algorithmen, basierend auf den theoretischen Grundlagen.
    * **Inhalt:**
        * [cite_start]Herkunft und Definition (al-Chwarizmi, Handlungsvorschrift) [cite: 380-387].
        * [cite_start]Eigenschaften von Algorithmen (Endlichkeit, Termination, Determinismus, Determiniertheit) [cite: 409-416]. Wir diskutieren den feinen Unterschied zwischen deterministisch (fester Ablauf) und determiniert (festes Ergebnis).
        * [cite_start]Effizienz von Algorithmen: Kurzer, konzeptioneller Ausblick auf die Relevanz von Ausführungszeit und Speicherplatzbedarf [cite: 505-508].
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Theoretische Transferaufgaben. "Erkläre den Unterschied zwischen einem Rezept und einem Algorithmus", "Ist die Wegbeschreibung eines Freundes immer ein deterministischer Algorithmus? Begründe deine Antwort."

#### **Tag 2: Wiederverwertbarkeit II (Rekursion)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Eine neue Denkweise: Rekursion als Alternative zur Schleife.
    * **Inhalt:**
        * Kurze Wiederholung der iterativen Funktionen.
        * Einführung in die **Rekursion**: Eine Funktion, die sich selbst aufruft.
        * Die zwei Kernkomponenten: **Basisfall** (Abbruchbedingung) und **rekursiver Schritt**.
    * [cite_start]**Praxis:** Wir erarbeiten die **Fakultätsberechnung** [cite: 747] [cite_start]und implementieren sie sowohl **iterativ** [cite: 769] [cite_start]als auch **rekursiv**[cite: 790], um den Unterschied direkt zu vergleichen.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Die rekursive Logik nachvollziehen. Eine einfache rekursive Funktion (z.B. Summe einer Liste) selbst schreiben.

#### **Tag 3: Standardalgorithmen I (Suchen & Sortieren)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Klassische Probleme der Informatik lösen.
    * **Inhalt:**
        * **Lineare Suche:** Formalisierung des einfachen Suchproblems. Logik entwickeln und als Funktion implementieren.
        * [cite_start]**Bubble Sort:** Detaillierte Erarbeitung nach dem Vorbild deines Kollegen-Skripts: Was ist der Algorithmus und wofür ist er nützlich? [cite: 687-690] [cite_start]Schritt-für-Schritt-Logik [cite: 692-697]. Visuelle Live-Demo am Whiteboard. Gemeinsame Implementierung der `bubbleSort()`-Funktion.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Eigene Implementierung von linearer Suche und Bubble Sort. Testen der Algorithmen mit verschiedenen Listen (unsortiert, sortiert, rückwärts sortiert) und Beobachtung des Verhaltens.

#### **Tag 4: Standardalgorithmen II (Mathematische Algorithmen)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Effiziente mathematische Lösungen.
    * **Inhalt:**
        * [cite_start]**Euklidischer Algorithmus:** Detaillierte Erarbeitung nach Vorbild des Skripts: Was ist der GGT und wofür braucht man ihn? [cite: 644-648] [cite_start]Schritt-für-Schritt-Logik [cite: 649-653]. [cite_start]Live-Beispiel mit `a = 48` und `b = 18` [cite: 655-661]. Gemeinsame Implementierung.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Eigene Implementierung des Euklidischen Algorithmus. Eine darauf aufbauende Funktion `kuerzeBruch(zaehler, nenner)` schreiben, die den GGT nutzt.

#### **Tag 5: Fehlerbehandlung & Debugging**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Mit Fehlern professionell umgehen.
    * **Inhalt:**
        * **Fehlerarten:** Syntax-, Laufzeit- und logische Fehler.
        * **Vertiefung Debugger:** `Call Stack` (Aufrufstapel) analysieren, `Step Into` vs. `Step Over` bei verschachtelten Funktionsaufrufen.
        * **Strukturierte Fehlerbehandlung:** Einführung in `try-except` (Python) bzw. `try-catch` (Java/JS), um Programmabstürze bei erwartbaren Fehlern (z.B. Falscheingaben) zu verhindern.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** "Finde den Bug"-Aufgaben in komplexeren Funktionen. Aufgaben zur Absicherung von Benutzereingaben mit `try-catch`.

#### **Tag 6: Anwendungen I (Zahlenrate-Spiel)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Das Gelernte in einem ersten kleinen Projekt anwenden.
    * **Inhalt:**
        * **Gemeinsame Planung:** Wir zerlegen die Anforderungen an das "Zahlenrate-Spiel" mittels Top-Down-Design und entwerfen den Algorithmus in Pseudocode.
        * **Gemeinsame Implementierung:** Wir beginnen mit der Umsetzung des Spiels in der Zielsprache. Fokus auf die Hauptschleife, die Zufallszahlengenerierung und die `if-elif-else`-Logik für die Hinweise.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Die Schüler vervollständigen das Zahlenrate-Spiel und bauen Zusatzfeatures ein (z.B. eine begrenzte Anzahl an Versuchen, eine "Nochmal spielen?"-Funktion).

#### **Tag 7: Anwendungen II (Weitere Projekte & Puffer)**
* **Vormittag (ca. 4 UE):**
    * **Thema:** Kreative Anwendung und Festigung.
    * **Inhalt:** Ich stelle 2-3 weitere Mini-Projekte vor (siehe Liste unten). Die Schüler können sich eines aussuchen.
    * **Praxis:** Die Schüler arbeiten in Einzel- oder Gruppenarbeit an ihrem gewählten Projekt. Du agierst als Coach und gibst individuelle Hilfestellungen.
* **Nachmittag (Selbstlernphase, ca. 3.5 UE):**
    * **Übungsblock:** Fortsetzung der Arbeit an den Mini-Projekten.

---
### **Vorschläge für weitere Mini-Projekte**

Wie gewünscht, hier noch weitere Ideen für typische Anfänger-Anwendungen:

* **Konsolen-Taschenrechner:** Das Programm fragt nach zwei Zahlen und einer Operation (+, -, \*, /) und gibt das Ergebnis aus. Dies trainiert Funktionen und `if-elif-else` oder `switch`.
* **ToDo-Listen-Verwaltung (Textbasiert):** Ein Programm, das eine Liste von Aufgaben verwaltet. Der Benutzer kann Aufgaben hinzufügen, anzeigen, als erledigt markieren und löschen. Dies trainiert den Umgang mit Listen/Arrays und Schleifen.
* **Einfaches Text-Adventure:** Ein kleines Spiel, bei dem der Benutzer durch Texteingaben ("gehe nach norden", "nimm schwert") durch eine einfache Geschichte navigiert. Dies trainiert `if-else`-Strukturen und die Verwaltung eines "Spielzustands" in Variablen.
