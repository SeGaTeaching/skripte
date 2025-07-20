
# Composite Data Types in JavaScript (JSA Course)

## 3.2.1 Composite Data Types Overview
In JavaScript, composite data types allow the storage of multiple values within a single structure. These types are dynamic, meaning both their content and size can change over time.

---

## 3.2.2 Arrays: Basics and Definition
An **array** is a type of data structure that stores elements in an ordered sequence. Arrays use zero-based indexing to access elements.

### Syntax
```javascript
let arrayName = [element1, element2, ..., elementN];
// or
let arrayName = new Array(element1, element2, ..., elementN);
```

- **element1, element2, ..., elementN**: Initial elements of the array (optional). Can be of any data type.

### Examples and Explanations:
```javascript
let mixedArray = [1, "two", true, { key: "value" }];
console.log(mixedArray[1]); // Output: "two"
console.log(mixedArray.length); // Output: 4

// Accessing non-existent elements returns 'undefined'
console.log(mixedArray[5]); // Output: undefined
```

---

## 3.2.3 Creating Arrays
Arrays can be created with the array literal `[]` or the Array constructor `new Array()`. Using literals is preferred as it’s more concise.

### Syntax
```javascript
let array = [];
let arrayWithElements = [element1, element2, ..., elementN];
let newArray = new Array(length);
```

- **length**: When used with `new Array()`, defines the initial length of the array, setting each position to `undefined`.

### Examples and Explanations:
```javascript
let emptyArray = []; // An empty array with zero elements
let numericArray = [1, 2, 3, 4, 5]; // Array with initial values
let constructedArray = new Array(3); // Creates an array with 3 empty slots

// Mixed elements within the array
let mixedArray = ["apple", 42, false, [1, 2, 3]];
console.log(mixedArray.length); // Output: 4
```

---

## 3.2.4 Merging Arrays with `concat`
The `concat` method joins two or more arrays, producing a new array while leaving the original arrays unmodified.

### Syntax
```javascript
array.concat(array1, array2, ..., arrayN);
```

- **array1, array2, ..., arrayN**: Arrays or values to concatenate with the original array.

### Examples and Explanations:
```javascript
let array1 = [1, 2, 3];
let array2 = [4, 5];
let mergedArray = array1.concat(array2); // -> [1, 2, 3, 4, 5]

// Original arrays remain unaltered
console.log(array1); // Output: [1, 2, 3]
console.log(mergedArray); // Output: [1, 2, 3, 4, 5]
```

---

## 3.2.5 Adding Elements with `push` and `unshift`
- `push` adds elements to the array's end.
- `unshift` adds elements to the array's start.

### Syntax
```javascript
array.push(element1, element2, ..., elementN);
array.unshift(element1, element2, ..., elementN);
```

- **element1, element2, ..., elementN**: Elements to add at the beginning or end of the array.

### Examples and Explanations:
```javascript
let fruits = ["apple", "banana"];
fruits.push("cherry"); // -> ["apple", "banana", "cherry"]
fruits.unshift("mango"); // -> ["mango", "apple", "banana", "cherry"]
console.log(fruits); // Output: ["mango", "apple", "banana", "cherry"]
```

---

## 3.2.6 Removing Elements with `pop` and `shift`
- `pop` removes the last element, returning it.
- `shift` removes the first element, returning it.

### Syntax
```javascript
array.pop();
array.shift();
```

- **Returns**: The removed element, or `undefined` if the array is empty.

### Examples and Explanations:
```javascript
let colors = ["red", "blue", "green"];
let lastColor = colors.pop(); // Output: "green", colors -> ["red", "blue"]
let firstColor = colors.shift(); // Output: "red", colors -> ["blue"]
```

---

## 3.2.7 Direct Addition and Deletion of Elements
You can add elements by assigning them to an index. `delete` removes an element but leaves an empty slot.

### Syntax
```javascript
array[index] = value;
delete array[index];
```

- **index**: Position of the element to be added or deleted.
- **value**: Value to assign at the specified position.

### Examples and Explanations:
```javascript
let array = [1, 2, 3];
array[5] = 6; // Adds elements up to index 5, array -> [1, 2, 3, undefined, undefined, 6]
delete array[1]; // -> [1, undefined, 3, undefined, undefined, 6]
```

---

## 3.2.8 Iterating with `forEach`
`forEach` executes a function on each element. Useful for applying a consistent operation.

