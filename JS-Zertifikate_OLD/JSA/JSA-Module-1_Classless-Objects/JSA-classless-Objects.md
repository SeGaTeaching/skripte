# JSA – Certified Associate JavaScript Programmer Course

## Part 1: JavaScript Data Types and Arrays

### 1.1 Primitive Data Types
JavaScript unterstützt mehrere primitive Datentypen: **number**, **boolean**, **sstring** und **undefined**. So können Sie mit dem Operator `typeof` den Typ eines Wertes überprüfen:
```javascript
console.log(typeof 42); // "number"
console.log(typeof "Hello, world!"); // "string"
console.log(typeof true); // "boolean"
console.log(typeof undefined); // "undefined"
```
Werte können in Variablen gespeichert und manipuliert werden. Wenn eine Variable deklariert, aber nicht zugewiesen ist, enthält sie einen undefinierten Wert.

```javascript
let myVar;
console.log(typeof myVar); // "undefined"

myVar = 15;
console.log(typeof myVar); // "number"
```
Primitive sind einfache Datentypen, die einen einzigen Wert enthalten.

### 1.2 Arrays as a Complex Type
Arrays werden verwendet, um geordnete Sammlungen von Werten zu speichern. Auf Array-Elemente kann über ihren Index (beginnend bei 0) zugegriffen werden:
```javascript
let myArray = [10, "hello", true, 50];
console.log(myArray[1]); // "hello"
myArray[3] = myArray[3] * 2;
console.log(myArray[3]); // 100
```
Arrays sind flexibel, und die Elemente können von verschiedenen Typen sein. JavaScript-Arrays sind null-indiziert, d.h. das erste Element hat einen Index von 0, das zweite einen Index von 1 und so weiter.

### 1.3 Objekte als komplexe Typen
Objekte sind Sammlungen von Eigenschaften, wobei jede Eigenschaft ein Schlüssel-Wert-Paar ist. Der Zugriff auf Objekteigenschaften erfolgt über die Punkt- oder Klammerschreibweise:
```javascript
let person = {
    name: "John",
    age: 30,
    isEmployed: true
};
console.log(person.name); // "John"
person.age = 31;
console.log(person.age); // 31
```
Objekte sind nützlich für die Speicherung strukturierter Daten und können mehrere Eigenschaften verschiedener Datentypen, einschließlich anderer Objekte oder Arrays, enthalten.

### 1.4 Arrays und Objekt kombinieren
JavaScript ermöglicht die Erstellung von verschachtelten Strukturen, die Arrays und Objekte kombinieren:
```javascript
let company = {
    name: "Tech Corp",
    employees: [
        { name: "Alice", role: "Engineer" },
        { name: "Bob", role: "Designer" }
    ]
};

console.log(company.employees[0].name); // "Alice"
company.employees[1].role = "Lead Designer";
console.log(company.employees[1].role); // "Lead Designer"
```
Durch die Verschachtelung von Arrays innerhalb von Objekten oder umgekehrt können wir in JavaScript komplexere Datenstrukturen darstellen.


## Part 2: Objects and Methods in JavaScript

### 2.1 Creating and Modifying Objects
JavaScript objects are collections of properties, where each property is a key-value pair. You can create objects using literal notation, the `new Object()` syntax, or constructor functions.

### Object Literal Notation
```javascript
let car = {
    make: "Toyota",
    model: "Corolla",
    year: 2020
};
car.color = "blue"; // Adding a new property
delete car.year; // Removing a property
```

Using new Object()
```javascript
let person = new Object();
person.name = "Alice";
person.age = 25;
```

### 2.2 Dot Notation vs Bracket Notation
Der Zugriff auf Eigenschaften kann in Punktschreibweise (object.property) oder in Klammerschreibweise (object[„property“]) erfolgen.

#### Dot Notation
```javascript
let book = { title: "1984", author: "George Orwell" };
console.log(book.title); // "1984"
```
#### Bracket Notation
Nützlich, wenn Eigenschaftsnamen dynamisch sind oder Leerzeichen enthalten:
```javascript
let movie = { "movie title": "Inception" };
console.log(movie["movie title"]); // "Inception"

let propertyName = "title";
console.log(book[propertyName]); // "1984"
```

### 2.3 Object Methods and `this` keyword
Methoden sind Funktionen, die als Objekteigenschaften gespeichert werden. Das Schlüsselwort this bezieht sich auf den Objektkontext.
```javascript
let calculator = {
    add: function(a, b) { return a + b; },
    subtract(a, b) { return a - b; } // Shorthand method
};
console.log(calculator.add(5, 3)); // 8
```

```javascript
let user = {
    name: "John",
    greet() {
        return `Hello, ${this.name}!`;
    }
};
console.log(user.greet()); // "Hello, John!"
```

### 2.4 Getters and Setters
Getter und Setter ermöglichen die Kontrolle darüber, wie auf Eigenschaften zugegriffen oder diese geändert werden.

