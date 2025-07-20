
# JavaScript Aufgaben zu Date- und Array-Methoden

## Date Aufgaben

### Aufgabe 1
Erstellen Sie eine Funktion, die prüft, ob ein bestimmtes Datum in der Zukunft liegt und geben Sie die Anzahl der verbleibenden Tage bis zu diesem Datum zurück.
**Beispieldatum:** `new Date("2025-12-31")`

### Aufgabe 2
Entwickeln Sie eine Funktion, die das aktuelle Datum und die Uhrzeit formatiert und in einem benutzerdefinierten Format ausgibt (z.B. "Montag, 20. Januar 2023, 15:30").
**Kein Beispiel-Array erforderlich.**

### Aufgabe 3
Schreiben Sie eine Funktion, die die Differenz zwischen zwei Daten in Wochen berechnet und das Ergebnis zurückgibt.
**Beispieldaten:** `new Date("2024-01-01")`, `new Date("2024-12-31")`

### Aufgabe 4
Erstellen Sie eine Funktion, die prüft, ob ein bestimmtes Jahr ein Schaltjahr ist, und das Ergebnis als `true` oder `false` zurückgibt.
**Beispieljahr:** `2024`

### Aufgabe 5
Entwickeln Sie eine Funktion, die ein zufälliges Datum innerhalb eines bestimmten Zeitraums (Start- und Enddatum) zurückgibt.
**Beispieldaten:** `new Date("2023-01-01")`, `new Date("2025-12-31")`

## Array Aufgaben

### Aufgabe 6
Schreiben Sie eine Funktion, die alle doppelten Werte aus einem Array entfernt und nur eindeutige Werte zurückgibt.
**Beispielarray:** `[1, 2, 2, 3, 4, 4, 5]`

### Aufgabe 7
Entwickeln Sie eine Funktion, die das längste Wort in einem Array von Strings findet.
**Beispielarray:** `["apple", "banana", "strawberry", "kiwi"]`

### Aufgabe 8
Erstellen Sie eine Funktion, die die n häufigsten Elemente eines Arrays zurückgibt.
**Beispielarray:** `[1, 3, 3, 7, 7, 7, 2, 5, 5]`, **n:** `2`

### Aufgabe 9
Schreiben Sie eine Funktion, die prüft, ob alle Elemente eines Arrays innerhalb eines bestimmten Bereichs liegen.
**Beispielarray:** `[10, 15, 20, 25]`, **min:** `10`, **max:** `30`

### Aufgabe 10
Entwickeln Sie eine Funktion, die ein Array von Zahlen nach Häufigkeit ihrer Werte sortiert.
**Beispielarray:** `[3, 3, 2, 1, 3, 2, 4]`

### Aufgabe 11
Erstellen Sie eine Funktion, die die Elemente eines Arrays in umgekehrter Reihenfolge zurückgibt, ohne das Originalarray zu ändern.
**Beispielarray:** `[1, 2, 3, 4, 5]`

### Aufgabe 12
Schreiben Sie eine Funktion, die den Durchschnittswert eines Arrays berechnet und zurückgibt.
**Beispielarray:** `[10, 20, 30, 40, 50]`

### Aufgabe 13
Entwickeln Sie eine Funktion, die prüft, ob mindestens eines der Elemente in einem Array in einem anderen Array vorhanden ist.
**Beispielarrays:** `[1, 2, 3, 4]`, `[5, 6, 3, 7]`

### Aufgabe 14
Erstellen Sie eine Funktion, die ein verschachteltes Array in ein flaches Array umwandelt.
**Beispielarray:** `[1, [2, 3], [4, [5, 6]], 7]`

### Aufgabe 15
Schreiben Sie eine Funktion, die aus zwei Arrays die Schnittmenge bildet.
**Beispielarrays:** `[1, 2, 3, 4]`, `[3, 4, 5, 6]`

### Aufgabe 16
Entwickeln Sie eine Funktion, die prüft, ob ein Array leer ist oder nur leere Werte (null, undefined, NaN) enthält.
**Beispielarray:** `[null, undefined, NaN, ""]`

### Aufgabe 17
Erstellen Sie eine Funktion, die eine Liste von Objekten basierend auf einem bestimmten Attribut gruppiert und das Ergebnis als Objekt zurückgibt.
**Beispielarray:** `[{ name: "Alice", group: "A" }, { name: "Bob", group: "B" }, { name: "Charlie", group: "A" }]`

