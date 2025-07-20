# Kapitel 1: Programmierlogik

## **1.1 Die Analogie des Architekten**

Ein unerfahrener Bauherr beginnt vielleicht damit, wahllos Ziegel aufeinander zu schichten. Das Ergebnis wird instabil, schief und am Ende unbrauchbar. Ein professioneller Architekt hingegen zeichnet zuerst einen detaillierten **Bauplan**. Er plant die Statik, die Raumaufteilung und die Leitungen, lange bevor der erste Bagger rollt. In der Softwareentwicklung ist die **Programmierlogik** unser Bauplan. Sie ist die Kunst, ein Problem vollständig zu durchdenken und eine strukturierte Lösungsstrategie zu entwickeln, *bevor* wir an eine Programmiersprache überhaupt nur denken.

In der Softwareentwicklung ist die **Programmierlogik** unser Bauplan. Bevor wir eine einzige Zeile Code schreiben, müssen wir das Problem vollständig verstehen und den Lösungsweg strukturieren.

---

![alt text](image.png)

---

## **1.2 Top-Down-Design: Vom Ganzen ins Detail**

Das wichtigste Prinzip der Programmierlogik ist das **Top-Down-Design** (auch "Prinzip der schrittweisen Verfeinerung"). Es ist eine Methode, um nicht vom Komplexen überwältigt zu werden. Wir nehmen ein großes, unübersichtliches Problem und zerlegen es systematisch in immer kleinere, greifbare Teilprobleme, bis jedes Teilproblem so einfach ist, dass wir es sofort lösen oder in einer einzigen Code-Funktion beschreiben könnten.

**Beispiel:**
* **Großes Problem:** "Erstelle einen Online-Shop"
    * **Teilproblem 1:** "Benutzerverwaltung implementieren"
        * **Unter-Teilproblem 1.1:** "Login-Funktion erstellen"
        * **Unter-Teilproblem 1.2:** "Registrierungs-Funktion erstellen"
    * **Teilproblem 2:** "Produktkatalog anzeigen"
    * **Teilproblem 3:** "Warenkorb-Funktion umsetzen"

Dieses Vorgehen stellt sicher, dass wir nicht den Überblick verlieren und systematisch arbeiten.

---
## **1.3 Die Werkzeuge des Architekten: Sequenz, Selektion, Iteration**

Die gute Nachricht ist: Um die Logik für jedes dieser kleinen Teilprobleme zu beschreiben, benötigen wir nur drei fundamentale Bausteine, die wir bereits aus Block 1 kennen:

1.  **Sequenz:** Eine feste Reihenfolge von Anweisungen. (Zuerst den Salat waschen, DANN schneiden, DANN das Dressing machen).
2.  **Selektion (Verzweigung):** Eine Entscheidung, die den Weg teilt. (`WENN` der Gast Vegetarier ist, `DANN` biete die Gemüse-Spieße an, `SONST` das Steak).
3.  **Iteration (Schleife):** Eine sich wiederholende Aufgabe. (`FÜR` jeden Gast auf der Einladungsliste, `MACHE` folgendes: 'Schreibe eine Einladungskarte').

Wenn man diese drei Strukturen beherrscht, kann man theoretisch jedes lösbare Problem der Welt programmieren.

---

## **1.4 Abstraktion: Das Prinzip der "Schwarzen Kiste"**

##### **Skript-Text**

Abstraktion ist die direkte Folge von gutem Top-Down-Design. Es bedeutet, die inneren Details eines gelösten Teilproblems zu ignorieren und es wie eine "Schwarze Kiste" (Black Box) zu behandeln. Wir wissen, *was* die Kiste tut, aber es interessiert uns nicht mehr, *wie* sie es tut. Wir vertrauen einfach darauf, dass sie funktioniert. In der Programmierung ist das eine Funktion oder eine Klasse.

## **Praxis-Demo (Gedankenexperiment)**
> _**Anmerkung für den Lehrer:** Führe dieses Gedankenexperiment interaktiv an einem Whiteboard durch, um das Prinzip der Zerlegung zu visualisieren._

**Problem:** "Koche eine Tasse Kaffee mit einer Filterkaffeemaschine."

Wie zerlegen wir das?

* **Schritt 1 (Hohe Ebene):**
    1. Maschine vorbereiten.
    2. Brühvorgang starten.
    3. Kaffee entnehmen.

* **Schritt 2 (Detaillierung von "Maschine vorbereiten"):**
    1. Kanne mit Wasser füllen.
    2. Wasser in den Tank der Maschine gießen.
    3. Filtertüte in den Filterhalter einlegen.
    4. Kaffeepulver in die Filtertüte füllen.
    5. Kanne auf die Heizplatte stellen.

* **Schritt 3 (Detaillierung von "Brühvorgang starten"):**
    1. Maschine einschalten.
    2. Warten, bis das Wasser durchgelaufen ist.
    3. Maschine ausschalten.

Wir haben ein komplexes Problem erfolgreich in eine logische **Sequenz** von einfachen, unmissverständlichen Anweisungen zerlegt. Das ist die Essenz der Programmierlogik.