### Syntax
```javascript
array.forEach(function(element, index, array) { /* code */ });
```

- **element**: Current element being processed.
- **index**: Position of the current element (optional).
- **array**: The original array being processed (optional).

### Examples and Explanations:
```javascript
let animals = ["cat", "dog", "elephant"];
animals.forEach((animal, index) => {
    console.log(`${index}: ${animal}`);
});
// Output:
// 0: cat
// 1: dog
// 2: elephant
```

---

## 3.2.9 Testing Conditions with `every` and `some`
- `every`: checks if all elements satisfy a condition.
- `some`: checks if at least one element satisfies a condition.

### Syntax
```javascript
array.every(callback(element, index, array));
array.some(callback(element, index, array));
```

- **callback**: A function testing each element (returns true or false).

### Examples and Explanations:
```javascript
let scores = [50, 70, 80];
console.log(scores.every(score => score > 40)); // Output: true
console.log(scores.some(score => score > 75)); // Output: true
```

---

## 3.2.10 Filtering Elements with `filter`
`filter` creates a new array with elements that pass a given condition.

### Syntax
```javascript
array.filter(callback(element, index, array));
```

- **callback**: Function to test each element; elements returning true are included.

### Examples and Explanations:
```javascript
let numbers = [5, 12, 8, 130, 44];
let largeNumbers = numbers.filter(num => num > 10);
console.log(largeNumbers); // Output: [12, 130, 44]
```

---

## 3.2.11 Mapping Elements with `map`
The `map` method returns a new array after applying a function to each element.

### Syntax
```javascript
array.map(callback(element, index, array));
```

- **callback**: Function that modifies each element for the new array.

### Examples and Explanations:
```javascript
let numbers = [1, 2, 3];
let doubled = numbers.map(num => num * 2); // Output: [2, 4, 6]
```

---

## 3.2.12 Sorting Arrays with `sort`
The `sort` method arranges elements by a comparison function. Works on the original array.

### Syntax
```javascript
array.sort([compareFunction(firstEl, secondEl)]);
```

- **compareFunction**: Function that defines the sorting order.

### Examples and Explanations:
```javascript
let nums = [30, 4, 12, 100];
nums.sort((a, b) => a - b); // Output: [4, 12, 30, 100]
```

---

## 3.2.13 Reducing Arrays with `reduce`
`reduce` processes all elements to accumulate a result.

### Syntax
```javascript
array.reduce(callback(accumulator, element, index, array), initialValue);
```

- **callback**: Function to reduce elements.
- **initialValue**: Optional initial value of the accumulator.

### Examples and Explanations:
```javascript
let numbers = [1, 2, 3, 4];
let sum = numbers.reduce((acc, val) => acc + val, 0);
console.log(sum); // Output: 10
```

Die Methode reduce ist in JavaScript eine kraftvolle Möglichkeit, um Werte in einem Array auf einen einzigen kumulierten Wert zu reduzieren. Dabei kann diese Funktion nicht nur für einfache Summen oder Produkte verwendet werden, sondern auch für komplexere Transformationen und Aggregationen.

Funktionsweise und Syntax
Die reduce-Methode geht von links nach rechts durch das Array und führt eine Funktion auf jedes Element aus. Diese Funktion hat Zugriff auf einen sogenannten Akkumulator, der den "angesammelten" Wert zwischen den einzelnen Schleifendurchläufen enthält.

Syntax
```javascript
Copy code
array.reduce((accumulator, currentValue, index, array) => {
    // Transformation des Accumulators
}, initialValue);
```
Parameter
accumulator: Speichert das Zwischenergebnis und wird bei jedem Durchlauf aktualisiert.
currentValue: Das aktuelle Element, das gerade verarbeitet wird.
index: Der Index des aktuellen Elements (optional).
array: Das gesamte Array, auf dem reduce angewendet wird (optional).
initialValue: Ein optionaler Startwert für den Akkumulator. Wenn dieser Wert nicht angegeben wird, nimmt reduce den ersten Wert des Arrays als Startwert und beginnt erst beim zweiten Element.
Ablauf von reduce
Beim ersten Durchlauf ist der accumulator entweder der initialValue oder (wenn keiner angegeben ist) das erste Element des Arrays.
Die reduce-Funktion wendet die Logik auf den currentValue und den accumulator an und gibt den neuen Wert des accumulators zurück.
Der neue Wert des accumulators wird im nächsten Durchlauf als accumulator weitergegeben.
Dieser Prozess wiederholt sich, bis alle Array-Elemente durchlaufen sind.
Am Ende gibt reduce den finalen accumulator zurück.
Beispiel: Summe berechnen
Hier summieren wir alle Zahlen in einem Array:

