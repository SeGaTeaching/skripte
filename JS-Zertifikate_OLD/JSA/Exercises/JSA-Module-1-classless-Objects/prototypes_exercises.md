# Übungsaufgaben: Understanding Prototypes in JavaScript

## Aufgabe 1
Erstelle ein Objekt `animal` mit der Eigenschaft `species`. Erstelle ein weiteres Objekt `dog`, setze dessen Prototyp auf `animal`, und greife auf die `species`-Eigenschaft über das `dog`-Objekt zu. Überprüfe das Ergebnis in der Konsole.

## Aufgabe 2
Verwende `Object.setPrototypeOf`, um das Objekt `car` als Prototyp des Objekts `electricCar` festzulegen. Gib in der Konsole eine Eigenschaft von `car` über das `electricCar`-Objekt aus.

## Aufgabe 3
Nutze `Object.create`, um ein neues Objekt `square` mit dem Prototyp `shape` zu erstellen. Füge dem `square`-Objekt eine Eigenschaft `sideLength` hinzu und gib diese in der Konsole aus.

## Aufgabe 4
Erstelle eine Constructor-Funktion `Animal` mit einer Methode `speak`. Erstelle eine weitere Constructor-Funktion `Dog`, setze den Prototyp von `Dog` auf `Animal`, und teste, ob Instanzen von `Dog` auf die Methode `speak` zugreifen können.

## Aufgabe 5
Füge der `Array.prototype` eine Methode `first` hinzu, die das erste Element eines Arrays zurückgibt. Verwende diese Methode an einem Beispiel-Array, um das erste Element auszugeben.

## Aufgabe 6
Erstelle ein Objekt `person` mit einer Methode `greet`. Verwende den `__proto__`-Weg, um ein weiteres Objekt `friend` zu erstellen, das von `person` erbt. Rufe die Methode `greet` auf `friend` auf.

## Aufgabe 7
Definiere eine Methode `toUpperCaseFirst` auf `String.prototype`, die den ersten Buchstaben eines Strings in Großbuchstaben umwandelt. Verwende diese Methode an einem Beispielstring.

---

# Lösungen

## Lösung 1
```javascript
let animal = { species: "mammal" };
let dog = {};
dog.__proto__ = animal;
console.log(dog.species); // Output: "mammal"
```

## Lösung 2
```javascript
let car = { wheels: 4 };
let electricCar = {};
Object.setPrototypeOf(electricCar, car);
console.log(electricCar.wheels); // Output: 4

```

## Lösung 3
```javascript
let shape = { type: "2D" };
let square = Object.create(shape);
square.sideLength = 5;
console.log(square.sideLength); // Output: 5

```

## Lösung 4
```javascript
function Animal() {
    this.speak = function() {
        console.log("Animal speaking");
    };
}

function Dog() {
    this.bark = function() {
        console.log("Woof!");
    };
}

Dog.prototype = new Animal();
let myDog = new Dog();
myDog.speak(); // Output: "Animal speaking"
myDog.bark();  // Output: "Woof!"

```

## Lösung 5
```javascriptc
Array.prototype.first = function() {
    return this[0];
};

let numbers = [1, 2, 3, 4];
console.log(numbers.first()); // Output: 1

```

## Lösung 6
```javascript
let person = {
    greet: function() {
        console.log("Hello!");
    }
};

let friend = {};
friend.__proto__ = person;
friend.greet(); // Output: "Hello!"

```

## Lösung 7
```javascript
String.prototype.toUpperCaseFirst = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

let greeting = "hello";
console.log(greeting.toUpperCaseFirst()); // Output: "Hello"

```