### Aufgabe 18
Schreiben Sie eine Funktion, die die gemeinsamen Werte von drei oder mehr Arrays findet.
**Beispielarrays:** `[1, 2, 3]`, `[2, 3, 4]`, `[3, 4, 5]`

### Aufgabe 19
Entwickeln Sie eine Funktion, die die längste aufeinanderfolgende Sequenz in einem Array von Zahlen findet.
**Beispielarray:** `[100, 4, 200, 1, 3, 2]`

### Aufgabe 20
Erstellen Sie eine Funktion, die alle Elemente eines Arrays so verschiebt, dass das letzte Element zum ersten wird.
**Beispielarray:** `[1, 2, 3, 4, 5]`

### Aufgabe 21
Schreiben Sie eine Funktion, die ein Array in mehrere gleich große Teile aufteilt.
**Beispielarray:** `[1, 2, 3, 4, 5, 6, 7, 8]`, **Größe:** `3`

### Aufgabe 22
Entwickeln Sie eine Funktion, die den Median eines Arrays berechnet und zurückgibt.
**Beispielarray:** `[5, 3, 1, 2, 4]`

### Aufgabe 23
Erstellen Sie eine Funktion, die die Summe aller positiven Werte in einem Array zurückgibt.
**Beispielarray:** `[-1, 2, -3, 4, 5]`

### Aufgabe 24
Schreiben Sie eine Funktion, die prüft, ob alle Zeichenketten in einem Array die gleiche Länge haben.
**Beispielarray:** `["cat", "dog", "bat"]`

### Aufgabe 25
Entwickeln Sie eine Funktion, die ein Array von Objekten nach mehreren Eigenschaften sortiert (z.B. nach Name und Alter).
**Beispielarray:** `[{ name: "Alice", age: 25 }, { name: "Bob", age: 20 }, { name: "Charlie", age: 25 }]`

---


## Lösungen
# Lösungen für JavaScript Aufgaben zu Date- und Array-Methoden

## Date Lösungen
1. **Lösung zu Aufgabe 1:** Prüfen, ob ein Datum in der Zukunft liegt und verbleibende Tage berechnen.
```javascript
function daysUntil(date) {
    const target = new Date(date);
    const today = new Date();
    if (target > today) {
        const diffTime = target - today;
        return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    } else {
        return 0; // Datum liegt nicht in der Zukunft
    }
}
```

2. **Lösung zu Aufgabe 2:** Formatierung des aktuellen Datums und der Uhrzeit in benutzerdefiniertem Format.
```javascript
function formatCurrentDate() {
    const date = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return date.toLocaleDateString('de-DE', options);
}
```

3. **Lösung zu Aufgabe 3:** Differenz in Wochen zwischen zwei Daten berechnen.
```javascript
function weeksBetween(date1, date2) {
    const diffTime = Math.abs(new Date(date2) - new Date(date1));
    return Math.floor(diffTime / (1000 * 60 * 60 * 24 * 7));
}
```

4. **Lösung zu Aufgabe 4:** Prüfen, ob ein Jahr ein Schaltjahr ist.
```javascript
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
```

5. **Lösung zu Aufgabe 5:** Zufälliges Datum innerhalb eines bestimmten Zeitraums generieren.
```javascript
function randomDate(start, end) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}
```

## Array Lösungen
6. **Lösung zu Aufgabe 6:** Doppelte Werte aus einem Array entfernen.
```javascript
function uniqueValues(arr) {
    return [...new Set(arr)];
}
```

7. **Lösung zu Aufgabe 7:** Das längste Wort in einem Array finden.
```javascript
function longestWord(words) {
    return words.reduce((longest, word) => word.length > longest.length ? word : longest, "");
}
```

8. **Lösung zu Aufgabe 8:** Die n häufigsten Elemente in einem Array finden.
```javascript
function mostFrequent(arr, n) {
    const frequency = arr.reduce((count, item) => (count[item] = (count[item] || 0) + 1, count), {});
    return Object.entries(frequency).sort((a, b) => b[1] - a[1]).slice(0, n).map(item => item[0]);
}
```

9. **Lösung zu Aufgabe 9:** Prüfen, ob alle Array-Elemente innerhalb eines bestimmten Bereichs liegen.
```javascript
function withinRange(arr, min, max) {
    return arr.every(num => num >= min && num <= max);
}
```

