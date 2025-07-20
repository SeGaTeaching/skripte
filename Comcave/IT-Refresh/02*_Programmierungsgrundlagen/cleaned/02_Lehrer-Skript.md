## ✍️ **KAPITEL 2: Pseudocode (Die Brückensprache)**

*(Geschätzte Dauer: 1 voller Unterrichtstag)*

-----

### **📝 SKRIPT (für Präsentation / Notebook)**

#### **2.1 Was ist Pseudocode und warum ist er nützlich?**

Nachdem wir im letzten Kapitel gelernt haben, Probleme logisch zu zerlegen, brauchen wir nun eine Methode, um unsere Lösungspläne aufzuschreiben. Hier kommt der **Pseudocode** ins Spiel.

**Analogie: Das Rezept des Chefkochs**
Ein Gedanke ("Ich will einen Schokoladenkuchen backen") ist noch kein Plan. Ein detailliertes Rezept hingegen schon. Pseudocode ist das Rezept für den Programmierer:

  * Es ist detaillierter und strukturierter als eine bloße Idee.
  * Es ist aber flexibler und verständlicher als eine starre chemische Formel (der finale Programmcode).

**Definition**
[cite\_start]Pseudocode ist ein informelles Werkzeug zur Planung von Algorithmen[cite: 115]. [cite\_start]Er ist eine Brückensprache, eine Kombination aus menschlicher Sprache und Programmiersprache[cite: 118]. Ziel ist es, die Logik eines Programms klar und verständlich darzustellen, ohne sich um die exakte Syntax einer bestimmten Programmiersprache kümmern zu müssen.

**Der Nutzen von Pseudocode**

  * [cite\_start]**Planung:** Er hilft, komplexe Abläufe zu strukturieren, bevor man programmiert[cite: 116]. Logikfehler findet man so viel schneller als im fertigen Code.
  * [cite\_start]**Kommunikation:** Er erleichtert die Erklärung von Algorithmen gegenüber Teammitgliedern oder weniger technischen Personen[cite: 125, 134].
  * [cite\_start]**Dokumentation:** Guter Pseudocode kann später als Kommentar direkt in den finalen Programmcode übernommen werden und erklärt die Absicht hinter dem Code[cite: 129].

-----

#### **2.2 Unser Pseudocode-Standard**

[cite\_start]Es gibt keinen weltweit gültigen Standard für Pseudocode[cite: 137, 138]. [cite\_start]Für unseren Kurs legen wir aber einen gemeinsamen Stil fest, damit unsere Pläne für jeden im Team klar verständlich sind[cite: 141].

**Unsere Schlüsselwörter (immer in GROSSBUCHSTABEN)**

| Schlüsselwort | Bedeutung |
| :--- | :--- |
| `START` / `ENDE` | Markiert den Anfang und das Ende des Programms. |
| `EINGABE von [Variable]` | Fordert eine Eingabe vom Benutzer an und speichert sie. |
| `AUSGABE von [Variable/Text]`| Gibt einen Wert oder Text auf dem Bildschirm aus. |
| `SETZE [Variable] AUF [Wert]`| Weist einer Variable einen Wert zu. |
| `WENN...DANN...SONST` | Leitet eine bedingte Anweisung ein (`if-else`). |
| `SOLANGE...MACHE` | Leitet eine kopfgesteuerte Schleife ein (`while`). |

**Unsere Grundregeln**

1.  [cite\_start]**Eine Anweisung pro Zeile:** Jeder Schritt ist eine eigene Zeile[cite: 225].
2.  [cite\_start]**Einrückungen zeigen Struktur:** Code-Blöcke innerhalb von Bedingungen oder Schleifen werden eingerückt[cite: 274].
3.  **Klartext statt Code:** Wir beschreiben die Logik verständlich.
      * **Gut:** `WENN zahl ungerade ist DANN`
      * [cite\_start]**Schlecht:** `WENN zahl % 2 != 0 DANN` [cite: 247]

-----

#### **2.3 Pseudocode in Aktion**

**Beispiel 1: Einfache Sequenz (Flächenberechnung)**

```
START
  AUSGABE von "Bitte die Höhe des Rechtecks eingeben:"
  EINGABE von hoehe

  AUSGABE von "Bitte die Breite des Rechtecks eingeben:"
  EINGABE von breite

  SETZE flaeche AUF hoehe * breite
  AUSGABE von "Die Fläche beträgt: " + flaeche
ENDE
```

**Beispiel 2: Selektion (Altersprüfung)**

