### **Kapitel 1: Vom Problem zum Plan – Die Logik hinter dem Code**

*(Dauer: ca. 2 Stunden)*

#### **1.1 Einführung: Die Reise vom Wunsch zur Lösung**

Willkommen in der Welt der Programmierung\! Fast jede Software, die wir heute nutzen, begann mit einem einfachen Wunsch oder einem Problem. "Ich möchte mit meinen Freunden in Kontakt bleiben" führte zu Social Media. "Ich muss meine Finanzen überblicken" führte zu Banking-Apps.

Unsere Aufgabe als Programmierer ist es, die Brücke zwischen einem menschlichen Wunsch und einer technischen Lösung zu bauen. Einfach "drauf los zu programmieren" ist wie der Versuch, ein Haus ohne Bauplan zu errichten – es wird sehr wahrscheinlich schiefgehen. Der erste und wichtigste Schritt ist immer das **Denken** und **Planen**.

#### **1.2 Die Kunst des Kochens: Der Algorithmus**

Stellt euch vor, ihr wollt einen Kuchen backen. Ihr folgt einem Rezept. Dieses Rezept ist eine Liste von Anweisungen in einer bestimmten Reihenfolge:

1.  Heize den Ofen auf 200°C vor.
2.  Mische 250g Mehl, 150g Zucker und 1 Päckchen Backpulver in einer Schüssel.
3.  Füge 3 Eier und 100ml Milch hinzu.
4.  Verrühre alles zu einem glatten Teig.
5.  Fülle den Teig in eine Form und backe ihn für 45 Minuten.

Genau das ist ein **Algorithmus**: eine **eindeutige, endliche Folge von Anweisungen zur Lösung eines Problems**. Ein Computer ist wie ein extrem gehorsamer, aber auch extrem begriffsstutziger Koch. Er tut *exakt*, was man ihm sagt – nicht mehr und nicht weniger. Wenn eine Anweisung fehlt (z.B. "Ofen vorheizen"), wird das Ergebnis unbrauchbar sein.

#### **1.3 Was ist ein Programm?**

Ein Programm ist im Grunde nichts anderes als ein Algorithmus (ein Rezept), der in einer Sprache geschrieben ist, die ein Computer verstehen kann. Diese Sprachen nennen wir **Programmiersprachen**. Sie sind das eigentliche Werkzeug, mit dem wir unsere logischen Pläne in eine Form gießen, die eine Maschine ausführen kann.

#### **1.4 Die Sprachen der Maschine**

Es gibt hunderte Programmiersprachen, und jede hat ihre Stärken. Man kann sie grob in Kategorien einteilen. Für uns sind zunächst zwei wichtig:

  * **Skriptsprachen (oft für das Web):** Sprachen wie **JavaScript** werden häufig direkt im Webbrowser ausgeführt. Sie sind oft flexibler und verzeihen mehr Fehler, was sie für Anfänger zugänglich macht. Sie erwecken Webseiten zum Leben.
  * **Kompilierte Sprachen (oft für Anwendungen):** Sprachen wie **Java** oder **C++** werden vor der Ausführung von einem "Compiler" in Maschinencode übersetzt. Dieser Prozess ist strenger, findet mehr Fehler im Voraus und führt oft zu schnelleren Programmen. Sie sind das Fundament für Betriebssysteme, große Unternehmensanwendungen und Spiele.

In diesem Kurs werden wir sehen, dass die *logischen Konzepte* (wie das Rezept) in fast allen Sprachen gleich sind. Nur die "Vokabeln" und die "Grammatik" (die **Syntax**) ändern sich.

---

### **Kapitel 2: Das Gedächtnis des Programms – Variablen und Datentypen**

*(Dauer: ca. 3.5 Stunden)*

> ***Anmerkung für den Lehrer:** Dies ist der überarbeitete, stark erweiterte Text für Kapitel 2. Die Praxis-Demos sind jetzt deutlich ausführlicher und für die Live-Vorführung gedacht. Die Code-Beispiele sind in ausklappbaren Blöcken organisiert, um die Übersicht zu wahren.*

#### **2.1 Variablen-Grundlagen**

