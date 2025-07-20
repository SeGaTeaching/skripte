
# Übungsaufgaben: Vererbung in JavaScript

## Übung 1: Vererbung in Fahrzeugklassen
Erstelle eine Basisklasse `Vehicle` mit den Eigenschaften `id`, `status`, `latitude` und `longitude`. Dann erstelle eine abgeleitete Klasse `Car`, die zusätzlich die Eigenschaft `brand` hat.

1. Erstelle ein Objekt der Klasse `Car` mit `id = "C001"`, `brand = "Toyota"`, `latitude = 48.8566` und `longitude = 2.3522`.
2. Gib die Eigenschaften `id`, `brand`, `latitude` und `longitude` in der Konsole aus.

---

## Übung 2: Tiere und Vögel
Erstelle eine Basisklasse `Animal` mit der Eigenschaft `species` und einer Methode `makeSound`. Dann erstelle eine abgeleitete Klasse `Bird`, die zusätzlich die Methode `fly` hat.

1. Erstelle ein Objekt der Klasse `Bird` mit `species = "Eagle"`.
2. Rufe die Methoden `makeSound` und `fly` auf.

---

## Übung 3: Überschattung in Haushaltsgeräten
Erstelle eine Basisklasse `Appliance` mit einer Methode `turnOn`. Dann erstelle eine abgeleitete Klasse `Oven`, die die Methode `turnOn` überschreibt.

1. Erstelle ein Objekt der Klasse `Oven` und rufe die Methode `turnOn` auf.
2. Verwende `super.turnOn()`, um die Methode der Basisklasse aufzurufen.

---

## Übung 4: Vererbung von Konstruktorfunktionen
Erstelle eine Konstruktorfunktion `Device` mit der Eigenschaft `model`. Dann erstelle eine Klasse `Phone`, die von `Device` erbt und eine zusätzliche Methode `call` hat.

1. Erstelle ein Objekt der Klasse `Phone` mit `model = "iPhone 12"`.
2. Rufe die Methode `call` auf und gib das `model` in der Konsole aus.

---

## Übung 5: Schattenmethoden in Fahrzeugklassen
Erstelle eine Basisklasse `Vehicle` mit der Methode `startEngine`. Dann erstelle eine abgeleitete Klasse `ElectricCar`, die die Methode `startEngine` überschreibt, aber auch die Methode der Basisklasse aufruft.

1. Erstelle ein Objekt der Klasse `ElectricCar` und rufe die Methode `startEngine` auf.

---

## Übung 6: Vererbung mit Konstruktoren
Erstelle eine Klasse `Shape` mit dem Attribut `type`. Dann erstelle eine abgeleitete Klasse `Circle`, die das Attribut `radius` hinzufügt und die Methode `getArea` implementiert.

1. Erstelle ein Objekt der Klasse `Circle` mit `type = "circle"` und `radius = 5`.
2. Berechne und gib die Fläche des Kreises aus.

---

## Übung 7: Abgeleitete Klasse `Dog` von `Animal`
Erstelle eine Klasse `Animal` mit den Eigenschaften `name` und `age`. Dann erstelle eine Klasse `Dog`, die von `Animal` erbt und eine Methode `bark` hat.

1. Erstelle ein Objekt der Klasse `Dog` mit `name = "Buddy"` und `age = 3`.
2. Rufe die Methode `bark` auf und gib das Alter des Hundes in der Konsole aus.

---

## Übung 8: Vererbung mit privater Methode
Erstelle eine Klasse `Gadget` mit einer privaten Methode `#updateSoftware`. Dann erstelle eine abgeleitete Klasse `Smartphone`, die die Methode `updateSoftware` aufruft.

1. Erstelle ein Objekt der Klasse `Smartphone` und rufe die Methode `updateSoftware` über eine öffentliche Methode auf.

---

## Übung 9: Überschattung in Fahrzeugklassen
Erstelle eine Klasse `Vehicle` mit einer Methode `getFuelType`. Dann erstelle eine abgeleitete Klasse `Truck`, die diese Methode überschattet und `super.getFuelType()` aufruft.

1. Erstelle ein Objekt der Klasse `Truck` und rufe die Methode `getFuelType` auf.

---

