
# Modul 4.1: Advanced Functions und Dekoratoren - Zusammenfassung

## 4.1.1 Extended Parameter Handling – Default Parameter Values

Mit der Einführung von ES6 können Parameter in Funktionen jetzt standardmäßig definierte Werte haben. Falls ein Parameter nicht angegeben wird, übernimmt er den vordefinierten Wert, anstatt `undefined` zu sein.

**Beispiel:**
```javascript
function greet(name = "Gast") {
    console.log(`Hallo, ${name}!`);
}

greet();         // Ausgabe: Hallo, Gast!
greet("Anna");   // Ausgabe: Hallo, Anna!
```

Hier ist `name` auf "Gast" festgelegt. Ruft man `greet()` ohne Argument auf, wird der Standardwert "Gast" verwendet.

**Mehrere Parameter mit Standardwerten:**
```javascript
function test(a, b = 1, c, d = 2) {
    console.log(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);
}
test();               // a: undefined, b: 1, c: undefined, d: 2
test(100);            // a: 100, b: 1, c: undefined, d: 2
test(100, 200);       // a: 100, b: 200, c: undefined, d: 2
```

---

## 4.1.2 The Rest Parameter

Der `Rest-Parameter` erlaubt es, eine variable Anzahl von Argumenten als Array zu verarbeiten.

**Beispiel:**
```javascript
function addNumbers(...numbers) {
    let sum = 0;
    numbers.forEach(num => sum += num);
    console.log(`Summe: ${sum}`);
}

addNumbers(1, 2, 3, 4);   // Ausgabe: Summe: 10
addNumbers(5, 10);        // Ausgabe: Summe: 15
```

---

## 4.1.3 The Spread Operator

Der `Spread-Operator` entpackt ein Array in einzelne Elemente, die dann als separate Argumente an eine Funktion übergeben werden können.

**Beispiel:**
```javascript
function logCoordinates(x, y, z) {
    console.log(`Koordinaten: x=${x}, y=${y}, z=${z}`);
}

let coordinates = [10, 20, 30];
logCoordinates(...coordinates);   // Ausgabe: Koordinaten: x=10, y=20, z=30
```

---

## 4.1.4 Simulating Named Parameters

In JavaScript kann man „Named Parameters“ simulieren, indem man ein Objekt verwendet, in dem die Parameter als Schlüssel-Wert-Paare gespeichert sind.

**Beispiel:**
```javascript
function createUser({ name, age, role = "User" }) {
    console.log(`Name: ${name}, Alter: ${age}, Rolle: ${role}`);
}

createUser({ name: "Max", age: 25 });                    // Name: Max, Alter: 25, Rolle: User
createUser({ name: "Lara", age: 30, role: "Admin" });   // Name: Lara, Alter: 30, Rolle: Admin
```

---

## 4.1.5 Closures

Ein *Closure* ist eine Funktion, die Zugriff auf ihre eigene lokale Umgebung sowie auf die Umgebungen ihrer äußeren Funktionen hat, auch nachdem die äußere Funktion beendet ist.

**Beispiel:**
```javascript
function counter() {
    let count = 0;
    return function() {
        count += 1;
        return count;
    };
}

let myCounter = counter();
console.log(myCounter());   // Ausgabe: 1
console.log(myCounter());   // Ausgabe: 2
console.log(myCounter());   // Ausgabe: 3
```

---

## 4.1.6 IIFE (Immediately Invoked Function Expression)

Ein *IIFE* ist eine Funktion, die sofort nach ihrer Definition ausgeführt wird. Sie hilft, den globalen Namensraum zu schützen.

**Beispiel:**
```javascript
(function() {
    let privateVar = "vertraulich";
    console.log("IIFE läuft!");
})();
```

---

## 4.1.7 Forwarding Calls (apply, call, bind)

Die Methoden `apply`, `call` und `bind` erlauben die Steuerung des `this`-Kontexts bei der Funktionsausführung.

**Beispiel:**
```javascript
let person = { name: "Lisa" };
function sayHi(greeting) {
    console.log(`${greeting}, ${this.name}`);
}
sayHi.call(person, "Hallo");      // Ausgabe: Hallo, Lisa
sayHi.apply(person, ["Hi"]);      // Ausgabe: Hi, Lisa

let boundSayHi = sayHi.bind(person);
boundSayHi("Hey");                // Ausgabe: Hey, Lisa
```

---

## 4.1.8 First-class Functions

In JavaScript sind Funktionen *First-class Citizens*, d.h., sie können wie Variablen verwendet werden.

**Beispiel:**
```javascript
let double = function(num) {
    return num * 2;
};
function processNum(fn, num) {
    return fn(num);
}

console.log(processNum(double, 5));   // Ausgabe: 10
```

---

## 4.1.9 Decorating Functions (Wrappers, Higher-order Functions)

Dekoratoren sind Funktionen, die andere Funktionen erweitern, indem sie zusätzliche Funktionalitäten hinzufügen.

**Beispiel:**
```javascript
function logDecorator(fn) {
    return function(...args) {
        console.log(`Aufruf mit Argumenten: ${args}`);
        return fn(...args);
    };
}

function add(a, b) {
    return a + b;
}

let decoratedAdd = logDecorator(add);
console.log(decoratedAdd(3, 4));   // Ausgabe: Aufruf mit Argumenten: 3,4
                                   // 7
```
