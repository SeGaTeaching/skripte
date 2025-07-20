
# Composite Data Types and Arrays in JavaScript - Exercises

## Aufgabenblock

### Aufgabe 1
**Erstelle eine Funktion, die alle geraden Zahlen aus einem Array von Zahlen entfernt und den Rest der Werte verdoppelt.**

### Aufgabe 2
**Schreibe eine Funktion, die den Durchschnittswert eines Arrays von Zahlen zurückgibt.** Benutze in deiner Lösung nur eine Schleife.

### Aufgabe 3
**Sortiere die Werte eines Arrays von Strings nach der Länge der Zeichenketten in absteigender Reihenfolge.**

### Aufgabe 4
**Erstelle eine Funktion, die ein Array von Strings akzeptiert und ein neues Array zurückgibt, das nur Strings enthält, die mit dem Buchstaben 'a' beginnen.**

### Aufgabe 5
**Schreibe eine Funktion, die alle positiven Zahlen in einem Array quadriert und alle negativen Zahlen entfernt.**

### Aufgabe 6
**Finde den größten und den kleinsten Wert in einem Array von Zahlen ohne Verwendung von Math.max oder Math.min.**

### Aufgabe 7
**Schreibe eine Funktion, die den Median eines Arrays von Zahlen berechnet.** (Tipp: Median ist der mittlere Wert, wenn das Array sortiert ist.)

### Aufgabe 8
**Erstelle eine Funktion, die ein Array von Objekten akzeptiert, in denen jedes Objekt eine "name"-Eigenschaft hat, und gib ein Array aller Namen zurück, die aus mindestens 5 Zeichen bestehen.**

### Aufgabe 9
**Implementiere eine Funktion, die prüft, ob ein Array eine aufsteigende Reihenfolge hat.** Die Funktion soll `true` zurückgeben, wenn das Array sortiert ist, andernfalls `false`.

### Aufgabe 10
**Schreibe eine Funktion, die alle Duplikate in einem Array entfernt und nur einzigartige Werte beibehält.**

### Aufgabe 11
**Finde die zweithöchste Zahl in einem Array.** (Tipp: Sortiere das Array und greife auf den zweitgrößten Wert zu.)

### Aufgabe 12
**Erstelle eine Funktion, die alle Zeichenketten in einem Array umdreht, jedoch nur, wenn die Zeichenkette mehr als 4 Zeichen enthält.**

### Aufgabe 13
**Schreibe eine Funktion, die die Länge jeder Zeichenkette in einem Array zählt und die Werte in einem neuen Array speichert.**

### Aufgabe 14
**Erstelle eine Funktion, die ein Array von Zahlen akzeptiert und ein neues Array zurückgibt, das nur die Zahlen enthält, deren Summe der Ziffern gerade ist.**

### Aufgabe 15
**Schreibe eine Funktion, die die Anzahl der Vorkommen jedes Elements in einem Array zählt und als Objekt zurückgibt.** Die Schlüssel im Objekt sollen die Werte aus dem Array sein, die Werte die Häufigkeiten.

### Aufgabe 16
**Erstelle eine Funktion, die zwei Arrays akzeptiert und ein neues Array zurückgibt, das die Schnittmenge der beiden Arrays enthält.** (Tipp: Nur Werte, die in beiden Arrays vorkommen, sollen enthalten sein.)

### Aufgabe 17
**Schreibe eine Funktion, die ein Array von Strings akzeptiert und ein neues Array zurückgibt, das nur Strings mit einer ungeraden Anzahl von Zeichen enthält.**

### Aufgabe 18
**Erstelle eine Funktion, die überprüft, ob alle Elemente eines Arrays entweder wahrheitsgemäß (truthy) oder falsch (falsy) sind.**

### Aufgabe 19
**Schreibe eine Funktion, die alle Zahlen aus einem Array verdoppelt und dann alle Werte, die größer als 10 sind, entfernt.**

