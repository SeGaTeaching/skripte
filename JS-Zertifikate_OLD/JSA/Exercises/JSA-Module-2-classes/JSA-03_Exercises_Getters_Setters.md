
# Übungsaufgaben: Getters und Setters in JavaScript

## Übung 1: Fahrzeug-Klasse mit Getter und Setter
Erstelle eine Klasse `Vehicle`, die die Eigenschaften `id`, `latitude`, `longitude` und `status` hat. Verwende Getter und Setter, um die Position (`latitude`, `longitude`) des Fahrzeugs zu setzen und abzurufen.

1. Erstelle ein Objekt `vehicle1` mit `id = "V001"`, `latitude = 40.7128` und `longitude = -74.0060`.
2. Aktualisiere die Position auf `latitude = 34.0522` und `longitude = -118.2437` mit dem Setter.
3. Gib die aktualisierte Position in der Konsole aus.

---

## Übung 2: Buch-Klasse mit Verfügbarkeitsstatus
Erstelle eine Klasse `Book`, die die Eigenschaften `title`, `author` und `availability` hat. Verwende Getter und Setter, um den Verfügbarkeitsstatus des Buches zu setzen und abzurufen.

1. Erstelle ein Objekt `book1` mit dem Titel `"JavaScript for Beginners"` und dem Autor `"John Doe"`.
2. Gib den Verfügbarkeitsstatus aus, setze ihn auf `"Checked out"` und gib den aktualisierten Status aus.

---

## Übung 3: Konto-Klasse mit Validierung
Erstelle eine Klasse `BankAccount` mit den Eigenschaften `owner` und `balance`. Verwende Getter und Setter, um den Kontostand abzurufen und zu aktualisieren. Der Setter sollte sicherstellen, dass der Kontostand nicht negativ sein kann.

1. Erstelle ein Objekt `account1` mit dem Besitzer `"Alice"` und einem Anfangssaldo von 0.
2. Zahle 200 auf das Konto ein und gib den neuen Saldo aus.
3. Versuche, einen negativen Betrag einzuzahlen, und gib die Fehlermeldung aus.

---

## Übung 4: Person-Klasse mit vollständigem Namen
Erstelle eine Klasse `Person`, die die Eigenschaften `firstName` und `lastName` hat. Verwende Getter und Setter, um den vollständigen Namen zu setzen und abzurufen.

1. Erstelle ein Objekt `person1` mit den Werten `"John"` für `firstName` und `"Doe"` für `lastName`.
2. Gib den vollständigen Namen aus und ändere ihn auf `"Jane Smith"`.
3. Gib den aktualisierten vollständigen Namen aus.

---

## Übung 5: Fahrzeug-Klasse mit Zeitstempel
Erstelle eine Klasse `Vehicle`, die die Eigenschaften `id`, `latitude`, `longitude` und `status` hat. Verwende einen Setter, um die Position des Fahrzeugs zu aktualisieren und dabei den aktuellen Zeitstempel (`Date.now()`) zu speichern. Verwende einen Getter, um die Position und den Zeitstempel abzurufen.

1. Erstelle ein Objekt `vehicle2` mit `id = "V002"`, `latitude = 51.5074` und `longitude = -0.1278`.
2. Aktualisiere die Position auf `latitude = 48.8566` und `longitude = 2.3522`.
3. Gib die aktualisierte Position und den Zeitstempel in der Konsole aus.

---

# Lösungen

## Lösung 1:
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.position = { latitude, longitude };
        this.status = "unavailable";
    }

    set position({ latitude, longitude }) {
        this.longitude = longitude;
        this.latitude = latitude;
    }

    get position() {
        return {
            latitude: this.latitude,
            longitude: this.longitude
        };
    }
}

let vehicle1 = new Vehicle({ id: "V001", latitude: 40.7128, longitude: -74.0060 });
vehicle1.position = { latitude: 34.0522, longitude: -118.2437 };
console.log(vehicle1.position);
```

---

## Lösung 2:
```javascript
class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
        this._isAvailable = true;
    }

    get availability() {
        return this._isAvailable ? "Available" : "Checked out";
    }

    set availability(status) {
        this._isAvailable = status;
    }
}

let book1 = new Book("JavaScript for Beginners", "John Doe");
console.log(book1.availability); // -> "Available"
book1.availability = false;
console.log(book1.availability); // -> "Checked out"
```

---

## Lösung 3:
```javascript
class BankAccount {
    constructor(owner, balance = 0) {
        this.owner = owner;
        this._balance = balance;
    }

    get balance() {
        return this._balance;
    }

    set balance(amount) {
        if (amount < 0) {
            console.log("Balance cannot be negative");
        } else {
            this._balance = amount;
        }
    }
}

let account1 = new BankAccount("Alice");
account1.balance = 200;
console.log(account1.balance); // -> 200
account1.balance = -50; // -> "Balance cannot be negative"
```

---

## Lösung 4:
```javascript
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }

    set fullName(name) {
        [this.firstName, this.lastName] = name.split(" ");
    }
}

let person1 = new Person("John", "Doe");
console.log(person1.fullName); // -> "John Doe"
person1.fullName = "Jane Smith";
console.log(person1.fullName); // -> "Jane Smith"
```

---

## Lösung 5:
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.position = { latitude, longitude };
        this.status = "unavailable";
        this.time = Date.now();
    }

    set position({ latitude, longitude }) {
        this.latitude = latitude;
        this.longitude = longitude;
        this.time = Date.now();
    }

    get position() {
        return {
            latitude: this.latitude,
            longitude: this.longitude,
            time: this.time
        };
    }
}

let vehicle2 = new Vehicle({ id: "V002", latitude: 51.5074, longitude: -0.1278 });
vehicle2.position = { latitude: 48.8566, longitude: 2.3522 };
console.log(vehicle2.position);
```