## Übung 10: Abgeleitete Klasse mit zusätzlichen Methoden
Erstelle eine Klasse `Device` mit der Methode `powerOn`. Dann erstelle eine abgeleitete Klasse `Laptop`, die zusätzlich die Methode `sleep` hat.

1. Erstelle ein Objekt der Klasse `Laptop` und rufe beide Methoden auf.

---

# Lösungen

## Lösung 1:
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.status = "unavailable";
    }
}

class Car extends Vehicle {
    constructor({ id, brand, latitude, longitude }) {
        super({ id, latitude, longitude });
        this.brand = brand;
    }
}

let car1 = new Car({ id: "C001", brand: "Toyota", latitude: 48.8566, longitude: 2.3522 });
console.log(car1.id); // -> "C001"
console.log(car1.brand); // -> "Toyota"
console.log(car1.latitude); // -> 48.8566
console.log(car1.longitude); // -> 2.3522
```

---

## Lösung 2:
```javascript
class Animal {
    constructor(species) {
        this.species = species;
    }

    makeSound() {
        console.log("Some generic animal sound...");
    }
}

class Bird extends Animal {
    fly() {
        console.log("Flying...");
    }
}

let bird = new Bird("Eagle");
bird.makeSound(); // -> "Some generic animal sound..."
bird.fly(); // -> "Flying..."
```

---

## Lösung 3:
```javascript
class Appliance {
    turnOn() {
        console.log("Appliance is now on.");
    }
}

class Oven extends Appliance {
    turnOn() {
        console.log("Oven is heating up...");
    }

    useSuperTurnOn() {
        super.turnOn();
    }
}

let oven = new Oven();
oven.turnOn(); // -> "Oven is heating up..."
oven.useSuperTurnOn(); // -> "Appliance is now on."
```

---

## Lösung 4:
```javascript
let Device = function(model) {
    this.model = model;
};

class Phone extends Device {
    call() {
        console.log("Calling from " + this.model);
    }
}

let phone = new Phone("iPhone 12");
phone.call(); // -> "Calling from iPhone 12"
```

---

## Lösung 5:
```javascript
class Vehicle {
    startEngine() {
        console.log("Starting engine...");
    }
}

class ElectricCar extends Vehicle {
    startEngine() {
        console.log("Starting electric engine silently...");
        super.startEngine();
    }
}

let tesla = new ElectricCar();
tesla.startEngine(); // -> "Starting electric engine silently..."
                     // -> "Starting engine..."
```

---

## Lösung 6:
```javascript
class Shape {
    constructor(type) {
        this.type = type;
    }
}

class Circle extends Shape {
    constructor(type, radius) {
        super(type);
        this.radius = radius;
    }

    getArea() {
        return Math.PI * this.radius ** 2;
    }
}

let circle = new Circle("circle", 5);
console.log(circle.getArea()); // -> 78.53981633974483
```

---

## Lösung 7:
```javascript
class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

class Dog extends Animal {
    bark() {
        console.log("Woof! Woof!");
    }
}

let dog = new Dog("Buddy", 3);
dog.bark(); // -> "Woof! Woof!"
console.log(dog.age); // -> 3
```

---

## Lösung 8:
```javascript
class Gadget {
    #updateSoftware() {
        console.log("Updating software...");
    }

    triggerUpdate() {
        this.#updateSoftware();
    }
}

class Smartphone extends Gadget {}

let phone = new Smartphone();
phone.triggerUpdate(); // -> "Updating software..."
```

---

## Lösung 9:
```javascript
class Vehicle {
    getFuelType() {
        return "Unknown fuel type";
    }
}

class Truck extends Vehicle {
    getFuelType() {
        console.log("Truck fuel type: Diesel");
        return super.getFuelType();
    }
}

let truck = new Truck();
console.log(truck.getFuelType()); // -> "Truck fuel type: Diesel"
                                  // -> "Unknown fuel type"
```

---

## Lösung 10:
```javascript
class Device {
    powerOn() {
        console.log("Device is powering on...");
    }
}

class Laptop extends Device {
    sleep() {
        console.log("Laptop is going to sleep...");
    }
}

let laptop = new Laptop();
laptop.powerOn(); // -> "Device is powering on..."
laptop.sleep(); // -> "Laptop is going to sleep..."
```
