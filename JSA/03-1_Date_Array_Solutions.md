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
cd 
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

