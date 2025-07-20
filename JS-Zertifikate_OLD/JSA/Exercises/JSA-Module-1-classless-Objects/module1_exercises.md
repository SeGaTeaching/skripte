# Modul "classless Objects" – Übungsaufgaben

## Aufgabe 1
Erstelle ein Objekt `person` mit den Eigenschaften `firstName` und `lastName`. Überprüfe, ob die Eigenschaft `age` existiert, und gib das Ergebnis in der Konsole aus.

## Aufgabe 2
Erstelle ein Objekt `car` und füge die Eigenschaften `make`, `model` und `year` hinzu. Verwende die `delete`-Anweisung, um die Eigenschaft `year` zu entfernen, und überprüfe anschließend, ob sie noch vorhanden ist.

## Aufgabe 3
Erstelle ein Objekt `book` und füge die Eigenschaft `title` hinzu. Erstelle eine Kopie des Objekts und ändere `title` in der Kopie. Überprüfe, ob sich das Original geändert hat.

## Aufgabe 4
Erstelle ein Objekt `user` und füge eine Methode `greet` hinzu, die den Text „Hello!“ in der Konsole ausgibt. Verwende die Methode und überprüfe das Ergebnis.

## Aufgabe 5
Erstelle ein Objekt `rectangle` mit den Eigenschaften `width` und `height`. Füge Getter- und Setter-Methoden für `area` hinzu, um die Fläche basierend auf `width` und `height` zu berechnen.

## Aufgabe 6
Erstelle ein Objekt `config` und definiere die Eigenschaft `theme` als nicht überschreibbar und nicht konfigurierbar. Teste, ob du `theme` ändern oder löschen kannst.

## Aufgabe 7
Erstelle eine Factory-Funktion `createPerson` mit den Parametern `firstName` und `lastName`. Verwende die Funktion, um ein neues Objekt zu erstellen und gib es in der Konsole aus.

## Aufgabe 8
Erstelle eine Constructor-Funktion `Animal`, die die Eigenschaften `species` und `age` setzt. Erzeuge ein neues Objekt und gib es in der Konsole aus.

## Aufgabe 9
Erstelle ein Objekt `vehicle` und verwende `Object.create()` um ein neues Objekt `bike` zu erstellen, das von `vehicle` erbt. Füge dem Prototyp `vehicle` eine Methode `move` hinzu und rufe diese über `bike` auf.

## Aufgabe 10
Erstelle ein Objekt `account` und füge eine Eigenschaft `balance` hinzu. Erstelle eine flache Kopie und überprüfe, ob beide Objekte unabhängig voneinander sind, indem du `balance` in einem der beiden änderst.

## Aufgabe 11
Erstelle ein verschachteltes Objekt `user` mit `address` als innerem Objekt. Führe eine tiefe Kopie durch und überprüfe, ob Änderungen im inneren Objekt des Klons das Original nicht beeinflussen.

## Aufgabe 12
Definiere eine Methode `addItem` auf dem Prototyp eines `Store`-Objekts. Erstelle ein `store`-Objekt und füge ein neues Item hinzu. Überprüfe, ob das Item korrekt hinzugefügt wurde.

## Aufgabe 13
Erstelle eine Methode `toUpperCase` im Prototyp von `String`, die den gesamten String in Großbuchstaben umwandelt. Verwende diese Methode an einem Beispielstring.

## Aufgabe 14
Erstelle ein Objekt `product` mit einer nicht-änderbaren und nicht-überschreibbaren Eigenschaft `id`. Verwende `Object.defineProperty` und überprüfe, ob die Eigenschaft tatsächlich unveränderlich ist.

## Aufgabe 15
Verwende `Object.getOwnPropertyDescriptor` auf einem Objekt, um die Konfigurationseinstellungen der Eigenschaft `price` anzuzeigen. Zeige die Einstellungen in der Konsole an.

## Aufgabe 16
Erstelle eine Factory-Funktion `createRectangle` mit den Parametern `width` und `height`. Füge eine Methode `getArea` hinzu, die die Fläche berechnet. Überprüfe die Methode mit einem Beispielrechteck.

## Aufgabe 17
Erstelle eine Constructor-Funktion `Person`, die Getters und Setters für die Eigenschaft `fullName` enthält. Teste die Getter- und Setter-Funktionalität.

## Aufgabe 18
Füge `Array.prototype` eine Methode `first` hinzu, die das erste Element eines Arrays zurückgibt. Teste die Methode an einem Beispielarray.

## Aufgabe 19
Erstelle ein `Employee`-Objekt mit einem nicht-überschreibbaren Prototyp. Versuche, den Prototyp zu ändern, und überprüfe das Ergebnis.