```
START
  AUSGABE von "Bitte gib dein Alter ein:"
  EINGABE von alter

  WENN alter < 18 DANN
    AUSGABE von "Zugang für Minderjährige verweigert."
  SONST
    AUSGABE von "Zugang gewährt."
  ENDEWENN
ENDE
```

**Beispiel 3: Iteration (Countdown)**

```
START
  SETZE zaehler AUF 10

  SOLANGE zaehler > 0 MACHE
    AUSGABE von zaehler
    SETZE zaehler AUF zaehler - 1
  ENDESOLANGE

  AUSGABE von "Start!"
ENDE
```

-----

> ### 👨‍🏫 **VISUALISIERUNG & DEMO (Live via Teams)**
>
> **Tool-Empfehlung:** **Miro** oder ein anderes digitales Whiteboard.
>
> **Vorgehen:**
>
> 1.  Nimm eine der komplexeren Aufgaben aus dem letzten Übungs-Set, z.B. die **"FizzBuzz"-Aufgabe**.
> 2.  Schreibe auf dem Whiteboard nur die Aufgabenstellung hin.
> 3.  Entwickle nun den Pseudocode **live und interaktiv** mit den Schülern.
>
> **Live-Entwicklung (Beispielhafter Ablauf):**
>
>   * "Okay, was ist der allererste Schritt in jedem unserer Pläne?" -\> `START`
>   * "Was müssen wir tun? Die Zahlen von 1 bis 100 durchgehen. Welches logische Konstrukt ist das?" -\> Eine Schleife.
>   * Schreibe den Schleifenkopf hin: `FÜR jede zahl VON 1 BIS 100 MACHE`
>   * "So, und was passiert jetzt in der Schleife? Wir haben mehrere Bedingungen. Die komplexeste zuerst: Was ist, wenn die Zahl durch 3 UND 5 teilbar ist?"
>   * Füge den ersten `WENN`-Block ein: `WENN zahl durch 3 teilbar UND zahl durch 5 teilbar DANN...`
>   * "Was kommt als Nächstes? Der `SONST WENN`-Fall..."
>   * Entwickle so das gesamte logische Gerüst, bis der fertige Pseudocode auf dem Board steht.

-----

> ### 🗣️ **MANUSKRIPT LEHRER (Stichpunkte)**
>
>   * **Einstieg & Verbindung:**
>
>       * Bezug zu Kapitel 1 herstellen: "Wir haben unseren Bauplan im Kopf (Programmierlogik), jetzt brauchen wir eine Methode, ihn zu Papier zu bringen. Das ist Pseudocode."
>       * Analogie: "Das ist die Sprache, die der Architekt (ihr) benutzt, um dem Bauleiter (dem Programmierer, also auch ihr) klare Anweisungen zu geben."
>
>   * **Unser Standard:**
>
>       * *Kernbotschaft:* "Es geht hier nicht um richtig oder falsch, es geht um **Klarheit und Eindeutigkeit**. Unser Standard ist unsere Teamsprache. Solange wir uns alle daran halten, vermeiden wir Missverständnisse."
>       * Betone die Regel "Klartext statt Code". Frage: "Warum ist `WENN zahl ungerade ist` besser als `WENN zahl % 2 != 0` in dieser Planungsphase?" -\> Antwort: Weil es die *Absicht* beschreibt und nicht die *Implementierung*. Ein Nicht-Programmierer versteht es sofort.
>
>   * **Live-Demo (FizzBuzz):**
>
>       * *Interaktion:* Lass die Schüler die Schlüsselwörter vorschlagen. "Welches Schlüsselwort brauchen wir für eine Entscheidung?" -\> `WENN`. "Und für eine Wiederholung?" -\> `FÜR` oder `SOLANGE`.
>       * Führe die Schüler durch die logische Herleitung. "Warum prüfen wir 'durch 3 und 5' zuerst und nicht nur 'durch 3'?" -\> Weil eine Zahl wie 15 sonst fälschlicherweise nur als "Fizz" erkannt und die Schleife beendet würde, bevor der "FizzBuzz"-Fall geprüft wird. Dies ist ein wichtiger Punkt zur Logik von `if-elif-else`-Ketten.
>
>   * **Überleitung:**
>
>       * "Perfekt. Wir haben jetzt einen klaren, textuellen Plan. Aber Menschen sind oft visuelle Wesen. Im nächsten Kapitel schauen wir uns an, wie wir genau diesen Plan auch als Grafik zeichnen können."