**Getters**
```javascript
let person = {
    firstName: "Alice",
    lastName: "Smith",
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
};
console.log(person.fullName); // "Alice Smith"
```

**Setters**
```javascript
let employee = {
    _salary: 50000,
    set salary(newSalary) {
        if (newSalary > 0) this._salary = newSalary;
        else console.log("Invalid salary!");
    }
};
employee.salary = 55000;
console.log(employee._salary); // 55000
```
Getter und Setter ermöglichen die Kapselung und erlauben den indirekten Zugriff auf Eigenschaften bei gleichzeitiger Hinzufügung von Steuerungslogik.

### 2.5 Cloning
Das Kopieren von Objekten kann auf zwei Arten erfolgen: oberflächliches Klonen und tiefes Klonen.

Oberflächliches Klonen mit Object.assign und Spread Operator

Beim oberflächlichen Klonen werden nur die Eigenschaften der obersten Ebene dupliziert.

```javascript
let obj = { a: 1, b: { c: 2 } };
let shallowCopy = { ...obj };
shallowCopy.b.c = 3;
console.log(obj.b.c); // 3, original object is affected
```

**Deep Cloning with JSON and Recursive Functions**
```javascript
let deepCopy = JSON.parse(JSON.stringify(obj));
deepCopy.b.c = 4;
console.log(obj.b.c); // 3, original object remains unchanged
```

More Complex
```javascript
function deepClone(obj) {
    if (obj === null || typeof obj !== 'object') return obj;
    let copy = Array.isArray(obj) ? [] : {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            copy[key] = deepClone(obj[key]);
        }
    }
    return copy;
}

let anotherCopy = deepClone(obj);
anotherCopy.b.c = 5;
console.log(obj.b.c); // 3, deep clone is independent
```
Für zirkuläre Referenzen bieten Bibliotheken wie Lodash tiefgreifende Klonwerkzeuge. Diese Beispiele decken das Wesentliche für manuelles Klonen ab und bieten eine Grundlage für das Verständnis der Objektmanipulation in JavaScript.


## Part 3: Advanced Object Concepts in JavaScript

### 3.1 Property Configuration with `Object.defineProperty`
JavaScript allows detailed configuration of object properties using `Object.defineProperty`. You can control three main attributes:
- **writable**: Determines if the property’s value can be changed.
- **enumerable**: Determines if the property can be iterated over or listed.
- **configurable**: Determines if the property can be deleted or reconfigured.

#### Example with Writable, Enumerable, and Configurable Flags
```javascript
let person = {};
Object.defineProperty(person, 'name', {
    value: 'Alice',
    writable: false,
    enumerable: true,
    configurable: true
});

console.log(person.name); // "Alice"
person.name = 'Bob'; // Error in strict mode
console.log(Object.keys(person)); // ["name"]
delete person.name; // Successfully deletes as configurable is true
```
Durch das Ändern dieser Flags steuern Sie das Verhalten der Eigenschaften und können so die Objektstruktur schützen.

### 3.2 Prototypes and Inheritance
JavaScript verwendet ein prototypisches Vererbungsmodell, bei dem Objekte Eigenschaften von anderen Objekten erben können. Jedes Objekt hat einen Prototyp, der über Object.create() oder __proto__ zugänglich ist.
```javascript
let animal = {
    eats: true,
    walk() { console.log("Animal walks"); }
};

let rabbit = Object.create(animal);
rabbit.jumps = true;

console.log(rabbit.eats); // true, inherited
rabbit.walk(); // "Animal walks"
```
Das Kaninchenobjekt erbt von animal. Eigenschaften und Methoden, die sich nicht direkt auf rabbit beziehen, werden in seinem Prototyp (animal) nachgeschlagen.

Mit Prototypen können Sie eine Hierarchie von Objekten erstellen:
```javascript
let cat = {
    meow() { console.log("Meow!"); }
};

let fluffy = Object.create(cat);
fluffy.name = "Fluffy";
fluffy.meow(); // "Meow!"
```
Hier erbt fluffy die Miau-Methode von cat und zeigt damit, wie Objekte ein gemeinsames Verhalten haben können.


### 3.3 Constructors and the new Keyword
Mit Konstruktoren können Sie mehrere Instanzen ähnlicher Objekte erstellen. Der Konvention nach beginnen Konstruktoren mit einem Großbuchstaben.
```javascript
function Car(make, model) {
    this.make = make;
    this.model = model;
}

Car.prototype.start = function() {
    console.log(this.make + " " + this.model + " starts.");
};

let myCar = new Car("Honda", "Civic");
myCar.start(); // "Honda Civic starts."
```
Mit new erstellt JavaScript eine Instanz mit einer Verbindung zu Car.prototype.

**Chaining Constructors with Inheritance**
```javascript
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    console.log(this.name + " makes a noise.");
};

function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

let dog = new Dog("Rex", "Labrador");
dog.speak(); // "Rex makes a noise."
```
Hier erbt Dog von Animal, so dass Sie Eigenschaften und Methoden verketten können.




