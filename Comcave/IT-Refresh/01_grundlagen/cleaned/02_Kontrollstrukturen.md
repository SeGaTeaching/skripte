## **Kapitel 3: Den Programmfluss steuern – Kontrollstrukturen**

*(Dauer: ca. 2.5 Stunden)*

> ***Anmerkung für den Lehrer:** Dieses Kapitel ist sehr praxisintensiv. Jeder Block ist so konzipiert, dass du die Theorie kurz erklärst und dann direkt in die Live-Programmierung des Beispiels in den drei Sprachen übergehen kannst.*

#### **3.1 Die Gabelung im Code: Verzweigungen**

**Theorie:** Normalerweise läuft ein Programm wie ein gerader Fluss von oben nach unten ab. Das nennt man **Sequenz**. Aber oft muss ein Programm Entscheidungen treffen und je nach Situation einen anderen Weg einschlagen. Diese Gabelungen im Programmfluss nennen wir **Verzweigungen**. Sie sind das Herzstück intelligenter Programme.

-----

##### **Die `if`-Anweisung (Die einfachste Entscheidung)**

Die `if`-Anweisung prüft eine einzige Bedingung. Ist die Bedingung `wahr`, wird der zugehörige Code-Block ausgeführt. Ist sie `falsch`, wird der Block einfach übersprungen.

**Praxis-Demo:** Wir prüfen, ob es regnet und geben nur dann eine Warnung aus.

### 🐍 Python

```python
es_regnet = True
if es_regnet: # Die Prüfung auf '== True' kann man sich sparen
    print("Regenschirm nicht vergessen!")
print("Programmende.") # Dieser Teil wird immer ausgeführt
```

### 📜 JavaScript

```javascript
let esRegnet = true;
if (esRegnet) { // Auch hier ist '=== true' optional
    console.log("Regenschirm nicht vergessen!");
}
console.log("Programmende."); // Dieser Teil wird immer ausgeführt
```

### ☕ Java

```java
boolean esRegnet = true;
if (esRegnet) { // '== true' ist auch hier unnötig
    System.out.println("Regenschirm nicht vergessen!");
}
System.out.println("Programmende."); // Dieser Teil wird immer ausgeführt
```

-----

##### **Die `if-else`-Struktur (Die Entweder-Oder-Entscheidung)**

Dies ist die klassische Gabelung. Wenn die Bedingung `wahr` ist, tue A, **sonst** (`else`) tue B. Es wird immer genau einer der beiden Blöcke ausgeführt.

**Praxis-Demo:** Jacke anziehen oder nicht, basierend auf der Temperatur.

### 🐍 Python

```python
temperatur = 12
if temperatur < 15:
    print("Zieh eine Jacke an, es ist kühl.")
else:
    print("Keine Jacke nötig, das Wetter ist gut.")
```

### 📜 JavaScript

```javascript
let temperatur = 12;
if (temperatur < 15) {
    console.log("Zieh eine Jacke an, es ist kühl.");
} else {
    console.log("Keine Jacke nötig, das Wetter ist gut.");
}
```

### ☕ Java

```java
int temperatur = 12;
if (temperatur < 15) {
    System.out.println("Zieh eine Jacke an, es ist kühl.");
} else {
    System.out.println("Keine Jacke nötig, das Wetter ist gut.");
}
```

-----

##### **Die `if-else if-else`-Kaskade (Die mehrstufige Entscheidung)**

Hiermit können wir mehrere Bedingungen nacheinander prüfen. Sobald eine Bedingung `wahr` ist, wird der zugehörige Block ausgeführt und der Rest der Kette wird ignoriert. Der `else`-Block am Ende fängt alle übrigen Fälle ab.

**Praxis-Demo:** Noten-Feedback basierend auf einer Schulnote.

### 🐍 Python

```python
note = 2
if note == 1:
    print("Sehr gut!")
elif note == 2:
    print("Gut.")
elif note == 3:
    print("Befriedigend.")
else:
    print("Ausreichend oder schlechter.")
```

### 📜 JavaScript

```javascript
let note = 2;
if (note === 1) {
    console.log("Sehr gut!");
} else if (note === 2) {
    console.log("Gut.");
} else if (note === 3) {
    console.log("Befriedigend.");
} else {
    console.log("Ausreichend oder schlechter.");
}
```

### ☕ Java

```java
int note = 2;
if (note == 1) {
    System.out.println("Sehr gut!");
} else if (note == 2) {
    System.out.println("Gut.");
} else if (note == 3) {
    System.out.println("Befriedigend.");
} else {
    System.out.println("Ausreichend oder schlechter.");
}
```

-----

##### **Die `switch-case`-Anweisung (Der Spezialist für einen Wert)**