10. **Lösung zu Aufgabe 10:** Array von Zahlen nach Häufigkeit ihrer Werte sortieren.
```javascript
function sortByFrequency(arr) {
    const frequency = arr.reduce((count, num) => (count[num] = (count[num] || 0) + 1, count), {});
    return arr.sort((a, b) => frequency[b] - frequency[a] || a - b);
}
```

11. **Lösung zu Aufgabe 11:** Elemente eines Arrays umgekehrt zurückgeben.
```javascript
function reverseArray(arr) {
    return [...arr].reverse();
}
```

12. **Lösung zu Aufgabe 12:** Durchschnittswert eines Arrays berechnen.
```javascript
function average(arr) {
    return arr.reduce((sum, num) => sum + num, 0) / arr.length;
}
```

13. **Lösung zu Aufgabe 13:** Prüfen, ob ein Element in einem anderen Array vorhanden ist.
```javascript
function hasCommonElements(arr1, arr2) {
    return arr1.some(item => arr2.includes(item));
}
```

14. **Lösung zu Aufgabe 14:** Verschachteltes Array in ein flaches Array umwandeln.
```javascript
function flattenArray(arr) {
    return arr.flat(Infinity);
}
```

15. **Lösung zu Aufgabe 15:** Schnittmenge von zwei Arrays bilden.
```javascript
function intersection(arr1, arr2) {
    return arr1.filter(item => arr2.includes(item));
}
```

16. **Lösung zu Aufgabe 16:** Prüfen, ob ein Array leer oder nur leere Werte enthält.
```javascript
function isEmptyArray(arr) {
    return arr.every(item => item === null || item === undefined || Number.isNaN(item));
}
```

17. **Lösung zu Aufgabe 17:** Liste von Objekten basierend auf einem Attribut gruppieren.
```javascript
function groupBy(arr, key) {
    return arr.reduce((group, obj) => {
        const val = obj[key];
        group[val] = (group[val] || []).concat(obj);
        return group;
    }, {});
}
```

18. **Lösung zu Aufgabe 18:** Gemeinsame Werte in drei oder mehr Arrays finden.
```javascript
function commonElements(...arrays) {
    return arrays.reduce((a, b) => a.filter(c => b.includes(c)));
}
```

19. **Lösung zu Aufgabe 19:** Längste aufeinanderfolgende Sequenz in einem Array finden.
```javascript
function longestConsecutiveSequence(arr) {
    const set = new Set(arr);
    let maxLength = 0;
    for (const num of set) {
        if (!set.has(num - 1)) {
            let length = 1;
            while (set.has(num + length)) length++;
            maxLength = Math.max(maxLength, length);
        }
    }
    return maxLength;
}
```

20. **Lösung zu Aufgabe 20:** Letztes Element zum ersten Element verschieben.
```javascript
function rotateArray(arr) {
    return [arr.pop(), ...arr];
}
```

21. **Lösung zu Aufgabe 21:** Array in mehrere gleich große Teile aufteilen.
```javascript
function chunkArray(arr, size) {
    const chunks = [];
    for (let i = 0; i < arr.length; i += size) {
        chunks.push(arr.slice(i, i + size));
    }
    return chunks;
}
```

22. **Lösung zu Aufgabe 22:** Median eines Arrays berechnen.
```javascript
function median(arr) {
    arr.sort((a, b) => a - b);
    const mid = Math.floor(arr.length / 2);
    return arr.length % 2 !== 0 ? arr[mid] : (arr[mid - 1] + arr[mid]) / 2;
}
```

23. **Lösung zu Aufgabe 23:** Summe aller positiven Werte in einem Array berechnen.
```javascript
function sumPositive(arr) {
    return arr.filter(num => num > 0).reduce((sum, num) => sum + num, 0);
}
```

24. **Lösung zu Aufgabe 24:** Prüfen, ob alle Strings in einem Array die gleiche Länge haben.
```javascript
function sameLengthStrings(arr) {
    return arr.every(str => str.length === arr[0].length);
}
```

25. **Lösung zu Aufgabe 25:** Array von Objekten nach mehreren Eigenschaften sortieren.
```javascript
function sortByAttributes(arr, ...attrs) {
    return arr.sort((a, b) => {
        for (let attr of attrs) {
            if (a[attr] > b[attr]) return 1;
            if (a[attr] < b[attr]) return -1;
        }
        return 0;
    });
}
```