```javascript
Copy code
let numbers = [10, 20, 30, 40];
let sum = numbers.reduce((acc, curr) => acc + curr, 0);
console.log(sum); // Ausgabe: 100
```
accumulator startet mit dem Wert 0 (da wir 0 als initialValue angegeben haben).
Bei jedem Durchlauf wird curr (das aktuelle Element) zum accumulator addiert.
Am Ende der Schleife beträgt der accumulator 100.
Beispiel ohne initialValue

javascript
Copy code
let numbers = [10, 20, 30, 40];
let sum = numbers.reduce((acc, curr) => acc + curr);
console.log(sum); // Ausgabe: 100
In diesem Fall startet der accumulator automatisch mit dem ersten Wert des Arrays (10), und der currentValue beginnt bei 20.

Fortgeschrittenes Beispiel: Array in ein Objekt umwandeln
Mit reduce lässt sich auch komplexere Logik umsetzen, wie zum Beispiel das Erstellen eines Zähler-Objekts, das die Anzahl jedes Werts im Array speichert.

```javascript
let fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];
let fruitCount = fruits.reduce((acc, fruit) => {
    acc[fruit] = (acc[fruit] || 0) + 1;
    return acc;
}, {});
console.log(fruitCount);
// Ausgabe: { apple: 3, banana: 2, orange: 1 }
```
Hier verwenden wir acc als Objekt, das die Häufigkeit jedes Obstnamens speichert.
Bei jedem Durchlauf prüfen wir, ob fruit im acc-Objekt existiert. Wenn ja, wird der Wert um eins erhöht. Falls nicht, wird der Wert auf 1 gesetzt.
Beispiel mit initialValue als Objekt
In diesem Beispiel wird reduce verwendet, um ein Array in ein Objekt mit Schlüsseln und Werten zu verwandeln.

```javascript
let words = ["one", "two", "three"];
let wordLengths = words.reduce((acc, word) => {
    acc[word] = word.length;
    return acc;
}, {});
console.log(wordLengths);
// Ausgabe: { one: 3, two: 3, three: 5 }
```
Hier wird reduce mit einem leeren Objekt {} als initialValue aufgerufen, und jede Schleifeniteration fügt dem Objekt den aktuellen Wert als Schlüssel und die Länge des Worts als Wert hinzu.

Wichtige Hinweise zur Verwendung
Eingriffsmöglichkeiten: reduce bietet große Flexibilität, da der accumulator jede beliebige Struktur annehmen kann, z.B. Zahlen, Strings, Arrays oder Objekte.
Kein initialValue: Wenn kein initialValue angegeben wird, startet reduce mit dem ersten Element des Arrays als accumulator. Dies kann problematisch sein, wenn das Array leer ist.
Fazit
reduce eignet sich hervorragend zur Aggregation und Transformation von Array-Daten und bietet eine leistungsfähige Möglichkeit, komplexe Operationen und Berechnungen auf Array-Elementen durchzuführen. Es ist jedoch wichtig, die Funktionsweise zu verstehen, um Fehler zu vermeiden, und die initialen Werte sinnvoll zu wählen.
---

## 3.2.15 Searching for an Element in an Array

JavaScript provides multiple methods to search for specific items within an array, including **`includes`**, **`indexOf`**, **`lastIndexOf`**, **`find`**, and **`findIndex`**.

### 1. `includes`
Checks if a specific value is present in the array.

#### Syntax
```javascript
array.includes(valueToFind, fromIndex);
```

- **valueToFind**: The value to search for.
- **fromIndex**: (Optional) The index to start the search from. Defaults to `0`.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster"];
console.log(animals.includes("dog")); // Output: true
console.log(animals.includes("elephant")); // Output: false
console.log(animals.includes("cat", 1)); // Output: false
```

### 2. `indexOf`
Returns the index of the first occurrence of a specified value, or `-1` if it is not found.

#### Syntax
```javascript
array.indexOf(searchElement, fromIndex);
```

- **searchElement**: The value to search for.
- **fromIndex**: (Optional) The index to start searching from. Defaults to `0`.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster", "dog"];
console.log(animals.indexOf("dog")); // Output: 1
console.log(animals.indexOf("elephant")); // Output: -1
console.log(animals.indexOf("dog", 2)); // Output: 3
```

