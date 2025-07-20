
# Übungsaufgaben: Klassen und Eigenschaften in JavaScript

## Übung 1: Fahrzeug mit Eigenschaften
Erstelle eine Klasse `Vehicle`, die die folgenden Eigenschaften hat: `id`, `latitude`, `longitude` und `status`. Die Methode `setPosition` soll die `latitude` und `longitude` Eigenschaften aktualisieren und die aktuelle Zeit speichern.

1. Erstelle ein Objekt `vehicle1` mit den Werten `id = "AL2023"`, `latitude = 48.8566` und `longitude = 2.3522`.
2. Aktualisiere die Position auf `latitude = 50.1109` und `longitude = 8.6821`.
3. Gib die aktualisierte Position in der Konsole aus.

---

## Übung 2: Öffentliche Eigenschaften
Erstelle eine Klasse `Laptop`, die eine Eigenschaft `brand` im Klassenkörper deklariert. Der Konstruktor akzeptiert das Modell als Parameter.

1. Erstelle ein Objekt `laptop` mit dem Modell `"Dell XPS 13"`.
2. Gib die Marke (`brand`) und das Modell des Laptops in der Konsole aus.

---

## Übung 3: Private Eigenschaften
Erstelle eine Klasse `BankAccount` mit einer privaten Eigenschaft `#balance`. Die Klasse sollte Methoden haben, um Einzahlungen zu machen und den Kontostand abzurufen.

1. Erstelle ein Objekt `account` mit dem Eigentümer `"John"` und einem anfänglichen Guthaben von 500.
2. Zahle 200 auf das Konto ein.
3. Gib den Kontostand in der Konsole aus.

---

## Übung 4: Getter und Setter
Erstelle eine Klasse `Book`, die im Konstruktor die Eigenschaften `title` und `author` setzt. Verwende Getter und Setter, um den Titel des Buches zu erhalten und zu ändern.

1. Erstelle ein Objekt `book` mit dem Titel `"The Great Gatsby"` und dem Autor `"F. Scott Fitzgerald"`.
2. Ändere den Titel des Buches in `"1984"`.
3. Gib den aktualisierten Titel in der Konsole aus.

---

## Übung 5: Fahrzeug mit privater Position
Erstelle eine Klasse `Vehicle` mit privaten Eigenschaften `#latitude` und `#longitude`, die im Konstruktor initialisiert werden. Erstelle Methoden, um die Position zu setzen und abzurufen.

1. Erstelle ein Objekt `vehicle2` mit den Werten `id = "AL1024"`, `latitude = 40.7128` und `longitude = -74.0060`.
2. Aktualisiere die Position auf `latitude = 34.0522` und `longitude = -118.2437`.
3. Gib die aktualisierte Position in der Konsole aus.

---

## Übung 6: Haus mit Räumen
Erstelle eine Klasse `House`, die die Eigenschaft `rooms` im Klassenkörper deklariert und eine Methode `addRoom` hat, um Räume hinzuzufügen.

1. Erstelle ein Objekt `myHouse` mit der Adresse `"456 Maple St"` und initialisiere es mit 2 Räumen.
2. Füge 3 Räume hinzu.
3. Gib die Anzahl der Räume in der Konsole aus.

---

# Lösungen

## Lösung 1:
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.status = "unavailable";
        this.setPosition({ latitude, longitude });
    }

    setPosition({ latitude, longitude }) {
        this.time = Date.now();
        this.latitude = latitude;
        this.longitude = longitude;
    }

    getPosition() {
        return {
            latitude: this.latitude,
            longitude: this.longitude
        };
    }
}

let vehicle1 = new Vehicle({ id: "AL2023", latitude: 48.8566, longitude: 2.3522 });
vehicle1.setPosition({ latitude: 50.1109, longitude: 8.6821 });
console.log(vehicle1.getPosition());
```

---

## Lösung 2:
```javascript
class Laptop {
    brand = "unknown";
    constructor(model) {
        this.model = model;
    }
}

let laptop = new Laptop("Dell XPS 13");
console.log(laptop.brand);  // -> "unknown"
console.log(laptop.model);  // -> "Dell XPS 13"
```

---

## Lösung 3:
```javascript
class BankAccount {
    #balance = 500;
    constructor(owner) {
        this.owner = owner;
    }

    deposit(amount) {
        this.#balance += amount;
    }

    getBalance() {
        return this.#balance;
    }
}

let account = new BankAccount("John");
account.deposit(200);
console.log(account.getBalance()); // -> 700
```

---

## Lösung 4:
```javascript
class Book {
    constructor(title, author) {
        this._title = title;
        this.author = author;
    }

    get title() {
        return this._title;
    }

    set title(newTitle) {
        this._title = newTitle;
    }
}

let book = new Book("The Great Gatsby", "F. Scott Fitzgerald");
book.title = "1984";
console.log(book.title); // -> "1984"
```

---

## Lösung 5:
```javascript
class Vehicle {
    #latitude;
    #longitude;
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.setPosition({ latitude, longitude });
    }

    setPosition({ latitude, longitude }) {
        this.#latitude = latitude;
        this.#longitude = longitude;
    }

    getPosition() {
        return {
            latitude: this.#latitude,
            longitude: this.#longitude
        };
    }
}

let vehicle2 = new Vehicle({ id: "AL1024", latitude: 40.7128, longitude: -74.0060 });
vehicle2.setPosition({ latitude: 34.0522, longitude: -118.2437 });
console.log(vehicle2.getPosition()); // -> {latitude: 34.0522, longitude: -118.2437}
```

---

## Lösung 6:
```javascript
class House {
    rooms = 2;
    constructor(address) {
        this.address = address;
    }

    addRoom() {
        this.rooms += 1;
    }
}

let myHouse = new House("456 Maple St");
myHouse.addRoom();
myHouse.addRoom();
myHouse.addRoom();
console.log(myHouse.rooms); // -> 5
```