Wie wir besprochen haben, ist eine Variable wie eine beschriftete Schublade in einer Kommode. Sie hat einen **Namen** (das Etikett) und einen **Wert** (der Inhalt). Die grundlegenden Aktionen sind die **Deklaration** (Schublade beschriften), **Initialisierung** (erstmals befüllen) und **Zuweisung** (Inhalt austauschen).

---

#### **2.2 Primitive Datentypen (Die atomaren Bausteine)**

Primitive Datentypen sind die fundamentalen, nicht weiter zerlegbaren Bausteine der Programmierung. Sie speichern immer nur einen einzigen, simplen Wert.

##### **Ganze Zahlen (`int`, `number`)**

Der Datentyp für alles Zählbare ohne Nachkommastellen.

**Praxis-Demo: Arithmetik & Modulo**
Der Modulo-Operator (`%`) ist extrem nützlich. Er gibt den Rest einer Division zurück. Ein klassischer Anwendungsfall: Prüfen, ob eine Zahl gerade ist (`zahl % 2 == 0`).


- **Python**

```python
a = 10
b = 3

# Arithmetik
print(f"Summe: {a + b}") # 13
print(f"Ganzzahl-Division: {a // b}") # 3
print(f"Gleitkomma-Division: {a / b}") # 3.33...

# Modulo
print(f"Rest bei 10 / 3: {a % b}") # 1
print(f"Ist 10 gerade? {10 % 2 == 0}") # True
```



- **JavaScript**

```javascript
let a = 10;
let b = 3;

// Arithmetik
console.log("Summe: " + (a + b)); // 13
console.log("Division: " + (a / b)); // 3.33...

// Modulo
console.log("Rest bei 10 / 3: " + (a % b)); // 1
console.log("Ist 10 gerade? " + (10 % 2 === 0)); // true
```



- **Java**

```java
int a = 10;
int b = 3;

// Arithmetik
System.out.println("Summe: " + (a + b)); // 13
// Achtung: int-Division schneidet den Rest ab!
System.out.println("Ganzzahl-Division: " + (a / b)); // 3 

// Modulo
System.out.println("Rest bei 10 / 3: " + (a % b)); // 1
System.out.println("Ist 10 gerade? " + (10 % 2 == 0)); // true
```



**Praxis-Demo: Typumwandlung (int -\> float)**
Man kann eine Ganzzahl problemlos in eine Gleitkommazahl umwandeln. Dabei gehen keine Informationen verloren.


- **Python**

```python
ganze_zahl = 5
gleitkommazahl = float(ganze_zahl)
print(f"{ganze_zahl} wird zu {gleitkommazahl}") # 5 wird zu 5.0
```



- **JavaScript**

```javascript
// In JS gibt es nur 'number', die Umwandlung ist also nicht nötig/sichtbar.
let zahl = 5;
console.log(zahl); // 5
```



- **Java**

```java
int ganzeZahl = 5;
double gleitkommaZahl = (double) ganzeZahl; // Explizites "Casting"
System.out.println(ganzeZahl + " wird zu " + gleitkommaZahl); // 5 wird zu 5.0
```



##### **Gleitkommazahlen (`float`, `double`, `number`)**

Für alle Zahlen mit Nachkommastellen.

> ***Anmerkung für den Lehrer:** Hier ist der Moment, um kurz zu demonstrieren, was `0.1 + 0.2` in der Konsole ergibt, um die Präzisions-Thematik greifbar zu machen.*

**Praxis-Demo: Rundungsfunktionen**
Oft müssen wir Zahlen auf- oder abrunden. Dafür gibt es eingebaute mathematische Funktionen.


- **Python**

```python
import math

preis = 9.75

# Kaufmännisch runden (Standard)

print(f"Gerundet: {round(preis)}") \# 10

# Abrunden

print(f"Abgerundet (floor): {math.floor(preis)}") \# 9

# Aufrunden

print(f"Aufgerundet (ceil): {math.ceil(preis)}") \# 10

```

- **JavaScript**
```javascript
let preis = 9.75;
// Kaufmännisch runden
console.log("Gerundet: " + Math.round(preis)); // 10
// Abrunden
console.log("Abgerundet (floor): " + Math.floor(preis)); // 9
// Aufrunden
console.log("Aufgerundet (ceil): " + Math.ceil(preis)); // 10
```



- **Java**

