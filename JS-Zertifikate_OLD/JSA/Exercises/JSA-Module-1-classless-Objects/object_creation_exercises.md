# Übungsaufgaben: Alternative Ways to Create Objects in JavaScript

## Aufgabe 1
Erstelle ein Objekt namens `car` mithilfe der Objekt-Literal-Notation. Das Objekt sollte die Eigenschaften `make`, `model` und `year` enthalten.

## Aufgabe 2
Definiere eine Factory-Funktion `createCar`, die die Eigenschaften `make`, `model` und `year` verwendet, um ein neues Auto-Objekt zu erstellen. Verwende diese Funktion, um ein Auto-Objekt zu erstellen und die Eigenschaften in der Konsole anzuzeigen.

## Aufgabe 3
Erstelle eine weitere Factory-Funktion `createCircle` mit den Parametern `radius` und `color`. Nutze die Kurznotation (shorthand notation), um die Funktion zu erstellen und ein Beispiel-Objekt zu erzeugen. Gib das erstellte Objekt in der Konsole aus.

## Aufgabe 4
Verändere die `createCar` Factory-Funktion, sodass sie eine private Eigenschaft `_vin` enthält. Erstelle eine Methode `getVin`, die den Wert der privaten Eigenschaft zurückgibt. Verwende die Funktion, um ein neues Auto-Objekt zu erstellen und den `vin`-Wert in der Konsole anzuzeigen.

## Aufgabe 5
Schreibe eine Constructor-Funktion `Car` und erzeuge ein Auto-Objekt mit den Eigenschaften `make`, `model` und `year`. Verwende das Schlüsselwort `new`, um das Objekt zu erstellen und überprüfe, ob die Eigenschaften richtig gesetzt wurden.

## Aufgabe 6
Erstelle eine Constructor-Funktion `Rectangle`, die die Eigenschaften `width` und `height` annimmt. Implementiere eine Methode `getArea`, die die Fläche des Rechtecks berechnet und zurückgibt. Erstelle ein Rechteck-Objekt und rufe die Methode `getArea` auf.

## Aufgabe 7
Erstelle ein leeres Objekt mit dem `new Object()` Konstruktor. Füge anschließend die Eigenschaften `name` und `age` dynamisch hinzu und gib das Objekt in der Konsole aus.

## Aufgabe 8
Verwende `Object.create`, um ein neues Objekt `student` mit dem Prototyp `person` zu erstellen. Setze die Eigenschaft `person` so, dass sie den Wert `"Learner"` enthält. Überprüfe, ob `student` die `species`-Eigenschaft erbt.

## Aufgabe 9
Erstelle ein Objekt ohne Prototyp mithilfe von `Object.create(null)`. Überprüfe, ob es sich wie ein reguläres Objekt verhält und ob du ihm Eigenschaften hinzufügen kannst.

## Aufgabe 10
Definiere eine Klasse `Dog` mit einem Konstruktor, der die Eigenschaften `breed` und `age` initialisiert. Füge eine Methode `bark` hinzu, die den Text „Woof!“ in der Konsole ausgibt. Erstelle ein Hund-Objekt und lasse es „bellen“.

---

# Lösungen

## Lösung 1
```javascript
let car = {
    make: "Toyota",
    model: "Corolla",
    year: 2020
};
console.log(car);
```

## Lösung 2
```javascript
function createCar(make, model, year) {
    return {
        make: make,
        model: model,
        year: year
    };
}

let myCar = createCar("Honda", "Civic", 2018);
console.log(myCar);

```

## Lösung 3
```javascript
let createCircle = (radius, color) => ({ radius, color });

let circle = createCircle(10, "red");
console.log(circle);

```

## Lösung 4
```javascript
function createCar(make, model, year, vin) {
    let _vin = vin;
    return {
        make,
        model,
        year,
        getVin: () => _vin
    };
}

let carWithVin = createCar("Ford", "Fiesta", 2019, "123456");
console.log(carWithVin.getVin());

```

## Lösung 5
```javascript
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
}

let carObj = new Car("BMW", "X5", 2021);
console.log(carObj);

```

## Lösung 6
```javascript
function Rectangle(width, height) {
    this.width = width;
    this.height = height;
    
    this.getArea = function() {
        return this.width * this.height;
    };
}

let rect = new Rectangle(5, 10);
console.log(rect.getArea());

```

## Lösung 7
```javascript
let person = new Object();
person.name = "John";
person.age = 25;
console.log(person);

```

## Lösung 8
```javascript
let person = { species: "Learner" };
let student = Object.create(person);
console.log(student.species); // Output: "Learner"

```

## Lösung 9
```javascript
let trulyEmptyObject = Object.create(null);
trulyEmptyObject.name = "Nameless";
console.log(trulyEmptyObject);

```

## Lösung 10
```javascript
class Dog {
    constructor(breed, age) {
        this.breed = breed;
        this.age = age;
    }
    
    bark() {
        console.log("Woof!");
    }
}

let myDog = new Dog("Labrador", 3);
myDog.bark();

```