### Aufgabe 20
**Erstelle eine Funktion, die die Summe der Differenzen zwischen aufeinanderfolgenden Elementen in einem Array berechnet.**

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
function processArray(arr) {
    return arr.filter(num => num % 2 !== 0).map(num => num * 2);
}
```

### Lösung zu Aufgabe 2
```javascript
function averageArray(arr) {
    return arr.reduce((sum, num) => sum + num, 0) / arr.length;
}
```

### Lösung zu Aufgabe 3
```javascript
function sortByStringLength(arr) {
    return arr.slice().sort((a, b) => b.length - a.length);
}
```

### Lösung zu Aufgabe 4
```javascript
function filterStringsStartingWithA(arr) {
    return arr.filter(str => str[0].toLowerCase() === 'a');
}
```

### Lösung zu Aufgabe 5
```javascript
function processNumbers(arr) {
    return arr.filter(num => num > 0).map(num => num * num);
}
```

### Lösung zu Aufgabe 6
```javascript
function findMinMax(arr) {
    let min = arr[0], max = arr[0];
    arr.forEach(num => {
        if (num > max) max = num;
        if (num < min) min = num;
    });
    return { min, max };
}
```

### Lösung zu Aufgabe 7
```javascript
function findMedian(arr) {
    arr = arr.slice().sort((a, b) => a - b);
    const mid = Math.floor(arr.length / 2);
    return arr.length % 2 !== 0 ? arr[mid] : (arr[mid - 1] + arr[mid]) / 2;
}
```

### Lösung zu Aufgabe 8
```javascript
function filterLongNames(arr) {
    return arr.filter(obj => obj.name.length >= 5).map(obj => obj.name);
}
```

### Lösung zu Aufgabe 9
```javascript
function isAscending(arr) {
    return arr.every((num, i) => i === 0 || num >= arr[i - 1]);
}
```

### Lösung zu Aufgabe 10
```javascript
function removeDuplicates(arr) {
    return arr.filter((item, index) => arr.indexOf(item) === index);
}
```

### Lösung zu Aufgabe 11
```javascript
function findSecondHighest(arr) {
    let uniqueSorted = Array.from(new Set(arr)).sort((a, b) => b - a);
    return uniqueSorted[1];
}
```

### Lösung zu Aufgabe 12
```javascript
function reverseLongStrings(arr) {
    return arr.map(str => str.length > 4 ? str.split('').reverse().join('') : str);
}
```

### Lösung zu Aufgabe 13
```javascript
function stringLengths(arr) {
    return arr.map(str => str.length);
}
```

### Lösung zu Aufgabe 14
```javascript
function filterEvenDigitSum(arr) {
    return arr.filter(num => {
        const digitSum = num.toString().split('').reduce((sum, digit) => sum + Number(digit), 0);
        return digitSum % 2 === 0;
    });
}
```

### Lösung zu Aufgabe 15
```javascript
function countOccurrences(arr) {
    return arr.reduce((acc, val) => {
        acc[val] = (acc[val] || 0) + 1;
        return acc;
    }, {});
}
```

### Lösung zu Aufgabe 16
```javascript
function intersection(arr1, arr2) {
    return arr1.filter(item => arr2.includes(item));
}
```

### Lösung zu Aufgabe 17
```javascript
function filterOddLengthStrings(arr) {
    return arr.filter(str => str.length % 2 !== 0);
}
```

### Lösung zu Aufgabe 18
```javascript
function allTruthyOrFalsy(arr) {
    return arr.every(Boolean) || arr.every(val => !val);
}
```

### Lösung zu Aufgabe 19
```javascript
function processArray(arr) {
    return arr.map(num => num * 2).filter(num => num <= 10);
}
```

### Lösung zu Aufgabe 20
```javascript
function sumOfDifferences(arr) {
    return arr.slice(1).reduce((sum, num, i) => sum + Math.abs(num - arr[i]), 0);
}
```

