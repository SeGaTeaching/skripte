
# Übungsaufgaben: Klassen-Deklaration in JavaScript

## Übung 1: Fahrzeug-Konstruktor
Schreibe eine Funktion `Vehicle`, die folgende Parameter akzeptiert: `id`, `latitude`, `longitude`. Die Funktion soll die Eigenschaften `id`, `latitude`, `longitude` und eine Methode `setPosition` haben, die `latitude` und `longitude` ändert und die Zeit aktualisiert.

1. Erstelle ein Objekt `vehicle1` mit `id = "TX123"`, `latitude = 40.7128` und `longitude = -74.0060`.
2. Ändere die Position des Fahrzeugs mit der Methode `setPosition` auf `latitude = 34.0522` und `longitude = -118.2437`.
3. Gib die neue Position in der Konsole aus.

---

## Übung 2: Klassen statt Konstruktor-Funktionen
Erstelle die Klasse `Vehicle` mit einem Konstruktor, der `id`, `latitude` und `longitude` als Parameter akzeptiert. Implementiere die Methode `setPosition` in der Klasse, die die neuen Positionen (Breitengrad und Längengrad) des Fahrzeugs setzt.

1. Erstelle ein Objekt der Klasse `Vehicle` mit `id = "AL1024"`, `latitude = 59.358615` und `longitude = 17.947589`.
2. Setze die neue Position auf `latitude = 59.367647` und `longitude = 18.213451`.
3. Verwende die Methode `getPosition` und gib die neuen Koordinaten in der Konsole aus.

---

## Übung 3: Verwenden von `instanceof`
1. Erstelle eine Klasse `Book` mit den Eigenschaften `title` und `author`.
2. Erstelle ein Objekt `myBook` mit dem Titel "JavaScript Guide" und dem Autor "John Doe".
3. Überprüfe, ob `myBook` eine Instanz der Klasse `Book` ist, und gib das Ergebnis in der Konsole aus.

---

## Übung 4: Statische Methoden
1. Erstelle eine Klasse `MathOperations` mit einer statischen Methode `add`, die zwei Zahlen als Parameter akzeptiert und deren Summe zurückgibt.
2. Rufe die Methode `MathOperations.add` auf und gib das Ergebnis in der Konsole aus.
3. Versuche, `add` auf einem Instanzobjekt der Klasse aufzurufen und sieh, was passiert.

---

## Übung 5: Destrukturierung in Konstruktoren
Erstelle eine Klasse `Person`, die im Konstruktor ein Objekt mit den Eigenschaften `firstName` und `lastName` akzeptiert. Die Klasse sollte auch eine Methode `getFullName` haben, die den vollständigen Namen zurückgibt.

1. Erstelle ein Objekt `person` mit `firstName = "Jane"` und `lastName = "Doe"`.
2. Verwende die Methode `getFullName`, um den vollständigen Namen in der Konsole anzuzeigen.

---

# Lösungen

## Lösung 1:
```javascript
let Vehicle = function(id, latitude, longitude) {
    this.setPosition = function(latitude, longitude) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    };
    this.id = id;
    this.status = "unavailable";
    this.time = Date.now();
    this.latitude = latitude;
    this.longitude = longitude;
};

let vehicle1 = new Vehicle("TX123", 40.7128, -74.0060);
vehicle1.setPosition(34.0522, -118.2437);
console.log(vehicle1);
```

---

## Lösung 2:
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.status = "unavailable";
        this.setPosition({ latitude, longitude });
    }

    setPosition({ latitude, longitude }) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    }

    getPosition() {
        return {
            latitude: this.latitude,
            longitude: this.longitude
        };
    }
}

let vehicle1 = new Vehicle({ id: "AL1024", latitude: 59.358615, longitude: 17.947589 });
vehicle1.setPosition({ latitude: 59.367647, longitude: 18.213451 });
console.log(vehicle1.getPosition());
```

---

## Lösung 3:
```javascript
class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }
}

let myBook = new Book("JavaScript Guide", "John Doe");
console.log(myBook instanceof Book); // -> true
```

---

## Lösung 4:
```javascript
class MathOperations {
    static add(a, b) {
        return a + b;
    }
}

console.log(MathOperations.add(5, 10)); // -> 15

let mathOp = new MathOperations();
console.log(mathOp.add(5, 10)); // -> TypeError: mathOp.add is not a function
```

---

## Lösung 5:
```javascript
class Person {
    constructor({ firstName, lastName }) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    getFullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}

let person = new Person({ firstName: "Jane", lastName: "Doe" });
console.log(person.getFullName()); // -> "Jane Doe"
```
