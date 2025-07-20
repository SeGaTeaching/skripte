
# Umgang mit `const` in JavaScript

## 1. `const` und einfache Datentypen
```javascript
const x = 10;
x = 20; // TypeError: Assignment to constant variable.
```

`const` schützt einfache Datentypen (wie Zahlen oder Strings) vor einer erneuten Zuweisung. Einmal zugewiesen, kann der Wert nicht geändert werden.

## 2. `const` und komplexe Datentypen
```javascript
const contact = {};
contact = { email: "RonaldSMurphy@freepost.org"}; // TypeError: Assignment to constant variable.
```

Auch bei Objekten verhindert `const`, dass wir die gesamte Referenz ändern können. Allerdings können die Eigenschaften eines Objekts, das mit `const` deklariert wurde, verändert werden:
```javascript
const contact = {};
contact.email = "RonaldSMurphy@freepost.org";
console.log(contact.email); // "RonaldSMurphy@freepost.org"
```

## 3. Vergleich von Objekten
Vergleiche von Objekten prüfen die Referenz, nicht den Inhalt:
```javascript
var point1 = {x: 10, y: 20};
var point2 = {x: 10, y: 20};
console.log(point1 === point2); // false
```

Zwei Objekte sind nur gleich, wenn sie auf dasselbe Objekt verweisen:
```javascript
let point3 = point1;
console.log(point1 === point3); // true
```

## 4. Kopieren und Klonen von Objekten

### 4.1 Referenzkopie
```javascript
let point0 = {x:10, y: 20 };
let point1 = point0; // Kopiert die Referenz
```

### 4.2 Shallow Copy (flache Kopie)
```javascript
let point0 = {x:10, y: 20 };
let point2 = Object.assign({}, point0);
console.log(point2.x); // 10
console.log(point1 === point0); // true
console.log(point1 === point2); // false
```

Alternativ kann der Spread-Operator verwendet werden:
```javascript
let point2 = { ...point0 };
```

### 4.3 Shallow Copy mit mehreren Quellen
```javascript
let point3 = {};
Object.assign(point3, point0, {z: 100});
console.log(point3.z); // 100
```

### 4.4 Deep Copy (tiefe Kopie)
Um tiefe Kopien von Objekten zu erstellen, die auch verschachtelte Objekte kopieren, verwenden wir eine rekursive Funktion:
```javascript
let deepClone = function(obj) {
    let newObj = {...obj};
    for(let property in newObj) {
        if(typeof newObj[property] === "object") {
            newObj[property] = deepClone(newObj[property]);
        }
    }
    return newObj;
}
```

#### Beispiel für eine tiefe Kopie
```javascript
let circle1 = {
    radius: 100,
    center: {
        x: 100,
        y: 100
    }
};
let circle2 = deepClone(circle1);
circle1.center.x = 200;
console.log(circle2.center.x); // 100
```

## Fazit
In JavaScript speichert `const` bei Objekten nur die Referenz, nicht den Inhalt. Für tiefe Kopien muss man eine spezielle Funktion verwenden, die auch die inneren Objekte kopiert.
