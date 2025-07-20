## Übungs-Set: Schleifen (`for`, `while`)

### **Aufgaben**

#### **Einfache Aufgaben (Grundlagen)**

1.  **Zähle bis 10:** Schreibe eine Schleife, die alle Zahlen von 1 bis 10 auf der Konsole ausgibt.
2.  **Countdown:** Gib einen Countdown von 10 bis 1 aus. Nach der 1 soll "Start\!" ausgegeben werden.
3.  **Summe berechnen:** Berechne die Summe aller Zahlen von 1 bis 50.
4.  **Gerade Zahlen:** Gib alle geraden Zahlen zwischen 1 und 20 aus.
5.  **Zeichen für Zeichen:** Gib jeden Buchstaben eines eingegebenen Wortes einzeln in einer neuen Zeile aus.
6.  **Einmaleins:** Erstelle die Multiplikationstabelle für die Zahl 8 (von 8x1 bis 8x10).
7.  **Passwort-Abfrage:** Simuliere eine Passwort-Abfrage, die so lange nach dem Passwort fragt, bis der Benutzer "geheim" eingibt. Gib danach "Zugang gewährt" aus.

#### **Mittelschwere Aufgaben (Logik & Kombinationen)**

8.  **Fakultät berechnen:** Berechne die Fakultät einer Zahl `n` (n\!). Die Fakultät von 5 (5\!) ist z.B. `5 * 4 * 3 * 2 * 1 = 120`.
9.  **Vokale zählen:** Zähle die Anzahl der Vokale (a, e, i, o, u) in einem eingegebenen Satz. Groß- und Kleinschreibung soll ignoriert werden.
10. **Maximum finden:** Finde die größte Zahl in einer vorgegebenen Liste/einem Array von Zahlen, ohne eine eingebaute `max()`-Funktion zu verwenden.
11. **Fibonacci-Folge:** Generiere die ersten 15 Zahlen der Fibonacci-Folge (0, 1, 1, 2, 3, 5, 8, ...).
12. **Wort umkehren:** Kehre eine eingegebene Zeichenfolge um, ohne eine eingebaute `reverse()`-Funktion zu benutzen. Aus "Hallo" wird "ollaH".
13. **Quersumme:** Berechne die Quersumme einer Zahl. Die Quersumme von 472 ist z.B. `4 + 7 + 2 = 13`.
14. **Zahlenraten:** Das Programm "denkt" sich eine Zufallszahl zwischen 1 und 100. Der Benutzer muss raten. Nach jedem Versuch gibt das Programm einen Hinweis ("zu hoch" oder "zu niedrig"), bis die Zahl erraten wurde.
15. **`break`-Anweisung:** Summiere die Zahlen in einer Liste. Wenn die Schleife auf eine negative Zahl trifft, soll sie sofort abbrechen und die bis dahin berechnete Summe ausgeben.

#### **Schwerere Aufgaben (Verschachtelte Logiken & Muster)**

16. **Primzahl-Prüfung:** Prüfe, ob eine eingegebene Zahl eine Primzahl ist. Eine Primzahl ist nur durch 1 und sich selbst teilbar.
17. **Rechteck zeichnen:** Zeichne ein Rechteck aus Sternchen (`*`) basierend auf einer eingegebenen Höhe und Breite.
18. **Dreieck zeichnen:** Zeichne ein rechtwinkliges Dreieck aus Sternchen (`*`) basierend auf einer eingegebenen Höhe.
19. **FizzBuzz:** Gehe die Zahlen von 1 bis 100 durch.
      * Wenn eine Zahl durch 3 teilbar ist, gib "Fizz" aus.
      * Wenn eine Zahl durch 5 teilbar ist, gib "Buzz" aus.
      * Wenn eine Zahl durch 3 und 5 teilbar ist, gib "FizzBuzz" aus.
      * Ansonsten gib die Zahl selbst aus.
20. **Alle Teiler finden:** Finde und gib alle Teiler einer eingegebenen Zahl aus. Die Teiler von 12 sind z.B. 1, 2, 3, 4, 6, 12.

---

<div style="page-break-after: always;"></div>


### **Lösungen**

### 🐍 Python Lösungen