### 3. `lastIndexOf`
Works like `indexOf`, but starts the search from the end of the array.

#### Syntax
```javascript
array.lastIndexOf(searchElement, fromIndex);
```

- **searchElement**: The value to search for.
- **fromIndex**: (Optional) The index to start searching backwards from.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster", "dog"];
console.log(animals.lastIndexOf("dog")); // Output: 3
console.log(animals.lastIndexOf("elephant")); // Output: -1
console.log(animals.lastIndexOf("dog", 2)); // Output: 1
```

### 4. `find`
Returns the first element that meets the specified condition in a testing function.

#### Syntax
```javascript
array.find(callback(element, index, array));
```

- **callback**: Function to execute on each element.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster"];
console.log(animals.find(animal => animal.length > 3)); // Output: "hamster"
console.log(animals.find(animal => animal.includes("z"))); // Output: undefined
```

### 5. `findIndex`
Works like `find`, but returns the index of the found element instead of the element itself.

#### Syntax
```javascript
array.findIndex(callback(element, index, array));
```

- **callback**: Function to execute on each element.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster"];
console.log(animals.findIndex(animal => animal.length > 3)); // Output: 2
console.log(animals.findIndex(animal => animal.includes("z"))); // Output: -1
```

---

## 3.2.16 Copying a Selected Part of the Array with `slice`
The `slice` method creates a shallow copy of a portion of an array into a new array. The original array is not modified.

#### Syntax
```javascript
array.slice(start, end);
```

- **start**: The index to start copying from (inclusive).
- **end**: (Optional) The index to end copying (exclusive).

#### Examples
```javascript
let animals = ["cat", "dog", "hamster", "canary"];
console.log(animals.slice(1, 3)); // Output: ["dog", "hamster"]
console.log(animals.slice(-2)); // Output: ["hamster", "canary"]
console.log(animals.slice(2, 5)); // Output: ["hamster", "canary"]
```

---

## 3.2.17 Modifying Part of the Array with `splice`
The `splice` method can be used to add, remove, or replace elements within an array.

#### Syntax
```javascript
array.splice(start, deleteCount, item1, item2, ...);
```

- **start**: The index at which to start modifying the array.
- **deleteCount**: The number of elements to remove.
- **item1, item2, ...**: Elements to add to the array.

#### Examples
```javascript
let animals = ["cat", "dog", "hamster"];
animals.splice(1, 1, "rabbit", "guinea pig"); 
console.log(animals); // Output: ["cat", "rabbit", "guinea pig", "hamster"]

let moreAnimals = ["cat", "dog", "hamster"];
let removed = moreAnimals.splice(1, 2);
console.log(moreAnimals); // Output: ["cat"]
console.log(removed); // Output: ["dog", "hamster"]
```

---

## 3.2.18 Destructuring Assignment in Arrays
JavaScript allows you to assign array elements to variables directly with destructuring syntax.

#### Syntax
```javascript
let [var1, var2, ...rest] = array;
```

#### Examples
```javascript
let animals = ["cat", "dog", "hamster"];
let [pet1, pet2] = animals;
console.log(pet1); // Output: "cat"
console.log(pet2); // Output: "dog"

// Skipping elements
let [first, , third] = animals;
console.log(third); // Output: "hamster"

// Default values
let [a, b, c = "fish"] = ["cat", "dog"];
console.log(c); // Output: "fish"
```

---

## 3.2.19 The Spread Operator in Arrays
The spread operator (`...`) expands an array into individual elements.

#### Syntax
```javascript
let newArray = [...array1, ...array2];
```

#### Examples
```javascript
let animals1 = ["cat", "dog"];
let animals2 = ["hamster", "canary"];
let allAnimals = [...animals1, ...animals2];
console.log(allAnimals); // Output: ["cat", "dog", "hamster", "canary"]

// Passing as function arguments
let numbers = [10, 20, 30];
let addNumbers = (a, b, c) => a + b + c;
console.log(addNumbers(...numbers)); // Output: 60
```

---

### Summary
Each method provides a unique functionality that enables powerful data manipulation in JavaScript arrays, whether you're searching, modifying, or combining arrays.