## Aufgabe 20
Schreibe eine Funktion `checkProperty`, die überprüft, ob eine Eigenschaft im Prototyp eines Objekts existiert, und gib das Ergebnis zurück. Teste die Funktion an einem Objekt und seinem Prototyp.

---

# Lösungen

## Lösung 1
```javascript
let person = { firstName: "John", lastName: "Doe" };
console.log("age" in person); // Output: false
```

## Lösung 2
```javascript
let car = { make: "Toyota", model: "Corolla", year: 2021 };
delete car.year;
console.log("year" in car); // Output: false
```

## Lösung 3
```javascript
let book = { title: "JavaScript Guide" };
let bookCopy = { ...book };
bookCopy.title = "Advanced JavaScript";
console.log(book.title); // Output: "JavaScript Guide"

```

## Lösung 4
```javascript
let user = {
    greet: function() {
        console.log("Hello!");
    }
};

user.greet(); // Output: "Hello!"

```

## Lösung 5
```javascript
let rectangle = {
    width: 10,
    height: 5,
    get area() {
        return this.width * this.height;
    },
    set area(value) {
        this.width = value / this.height;
    }
};

console.log(rectangle.area); // Output: 50
rectangle.area = 100;
console.log(rectangle.width); // Output: 20

```

## Lösung 6
```javascript
let config = {};
Object.defineProperty(config, "theme", {
    value: "dark",
    writable: false,
    configurable: false
});

config.theme = "light"; // Keine Änderung möglich
delete config.theme; // Löschen nicht möglich
console.log(config.theme); // Output: "dark"

```

## Lösung 7
```javascript
function createPerson(firstName, lastName) {
    return { firstName, lastName };
}

let person = createPerson("Alice", "Smith");
console.log(person);

```

## Lösung 8
```javascript
function Animal(species, age) {
    this.species = species;
    this.age = age;
}

let animal = new Animal("Dog", 5);
console.log(animal);

```

## Lösung 9
```javascript
let vehicle = {
    move: function() {
        console.log("Vehicle moving");
    }
};

let bike = Object.create(vehicle);
bike.move(); // Output: "Vehicle moving"

```

## Lösung 10
```javascript
let account = { balance: 100 };
let accountCopy = { ...account };
accountCopy.balance = 200;
console.log(account.balance); // Output: 100

```

## Lösung 11
```javascript
let user = {
    name: "Alice",
    address: {
        city: "Wonderland"
    }
};

let userClone = JSON.parse(JSON.stringify(user));
userClone.address.city = "Atlantis";
console.log(user.address.city); // Output: "Wonderland"

```

## Lösung 12
```javascript
function Store() {
    this.items = [];
}

Store.prototype.addItem = function(item) {
    this.items.push(item);
};

let myStore = new Store();
myStore.addItem("Apples");
console.log(myStore.items); // Output: ["Apples"]

```

## Lösung 13
```javascript
String.prototype.toUpperCase = function() {
    return this.toUpperCase();
};

console.log("hello".toUpperCase()); // Output: "HELLO"

```

## Lösung 14
```javascript
let product = {};
Object.defineProperty(product, "id", {
    value: 123,
    writable: false,
    configurable: false
});

product.id = 456; // Keine Änderung möglich
console.log(product.id); // Output: 123

```

## Lösung 15
```javascript
let item = { price: 100 };
let descriptor = Object.getOwnPropertyDescriptor(item, "price");
console.log(descriptor); // Output: {value: 100, writable: true, enumerable: true, configurable: true}

```

## Lösung 16
```javascript
function createRectangle(width, height) {
    return {
        width,
        height,
        getArea: function() {
            return width * height;
        }
    };
}

let rectangle = createRectangle(4, 5);
console.log(rectangle.getArea()); // Output: 20

```

## Lösung 17
```javascript
function Person() {
    let _fullName = "";

    Object.defineProperty(this, "fullName", {
        get: function() {
            return _fullName;
        },
        set: function(value) {
            _fullName = value;
        }
    });
}

let person = new

```

## Lösung 18
```javascript
Array.prototype.first = function() {
    return this[0];
};

let array = [1, 2, 3, 4];
console.log(array.first()); // Output: 1
```

## Lösung 19
```javascript
let Employee = {};
Object.freeze(Employee); // Objekt und sein Prototyp sind nicht änderbar

let Manager = Object.create(Employee);
Object.setPrototypeOf(Manager, null); // Versuch, den Prototyp zu ändern
console.log(Object.getPrototypeOf(Manager) === Employee); // Output: false

```

## Lösung 20
```javascript
function checkProperty(prop, obj) {
    return prop in obj && !obj.hasOwnProperty(prop);
}

let shape = { type: "generic" };
let circle = Object.create(shape);
circle.radius = 5;

console.log(checkProperty("type", circle)); // Output: true (type exists in prototype)
console.log(checkProperty("radius", circle)); // Output: false (radius is own property)

```