```java
double preis = 9.75;
// Kaufmännisch runden
System.out.println("Gerundet: " + Math.round(preis)); // 10
// Abrunden
System.out.println("Abgerundet (floor): " + Math.floor(preis)); // 9.0
// Aufrunden
System.out.println("Aufgerundet (ceil): " + Math.ceil(preis)); // 10.0
```



**Praxis-Demo: Typumwandlung (float -\> int)**
Hierbei wird der Nachkommaanteil einfach **abgeschnitten**. Es findet **kein Runden** statt\! Das ist ein wichtiger Punkt, der oft zu Fehlern führt.


- **Python**

```python
preis = 9.75
ganze_zahl = int(preis)
print(f"{preis} wird zu {ganze_zahl}") # 9.75 wird zu 9
```



- **JavaScript**

```javascript
let preis = 9.75;
let ganzeZahl = parseInt(preis); // parseInt schneidet Nachkommastellen ab
console.log(preis + " wird zu " + ganzeZahl); // 9.75 wird zu 9
```

- **Java**

```java
double preis = 9.75;
int ganzeZahl = (int) preis; // Explizites "Casting"
System.out.println(preis + " wird zu " + ganzeZahl); // 9.75 wird zu 9
```

##### **Wahrheitswerte (`boolean`, `bool`)**

Kann nur zwei Zustände annehmen: `wahr` oder `falsch`. Das Fundament für alle Entscheidungen im Code.

**Praxis-Demo: Logische Operatoren**
`AND` (&&): Beide Bedingungen müssen wahr sein.
`OR` (||): Mindestens eine Bedingung muss wahr sein.
`NOT` (\!): Kehrt den Wahrheitswert um.

Beispiel: Man darf nur ins Kino, wenn man volljährig ist **UND** ein Ticket hat.
Man bekommt Rabatt, wenn es Dienstag ist **ODER** man einen Gutschein hat.

- **Python**

```python
alter = 20
hat_ticket = True
# AND
darf_ins_kino = alter &gt;= 18 and hat_ticket
print(f"Darf ins Kino? {darf_ins_kino}") # True

ist\_dienstag = False
hat\_gutschein = True

# OR

bekommt\_rabatt = ist\_dienstag or hat\_gutschein
print(f"Bekommt Rabatt? {bekommt\_rabatt}") \# True

# NOT

licht\_an = True
print(f"Licht ist an: {licht\_an}") \# True
print(f"Licht ist NICHT an: {not licht\_an}") \# False

```

- **JavaScript**
  
```javascript
let alter = 20;
let hatTicket = true;
// AND
let darfInsKino = alter >= 18 && hatTicket;
console.log("Darf ins Kino? " + darfInsKino); // true

let istDienstag = false;
let hatGutschein = true;
// OR
let bekommtRabatt = istDienstag || hatGutschein;
console.log("Bekommt Rabatt? " + bekommtRabatt); // true

// NOT
let lichtAn = true;
console.log("Licht ist an: " + lichtAn); // true
console.log("Licht ist NICHT an: " + \!lichtAn); // false

```

- **Java**

```java
int alter = 20;
boolean hatTicket = true;
// AND
boolean darfInsKino = alter &gt;= 18 &amp;&amp; hatTicket;
System.out.println("Darf ins Kino? " + darfInsKino); // true

boolean istDienstag = false;
boolean hatGutschein = true;
// OR
boolean bekommtRabatt = istDienstag || hatGutschein;
System.out.println("Bekommt Rabatt? " + bekommtRabatt); // true

// NOT
boolean lichtAn = true;
System.out.println("Licht ist an: " + lichtAn); // true
System.out.println("Licht ist NICHT an: " + \!lichtAn); // false

```

---

#### **2.3 Der erste komplexe Typ: Zeichenketten (`String`, `str`)**

**Theorie: Primitiv oder Komplex?**
Ein `String` ist der perfekte Übergang von der primitiven zur komplexen Welt. Warum?

  * Ein primitiver Typ (z.B. `int`) speichert nur **einen simplen Wert**. Er hat keine eigenen "Fähigkeiten".
  * Ein komplexer Typ (ein **Objekt**) ist eine Struktur, die **Daten enthält UND Fähigkeiten (Methoden)** besitzt.

