# 🗺️ **KAPITEL 4: Programmablaufpläne (PAP / Flowcharts)**

---
### **📝 SKRIPT (für Präsentation / Notebook)**

#### **4.1 Was ist ein Programmablaufplan?**

* **Analogie:** Eine **Straßenkarte** oder eine **GPS-Route**. Der Fokus liegt auf dem **Fluss** und den Wegen, die das Programm von einem Start- zu einem Endpunkt nehmen kann.
* **Definition:** Eine grafische Darstellung eines Algorithmus.
* **Kernmerkmal:** Verwendet standardisierte Symbole, die durch **Pfeile** (sog. Wirkungslinien) verbunden sind, um die genaue Reihenfolge und den Kontrollfluss zu zeigen.

#### **4.2 Die Symbole eines PAP (nach DIN 66001)**

| Symbol | Form | Bedeutung |
| :--- | :--- | :--- |
| **Terminalsymbol** | Oval | **Start** und **Ende** eines Programms. |
| **Operationssymbol** | ▭ | Eine Anweisung, Berechnung oder Wertzuweisung. |
| **Entscheidungssymbol**| ◇ | Eine **Verzweigung** (`if`) mit "Ja"- und "Nein"-Ausgängen. |
| **Ein-/Ausgabesymbol**| ▱ | Stellt das Einlesen (`EINGABE`) oder Ausgeben (`AUSGABE`) von Daten dar. |
| **Wirkungslinie** | → | Ein Pfeil, der die Symbole verbindet und die Leserichtung vorgibt. |

---

> ### 👨‍🏫 **VISUALISIERUNG & DEMO (Live via Teams)**
>
> #### **Tool-Empfehlung**
>
> * **Tool:** **diagrams.net** (früher draw.io) auf [https://app.diagrams.net/](https://app.diagrams.net/)
> * **Warum?** Es ist kostenlos, browserbasiert und die linke Seitenleiste enthält die fertige Form-Bibliothek **"Flowchart"** mit allen DIN-Symbolen.
>
> #### **Beispiel 1: Ticketpreis-Kalkulator (PAP mit Verzweigung)**
>
> **Anleitung zur Erstellung in diagrams.net:**
> 1.  Starte mit einem **Oval** ("START").
> 2.  Pfeil nach unten zu einem **Parallelogramm** ("Alter eingeben").
> 3.  Pfeil nach unten zu einer **Raute** ("Alter < 16 ODER >= 65?").
> 4.  Vom Ja-Ausgang der Raute: Pfeil zu einem **Rechteck** ("Preis = 9.00").
> 5.  Vom Nein-Ausgang der Raute: Pfeil zu einem **Rechteck** ("Preis = 12.00").
> 6.  Führe die Pfeile von beiden Rechtecken wieder zusammen und zeige auf ein **Parallelogramm** ("Preis ausgeben").
> 7.  Beende mit einem Pfeil zu einem **Oval** ("ENDE").
>
> ---
> #### **Beispiel 2: Notendurchschnitt (PAP mit Schleife)**
>
> **Anleitung zur Erstellung in diagrams.net:**
> 1.  START -> **Rechteck** (`gesamtsumme = 0`) -> **Rechteck** (`notenliste = [...]`).
> 2.  Pfeil zu einer **Raute** für die Schleifenbedingung ("Noch Noten in Liste?").
> 3.  **Ja-Pfad (Schleifenkörper):** Pfeil zu einem **Rechteck** ("Nächste Note aus Liste holen") -> Pfeil zu einem **Rechteck** (`gesamtsumme = gesamtsumme + note`).
> 4.  **Schleifen-Rückführung:** Ein Pfeil führt vom letzten Rechteck wieder nach oben, direkt vor die Raute der Schleifenbedingung.
> 5.  **Nein-Pfad (Nach der Schleife):** Pfeil zu einem **Rechteck** (`durchschnitt = gesamtsumme / anzahl`) -> Pfeil zu einem **Parallelogramm** ("Durchschnitt ausgeben") -> ENDE.
>
> ---
> #### **Beispiel 3: FizzBuzz (PAP mit verschachtelten Entscheidungen)**
>
> **Anleitung zur Erstellung in diagrams.net:**
> 1.  **Schleifenaufbau:** START -> **Rechteck** (`i = 1`) -> **Raute** (`i <= 100?`). Der Nein-Pfad führt direkt zum ENDE.
> 2.  **Schleifenkörper (Ja-Pfad):** Der Ja-Pfad führt zu einer Kaskade von weiteren Rauten.
>     * **Raute 1:** `i % 15 == 0?`
>         * Ja-Pfad -> **Parallelogramm** ("FizzBuzz ausgeben").
>         * Nein-Pfad -> **Raute 2:** `i % 3 == 0?`
>             * Ja-Pfad -> **Parallelogramm** ("Fizz ausgeben").
>             * Nein-Pfad -> **Raute 3:** `i % 5 == 0?`
>                 * Ja-Pfad -> **Parallelogramm** ("Buzz ausgeben").
>                 * Nein-Pfad -> **Parallelogramm** ("Zahl i ausgeben").
> 3.  **Zusammenführung:** Alle vier Ausgabe-Pfade werden mit Pfeilen wieder zusammengeführt.
> 4.  **Inkrement & Rückführung:** Der zusammengeführte Pfad zeigt auf ein **Rechteck** (`i = i + 1`), von dem ein Pfeil wieder hoch zur Schleifenbedingung (`i <= 100?`) führt.

---

> ### 🗣️ **MANUSKRIPT LEHRER (Stichpunkte)**
>
> * **Einstieg & Analogie:**
>     * "Nach dem starren LEGO-Bauplan (Struktogramm) kommt jetzt die flexible Straßenkarte (PAP)."
>     * Kernbotschaft: Fokus liegt auf dem **FLUSS** des Programms, den Wegen und Abzweigungen.
>
> * **Tool-Demo:**
>     * Zeige diagrams.net und die "Flowchart"-Bibliothek.
>     * Betone die einfache Bedienung per Drag & Drop und das Verbinden mit Pfeilen.
>
> * **Live-Demos:**
>     * Beim Erstellen die Rolle der Pfeile hervorheben: "Dieser Pfeil hier ist der entscheidende Unterschied zum Struktogramm. Er zeigt uns genau, wo es als Nächstes weitergeht."
>     * Bei der Schleife: "Und dieser Pfeil, der von unten wieder nach oben zeigt, macht die Wiederholung erst sichtbar. Das ist die visuelle Darstellung einer Iteration."
>
> * **Vergleich PAP vs. Struktogramm:**
>     * Zeige beide Diagramm-Typen für dasselbe Problem nebeneinander.
>     * *Frage:* "Was ist der größte Unterschied, den ihr seht?" -> **Pfeile vs. geschachtelte Blöcke**.
>     * *Diskussion:* Freiheit vs. Struktur. PAPs sind flexibler, können aber unübersichtlich werden. Struktogramme erzwingen saubere Logik.
>
> * **Fazit:**
>     * Beides sind wichtige Werkzeuge zur Planung.
>     * In der IHK-Prüfung kann beides verlangt werden, daher müssen beide verstanden werden.
>     * "Damit haben wir unseren Werkzeugkasten für die Programm-Planung komplettiert."