```python
# 1. Zähle bis 10
for i in range(1, 11):
    print(i)

# 2. Countdown
for i in range(10, 0, -1):
    print(i)
print("Start!")

# 3. Summe berechnen
summe = 0
for i in range(1, 51):
    summe += i
print(f"Summe 1-50: {summe}")

# 4. Gerade Zahlen
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 5. Zeichen für Zeichen
wort = "Python"
for char in wort:
    print(char)

# 6. Einmaleins
for i in range(1, 11):
    print(f"8 x {i} = {8 * i}")

# 7. Passwort-Abfrage
while input("Passwort: ") != "geheim":
    print("Falsch. Versuche es erneut.")
print("Zugang gewährt")

# 8. Fakultät berechnen
n = 5
fakultaet = 1
for i in range(1, n + 1):
    fakultaet *= i
print(f"Fakultät von {n} ist {fakultaet}")

# 9. Vokale zählen
satz = "Hallo Welt, wie geht es dir?"
anzahl_vokale = 0
for char in satz.lower():
    if char in "aeiou":
        anzahl_vokale += 1
print(f"Anzahl Vokale: {anzahl_vokale}")

# 10. Maximum finden
zahlen = [4, 12, 5, 42, 18, 3]
maximum = zahlen[0]
for zahl in zahlen:
    if zahl > maximum:
        maximum = zahl
print(f"Maximum: {maximum}")

# 11. Fibonacci-Folge
a, b = 0, 1
for _ in range(15):
    print(a, end=" ")
    a, b = b, a + b
print()

# 12. Wort umkehren
wort_original = "Hallo"
wort_umgekehrt = ""
for char in wort_original:
    wort_umgekehrt = char + wort_umgekehrt
print(f"'{wort_original}' umgekehrt ist '{wort_umgekehrt}'")

# 13. Quersumme
zahl = 472
quersumme = 0
temp_zahl = zahl
while temp_zahl > 0:
    ziffer = temp_zahl % 10
    quersumme += ziffer
    temp_zahl //= 10
print(f"Quersumme von {zahl} ist {quersumme}")

# 14. Zahlenraten
import random
zufallszahl = random.randint(1, 100)
while True:
    tipp = int(input("Rate eine Zahl zwischen 1 und 100: "))
    if tipp < zufallszahl:
        print("Zu niedrig!")
    elif tipp > zufallszahl:
        print("Zu hoch!")
    else:
        print("Korrekt!")
        break

# 15. `break`-Anweisung
zahlen_liste = [10, 20, 5, -3, 40]
summe_break = 0
for zahl in zahlen_liste:
    if zahl < 0:
        break
    summe_break += zahl
print(f"Summe bis zur negativen Zahl: {summe_break}")

# 16. Primzahl-Prüfung
num_prim = 29
ist_prim = True
if num_prim > 1:
    for i in range(2, int(num_prim**0.5) + 1):
        if num_prim % i == 0:
            ist_prim = False
            break
else:
    ist_prim = False
print(f"Ist {num_prim} eine Primzahl? {ist_prim}")

# 17. Rechteck zeichnen
hoehe, breite = 4, 10
for i in range(hoehe):
    print("*" * breite)

# 18. Dreieck zeichnen
hoehe_dreieck = 5
for i in range(1, hoehe_dreieck + 1):
    print("*" * i)

# 19. FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 20. Alle Teiler finden
zahl_teiler = 12
print(f"Teiler von {zahl_teiler}:", end=" ")
for i in range(1, zahl_teiler + 1):
    if zahl_teiler % i == 0:
        print(i, end=" ")
print()

```

<div style="page-break-after: always;"></div>

### 📜 JavaScript Lösungen