Ein String enthält Daten (die Zeichenkette) und hat eingebaute Fähigkeiten wie `.toUpperCase()`, die wir mit einem Punkt aufrufen. Deshalb behandeln wir ihn als unseren ersten komplexen Typ. In Java und Python ist ein `String` auch technisch ein Objekt.

**Theorie: Unveränderlichkeit (Immutability)**
In Java und Python sind Strings unveränderlich. Das bedeutet, eine Operation wie `.toUpperCase()` ändert nicht den ursprünglichen String, sondern erzeugt und liefert einen **neuen** String zurück.

**Massive Praxis-Demo: String-Methoden**

##### Länge ermitteln


```python
# Python
text = "Hallo Welt"
print(len(text)) # 10
```

```javascript
// JavaScript
let text = "Hallo Welt";
console.log(text.length); // 10
```

```java
// Java
String text = "Hallo Welt";
System.out.println(text.length()); // 10
```

##### Groß-/Kleinschreibung

```python
# Python
text = "Hallo Welt"
print(text.upper()) # HALLO WELT
print(text.lower()) # hallo welt
```

```javascript
// JavaScript
let text = "Hallo Welt";
console.log(text.toUpperCase()); // HALLO WELT
console.log(text.toLowerCase()); // hallo welt
```

```java
// Java
String text = "Hallo Welt";
System.out.println(text.toUpperCase()); // HALLO WELT
System.out.println(text.toLowerCase()); // hallo welt
```

##### Leerräume entfernen

Entfernt Leerzeichen am Anfang und Ende. Extrem wichtig bei Benutzereingaben.


```python
# Python
text = "  viel Leerraum  """
print(text.strip())
```

```javascript
// JavaScript
let text = "  viel Leerraum  ";
console.log("'" + text.trim() + "'"); // 'viel Leerraum'
```

```java
// Java
String text = "  viel Leerraum  ";
System.out.println("'" + text.trim() + "'"); // 'viel Leerraum'
```

##### Teile ersetzen

```python
# Python
text = "Ich mag Tee."
neuer_text = text.replace("Tee", "Kaffee")
print(neuer_text) # Ich mag Kaffee.
print(text) # Ich mag Tee. (Original ist unverändert!)
```

```javascript
// JavaScript
let text = "Ich mag Tee.";
let neuerText = text.replace("Tee", "Kaffee");
console.log(neuerText); // Ich mag Kaffee.
console.log(text); // Ich mag Tee. (Original ist unverändert!)
```

```java
// Java
String text = "Ich mag Tee.";
String neuerText = text.replace("Tee", "Kaffee");
System.out.println(neuerText); // Ich mag Kaffee.
System.out.println(text); // Ich mag Tee. (Original ist unverändert!)
```

##### Text aufteilen (`split`)

Zerlegt einen String anhand eines Trennzeichens in eine Liste/Array.


```python
# Python
einkaufsliste = "Milch,Brot,Eier"
teile = einkaufsliste.split(',')
print(teile) # ['Milch', 'Brot', 'Eier']
```

```javascript
// JavaScript
let einkaufsliste = "Milch,Brot,Eier";
let teile = einkaufsliste.split(',');
console.log(teile); // ["Milch", "Brot", "Eier"]
```

```java
// Java
String einkaufsliste = "Milch,Brot,Eier";
String[] teile = einkaufsliste.split(",");
// Ein Array gibt man in Java so aus:
System.out.println(java.util.Arrays.toString(teile)); // [Milch, Brot, Eier]
```

##### Teilstring extrahieren

```python
# Python (Slicing)
text = "Hallo Welt"
# extrahiere von Index 0 bis (aber nicht einschließlich) 5
print(text[0:5]) # Hallo
```

```javascript
// JavaScript (substring)
let text = "Hallo Welt";
// extrahiere von Index 0 bis (aber nicht einschließlich) 5
console.log(text.substring(0, 5)); // Hallo
```

```java
// Java (substring)
String text = "Hallo Welt";
// extrahiere von Index 0 bis (aber nicht einschließlich) 5
System.out.println(text.substring(0, 5)); // Hallo
```

---

#### **2.4 Ausblick: Weitere Komplexe Typen (Der erste Blick in die Werkzeugkiste)**

> ***Anmerkung für den Lehrer:** Dies ist der gewünschte Ausblick. Wichtig ist, zu betonen, dass dies nur ein kurzer Vorgeschmack ist und die wahre Tiefe dieser Typen in Block 3 behandelt wird.*