**Theorie:** Eine `switch-case`-Anweisung ist oft besser lesbar als eine lange `if-else-if`-Kette, wenn wir **eine einzelne Variable** auf viele verschiedene, exakte Werte prüfen. Wichtig ist das `break`-Statement, da der Code sonst in den nächsten `case` "durchfällt" (fall-through), was manchmal gewollt, aber meist ein Fehler ist.

> ***Anmerkung für den Lehrer:** Python hat erst seit Version 3.10 ein `match-case`. Zeige hier die moderne `match`-Variante und erwähne, dass man in älteren Versionen `if-elif-else` oder Dictionaries als Workaround nutzt. Das ist ein gutes Detail für die Praxis.*

**Praxis-Demo:** Das Noten-Feedback-Beispiel mit `switch-case`.

### 🐍 Python

```python
# Modernes Python (ab 3.10) mit match-case
note = 2
match note:
    case 1:
        print("Sehr gut!")
    case 2:
        print("Gut.")
    case 3:
        print("Befriedigend.")
    case _: # Der "default" Fall
        print("Ausreichend oder schlechter.")
```

### 📜 JavaScript

```javascript
let note = 2;
switch (note) {
    case 1:
        console.log("Sehr gut!");
        break; // Wichtig, sonst wird auch der nächste Fall ausgeführt!
    case 2:
        console.log("Gut.");
        break;
    case 3:
        console.log("Befriedigend.");
        break;
    default: // Fängt alle anderen Werte ab
        console.log("Ausreichend oder schlechter.");
}
```

### ☕ Java

```java
int note = 2;
switch (note) {
    case 1:
        System.out.println("Sehr gut!");
        break;
    case 2:
        System.out.println("Gut.");
        break;
    case 3:
        System.out.println("Befriedigend.");
        break;
    default:
        System.out.println("Ausreichend oder schlechter.");
}
```

-----

##### **Bonus: Der Ternär-Operator (Die kompakte Zuweisung)**

**Theorie:** Eine sehr kurze Schreibweise für eine `if-else`-Anweisung, deren einziges Ziel es ist, einer Variable einen von zwei möglichen Werten zuzuweisen.

**Praxis-Demo:** Einer Status-Variable je nach Alter einen Text zuweisen.

### 🐍 Python

```python
alter = 20
# Format: WERT_WENN_WAHR if BEDINGUNG else WERT_WENN_FALSCH
status = "Volljährig" if alter >= 18 else "Minderjährig"
print(status)
```

### 📜 JavaScript

```javascript
let alter = 20;
// Format: BEDINGUNG ? WERT_WENN_WAHR : WERT_WENN_FALSCH
let status = (alter >= 18) ? "Volljährig" : "Minderjährig";
console.log(status);
```

### ☕ Java

```java
int alter = 20;
// Format: BEDINGUNG ? WERT_WENN_WAHR : WERT_WENN_FALSCH
String status = (alter >= 18) ? "Volljährig" : "Minderjährig";
System.out.println(status);
```

-----

#### **3.2 Die Kunst der Wiederholung: Schleifen**

**Theorie:** Schleifen sind das Kernkonzept des **DRY-Prinzips ("Don't Repeat Yourself")**. Statt denselben Code 100-mal zu kopieren, schreiben wir ihn einmal in eine Schleife und lassen den Computer die Wiederholungen für uns erledigen.

-----

##### **Die `while`-Schleife (Die kopfgesteuerte Schleife)**

**Theorie:** Die `while`-Schleife wiederholt einen Code-Block, **solange** eine Bedingung `wahr` ist. Die Bedingung wird **vor** jedem Durchlauf geprüft. Wenn die Bedingung von Anfang an `falsch` ist, wird der Schleifen-Körper kein einziges Mal ausgeführt.

> ***Anmerkung für den Lehrer:** Dies ist der beste Ort, um über **Endlosschleifen** zu sprechen. Zeige ein Beispiel, bei dem die Schleifenvariable nicht verändert wird, und erkläre, warum das Programm dann "hängen" bleibt.*

**Praxis-Demo:** Ein Countdown von 5 bis 1.

### 🐍 Python

```python
zaehler = 5
while zaehler > 0:
    print(zaehler)
    zaehler = zaehler - 1 # Wichtig: Die Bedingung verändern!
print("Start!")
```

### 📜 JavaScript

```javascript
let zaehler = 5;
while (zaehler > 0) {
    console.log(zaehler);
    zaehler--; // Kurzschreibweise für zaehler = zaehler - 1
}
console.log("Start!");
```

### ☕ Java

```java
int zaehler = 5;
while (zaehler > 0) {
    System.out.println(zaehler);
    zaehler--;
}
System.out.println("Start!");
```

-----

##### **Die `do-while`-Schleife (Die fußgesteuerte Schleife)**