```javascript
// 1. Zähle bis 10
for (let i = 1; i <= 10; i++) { console.log(i); }

// 2. Countdown
for (let i = 10; i > 0; i--) { console.log(i); }
console.log("Start!");

// 3. Summe berechnen
let summe = 0;
for (let i = 1; i <= 50; i++) { summe += i; }
console.log(`Summe 1-50: ${summe}`);

// 4. Gerade Zahlen
for (let i = 1; i <= 20; i++) { if (i % 2 === 0) { console.log(i); } }

// 5. Zeichen für Zeichen
const wort = "JavaScript";
for (const char of wort) { console.log(char); }

// 6. Einmaleins
for (let i = 1; i <= 10; i++) { console.log(`8 x ${i} = ${8 * i}`); }

// 7. Passwort-Abfrage (simuliert für non-interaktive Umgebung)
let passwortInput = "";
while (passwortInput !== "geheim") {
    // In einer echten Umgebung: passwortInput = prompt("Passwort:");
    passwortInput = "geheim"; // Simulation
    console.log("Prüfe Eingabe...");
}
console.log("Zugang gewährt");

// 8. Fakultät berechnen
let n = 5;
let fakultaet = 1;
for (let i = 1; i <= n; i++) { fakultaet *= i; }
console.log(`Fakultät von ${n} ist ${fakultaet}`);

// 9. Vokale zählen
const satz = "Hallo Welt, wie geht es dir?";
let anzahlVokale = 0;
for (const char of satz.toLowerCase()) {
    if ("aeiou".includes(char)) { anzahlVokale++; }
}
console.log(`Anzahl Vokale: ${anzahlVokale}`);

// 10. Maximum finden
const zahlen = [4, 12, 5, 42, 18, 3];
let maximum = zahlen[0];
for (const zahl of zahlen) { if (zahl > maximum) { maximum = zahl; } }
console.log(`Maximum: ${maximum}`);

// 11. Fibonacci-Folge
let a = 0, b = 1;
let fiboString = "";
for (let i = 0; i < 15; i++) {
    fiboString += a + " ";
    let temp = a + b;
    a = b;
    b = temp;
}
console.log(fiboString.trim());

// 12. Wort umkehren
const wortOriginal = "Hallo";
let wortUmgekehrt = "";
for (let i = wortOriginal.length - 1; i >= 0; i--) {
    wortUmgekehrt += wortOriginal[i];
}
console.log(`'${wortOriginal}' umgekehrt ist '${wortUmgekehrt}'`);

// 13. Quersumme
let zahl = 472;
let quersumme = 0;
let tempZahl = zahl;
while (tempZahl > 0) {
    quersumme += tempZahl % 10;
    tempZahl = Math.floor(tempZahl / 10);
}
console.log(`Quersumme von ${zahl} ist ${quersumme}`);

// 14. Zahlenraten (simuliert)
const zufallszahl = 42; // Math.floor(Math.random() * 100) + 1;
let tipp = 0;
while (tipp !== zufallszahl) {
    tipp = 50; // Simuliert Tipp
    if (tipp < zufallszahl) console.log("Zu niedrig!");
    else if (tipp > zufallszahl) console.log("Zu hoch!");
    else console.log("Korrekt!");
    if(tipp !== zufallszahl) tipp = 42; // Simuliert zweiten, korrekten Tipp
}


// 15. `break`-Anweisung
const zahlenListe = [10, 20, 5, -3, 40];
let summeBreak = 0;
for (const zahl of zahlenListe) {
    if (zahl < 0) { break; }
    summeBreak += zahl;
}
console.log(`Summe bis zur negativen Zahl: ${summeBreak}`);

// 16. Primzahl-Prüfung
let numPrim = 29;
let istPrim = true;
if (numPrim > 1) {
    for (let i = 2; i <= Math.sqrt(numPrim); i++) {
        if (numPrim % i === 0) { istPrim = false; break; }
    }
} else { istPrim = false; }
console.log(`Ist ${numPrim} eine Primzahl? ${istPrim}`);

// 17. Rechteck zeichnen
let hoehe = 4, breite = 10;
for (let i = 0; i < hoehe; i++) { console.log("*".repeat(breite)); }

// 18. Dreieck zeichnen
let hoeheDreieck = 5;
for (let i = 1; i <= hoeheDreieck; i++) { console.log("*".repeat(i)); }

// 19. FizzBuzz
for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) console.log("FizzBuzz");
    else if (i % 3 === 0) console.log("Fizz");
    else if (i % 5 === 0) console.log("Buzz");
    else console.log(i);
}

// 20. Alle Teiler finden
let zahlTeiler = 12;
let teilerString = "";
for (let i = 1; i <= zahlTeiler; i++) {
    if (zahlTeiler % i === 0) { teilerString += i + " "; }
}
console.log(`Teiler von ${zahlTeiler}: ${teilerString.trim()}`);
```

<div style="page-break-after: always;"></div>

### ☕ Java Lösungen

