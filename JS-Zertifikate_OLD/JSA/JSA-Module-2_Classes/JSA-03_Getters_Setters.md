
# Getters und Setters in JavaScript-Klassen

## 2.3.1 Getters und Setters
In einem früheren Kapitel haben wir bereits Getter und Setter kennengelernt. Sie ermöglichen es uns, spezielle Methoden zu erstellen, um Objekt-Eigenschaften zu lesen und zu setzen. 

### Besonderheiten von Gettern und Settern
- Wir rufen Getter und Setter nicht wie normale Methoden auf, sondern verwenden sie wie Eigenschaften. 
- Ein Setter akzeptiert genau ein Argument, während ein Getter kein Argument akzeptiert.

Auch in Klassen können wir Getter und Setter mit den Schlüsselwörtern `get` und `set` definieren. Schauen wir uns an, wie wir die Methoden `setPosition` und `getPosition` in der `Vehicle`-Klasse durch einen Setter und einen Getter ersetzen können.

### Beispiel 1: Setter und Getter in der Vehicle-Klasse
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.position = { latitude, longitude };
        this.status = "unavailable";
    }

    set position({ latitude, longitude }) {
        this.time = Date.now();
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

let vehicle = new Vehicle({ id: "AL1024", latitude: 59.367628, longitude: 18.213423 });
vehicle.position = { latitude: 59.378654, longitude: 18.193121 };
console.log(vehicle.position);
```

### Unterschiede zur vorherigen Version:
1. **Setter und Getter statt Methoden:** Die Methode `setPosition` wurde durch den Setter `position` ersetzt, und `getPosition` durch den Getter `position`.
2. **Nutzung wie Eigenschaften:** Anstatt `vehicle.setPosition()` aufzurufen, setzen wir die `position`-Eigenschaft direkt.
3. **Automatische Zuweisung:** Der Setter wird verwendet, um automatisch die Werte für `longitude` und `latitude` zu setzen.
4. **Zeitstempel:** Der Setter aktualisiert automatisch den Zeitstempel mit `Date.now()`.

### Zusätzliche Beispiele:

#### Beispiel 2: Setter und Getter für ein Buch-Objekt
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

let myBook = new Book("1984", "George Orwell");
console.log(myBook.availability); // -> "Available"
myBook.availability = false;
console.log(myBook.availability); // -> "Checked out"
```

#### Beispiel 3: Setter und Getter für ein Konto-Objekt
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

let account = new BankAccount("Alice");
console.log(account.balance); // -> 0
account.balance = 100;
console.log(account.balance); // -> 100
account.balance = -50; // -> "Balance cannot be negative"
```

In diesem Beispiel haben wir einen `balance`-Setter, der überprüft, ob der Betrag negativ ist, bevor er den Kontostand ändert.

### Erklärung zu Gettern und Settern:
- **Getter**: Der Getter erlaubt uns, die private Eigenschaft (wie `_balance` im BankAccount-Beispiel) zu lesen, ohne direkt darauf zuzugreifen. Dies verbessert die Kapselung.
- **Setter**: Der Setter ermöglicht es, eine private Eigenschaft zu ändern, wobei zusätzliche Logik wie Validierung eingebaut werden kann, wie im obigen Beispiel, wo wir verhindern, dass ein negativer Wert gesetzt wird.

#### Beispiel 4: Setter und Getter für eine `Person`-Klasse
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

let person = new Person("John", "Doe");
console.log(person.fullName); // -> "John Doe"
person.fullName = "Jane Smith";
console.log(person.fullName); // -> "Jane Smith"
```

In diesem Beispiel zerlegen wir den vollständigen Namen in Vor- und Nachname mit einem Setter und fügen diese wieder mit dem Getter zusammen.

## Fazit
Getter und Setter in JavaScript ermöglichen es uns, Objekt-Eigenschaften zu verwalten, ohne den direkten Zugriff auf diese Eigenschaften zu gewähren. Sie verbessern die Datenkapselung und erlauben es, zusätzliche Logik einzubauen, wie z.B. Validierungen oder automatisches Hinzufügen von Zeitstempeln.
