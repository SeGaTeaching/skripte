
# Klassen und Eigenschaften in JavaScript

## 2.2.1 Eigenschaften in Klassen
In JavaScript haben Objekte nicht nur Methoden, sondern auch Eigenschaften. Es gibt zwei Methoden, um Eigenschaften in Klassen zu deklarieren: in der Konstruktorfunktion oder in Methoden (traditioneller Ansatz) sowie direkt im Klassenkörper (moderner Ansatz). Die direkte Deklaration von Eigenschaften im Klassenkörper ist eine relativ neue, experimentelle Technik, die nicht überall unterstützt wird.

## 2.2.2 Eigenschaften innerhalb von Methoden definieren
In der ursprünglichen Einführung von Klassen in JavaScript wurden Eigenschaften normalerweise in den Konstruktoren oder Methoden der Klasse definiert. Dies basiert auf der Tatsache, dass eine Eigenschaft automatisch erstellt wird, wenn ihr ein Wert zugewiesen wird, auch wenn sie vorher nicht explizit existiert hat.

### Beispiel 1:
```javascript
class Vehicle {
    constructor({id, latitude, longitude}) {
        this.id = id;
        this.status = "unavailable";
        this.setPosition({latitude, longitude});
    }

    setPosition({latitude, longitude}) {
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

let vehicle = new Vehicle({id: "V001", latitude: 40.7128, longitude: -74.0060});
console.log(vehicle.getPosition()); 
```

In diesem Beispiel werden die Eigenschaften `id`, `status`, `time`, `longitude` und `latitude` innerhalb der Konstruktor- und Methodenfunktionen definiert. Dies geschieht implizit, da diese Eigenschaften beim ersten Zuweisen des Werts erstellt werden.

### Zusätzliche Beispiele:
#### Beispiel 2:
```javascript
class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
        this.available = true;
    }

    markAsBorrowed() {
        this.available = false;
    }
}

let myBook = new Book("1984", "George Orwell");
console.log(myBook.available); 
myBook.markAsBorrowed();
console.log(myBook.available);
```

#### Beispiel 3:
```javascript
class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    birthday() {
        this.age += 1;
    }
}

let student = new Student("John", 20);
console.log(student.age); 
student.birthday();
console.log(student.age);
```

## 2.2.3 Direkte Deklaration im Klassenkörper
In neueren Versionen von JavaScript können Eigenschaften direkt im Klassenkörper deklariert werden. Es gibt zwei Arten von Eigenschaften: **öffentliche** und **private**. Öffentliche Eigenschaften sind von außerhalb des Objekts zugänglich, während private Eigenschaften nur innerhalb der Klasse verfügbar sind.

### Beispiel 1:
```javascript
class Vehicle {
    status = "unavailable";
    constructor({id, latitude, longitude}) {
        this.id = id;
        this.setPosition({latitude, longitude});
    }

    setPosition({latitude, longitude}) {
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

let vehicle = new Vehicle({id: "V001", latitude: 40.7128, longitude: -74.0060});
console.log(vehicle.status);
```

In diesem Beispiel wird die Eigenschaft `status` direkt im Klassenkörper deklariert, während `id`, `latitude` und `longitude` weiterhin im Konstruktor initialisiert werden. Der Vorteil ist, dass Eigenschaften, die keinen Konstruktorparameter benötigen, übersichtlicher und einfacher definiert werden können.

### Zusätzliche Beispiele:
#### Beispiel 2:
```javascript
class Laptop {
    brand = "unknown";
    constructor(model) {
        this.model = model;
    }
}

let laptop = new Laptop("MacBook Air");
console.log(laptop.brand);
console.log(laptop.model);
```

#### Beispiel 3:
```javascript
class House {
    rooms = 0;
    constructor(address) {
        this.address = address;
    }
}

let myHouse = new House("123 Main St");
console.log(myHouse.rooms);
console.log(myHouse.address);
```

## Private Eigenschaften
Private Eigenschaften werden mit einem `#` vor dem Eigenschaftsnamen deklariert und sind nur innerhalb der Klasse zugänglich. Ein Versuch, auf sie von außerhalb zuzugreifen, führt zu einem Fehler.

### Beispiel 1:
```javascript
class Vehicle {
    status = "unavailable";
    #longitude;
    #latitude;
    constructor({id, latitude, longitude}) {
        this.id = id;
        this.setPosition({latitude, longitude});
    }

    setPosition({latitude, longitude}) {
        this.time = Date.now();
        this.#longitude = longitude;
        this.#latitude = latitude;
    }

    getPosition() {
        return {
            latitude: this.#latitude,
            longitude: this.#longitude
        };
    }
}

let vehicle = new Vehicle({longitude: 18.213423, latitude: 59.367628, id: "AL1024"});
console.log(vehicle.getPosition()); 
console.log(vehicle.#longitude); // error
```

In diesem Beispiel werden die Eigenschaften `#longitude` und `#latitude` als private Eigenschaften deklariert. Sie können nur innerhalb der Klasse verwendet werden, und ein Versuch, sie außerhalb der Klasse zuzugreifen, führt zu einem Fehler.

### Zusätzliche Beispiele:
#### Beispiel 2:
```javascript
class BankAccount {
    #balance = 0;
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

let account = new BankAccount("Alice");
account.deposit(100);
console.log(account.getBalance()); 
console.log(account.#balance); // error
```

#### Beispiel 3:
```javascript
class Employee {
    #salary = 50000;
    constructor(name) {
        this.name = name;
    }

    giveRaise(amount) {
        this.#salary += amount;
    }

    getSalary() {
        return this.#salary;
    }
}

let employee = new Employee("Bob");
employee.giveRaise(5000);
console.log(employee.getSalary()); 
console.log(employee.#salary); // error
```

## Fazit
Die Deklaration von Eigenschaften in JavaScript-Klassen kann entweder im Konstruktor oder direkt im Klassenkörper erfolgen. Öffentliche Eigenschaften sind von außen zugänglich, während private Eigenschaften mit einem `#` nur innerhalb der Klasse genutzt werden können.