**Theorie:** Bisher kann eine Variable nur einen Wert speichern. Was aber, wenn wir eine ganze Einkaufsliste, alle Schüler einer Klasse oder alle Eigenschaften eines Autos speichern wollen? Dafür brauchen wir "Sammelbehälter". Die zwei wichtigsten sind Listen und Dictionaries.

**Praxis-Demo 1: Die Liste/Das Array (eine geordnete Einkaufsliste)**
Eine geordnete Sammlung von Elementen. Jedes Element hat einen festen Platz (Index), der bei 0 beginnt.


```python
# Python: 'list'
einkaufsliste = ["Milch", "Brot", "Eier"]
print(einkaufsliste[0]) # Gibt das erste Element aus: Milch
```

```javascript
// JavaScript: 'Array'
let einkaufsliste = ["Milch", "Brot", "Eier"];
console.log(einkaufsliste[0]); // Gibt das erste Element aus: Milch
```

```java
// Java: 'Array'
String[] einkaufsliste = {"Milch", "Brot", "Eier"};
System.out.println(einkaufsliste[0]); // Gibt das erste Element aus: Milch
```

**Praxis-Demo 2: Das Dictionary/Objekt (ein Steckbrief)**
Eine ungeordnete Sammlung von Schlüssel-Wert-Paaren. Man greift nicht über einen Index zu, sondern über den eindeutigen Schlüssel.


```python
# Python: 'dict'
person = {
    "name": "Max Mustermann",
    "alter": 30
}
print(person["name"]) # Gibt den Wert des Schlüssels 'name' aus
```

```javascript
// JavaScript: 'Object'
let person = {
    name: "Max Mustermann",
    alter: 30
};
console.log(person.name); // Zugriff mit Punkt-Notation
```

```java
// Java: 'Map' (komplexer, daher nur konzeptionell)
// In Java ist dies aufwändiger und ein klares Thema für später.
// Map<String, Object> person = new HashMap<>();
// person.put("name", "Max Mustermann");
// person.put("alter", 30);
// System.out.println(person.get("name"));
System.out.println("In Java wird dies mit 'Maps' realisiert, das schauen wir uns in Block 3 genau an!");
```


**Wichtiger Hinweis:** Das war nur ein kurzer Vorgeschmack. Die wahre Macht dieser Sammelbehälter – wie man Elemente hinzufügt, löscht oder sie mit Schleifen durchläuft – ist das zentrale Thema von Block 3\!

---

#### **2.5 Die finale Vergleichstabelle der Datentypen**

| Konzept | C | Java | Python | JavaScript | Anmerkung |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ganze Zahl** | `int`, `long` | `int`, `long` | `int` | `number` | Python's `int` kann beliebig groß werden. JS unterscheidet nicht zwischen Ganz- und Gleitkommazahlen. |
| **Gleitkommazahl**| `float`, `double`| `float`, `double`| `float` | `number` | `double` ist die präzisere Variante und meist der Standard. |
| **Wahrheitswert**| `bool` (via Header)| `boolean` | `bool` | `boolean` | Die Werte sind immer `true` und `false` (in Python: `True` und `False`). |
| **Zeichenkette** | `char[]` | `String` (Objekt) | `str` (Objekt) | `string` (Primitiv) | Obwohl in JS primitiv, verhält es sich wie ein Objekt. In C sind Strings Arrays von Zeichen. |
| **Typisierung** | Statisch | Statisch | Dynamisch| Dynamisch | Statisch: Typ muss bei Deklaration feststehen. Dynamisch: Typ wird zur Laufzeit bestimmt. |

Ja, wird erledigt. Hier ist der neue, eingeschobene Skript-Text für **Kapitel 2.6** mit einem starken Fokus auf Code-Beispiele, die das Zusammenspiel von Stack und Heap für die Vorführung verdeutlichen.

-----

### **Kapitel 2.6: Ein Blick unter die Haube – Variablen im Speicher**

*(Dauer: ca. 1.5 - 2 Stunden)*

> ***Anmerkung für den Lehrer:** Dieses Kapitel ist sehr theoretisch, aber fundamental. Der Schlüssel zum Verständnis liegt in der Visualisierung. Zeichne die Stack- und Heap-Speicherbereiche am besten live an einem Whiteboard oder in einem Grafikprogramm parallel zu den Code-Beispielen.*