**Theorie:** Diese Schleife ist der `while`-Schleife sehr ähnlich, mit einem entscheidenden Unterschied: Die Bedingung wird erst **am Ende** des Durchlaufs geprüft. Das garantiert, dass der Code-Block **mindestens einmal** ausgeführt wird, selbst wenn die Bedingung von Anfang an `falsch` ist.

> ***Anmerkung für den Lehrer:** Da Python keine direkte `do-while`-Schleife hat, ist die gezeigte `while True` mit `if...break`-Struktur der gängige und wichtige Workaround, den jeder Python-Entwickler kennen muss.*

**Praxis-Demo:** Ein Menü, das mindestens einmal angezeigt wird.

### 🐍 Python (Workaround)

```python
while True: # Beginnt eine Endlosschleife
    eingabe = input("Nochmal? (j/n): ")
    if eingabe.lower() != 'j':
        break # Bricht die Schleife bei jeder Eingabe außer 'j' ab
print("Schleife beendet.")
```

### 📜 JavaScript

```javascript
let eingabe;
do {
    // In einer echten Anwendung würde man hier eine Eingabe vom Benutzer lesen.
    // Wir simulieren es für die Demo:
    eingabe = "n"; // Simuliert die Eingabe 'n'
    console.log("Block wurde ausgeführt...");
} while (eingabe === "j"); // Prüft am Ende
console.log("Schleife beendet.");
```

### ☕ Java

```java
// Benötigt ein Scanner-Objekt für echte Eingaben
// import java.util.Scanner;
// Scanner scanner = new Scanner(System.in);
String eingabe;
do {
    System.out.println("Block wurde ausgeführt...");
    System.out.print("Nochmal? (j/n): ");
    // eingabe = scanner.nextLine();
    eingabe = "n"; // Simulation für die Demo
} while (eingabe.equals("j"));
System.out.println("Schleife beendet.");
```

-----

##### **Die `for`-Schleife (Der Zählspezialist)**

**Theorie:** Die `for`-Schleife ist die erste Wahl, wenn man vorher weiß, wie oft ein Code-Block wiederholt werden soll (z. B. "führe 10-mal aus", "gehe alle Elemente in einer Liste durch"). In Java/JS besteht sie aus drei Teilen: **Initialisierung** einer Zählvariable, **Bedingung** für die Wiederholung und **Inkrementierung** der Zählvariable. Python nutzt eine lesbarere `for item in sequenz`-Struktur.

**Praxis-Demo:** Die 7er-Reihe ausgeben.

### 🐍 Python

```python
# range(1, 11) erzeugt die Zahlen 1 bis 10
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

### 📜 JavaScript

```javascript
// for (Initialisierung; Bedingung; Inkrement)
for (let i = 1; i <= 10; i++) {
    console.log("7 x " + i + " = " + (7 * i));
}
```

### ☕ Java

```java
// for (Initialisierung; Bedingung; Inkrement)
for (int i = 1; i <= 10; i++) {
    System.out.println("7 x " + i + " = " + (7 * i));
}
```

-----

##### **Bonus: `break` und `continue` (Die Schleifen-Dompteure)**

**Theorie:** Manchmal müssen wir den Ablauf einer Schleife von innen heraus steuern.

  * `break`: Beendet die Schleife sofort und vollständig. Der Code wird nach der Schleife fortgesetzt.
  * `continue`: Beendet nur den **aktuellen Durchlauf** und springt sofort zum Anfang der nächsten Iteration.

**Praxis-Demo:**

  * `break`: Eine Zahl in einer Sammlung finden.
  * `continue`: Nur ungerade Zahlen ausgeben.

### 🐍 Python

```python
# break-Beispiel
zahlen = [1, 5, 12, 17, 25, 30]
for zahl in zahlen:
    if zahl == 17:
        print("Die 17 wurde gefunden!")
        break # Schleife sofort beenden
    print(f"Prüfe {zahl}...")

# continue-Beispiel
for i in range(1, 11):
    if i % 2 == 0: # Wenn die Zahl gerade ist...
        continue # ...überspringe den Rest des Blocks und starte die nächste Iteration
    print(i) # Wird nur für ungerade Zahlen ausgeführt
```

### 📜 JavaScript

```javascript
// break-Beispiel
let zahlen = [1, 5, 12, 17, 25, 30];
for (let zahl of zahlen) { // for..of ist hier eleganter
    if (zahl === 17) {
        console.log("Die 17 wurde gefunden!");
        break;
    }
    console.log("Prüfe " + zahl + "...");
}

// continue-Beispiel
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        continue;
    }
    console.log(i);
}
```

### ☕ Java

```java
// break-Beispiel
int[] zahlen = {1, 5, 12, 17, 25, 30};
for (int zahl : zahlen) { // "Enhanced for loop"
    if (zahl == 17) {
        System.out.println("Die 17 wurde gefunden!");
        break;
    }
    System.out.println("Prüfe " + zahl + "...");
}

// continue-Beispiel
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
    System.out.println(i);
}
```