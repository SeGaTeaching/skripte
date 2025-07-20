## **1.1 Die Analogie des Architekten (ca. 30 Min.)**

##### **Skript-Text**

Ein unerfahrener Bauherr beginnt vielleicht damit, wahllos Ziegel aufeinander zu schichten. Das Ergebnis wird instabil, schief und am Ende unbrauchbar. Ein professioneller Architekt hingegen zeichnet zuerst einen detaillierten **Bauplan**. Er plant die Statik, die Raumaufteilung und die Leitungen, lange bevor der erste Bagger rollt. In der Softwareentwicklung ist die **Programmierlogik** unser Bauplan. Sie ist die Kunst, ein Problem vollständig zu durchdenken und eine strukturierte Lösungsstrategie zu entwickeln, *bevor* wir an eine Programmiersprache überhaupt nur denken.

In der Softwareentwicklung ist die **Programmierlogik** unser Bauplan. Bevor wir eine einzige Zeile Code schreiben, müssen wir das Problem vollständig verstehen und den Lösungsweg strukturieren.

---

##### **Visuelle Darstellung**

  * Zeichne auf dem Whiteboard/Miro-Board eine simple Gegenüberstellung.
  * **Links:** Ein Haufen ungeordneter Ziegelsteine mit der Überschrift "Ohne Plan". Daneben ein trauriger Smiley.
  * **Rechts:** Eine saubere, architektonische Blaupause eines Hauses mit der Überschrift "Mit Plan". Daneben ein zufriedener Smiley.

![alt text](image.png)

---

##### **Manuskript für den Lehrer**

*(Du stehst vor dem Whiteboard)*
"Guten Morgen zusammen. Bevor wir heute lernen, WIE man Programme plant, müssen wir klären, WARUM das so überlebenswichtig ist. Schaut euch diese beiden Bilder an. Links sehen wir den Versuch, ein Haus zu bauen, indem man einfach anfängt, Steine aufeinander zu werfen. Was glaubt ihr, wie lange dieses 'Haus' stehen wird?" *(kurze Pause, auf Antworten der Schüler warten)*.
"Genau, wahrscheinlich nicht sehr lange. Es ist instabil, niemand will darin wohnen. Das ist das Ergebnis, wenn ein Programmierer ohne Plan einfach drauflos codiert. Rechts sehen wir den Ansatz eines Profis: den Bauplan. Alles ist durchdacht. Jeder weiß, was zu tun ist. Das Ergebnis ist stabil, sicher und erfüllt seinen Zweck. Und genau dieser Architekt, der den Plan entwirft – das seid ab heute ihr."

---
---
---

#### **1.2 Top-Down-Design: Vom Ganzen ins Detail (ca. 90 Min.)**

##### **Skript-Text**

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

##### **Visuelle Darstellung**

  * Nutze ein Mind-Map-Tool oder das Whiteboard.
  * Schreibe in die Mitte das Hauptproblem: **"Geburtstagsfeier planen"**.
  * Zeichne von dort aus Hauptäste für die erste Ebene der Zerlegung: `Gäste`, `Location`, `Verpflegung`, `Unterhaltung`.
  * Verfeinere nun einen der Äste live mit den Schülern. Z.B. den Ast `Verpflegung`:
      * `Verpflegung` -\> `Getränke`, `Kuchen`, `Herzhaftes Essen`
      * `Herzhaftes Essen` -\> `Vegetarische Option`, `Fleisch-Option`
      * `Vegetarische Option` -\> `Salat zubereiten`, `Gemüse-Spieße grillen`


---

##### **Manuskript für den Lehrer**

"Okay, Architekten. Unser 'Haus' für heute ist die Planung einer Geburtstagsfeier. Klingt erstmal nach einer riesigen Aufgabe, oder? Wo fängt man da an? Man wird leicht überwältigt. Genau hier hilft uns das Top-Down-Design. Wir schauen von ganz oben drauf – Top-Down – und benennen die großen Blöcke." *(zeichne die erste Ebene der Mind-Map)*. "Gäste, Location, Verpflegung, Unterhaltung. So, das ist schon übersichtlicher. Aber was heißt 'Verpflegung' konkret?" *(wende dich an die Schüler)*. "Was gehört da alles dazu?" *(sammle Antworten und verfeinere den 'Verpflegung'-Ast live)*.
"Seht ihr, was hier passiert? Wir nehmen einen großen, schwammigen Begriff und zerlegen ihn, bis wir bei ganz konkreten, machbaren Aufgaben ankommen, wie 'Salat zubereiten'. Das ist exakt der Denkprozess, den ihr bei jeder Programmieraufgabe anwenden müsst."

#### **1.3 Die Werkzeuge des Architekten: Sequenz, Selektion, Iteration (ca. 60 Min.)**

##### **Skript-Text**

Die gute Nachricht ist: Um die Logik für jedes dieser kleinen Teilprobleme zu beschreiben, benötigen wir nur drei fundamentale Bausteine, die wir bereits aus Block 1 kennen:

1.  **Sequenz:** Eine feste Reihenfolge von Anweisungen. (Zuerst den Salat waschen, DANN schneiden, DANN das Dressing machen).
2.  **Selektion (Verzweigung):** Eine Entscheidung, die den Weg teilt. (`WENN` der Gast Vegetarier ist, `DANN` biete die Gemüse-Spieße an, `SONST` das Steak).
3.  **Iteration (Schleife):** Eine sich wiederholende Aufgabe. (`FÜR` jeden Gast auf der Einladungsliste, `MACHE` folgendes: 'Schreibe eine Einladungskarte').

Wenn man diese drei Strukturen beherrscht, kann man theoretisch jedes lösbare Problem der Welt programmieren.

##### **Visuelle Darstellung**

  * Gehe zurück zu deiner Mind-Map.
  * Markiere verschiedene Teile der Mind-Map mit den Symbolen der Bausteine.
  * **Sequenz:** Zeichne Pfeile zwischen `Salat waschen` -\> `schneiden` -\> `Dressing machen`.
  * **Selektion:** Zeichne eine Raute (wie im PAP) an den Ast `Herzhaftes Essen` mit den Pfaden "Vegetarier: Ja/Nein".
  * **Iteration:** Zeichne ein Schleifen-Symbol um den Ast `Gäste` mit der Beschriftung "Für jeden Gast wiederholen".

##### **Manuskript für den Lehrer**

"Jetzt, wo wir unsere Teilaufgaben haben, brauchen wir die passenden Werkzeuge, um ihre interne Logik zu beschreiben. Und das Tolle ist: Es gibt nur drei\! Schauen wir uns unsere Party-Planung an. Die Zubereitung des Salats ist eine klare **Sequenz**. Ein Schritt nach dem anderen." *(zeige auf die Pfeile)*. "Die Essensausgabe erfordert eine **Selektion**, eine Entscheidung." *(zeige auf die Raute)*. "Und das Verschicken der Einladungen ist eine klassische **Iteration**. Wir machen ja nicht für jeden Gast einen komplett neuen Plan, sondern wiederholen denselben Prozess immer wieder. Mit diesen drei Werkzeugen könnt ihr die Logik für JEDES Problem beschreiben."

#### **1.4 Abstraktion: Das Prinzip der "Schwarzen Kiste" (ca. 45 Min.)**

##### **Skript-Text**

Abstraktion ist die direkte Folge von gutem Top-Down-Design. Es bedeutet, die inneren Details eines gelösten Teilproblems zu ignorieren und es wie eine "Schwarze Kiste" (Black Box) zu behandeln. Wir wissen, *was* die Kiste tut, aber es interessiert uns nicht mehr, *wie* sie es tut. Wir vertrauen einfach darauf, dass sie funktioniert. In der Programmierung ist das eine Funktion oder eine Klasse.

##### **Visuelle Darstellung**

  * Zeichne eine große, schwarze Kiste in die Mitte des Whiteboards.
  * Beschrifte die Kiste mit **"Kaffeemaschine"**.
  * Zeichne einen Pfeil, der in die Kiste hineingeht. Beschriftung: **Input** (Wasser, Pulver).
  * Zeichne einen Knopf auf die Kiste. Beschriftung: **Schnittstelle** (`start()`).
  * Zeichne einen Pfeil, der aus der Kiste herauskommt. Beschriftung: **Output** (Heißer Kaffee).
  * Male ins Innere der Kiste ganz klein und unleserlich die internen Details: "Heizspirale, Pumpe, Thermostat...".

##### **Manuskript für den Lehrer**

"So, letzter wichtiger Punkt für heute: Abstraktion. Klingt kompliziert, ist aber etwas, das ihr jeden Tag macht. Hier ist eine Kaffeemaschine." *(zeige auf die Black Box)*. "Was muss ich wissen, um sie zu benutzen?" *(Schüler fragen)*. "Richtig, ich muss wissen, wo Wasser und Pulver reinkommen – der **Input**. Und ich muss den Start-Knopf kennen – die **Schnittstelle**. Was am Ende rauskommt, ist der **Output**. Muss ich wissen, wie die Heizspirale funktioniert oder welche Spannung der Thermostat braucht, um einen Kaffee zu kochen?" *(klare Pause)*. "Nein\! Es interessiert mich nicht. Die komplexe interne Logik ist für mich abstrahiert, verborgen. Ich vertraue der schwarzen Kiste. Und genau das ist unser Ziel beim Programmieren. Wenn wir eine Teilaufgabe wie 'sende\_einladung()' einmal gelöst haben, behandeln wir sie wie eine Black Box und müssen nie wieder über ihre inneren Details nachdenken. Das macht große Projekte überhaupt erst beherrschbar."

-----

#### **Praxis-Demo (Gedankenexperiment) 🧠**
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