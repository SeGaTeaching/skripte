
# Vererbung in JavaScript

## 2.4.1 Vererbung
Eine der Hauptgründe für die Einführung von Klassen in JavaScript war die Vereinfachung der Vererbungssyntax. Mit dem Schlüsselwort `extends` können wir eine neue Klasse erstellen, die von einer anderen Klasse erbt.

### Beispiel 1: Vererbung zwischen Vehicle und Bus
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.status = "unavailable";
    }
}

class Bus extends Vehicle {
    constructor({ seats, id, latitude, longitude }) {
        super({ id, latitude, longitude });
        this.seats = seats;
    }
}

let bus = new Bus({ seats: 40, id: "AL1024", latitude: 59.367628, longitude: 18.213423 });
console.log(bus.seats); // -> 40
console.log(bus.id); // -> "AL1024"
```

In diesem Beispiel erbt die Klasse `Bus` alle Eigenschaften und Methoden der `Vehicle`-Klasse und fügt eine neue Eigenschaft `seats` hinzu. Mit `super()` rufen wir den Konstruktor der Basisklasse `Vehicle` auf.

### Zusätzliche Beispiele:

#### Beispiel 2: Vererbung zwischen `Person` und `Employee`
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

class Employee extends Person {
    constructor(name, age, position) {
        super(name, age);
        this.position = position;
    }
}

let employee = new Employee("Alice", 30, "Developer");
console.log(employee.name); // -> "Alice"
console.log(employee.position); // -> "Developer"
```

#### Beispiel 3: Vererbung zwischen `Animal` und `Dog`
```javascript
class Animal {
    constructor(type) {
        this.type = type;
    }

    makeSound() {
        console.log("Some generic sound...");
    }
}

class Dog extends Animal {
    constructor(type, breed) {
        super(type);
        this.breed = breed;
    }

    makeSound() {
        console.log("Bark! Bark!");
    }
}

let dog = new Dog("Mammal", "Golden Retriever");
console.log(dog.type); // -> "Mammal"
dog.makeSound(); // -> "Bark! Bark!"
```

## 2.4.2 Überschattung (Shadowing)
Wenn eine Methode in einer abgeleiteten Klasse denselben Namen wie eine Methode in der Basisklasse hat, überschattet die neue Methode die alte. Um auf die Methode der Basisklasse zuzugreifen, verwenden wir das Schlüsselwort `super`.

### Beispiel 1: Shadowing und `super` verwenden
```javascript
class AlmostEmptyClass {
    constructor(sth) {
        console.log(sth);
    }

    sayHi() {
        console.log("Hi!");
    }
}

class ExtendedClass extends AlmostEmptyClass {
    constructor(name) {
        super("I’m super ...");
        this.name = name;
    }

    sayHi() {
        console.log(`Hi ${this.name}!`);
    }

    newHi() {
        this.sayHi();
    }

    oldHi() {
        super.sayHi();
    }
}

let obj = new ExtendedClass("Bob");
obj.sayHi();    // -> Hi Bob!
obj.newHi();    // -> Hi Bob!
obj.oldHi();    // -> Hi!
```

In diesem Beispiel überschattet die Methode `sayHi` in der Klasse `ExtendedClass` die Methode `sayHi` aus der Basisklasse `AlmostEmptyClass`. Mit `super.sayHi()` können wir jedoch weiterhin auf die Methode der Basisklasse zugreifen.

### Zusätzliche Beispiele:

#### Beispiel 2: Shadowing zwischen `Car` und `ElectricCar`
```javascript
class Car {
    startEngine() {
        console.log("Engine started...");
    }
}

class ElectricCar extends Car {
    startEngine() {
        console.log("Electric engine started silently...");
    }

    startRegularEngine() {
        super.startEngine();
    }
}

let tesla = new ElectricCar();
tesla.startEngine(); // -> "Electric engine started silently..."
tesla.startRegularEngine(); // -> "Engine started..."
```

#### Beispiel 3: Shadowing zwischen `Appliance` und `WashingMachine`
```javascript
class Appliance {
    turnOn() {
        console.log("Appliance is now on.");
    }
}

class WashingMachine extends Appliance {
    turnOn() {
        console.log("Washing machine started washing.");
    }

    turnOnAppliance() {
        super.turnOn();
    }
}

let washer = new WashingMachine();
washer.turnOn(); // -> "Washing machine started washing."
washer.turnOnAppliance(); // -> "Appliance is now on."
```

## 2.4.3 Vererbung von einer Konstruktorfunktion
Neben der Vererbung von Klassen kann eine neue Klasse auch von einer Konstruktorfunktion erben.

### Beispiel 1: Vererbung von einer Konstruktorfunktion
```javascript
let AlmostEmpty = function(sth) {
    console.log(sth);
    this.sayHi = function() {
        console.log("Hi!");
    };
}

class ExtendedClass extends AlmostEmpty {
    constructor(name) {
        super("I’m super ...");
        this.name = name;
    }

    sayHi() {
        console.log(`Hi ${this.name}!`);
    }
}

let obj = new ExtendedClass("Bob");
obj.sayHi();    // -> Hi Bob!
```

In diesem Beispiel erbt die Klasse `ExtendedClass` von der Konstruktorfunktion `AlmostEmpty`. Wir verwenden `super()`, um den Konstruktor der Konstruktorfunktion aufzurufen.

## Fazit
Die Vererbung in JavaScript vereinfacht das Wiederverwenden von Code zwischen Klassen. Mit dem Schlüsselwort `extends` können wir eine Klasse erweitern, und `super()` ermöglicht es uns, auf den Konstruktor und die Methoden der Basisklasse zuzugreifen. Wenn Methoden überschattet werden, können wir mithilfe von `super` weiterhin auf die Methoden der Basisklasse zugreifen.