#### **2.6.1 Das Gedächtnis des Computers: RAM als Kommode**

Stellt euch den Arbeitsspeicher (RAM) eures Computers wie eine riesige Kommode mit Millionen von kleinen Schubladen vor. Jede Schublade hat eine eindeutige Nummer, ihre **Speicheradresse**. Wenn unser Programm läuft, mietet es sich einen Teil dieser Kommode, um seine Daten (Variablen) abzulegen. Dieser gemietete Teil wird hauptsächlich in zwei Bereiche aufgeteilt: den **Stack** und den **Heap**.

-----

#### **2.6.2 Der Stack (Der ordentliche Stapel)**

  * **Analogie:** Ein Stapel Teller. Man kann immer nur den obersten Teller nehmen und einen neuen nur oben drauflegen. Dieses Prinzip nennt man **LIFO (Last-In, First-Out)**.
  * **Was kommt auf den Stack?**
    1.  **Primitive Datentypen:** In Sprachen wie Java oder C\# werden die **Werte** von `int`, `double`, `boolean` etc. direkt auf dem Stack gespeichert.
    2.  **Referenzen (Speicheradressen):** Das sind die "Ticketnummern" oder Zeiger, die uns sagen, wo im großen Heap-Lager wir das eigentliche Objekt finden.
  * **Eigenschaften:**
      * **Sehr schnell:** Weil die Organisation so starr und einfach ist.
      * **Automatische Verwaltung:** Sobald eine Funktion beendet wird, wird ihr gesamter Bereich auf dem Stack automatisch und sofort "aufgeräumt".
      * **Begrenzte Größe:** Der Stack-Speicher ist relativ klein.

-----

#### **2.6.3 Der Heap (Der große Haufen)**

  * **Analogie:** Eine riesige, unorganisierte Lagerhalle. Wenn wir etwas Großes (ein Objekt) speichern wollen, geben wir es ab, es wird irgendwo im Lager platziert und wir bekommen eine **Ticketnummer (die Referenz)** zurück.
  * **Was kommt auf den Heap?**
    1.  **Alle Objekte:** Instanzen von Klassen (`String`, `Person`, etc.).
    2.  **Alle Arrays/Listen.**
  * **Eigenschaften:**
      * **Flexibel:** Objekte können zur Laufzeit erstellt werden und beliebig lange leben.
      * **Langsamer:** Die Suche nach freiem Platz und der Zugriff über eine Adresse sind aufwändiger.
      * **Manuelle/Automatische Verwaltung:** In Sprachen wie C/C++ muss der Programmierer den Speicher selbst freigeben. In Java, Python und JS übernimmt das die **"Müllabfuhr" (Garbage Collector)**, die regelmäßig nach ungenutzten Objekten sucht und sie löscht.

-----

#### **2.6.4 Das Zusammenspiel am Praxisbeispiel**

> ***Anmerkung für den Lehrer:** Die folgenden Beispiele eignen sich am besten für eine Vorführung in **Java**, da hier die Unterscheidung zwischen primitiven Typen und Referenztypen am klarsten ist. Erkläre, dass das Konzept in Python/JS ähnlich ist, aber durch die dynamische Typisierung weniger sichtbar.*

##### **Szenario 1: Primitive vs. Referenztypen**

Wir analysieren Zeile für Zeile, was im Speicher passiert.

**Der Code:**

```java
public void speicherDemo() {
    int alter = 30; // Primitiver Typ
    String name = "Max"; // Komplexer Typ (Objekt)
}
```

**Was passiert im Speicher?**

1.  **`int alter = 30;`**

      * Da `int` ein **primitiver Typ** ist, wird der Wert direkt auf dem Stack abgelegt.
      * **STACK:** `[ alter | 30 ]`
      * **HEAP:** (bleibt unberührt)

2.  **`String name = "Max";`**

      * Da `String` ein **Objekt** ist, passiert ein Zwei-Schritt-Prozess:
      * Schritt A: Das String-Objekt mit dem Inhalt "Max" wird im **Heap** erstellt. Sagen wir, es bekommt die fiktive Speicheradresse `@123`.
      * Schritt B: Die Variable `name` wird auf dem **Stack** angelegt, speichert aber nicht den Text selbst, sondern nur die **Referenz (Adresse)** `@123`.
      * **STACK:** `[ alter | 30 ] [ name | @123 ]`
      * **HEAP:** `(Adresse: @123) --> [ String-Objekt: "Max" ]`

