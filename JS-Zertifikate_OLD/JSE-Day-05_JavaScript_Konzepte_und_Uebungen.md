
# JavaScript Konzepte und Übungen

## 5.1.1 Parameterüberprüfung (Parameters validation)
Parameterüberprüfung bedeutet, dass man überprüft, ob die Eingabewerte (Parameter) einer Funktion den erwarteten Anforderungen entsprechen, bevor man mit der Funktion fortfährt.

```javascript
function divide(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    console.error('Beide Parameter müssen Zahlen sein.');
    return;
  }
  if (b === 0) {
    console.error('Division durch Null ist nicht erlaubt.');
    return;
  }
  return a / b;
}

console.log(divide(10, 2)); // 5
console.log(divide(10, '2')); // Error
console.log(divide(10, 0)); // Error
```

### Übung
Schreibe eine Funktion `calculateArea`, die die Fläche eines Rechtecks berechnet. Wenn einer der Parameter keine Zahl ist, oder wenn einer der Parameter kleiner oder gleich Null ist, soll eine Fehlermeldung ausgegeben werden.

**Lösung**
```javascript
function calculateArea(width, height) {
  if (typeof width !== 'number' || typeof height !== 'number') {
    console.error('Beide Parameter müssen Zahlen sein.');
    return;
  }
  if (width <= 0 || height <= 0) {
    console.error('Parameter müssen größer als Null sein.');
    return;
  }
  return width * height;
}

console.log(calculateArea(5, 10)); // 50
console.log(calculateArea(5, -10)); // Error
console.log(calculateArea('5', 10)); // Error
```

## 5.1.2 Rekursion
Rekursion liegt vor, wenn eine Funktion sich selbst aufruft, um eine Aufgabe zu lösen.

```javascript
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(5)); // 120
```

### Übung
Erstelle eine rekursive Funktion `sumOfNumbers`, die die Summe der Zahlen von 1 bis n berechnet.

**Lösung**
```javascript
function sumOfNumbers(n) {
  if (n <= 1) return n;
  return n + sumOfNumbers(n - 1);
}

console.log(sumOfNumbers(5)); // 15
```

## 5.1.3 Funktionen als erste Bürger (Functions as first-class members)
Funktionen in JavaScript sind Objekte und können wie Variablen behandelt werden.

```javascript
const greet = function(name) {
  return `Hallo, ${name}`;
};

console.log(greet('Anna')); // Hallo, Anna
```

### Übung
Erstelle eine Funktion `executeOperation`, die eine andere Funktion als Argument erhält und diese mit zwei Zahlen ausführt.

**Lösung**
```javascript
function executeOperation(a, b, operation) {
  return operation(a, b);
}

const add = (x, y) => x + y;
console.log(executeOperation(5, 10, add)); // 15
```

## 5.1.4 Funktionsausdrücke (Function expressions)
Ein Funktionsausdruck erstellt eine Funktion innerhalb einer Variablen.

```javascript
const square = function(x) {
  return x * x;
};

console.log(square(4)); // 16
```

### Übung
Schreibe eine Funktion `multiply`, die als Funktionsausdruck definiert ist und zwei Zahlen multipliziert.

**Lösung**
```javascript
const multiply = function(a, b) {
  return a * b;
};

console.log(multiply(3, 4)); // 12
```

## 5.1.5 Rückruffunktionen (Callbacks)
Eine Callback-Funktion ist eine Funktion, die als Argument an eine andere Funktion übergeben und dort ausgeführt wird.

```javascript
function processArray(arr, callback) {
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]);
  }
}

processArray([1, 2, 3], (num) => console.log(num * 2));
```

### Übung
Schreibe eine Funktion `filterArray`, die ein Array und eine Bedingung als Callback erhält und nur die Elemente zurückgibt, die der Bedingung entsprechen.

**Lösung**
```javascript
function filterArray(arr, condition) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (condition(arr[i])) {
      result.push(arr[i]);
    }
  }
  return result;
}

console.log(filterArray([1, 2, 3, 4], (num) => num > 2)); // [3, 4]
```

## 5.1.6 Asynchrone Rückrufe (Asynchronous callbacks)
Asynchrone Rückrufe werden verwendet, um nicht blockierende Aufgaben zu erledigen, wie z. B. HTTP-Anfragen.

```javascript
function getData(callback) {
  setTimeout(() => {
    callback('Daten geladen');
  }, 2000);
}

getData((message) => console.log(message));
```

### Übung
Schreibe eine Funktion `fetchData`, die nach 3 Sekunden "Daten abgerufen" in die Konsole schreibt.

**Lösung**
```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback('Daten abgerufen');
  }, 3000);
}

fetchData((message) => console.log(message));
```

## 5.1.7 setTimeout und setInterval
Mit `setTimeout` kann man eine Funktion nach einer bestimmten Zeit ausführen, und mit `setInterval` kann man eine Funktion in regelmäßigen Abständen ausführen.

```javascript
setTimeout(() => {
  console.log('Eine Sekunde vergangen');
}, 1000);

let counter = 0;
const intervalId = setInterval(() => {
  counter++;
  console.log(`Sekunde: ${counter}`);
  if (counter === 5) clearInterval(intervalId);
}, 1000);
```

### Übung
Erstelle ein Countdown-Timer mit `setInterval`, der von 5 bis 0 zählt.

**Lösung**
```javascript
let countdown = 5;
const countdownId = setInterval(() => {
  console.log(countdown);
  countdown--;
  if (countdown < 0) clearInterval(countdownId);
}, 1000);
```

## 5.1.8 Pfeilfunktionen (Arrow functions)
Pfeilfunktionen sind eine verkürzte Syntax für Funktionsausdrücke und eignen sich besonders für einfache Funktionen.

```javascript
const double = (x) => x * 2;

console.log(double(5)); // 10
```

### Übung
Schreibe eine Pfeilfunktion `greetUser`, die eine Nachricht mit einem Namen ausgibt.

**Lösung**
```javascript
const greetUser = (name) => `Hallo, ${name}!`;

console.log(greetUser('Max')); // Hallo, Max!
```
