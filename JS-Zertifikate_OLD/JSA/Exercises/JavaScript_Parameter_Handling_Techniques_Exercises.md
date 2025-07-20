
# JavaScript-Parameterbehandlungstechniken - Aufgabeen
## Aufgabe 1
Erstellen Sie eine Funktion, die zwei Parameter akzeptiert und jedem einen Standardwert zuweist. Rufen Sie die Funktion sowohl mit als auch ohne Parameter auf. Beobachten und protokollieren Sie die Ausgaben.

## Aufgabe 2
Schreiben Sie eine Funktion, die den Restparameter benutzt, um eine beliebige Anzahl von numerischen Argumenten zu summieren. Testen Sie die Funktion mit keinem Argument, einem Argument und mehreren Argumenten.

## Aufgabe 3
Erstellen Sie mit Hilfe des Spread-Operators eine Funktion, die drei Zahlen als Argumente annimmt und deren Durchschnitt zurückgibt. Rufen Sie diese Funktion mit einem Array von drei Zahlen auf.

## Aufgabe 4
Implementieren Sie eine Funktion, die zwei Arrays mit Hilfe des Spread-Operators zusammenführt. Die Funktion sollte das kombinierte Array zurückgeben. Testen Sie die Funktion mit verschiedenen Arrays.

## Aufgabe 5
Erstellen Sie eine Funktion, die ein Konfigurationsobjekt annimmt. Verwenden Sie Destrukturierung, um Standardwerte für die Konfigurationsfelder bereitzustellen. Rufen Sie die Funktion mit fehlenden Feldern auf, um die Vorgabewerte zu testen.

## Aufgabe 6
Schreiben Sie eine Funktion, die ein Objekt mit bestimmten Eigenschaften annimmt und eine Zusammenfassung der Eigenschaften des Objekts in einem String-Format zurückgibt. Verwenden Sie Destrukturierung in der Funktionsdefinition.

## Aufgabe 7
Implementieren Sie eine Funktion, die benannte Parameter für einen Einkaufswagen simuliert (z.B. `Name`, `Preis`, `Menge`). Berechnen und protokollieren Sie den Gesamtpreis unter Verwendung von Standardwerten für fehlende Parameter.

## Aufgabe 8
Erstellen Sie eine Schließungsfunktion, die bei jedem Aufruf eindeutige IDs erzeugt. Testen Sie, indem Sie sie mehrfach aufrufen.

## Aufgabe 9
Schreiben Sie eine Funktion, die einen Zählerabschluss erzeugt. Der Zähler sollte eine Inkrement-Methode, eine Reset-Methode und eine Methode zum Abrufen des aktuellen Zählerstands haben.

## Aufgabe 10
Implementieren Sie ein IIFE, das eine Variable initialisiert und ihren Wert sofort protokolliert. Stellen Sie sicher, dass auf die Variable außerhalb des IIFEs nicht zugegriffen werden kann.

## Aufgabe 11
Erstellen Sie eine Funktion, die `call` benutzt, um ihren `this` Wert zu setzen. Testen Sie sie, indem Sie die Funktion aufrufen und ein Objekt mit Eigenschaften übergeben, die dem erwarteten „this“-Kontext der Funktion entsprechen.

## Aufgabe 12
Schreiben Sie unter Verwendung von `apply` eine Funktion, die die Summe einer Reihe von Zahlen berechnet, indem sie eine andere Funktion mit der Reihe als individuelle Argumente aufruft.

## Aufgabe 13
Implementieren Sie eine Funktion, die eine gebundene Funktion zurückgibt, wobei der `this`-Kontext auf ein bestimmtes Objekt festgelegt ist. Überprüfen Sie, dass die zurückgegebene Funktion immer den gebundenen Kontext verwendet.

## Aufgabe 14
Schreiben Sie eine Funktion, die eine andere Funktion als Argument annimmt und eine dekorierte Funktion zurückgibt, die die Ausführungszeit protokolliert. Benutzen Sie `console.time` und `console.timeEnd` um zu messen.

## Aufgabe 15
Erstellen Sie eine Dekorfunktion, die einer teuren Funktion, wie der Berechnung von Fibonacci-Zahlen, Memoisierung hinzufügt. Stellen Sie sicher, dass der Dekorator die berechneten Ergebnisse speichert und sie abruft, wenn die Funktion mit den gleichen Argumenten aufgerufen wird.

---

## Solutions

```javascript
// Solution for Exercise 1
function greet(name = "User", role = "Guest") {
    console.log(`Hello, ${name}. You are a ${role}.`);
}
greet();
greet("Alice", "Admin");

// Solution for Exercise 2
function sumAll(...nums) {
    return nums.reduce((acc, num) => acc + num, 0);
}
console.log(sumAll());
console.log(sumAll(5));
console.log(sumAll(1, 2, 3));

// Solution for Exercise 3
function average(a, b, c) {
    return (a + b + c) / 3;
}
let nums = [4, 8, 12];
console.log(average(...nums));

// Solution for Exercise 4
function mergeArrays(arr1, arr2) {
    return [...arr1, ...arr2];
}
console.log(mergeArrays([1, 2], [3, 4]));

// Solution for Exercise 5
function configureServer({host = "localhost", port = 80, secure = false} = {}) {
    console.log(`Server running at ${host}:${port}, secure: ${secure}`);
}
configureServer({host: "127.0.0.1"});

// Solution for Exercise 6
function summarizeObject({name, age, occupation} = {}) {
    return `${name} is a ${age}-year-old ${occupation}.`;
}
console.log(summarizeObject({name: "Alice", age: 30, occupation: "Engineer"}));

// Solution for Exercise 7
function cartItem({name = "Item", price = 10, quantity = 1} = {}) {
    console.log(`Total for ${name}: ${price * quantity}`);
}
cartItem({name: "Apple", price: 2, quantity: 5});

// Solution for Exercise 8
function uniqueIDGenerator() {
    let id = 0;
    return function() { return ++id; };
}
const generateID = uniqueIDGenerator();
console.log(generateID());
console.log(generateID());

// Solution for Exercise 9
function createCounter() {
    let count = 0;
    return {
        increment() { count++; },
        reset() { count = 0; },
        getCount() { return count; }
    };
}
const counter = createCounter();
counter.increment();
console.log(counter.getCount());

// Solution for Exercise 10
(function() {
    let secret = "This is private";
    console.log(secret);
})();

// Solution for Exercise 11
function showCoords() {
    console.log(`${this.x}, ${this.y}`);
}
showCoords.call({x: 10, y: 20});

// Solution for Exercise 12
function sum(...args) {
    return args.reduce((a, b) => a + b, 0);
}
console.log(sum.apply(null, [5, 10, 15]));

// Solution for Exercise 13
const obj = {name: "Alice"};
function greet() { return `Hello, ${this.name}`; }
const boundGreet = greet.bind(obj);
console.log(boundGreet());

// Solution for Exercise 14
function measureExecution(fn) {
    return function(...args) {
        console.time("Execution Time");
        const result = fn(...args);
        console.timeEnd("Execution Time");
        return result;
    };
}
const fastFunction = measureExecution((num) => num * 2);
console.log(fastFunction(10));

// Solution for Exercise 15
function memoize(fn) {
    const cache = new Map();
    return function(arg) {
        if (cache.has(arg)) return cache.get(arg);
        const result = fn(arg);
        cache.set(arg, result);
        return result;
    };
}
const fibonacci = (n) => n <= 1 ? n : fibonacci(n - 1) + fibonacci(n - 2);
const memoizedFibonacci = memoize(fibonacci);
console.log(memoizedFibonacci(10));
```