-----

##### **Szenario 2: Zuweisung von Variablen - Der entscheidende Unterschied**

Dies ist die wichtigste Demo, um das Konzept zu verstehen\! Was passiert, wenn wir Variablen einander zuweisen?

**Der Code:**

```java
// ... Fortsetzung von oben
int alter_kopie = alter;
String name_kopie = name;

// Jetzt ändern wir die Originale
alter = 35;
name = "Anna";
```

**Was passiert im Speicher?**

1.  **`int alter_kopie = alter;`**

      * Der **Wert** von `alter` (`30`) wird kopiert und in `alter_kopie` auf dem Stack gespeichert. Es sind zwei unabhängige Variablen.
      * **STACK:** `[ alter | 30 ] [ name | @123 ] [ alter_kopie | 30 ]`

2.  **`String name_kopie = name;`**

      * Die **Referenz** von `name` (`@123`) wird kopiert und in `name_kopie` gespeichert. Beide Variablen zeigen jetzt auf **dasselbe Objekt** im Heap\!
      * **STACK:** `[ alter | 30 ] [ name | @123 ] [ alter_kopie | 30 ] [ name_kopie | @123 ]`
      * **HEAP:** `(Adresse: @123) --> [ String-Objekt: "Max" ]`

**Jetzt die Änderungen:**

3.  **`alter = 35;`**

      * Nur der Wert in der Schublade `alter` auf dem Stack wird geändert. `alter_kopie` ist davon **unberührt**.
      * **STACK:** `[ alter | 35 ] [ name | @123 ] [ alter_kopie | 30 ] [ name_kopie | @123 ]`

4.  **`name = "Anna";`**

      * Hier passiert etwas ganz anderes\! Es wird ein **neues** String-Objekt "Anna" im Heap erstellt (z.B. an Adresse `@456`). Die Variable `name` auf dem Stack bekommt diese **neue** Referenz. `name_kopie` zeigt aber **immer noch** auf die alte Adresse `@123` mit dem Objekt "Max".
      * **STACK:** `[ alter | 35 ] [ name | @456 ] [ alter_kopie | 30 ] [ name_kopie | @123 ]`
      * **HEAP:** `(Adresse: @123) --> [ String-Objekt: "Max" ]`
      * **HEAP:** `(Adresse: @456) --> [ String-Objekt: "Anna" ]`

> ***Anmerkung für den Lehrer:** Dieses Beispiel ist perfekt, um die Konzepte **"Value Type"** (bei Primitiven) und **"Reference Type"** (bei Objekten) zu erklären. Bei Value Types wird der Wert kopiert, bei Reference Types die Adresse.*

-----

#### **2.6.5 Vergleichstabelle: Stack vs. Heap**

| Eigenschaft | Stack (Der Stapel) | Heap (Der Haufen) |
| :--- | :--- | :--- |
| **Geschwindigkeit**| Sehr schnell | Langsamer |
| **Gespeicherte Daten**| Primitive Typen & Referenzen auf Objekte | Die Objekte selbst & Arrays |
| **Verwaltung** | Automatisch (Last-In, First-Out) | Komplex (Garbage Collector) |
| **Größe** | Klein und fest | Groß und dynamisch wachsend |
| **Lebensdauer** | Nur solange die Funktion aktiv ist | Solange eine Referenz auf das Objekt existiert |


---

Stack und Heap in der Speicherverwaltung

Einleitung

Beim Programmieren in Sprachen wie Java, C++ oder auch bei der Ausführung von Python-Programmen ist es wichtig zu verstehen, wie Daten im Speicher abgelegt werden. Zwei zentrale Speicherbereiche spielen hierbei eine Rolle: der Stack und der Heap. Dieses Skript erklärt die Unterschiede, die Funktionsweise, typische Anwendungsbeispiele und die Vor- und Nachteile beider Speicherformen.

⸻

1. Der Stack

1.1 Was ist der Stack?

