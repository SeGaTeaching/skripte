
# JavaScript Exercises: Working with `const`

## Aufgaben

### Aufgabe 1
Deklariere eine Konstante `pi` und weise ihr den Wert `3.14` zu. Versuche, den Wert von `pi` auf `3.14159` zu ändern. 
Was passiert?

### Aufgabe 2
Erstelle ein Objekt `user` mit den Eigenschaften `name` und `age` und verwende `const` zur Deklaration. 
Füge anschließend eine Eigenschaft `email` hinzu und gib das gesamte Objekt in der Konsole aus.

### Aufgabe 3
Gegeben seien die beiden Objekte `objA` und `objB`, die identische Inhalte besitzen, jedoch als separate Objekte erstellt wurden. 
Prüfe, ob die beiden Objekte gleich sind und erkläre das Ergebnis.

```javascript
let objA = {x: 5, y: 10};
let objB = {x: 5, y: 10};
```

### Aufgabe 4
Erstelle eine flache Kopie des Objekts `product` und füge eine neue Eigenschaft `price` hinzu. 
Verwende `Object.assign` und gib die Eigenschaften des neuen Objekts in der Konsole aus.

```javascript
const product = { name: "Laptop", brand: "Tech" };
```

### Aufgabe 5
Erstelle eine tiefe Kopie des Objekts `shape`, das eine verschachtelte Eigenschaft `dimensions` enthält. 
Verwende eine Funktion zum Klonen und zeige, dass Änderungen an `shape` nicht die Kopie beeinflussen.

```javascript
const shape = {
    type: "Rectangle",
    dimensions: {
        width: 100,
        height: 50
    }
};
```

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
const pi = 3.14;
pi = 3.14159; // TypeError: Assignment to constant variable.
```

### Lösung zu Aufgabe 2
```javascript
const user = { name: "Alice", age: 25 };
user.email = "alice@example.com";
console.log(user); // Output: { name: "Alice", age: 25, email: "alice@example.com" }
```

### Lösung zu Aufgabe 3
```javascript
let objA = {x: 5, y: 10};
let objB = {x: 5, y: 10};
console.log(objA === objB); // Output: false
// Erklärung: Die beiden Objekte haben zwar die gleichen Inhalte, sind aber unterschiedliche Referenzen.
```

### Lösung zu Aufgabe 4
```javascript
const product = { name: "Laptop", brand: "Tech" };
const productCopy = Object.assign({}, product, { price: 1200 });
console.log(productCopy); // Output: { name: "Laptop", brand: "Tech", price: 1200 }
```

### Lösung zu Aufgabe 5
```javascript
function deepClone(obj) {
    let newObj = {...obj};
    for (let key in newObj) {
        if (typeof newObj[key] === "object") {
            newObj[key] = deepClone(newObj[key]);
        }
    }
    return newObj;
}

const shape = {
    type: "Rectangle",
    dimensions: {
        width: 100,
        height: 50
    }
};

const shapeCopy = deepClone(shape);
shape.dimensions.width = 200;
console.log(shapeCopy.dimensions.width); // Output: 100
```

