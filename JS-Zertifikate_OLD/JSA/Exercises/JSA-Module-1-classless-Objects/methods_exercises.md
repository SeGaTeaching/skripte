
# JavaScript Exercises: Methods, `this` Keyword, Getters, and Setters

## Aufgaben

### Aufgabe 1
Erstelle ein Objekt `rectangle` mit den Eigenschaften `width` und `height`. Füge eine Methode `getArea` hinzu, 
die die Fläche des Rechtecks berechnet und zurückgibt.

### Aufgabe 2
Erstelle ein Objekt `car` mit der Eigenschaft `speed`. Füge eine Methode `increaseSpeed` hinzu, 
die die Geschwindigkeit um einen bestimmten Wert erhöht. Verwende `this` in der Methode.

### Aufgabe 3
Erstelle ein Objekt `book` mit einer verschachtelten Eigenschaft `author`, die eine Methode `getInfo` hat. 
Die Methode soll den Namen des Autors zurückgeben. Verwende `this` korrekt in der verschachtelten Methode.

### Aufgabe 4
Deklariere ein Objekt `thermometer` mit einer privaten Eigenschaft `_temperature` und einem Getter für `temperature`. 
Stelle sicher, dass der Getter die Temperatur in Grad Celsius zurückgibt.

### Aufgabe 5
Erstelle ein Objekt `student` mit den Eigenschaften `firstName`, `lastName` und einem Getter `fullName`. 
Füge einen Setter für `fullName` hinzu, der `firstName` und `lastName` auf Basis eines vollständigen Namens ändert.

### Aufgabe 6
Erstelle ein Objekt `wallet` mit einer privaten Eigenschaft `_balance` und einem Getter und Setter für `balance`. 
Der Setter sollte sicherstellen, dass der Wert von `_balance` nicht negativ wird.

### Aufgabe 7
Erstelle ein Objekt `point` mit den Eigenschaften `x` und `y`. Füge eine Methode `move` hinzu, 
die beide Werte um die angegebenen Beträge verschiebt und die neuen Koordinaten zurückgibt.

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
let rectangle = {
    width: 5,
    height: 10,
    getArea() {
        return this.width * this.height;
    }
};

console.log(rectangle.getArea()); // Output: 50
```

### Lösung zu Aufgabe 2
```javascript
let car = {
    speed: 60,
    increaseSpeed(value) {
        this.speed += value;
    }
};

car.increaseSpeed(20);
console.log(car.speed); // Output: 80
```

### Lösung zu Aufgabe 3
```javascript
let book = {
    title: "JavaScript Guide",
    author: {
        name: "Jane Doe",
        getInfo() {
            return this.name;
        }
    }
};

console.log(book.author.getInfo()); // Output: "Jane Doe"
```

### Lösung zu Aufgabe 4
```javascript
let thermometer = {
    _temperature: 25,
    get temperature() {
        return this._temperature;
    }
};

console.log(thermometer.temperature); // Output: 25
```

### Lösung zu Aufgabe 5
```javascript
let student = {
    firstName: "John",
    lastName: "Doe",
    get fullName() {
        return \`\${this.firstName} \${this.lastName}\`;
    },
    set fullName(name) {
        let parts = name.split(" ");
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};

student.fullName = "Jane Smith";
console.log(student.firstName); // Output: "Jane"
console.log(student.lastName); // Output: "Smith"
```

### Lösung zu Aufgabe 6
```javascript
let wallet = {
    _balance: 100,
    get balance() {
        return this._balance;
    },
    set balance(value) {
        if (value >= 0) {
            this._balance = value;
        }
    }
};

wallet.balance = 50;
console.log(wallet.balance); // Output: 50
wallet.balance = -20;
console.log(wallet.balance); // Output: 50 (no change)
```

### Lösung zu Aufgabe 7
```javascript
let point = {
    x: 10,
    y: 15,
    move(dx, dy) {
        this.x += dx;
        this.y += dy;
        return { x: this.x, y: this.y };
    }
};

console.log(point.move(5, -5)); // Output: { x: 15, y: 10 }
```

