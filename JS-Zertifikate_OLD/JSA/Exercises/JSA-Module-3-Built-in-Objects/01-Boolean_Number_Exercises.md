
# Übungen zu Boolean und Number in JavaScript

## Aufgaben

### Aufgabe 1
Erstelle ein Boolean-Objekt mit dem Standardwert und ein weiteres mit dem Wert `true`. Verwende `toString()` und `valueOf()`, um die Werte in beiden Objekten in eine Zeichenkette und einen primitiven Wert zu konvertieren.

### Aufgabe 2
Konvertiere die folgenden Werte in primitive boolesche Werte, ohne den `new` Operator zu verwenden: `"true"`, `0`, `undefined`, `1`, `NaN`.

### Aufgabe 3
Verwende `Boolean` und teste, ob eine leere Liste `[]`, ein leeres Objekt `{}` und eine nicht definierte Variable als "truthy" oder "falsy" gelten.

### Aufgabe 4
Erstelle ein Number-Objekt mit dem Wert `100` und verwende die Methoden `toString()` und `toFixed()`, um das Ergebnis in verschiedenen Formaten darzustellen: Hexadezimal, Binär und Dezimal mit 2 Nachkommastellen.

### Aufgabe 5
Verwende die statischen Methoden von `Number`, um zu überprüfen, ob die folgenden Werte Ganzzahlen sind, sicher gespeichert werden können und endliche Zahlen sind: `2e100`, `-999999999999999`, `0.5`, `Infinity`.

### Aufgabe 6
Schreibe eine Funktion, die eine Zeichenkette mit einer Zahl wie `"120px"` entgegennimmt und diese mit `parseInt()` und `parseFloat()` in eine Zahl umwandelt.

### Aufgabe 7
Verwende `toLocaleString()`, um die Zahl `123456.789` in den folgenden Regionen darzustellen: `de-DE`, `en-US`, `fr-FR`, und als Währung in Euro.

### Aufgabe 8
Runde die Zahl `1.255` mit `toFixed(2)` und erkläre, warum das Ergebnis eventuell nicht genau das ist, was du erwartest.

### Aufgabe 9
Schreibe eine Funktion, die eine Liste von Zahlen akzeptiert und für jede Zahl überprüft, ob sie eine Ganzzahl, eine sichere Ganzzahl und eine endliche Zahl ist. Gib die Ergebnisse für jede Zahl in einem strukturierten Format zurück.

### Aufgabe 10
Schreibe ein Programm, das zwei Gleitkommazahlen `x = 0.3` und `y = 0.6` addiert und das Ergebnis auf 1 Dezimalstelle mit `toFixed()` rundet. Erkläre, warum das nicht exakt `0.9` ist und wie du das Problem beheben kannst.

---

## Lösungen

### Lösung 1
```javascript
let boolObj1 = new Boolean();
let boolObj2 = new Boolean(true);
console.log(boolObj1.toString()); // -> "false"
console.log(boolObj1.valueOf());  // -> false
console.log(boolObj2.toString()); // -> "true"
console.log(boolObj2.valueOf());  // -> true
```

### Lösung 2
```javascript
console.log(Boolean("true"));      // -> true
console.log(Boolean(0));           // -> false
console.log(Boolean(undefined));   // -> false
console.log(Boolean(1));           // -> true
console.log(Boolean(NaN));         // -> false
```

### Lösung 3
```javascript
console.log(Boolean([]));   // -> true
console.log(Boolean({}));   // -> true
let notDefined;
console.log(Boolean(notDefined));  // -> false
```

### Lösung 4
```javascript
let numObj = new Number(100);
console.log(numObj.toString(16)); // -> "64" (Hexadezimal)
console.log(numObj.toString(2));  // -> "1100100" (Binär)
console.log(numObj.toFixed(2));   // -> "100.00" (Dezimal mit 2 Nachkommastellen)
```

### Lösung 5
```javascript
let values = [2e100, -999999999999999, 0.5, Infinity];
values.forEach(val => {
    console.log(`is ${val} Integer: ${Number.isInteger(val)}`);
    console.log(`is ${val} Safe Integer: ${Number.isSafeInteger(val)}`);
    console.log(`is ${val} Finite: ${Number.isFinite(val)}`);
});
```

### Lösung 6
```javascript
function convertToNumber(str) {
    let intVal = Number.parseInt(str);
    let floatVal = Number.parseFloat(str);
    return { intVal, floatVal };
}
console.log(convertToNumber("120px"));  // -> { intVal: 120, floatVal: 120 }
```

### Lösung 7
```javascript
let number = 123456.789;
console.log(number.toLocaleString("de-DE")); // -> "123.456,789"
console.log(number.toLocaleString("en-US")); // -> "123,456.789"
console.log(number.toLocaleString("fr-FR")); // -> "123 456,789"
console.log(number.toLocaleString("es-ES", { style: "currency", currency: "EUR" })); // -> "123.456,79 €"
```

### Lösung 8
```javascript
let num = 1.255;
console.log(num.toFixed(2)); // -> "1.25", aufgrund der binären Gleitkommadarstellung wird 1.255 nicht exakt dargestellt.
```

### Lösung 9
```javascript
function checkNumbers(numbers) {
    numbers.forEach(num => {
        console.log(`is ${num} Integer: ${Number.isInteger(num)}`);
        console.log(`is ${num} Safe Integer: ${Number.isSafeInteger(num)}`);
        console.log(`is ${num} Finite: ${Number.isFinite(num)}`);
    });
}
checkNumbers([2e100, 0.5, 100, Infinity]);
```

### Lösung 10
```javascript
let x = 0.3;
let y = 0.6;
let sum = x + y;
console.log(sum.toFixed(1));  // -> "0.9", die Darstellung von Gleitkommazahlen ist nicht exakt, was zu Rundungsfehlern führt.
```