```java
public class UebungenSchleifen {
    public static void main(String[] args) {
        // 1. Zähle bis 10
        for (int i = 1; i <= 10; i++) { System.out.print(i + " "); }
        System.out.println();

        // 2. Countdown
        for (int i = 10; i > 0; i--) { System.out.println(i); }
        System.out.println("Start!");

        // 3. Summe berechnen
        int summe = 0;
        for (int i = 1; i <= 50; i++) { summe += i; }
        System.out.println("Summe 1-50: " + summe);

        // 4. Gerade Zahlen
        for (int i = 1; i <= 20; i++) { if (i % 2 == 0) { System.out.print(i + " "); } }
        System.out.println();

        // 5. Zeichen für Zeichen
        String wort = "Java";
        for (char c : wort.toCharArray()) { System.out.println(c); }

        // 6. Einmaleins
        for (int i = 1; i <= 10; i++) { System.out.println("8 x " + i + " = " + (8 * i)); }

        // 7. Passwort-Abfrage (simuliert)
        String passwortInput = "";
        java.util.Scanner scanner = new java.util.Scanner("test\ngeheim"); // Simulation
        while (!passwortInput.equals("geheim")) {
            System.out.print("Passwort: ");
            passwortInput = scanner.nextLine();
            if (!passwortInput.equals("geheim")) System.out.println("Falsch.");
        }
        System.out.println("Zugang gewährt");

        // 8. Fakultät berechnen
        int n = 5;
        long fakultaet = 1; // long für größere Zahlen
        for (int i = 1; i <= n; i++) { fakultaet *= i; }
        System.out.println("Fakultät von " + n + " ist " + fakultaet);
        
        // 9. Vokale zählen
        String satz = "Hallo Welt, wie geht es dir?";
        int anzahlVokale = 0;
        for (char c : satz.toLowerCase().toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                anzahlVokale++;
            }
        }
        System.out.println("Anzahl Vokale: " + anzahlVokale);

        // 10. Maximum finden
        int[] zahlen = {4, 12, 5, 42, 18, 3};
        int maximum = zahlen[0];
        for (int zahl : zahlen) { if (zahl > maximum) { maximum = zahl; } }
        System.out.println("Maximum: " + maximum);

        // 11. Fibonacci-Folge
        int a = 0, b = 1;
        for (int i = 0; i < 15; i++) {
            System.out.print(a + " ");
            int temp = a + b;
            a = b;
            b = temp;
        }
        System.out.println();

        // 12. Wort umkehren
        String wortOriginal = "Hallo";
        String wortUmgekehrt = "";
        for (int i = wortOriginal.length() - 1; i >= 0; i--) {
            wortUmgekehrt += wortOriginal.charAt(i);
        }
        System.out.println("'" + wortOriginal + "' umgekehrt ist '" + wortUmgekehrt + "'");

        // 13. Quersumme
        int zahl = 472;
        int quersumme = 0;
        int tempZahl = zahl;
        while (tempZahl > 0) {
            quersumme += tempZahl % 10;
            tempZahl /= 10;
        }
        System.out.println("Quersumme von " + zahl + " ist " + quersumme);

        // 14. Zahlenraten (simuliert)
        int zufallszahl = 42;
        int tipp = 0;
        java.util.Scanner tippScanner = new java.util.Scanner("50\n30\n42\n");
        while (tipp != zufallszahl) {
            System.out.print("Rate eine Zahl zwischen 1 und 100: ");
            tipp = tippScanner.nextInt();
            if (tipp < zufallszahl) System.out.println("Zu niedrig!");
            else if (tipp > zufallszahl) System.out.println("Zu hoch!");
            else System.out.println("Korrekt!");
        }

        // 15. `break`-Anweisung
        int[] zahlenListe = {10, 20, 5, -3, 40};
        int summeBreak = 0;
        for (int zahl : zahlenListe) {
            if (zahl < 0) { break; }
            summeBreak += zahl;
        }
        System.out.println("Summe bis zur negativen Zahl: " + summeBreak);

        // 16. Primzahl-Prüfung
        int numPrim = 29;
        boolean istPrim = true;
        if (numPrim > 1) {
            for (int i = 2; i <= Math.sqrt(numPrim); i++) {
                if (numPrim % i == 0) { istPrim = false; break; }
            }
        } else { istPrim = false; }
        System.out.println("Ist " + numPrim + " eine Primzahl? " + istPrim);
        
        // 17. Rechteck zeichnen
        int hoehe = 4, breite = 10;
        for (int i = 0; i < hoehe; i++) {
            for (int j = 0; j < breite; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 18. Dreieck zeichnen
        int hoeheDreieck = 5;
        for (int i = 1; i <= hoeheDreieck; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 19. FizzBuzz
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) System.out.println("FizzBuzz");
            else if (i % 3 == 0) System.out.println("Fizz");
            else if (i % 5 == 0) System.out.println("Buzz");
            else System.out.println(i);
        }

        // 20. Alle Teiler finden
        int zahlTeiler = 12;
        System.out.print("Teiler von " + zahlTeiler + ": ");
        for (int i = 1; i <= zahlTeiler; i++) {
            if (zahlTeiler % i == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}
```