
# 3.1.4 Number in JavaScript

Der `Number`-Konstruktor repräsentiert den primitiven Zahlentyp und steht für Gleitkommazahlen im 64-Bit-Format.

## Eigenschaften von JavaScript-Zahlen

JavaScript verwendet für alle Zahlen einen einzigen Zahlentyp, der sowohl Ganzzahlen als auch Gleitkommazahlen abdeckt. Es gibt keine Unterscheidung zwischen diesen in JavaScript. Es gibt jedoch einige wichtige Einschränkungen:

- Zahlen werden als Annäherungen gespeichert.
- Der Wertebereich ist begrenzt. Für Ganzzahlen ist der kleinste Wert `-(2^53 - 1)` und der größte Wert `(2^53 - 1)`.

In der Praxis kann man jedoch auch größere Werte speichern, wobei die Genauigkeit leidet. Um größere Werte mit genauerer Darstellung zu speichern, kann der `BigInt`-Typ verwendet werden.

### Zahlenformate in JavaScript

Zahlen können in verschiedenen Formaten dargestellt werden:

- **Dezimal**: Der Standardmodus.
- **Hexadezimal**: Präfix `0x`.
- **Oktal**: Präfix `0o`.
- **Binär**: Präfix `0b`.
- **Exponentiell**: Zum Beispiel `9e3` für 9000.

### Beispiel 1: Verschiedene Zahlenformate

```javascript
let a = 10;   // Dezimal
let b = 0x10; // Hexadezimal
let c = 0o10; // Oktal
let d = 0b10; // Binär
console.log(a); // -> 10
console.log(b); // -> 16
console.log(c); // -> 8
console.log(d); // -> 2
```

### Beispiel 2: Gleitkommazahlen und Rundungsfehler

```javascript
let x = 0.3;
let y = 0.6;
console.log(x + y); // -> 0.8999999999999999
console.log((x + y).toFixed(1));    // -> 0.9
console.log(x / 0);      // -> Infinity
console.log(x / "abc");  // -> NaN
```

## 3.1.5 Number Konstruktor

Der `Number`-Konstruktor kann wie bei anderen primitiven Typen zur Erstellung von Objekten verwendet werden. Dies wird jedoch nicht empfohlen. Ohne den `new`-Operator konvertiert der Konstruktor das übergebene Argument in eine primitive Zahl.

### Beispiel 3: Verwendung von `Number` ohne `new`

```javascript
let nr = Number("100");
console.log(`nr : ${typeof nr} : ${nr}`); // -> nr : number : 100
```

### Beispiel 4: Verwendung des `Number`-Konstruktors mit `new`

```javascript
let numberObj1 = new Number();            // -> 0
let numberObj2 = new Number(100);         // -> 100
let numberObj3 = new Number("200");       // -> 200
let numberObj4 = new Number("abcd");      // -> NaN
let numberObj5 = new Number(9e10000);     // -> Infinity
console.log(numberObj1.valueOf()); // -> 0
```

## 3.1.6 Konvertierung von Zahlen in verschiedene String-Formate

Die Methode `toString()` kann mit einem Argument aufgerufen werden, das angibt, in welchem Format die Zahl zurückgegeben werden soll (z.B. Hexadezimal).

### Beispiel 5: Verwendung von `toString()`

```javascript
let nrStr1 = (11).toString();
let nrStr2 = (11).toString(16);
console.log(`nrStr1 : ${nrStr1}`); // -> 11
console.log(`nrStr2 : ${nrStr2}`); // -> b
```

Weitere nützliche Methoden sind `toExponential()`, `toFixed()` und `toLocaleString()`.

### Beispiel 6: Verwendung von `toExponential()` und `toFixed()`

```javascript
let a = 12345;
console.log(a.toExponential());   // -> 1.2345e+4
console.log(a.toExponential(1));  // -> 1.2e+4

let nr1 = 10.55;
console.log(nr1.toFixed(1)); // -> 10.6
console.log(nr1.toFixed(0)); // -> 11
console.log(nr1.toFixed(3)); // -> 10.550
```

### Beispiel 7: Verwendung von `toLocaleString()`

```javascript
let nr = 123456.789;
console.log(nr.toLocaleString("en-GB")); // -> 123,456.789
console.log(nr.toLocaleString("de-DE")); // -> 123.456,789
console.log(nr.toLocaleString("es-ES", { style: "currency", currency: "EUR" })); // -> 123.456,79 €
```

## 3.1.7 Statische Eigenschaften und Methoden von Number

Der `Number`-Konstruktor stellt einige statische Eigenschaften und Methoden zur Verfügung, um Werte zu überprüfen oder Begrenzungen zu testen.

### Beispiel 8: Statische Eigenschaften von `Number`

```javascript
console.log(Number.MAX_VALUE);      // -> 1.7976931348623157e+308
console.log(Number.MIN_VALUE);      // -> 5e-324
console.log(Number.MAX_SAFE_INTEGER); // -> 9007199254740991
console.log(Number.MIN_SAFE_INTEGER); // -> -9007199254740991
```

### Beispiel 9: Statische Methoden von `Number`

```javascript
let numbers = [2e100, 200000, 1.5, Infinity];
for (let i = 0; i < numbers.length; i++) {
    console.log(`is ${numbers[i]} Integer: ${Number.isInteger(numbers[i])}`);
    console.log(`is ${numbers[i]} safe Integer: ${Number.isSafeInteger(numbers[i])}`);
    console.log(`is ${numbers[i]} finite number: ${Number.isFinite(numbers[i])}`);
}
```

- `isInteger()` prüft, ob der Wert eine Ganzzahl ist.
- `isSafeInteger()` prüft, ob der Wert innerhalb des sicheren Ganzzahlbereichs liegt.
- `isFinite()` prüft, ob der Wert endlich ist.

### Beispiel 10: Verwendung von `parseInt()` und `parseFloat()`

```javascript
console.log(Number.parseFloat("123.12.12")); // -> 123.12
console.log(Number.parseInt("1204px")); // -> 1204
```

Diese Methoden können hilfreich sein, wenn Zeichenfolgen in Zahlen umgewandelt werden sollen, auch wenn sie nicht korrekt formatiert sind.

## Zusammenfassung

- Der `Number`-Konstruktor repräsentiert den primitiven Zahlentyp in JavaScript.
- Zahlen können in verschiedenen Formaten dargestellt werden: Dezimal, Hexadezimal, Oktal, Binär und Exponential.
- Verwende `toString()`, `toFixed()` und `toLocaleString()`, um Zahlen in verschiedene String-Formate zu konvertieren.
- Statische Methoden und Eigenschaften von `Number` ermöglichen die Überprüfung von Ganzzahlen, sicheren Ganzzahlen und endlichen Werten.
