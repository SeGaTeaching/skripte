
# JavaScript Math Objekt

Das `Math`-Objekt in JavaScript ist kein Konstruktor, sondern ein gewöhnliches Objekt, das mathematische Methoden und Konstanten zur Verfügung stellt. 
In dieser Anleitung werden die gängigsten Methoden und ihre Verwendung mit zusätzlichen Beispielen erläutert.

---

## 1. Mathematische Konstanten

JavaScript stellt mit dem `Math`-Objekt einige wichtige mathematische Konstanten bereit, wie die Kreiszahl π und die Basis des natürlichen Logarithmus e.

### Beispiel
```javascript
console.log(Math.PI); // -> 3.141592653589793
console.log(Math.E);  // -> 2.718281828459045
```

#### Zusatzbeispiel 1
```javascript
console.log("Kreisumfang für Radius 10: " + 2 * Math.PI * 10); // -> 62.83185307179586
console.log("Exponentielles Wachstum e^3: " + Math.pow(Math.E, 3)); // -> 20.085536923187668
```

#### Zusatzbeispiel 2
```javascript
console.log("Kreisfläche für Radius 7: " + Math.PI * Math.pow(7, 2)); // -> 153.93804002589985
console.log("Annäherung an e^2: " + Math.E * Math.E); // -> 7.3890560989306495
```

---

## 2. Runden

Die Methoden `Math.ceil()`, `Math.floor()` und `Math.round()` sind gängige Rundungsmethoden.

- `Math.ceil()` rundet auf die nächste ganze Zahl nach oben.
- `Math.floor()` rundet auf die nächste ganze Zahl nach unten.
- `Math.round()` rundet je nach Dezimalstelle.

### Beispiel
```javascript
console.log(Math.ceil(5.3));  // -> 6
console.log(Math.floor(5.3)); // -> 5
console.log(Math.round(5.5)); // -> 6
```

#### Zusatzbeispiel 1
```javascript
console.log(Math.ceil(-3.7));  // -> -3
console.log(Math.floor(-3.7)); // -> -4
console.log(Math.round(-3.5)); // -> -3
```

#### Zusatzbeispiel 2
```javascript
console.log(Math.ceil(0.1));   // -> 1
console.log(Math.floor(0.9));  // -> 0
console.log(Math.round(0.49)); // -> 0
```

---

## 3. Zufallszahlen generieren

Mit `Math.random()` lässt sich eine Pseudo-Zufallszahl zwischen 0 (inklusive) und 1 (exklusive) generieren.

### Beispiel
```javascript
console.log(Math.random()); // -> z.B. 0.4523
```

#### Zusatzbeispiel 1
```javascript
console.log(Math.random() * 10); // Zufallszahl zwischen 0 und 10
console.log(Math.floor(Math.random() * 100)); // Ganze Zufallszahl zwischen 0 und 99
```

#### Zusatzbeispiel 2
```javascript
console.log(Math.ceil(Math.random() * 50)); // Ganze Zufallszahl zwischen 1 und 50
console.log(Math.floor(Math.random() * 5) + 1); // Ganze Zufallszahl zwischen 1 und 5
```

---

## 4. Wichtige Mathematische Funktionen

### Absolute Werte mit `Math.abs()`
```javascript
console.log(Math.abs(-42)); // -> 42
```

#### Zusatzbeispiel 1
```javascript
console.log(Math.abs(0)); // -> 0
console.log(Math.abs(-0.5)); // -> 0.5
```

#### Zusatzbeispiel 2
```javascript
console.log(Math.abs(-123.456)); // -> 123.456
console.log(Math.abs(987.654)); // -> 987.654
```

### Kleinster und größter Wert: `Math.min()` und `Math.max()`
```javascript
console.log(Math.min(5, 10, 15)); // -> 5
console.log(Math.max(5, 10, 15)); // -> 15
```

#### Zusatzbeispiel 1
```javascript
let zahlen = [3, 7, 2, 8, -1];
console.log(Math.min(...zahlen)); // -> -1
console.log(Math.max(...zahlen)); // -> 8
```

#### Zusatzbeispiel 2
```javascript
console.log(Math.min(100, 200, 300)); // -> 100
console.log(Math.max(-50, -100, 0)); // -> 0
```

---

## 5. Potenzieren und Wurzelziehen

### Potenz mit `Math.pow()` und Quadratwurzel mit `Math.sqrt()`
```javascript
console.log(Math.pow(3, 3));   // -> 27
console.log(Math.sqrt(16));    // -> 4
```

#### Zusatzbeispiel 1
```javascript
console.log(Math.pow(5, 2));   // -> 25
console.log(Math.sqrt(81));    // -> 9
```

#### Zusatzbeispiel 2
```javascript
console.log(Math.pow(2, 10));  // -> 1024
console.log(Math.sqrt(144));   // -> 12
```

---

Die Datei enthält viele zusätzliche Beispiele und wird Ihnen und Ihren Schülern als umfassende Einführung in das `Math`-Objekt in JavaScript dienen.