Der Stack (Stapel) ist ein spezieller Speicherbereich, der nach dem Prinzip Last In, First Out (LIFO) arbeitet. Er wird primär zur Verwaltung von Funktionsaufrufen und lokalen Variablen verwendet.

1.2 Eigenschaften
	•	Sehr schneller Speicherzugriff
	•	Automatische Speicherverwaltung (durch das Betriebssystem)
	•	Lineare Speicherstruktur
	•	Feste Speichergröße (meist im MB-Bereich begrenzt)

1.3 Was wird im Stack gespeichert?
	•	Primitive Datentypen (z. B. int, boolean, char in Java)
	•	Lokale Variablen (nicht Objekte, sondern deren Referenzen)
	•	Funktions-/Methodenaufrufinformationen (z. B. Rücksprungadressen)

1.4 Beispiel Java

int x = 5;  // x liegt im Stack
String name = "Anna";  // name ist Referenz im Stack, Objekt im Heap


⸻

2. Der Heap

2.1 Was ist der Heap?

Der Heap ist ein dynamischer Speicherbereich, der zur Laufzeit vom Programm genutzt wird, um Objekte und komplexe Datenstrukturen zu speichern. Im Gegensatz zum Stack erfolgt die Speicherverwaltung über einen Garbage Collector oder manuell (z. B. in C/C++).

2.2 Eigenschaften
	•	Speichergröße deutlich größer als beim Stack
	•	Flexibler, aber langsamer Zugriff
	•	Speicher bleibt bestehen, bis er explizit freigegeben oder vom Garbage Collector entsorgt wird
	•	Nicht linear organisiert

2.3 Was wird im Heap gespeichert?
	•	Objekte (z. B. Instanzen von Klassen)
	•	Arrays
	•	Strings in Java (als Objekte)

2.4 Beispiel Java

Person p = new Person(); // p ist Referenz im Stack, Objekt im Heap


⸻

3. Warum die Trennung zwischen Stack und Heap?

3.1 Vorteile der Trennung
	•	Performanceoptimierung: Stack ist sehr schnell, Heap sehr flexibel
	•	Lebensdauersteuerung: Stack-Daten leben nur während der Funktionsausführung, Heap-Daten können global oder persistent sein
	•	Speicherorganisation: Ermöglicht parallele Verwaltung und Bereinigung (GC)

3.2 Nachteile der Trennung
	•	Komplexität: Entwickler müssen Referenztypen und Speicherverhalten verstehen
	•	Speicherlecks im Heap: Wenn Objekte nicht korrekt entfernt werden (bei fehlendem GC)
	•	Stackoverflow-Risiko: Zu viele oder zu tiefe Funktionsaufrufe können den Stack sprengen

⸻

4. Vergleich: Stack vs. Heap

Merkmal	Stack	Heap
Speicherart	Automatisch verwaltet	Dynamisch verwaltet
Speichergröße	Klein (MB)	Groß (bis GB)
Zugriffsgeschwindigkeit	Sehr schnell	Langsamer
Lebensdauer der Daten	Kurzlebig (Funktionszeitraum)	Langlebig (bis zur GC-Löschung)
Verwaltung	durch Compiler/Runtime	durch Garbage Collector
Inhalt	Primitive Werte, Referenzen	Objekte, Arrays


⸻

5. Python im Vergleich

In Python gibt es technisch gesehen ebenfalls einen Stack (für Funktionsaufrufe), aber alle Daten – selbst Zahlen und Strings – werden als Objekte im Heap gespeichert. Variablen sind lediglich Referenzen auf diese Objekte. Dadurch ist Python sehr flexibel, aber speicherintensiver und weniger performant bei einfachen Operationen.

Beispiel:

x = 42       # int-Objekt im Heap, x ist Referenz
name = "Tim" # str-Objekt im Heap, name ist Referenz


⸻

Fazit

Die Unterscheidung zwischen Stack und Heap ist ein fundamentaler Bestandteil des Speicher- und Performancemanagements in vielen Programmiersprachen. Statische Sprachen wie Java oder C++ trennen strikt zwischen diesen Bereichen, um Kontrolle, Effizienz und Vorhersagbarkeit zu gewährleisten. Dynamische Sprachen wie Python verzichten auf diese Trennung zugunsten von Einfachheit und Flexibilität – mit entsprechenden Kosten bei Performance und Speicherverbrauch.
