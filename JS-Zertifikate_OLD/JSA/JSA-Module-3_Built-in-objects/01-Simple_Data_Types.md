
# 3.1 Simple Data Types in JavaScript

In der Programmierung hat jedes Datenstück einen Typ, der dem Interpreter oder Compiler angibt, wie die Daten behandelt werden sollen. Diese Datentypen lassen sich in zwei Kategorien einteilen: **Primitive** (einfache) und **Komposite** (zusammengesetzte) Datentypen.

## 3.1.1 Primitive Datentypen

Primitive Datentypen enthalten einen einzigen Wert, wie zum Beispiel eine Zahl oder einen Text. Sie sind grundlegend und nicht in kleinere Bestandteile zerlegbar. Zu den primitiven Datentypen in JavaScript gehören:

- `boolean`
- `number`
- `string`

Primitive Datentypen haben selbst keine Methoden oder Eigenschaften. Sie sind reine Werte, die im entsprechenden Format im Speicher abgelegt werden.

## 3.1.2 Primitives und Autoboxing

Für jeden primitiven Datentyp gibt es in JavaScript spezielle Konstruktoren, die als Klassen fungieren. Diese sind:

- `Boolean`
- `Number`
- `String`

Diese Konstruktoren sind eingebaut und bieten hilfreiche Methoden und Eigenschaften für die Arbeit mit primitiven Datentypen. Der Grund, warum wir diese Konstruktoren nutzen, liegt in der Bequemlichkeit. Sie ermöglichen die Verwendung von Methoden über eine einfache Punktnotation, was den Code klarer und einfacher macht.

### Beispiel 1: Nutzung eines String-Objekts

```javascript
let strObj = new String("Do bats eat cats?");
console.log(typeof(strObj)); // -> object
console.log(strObj.length);  // -> 17
let words = strObj.split(" ");
console.log(words[0]);  // -> Do
```

In diesem Beispiel wird ein `String`-Objekt erstellt und wir können auf Methoden wie `.length` und `.split()` zugreifen, um die Länge des Strings zu ermitteln und ihn in einzelne Wörter zu zerlegen.

### Beispiel 2: Nutzung eines primitiven Strings mit Autoboxing

```javascript
let str = "Do bats eat cats?";
console.log(typeof(str));  // -> string
console.log(str.length);   // -> 17
let words = str.split(" ");
console.log(words[0]);     // -> Do
```

Hier verwenden wir einen primitiven String. Überraschenderweise können wir trotzdem auf `.length` und `.split()` zugreifen, obwohl primitive Typen keine Methoden haben. Dies geschieht durch **Autoboxing**: Der JavaScript-Engine konvertiert den primitiven Typ zur Laufzeit in ein temporäres Objekt, führt die Methode aus und entfernt das Objekt danach wieder aus dem Speicher.

### Beispiel 3: Number-Objekt vs. primitive Zahl

```javascript
let numObj = new Number(42);
console.log(typeof(numObj));  // -> object
console.log(numObj.toFixed(2));  // -> 42.00

let num = 42;
console.log(typeof(num));  // -> number
console.log(num.toFixed(2));  // -> 42.00
```

Auch hier sehen wir, dass sowohl das `Number`-Objekt als auch die primitive Zahl die Methode `.toFixed()` verwenden können. Bei der primitiven Zahl wird diese Funktionalität durch Autoboxing bereitgestellt.

### Empfehlung

Nutze **primitive Datentypen**, wann immer möglich. Das Erstellen von Objekten mittels `Boolean`, `Number` oder `String`-Konstruktoren ist zwar möglich, aber nicht empfohlen. Der JavaScript-Engine kann die benötigte Konvertierung automatisch durchführen, wenn du mit einem primitiven Typ arbeitest.

## Zusammenfassung

- Primitive Datentypen sind grundlegende Werte ohne Methoden oder Eigenschaften.
- JavaScript bietet eingebaute Objekte (`Boolean`, `Number`, `String`) für die Arbeit mit primitiven Werten an.
- **Autoboxing** ermöglicht es, primitive Typen wie Objekte zu behandeln, indem der JavaScript-Engine diese temporär in Objekte umwandelt.
- Aus Speicher- und Performancegründen sollten jedoch primitive Typen bevorzugt verwendet werden.

