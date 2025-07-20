
# JavaScript Sets – Einführung und Anwendungsbeispiele

## Was ist ein Set?

In JavaScript ist ein **Set** eine Sammlung, die nur **einzigartige Werte** speichert. Es verhindert automatisch doppelte Werte. Sets sind nützlich, wenn man eine Menge von Daten verwalten muss, in der jedes Element nur einmal vorkommen soll, ohne sich um die Reihenfolge der Elemente zu kümmern.

Ein Set kann mit dem Konstruktor `Set()` erstellt werden und bietet verschiedene Methoden zum Hinzufügen, Überprüfen, Löschen und Iterieren von Elementen. Im Gegensatz zu Arrays haben die Elemente in einem Set keine bestimmte Reihenfolge und Position. 

### Wichtige Eigenschaften eines Sets:
- **Keine Duplikate**: Ein Set speichert nur einzigartige Werte.
- **Keine Ordnung**: Elemente haben keine festgelegte Reihenfolge oder Position.
- **Schlüssel-Wert-Paare**: Jedes Element in einem Set wird als Schlüssel-Wert-Paar betrachtet, wobei beide identisch sind.

## Erstellen eines Sets

### Leer starten
Ein Set kann ohne Argumente erstellt und später mit Elementen gefüllt werden.

```javascript
let emptySet = new Set(); // -> {}
console.log(emptySet.size); // -> 0
```

#### Weitere Beispiele:
```javascript
let uniqueNumbers = new Set();
let uniqueStrings = new Set();
let uniqueItems = new Set();
```

### Set mit Elementen erstellen

Man kann ein Array als Argument übergeben, und die Werte werden in das Set übernommen (Duplikate werden ignoriert).

```javascript
let petsSet = new Set(["cat", "dog", "cat"]); // -> {"cat", "dog"}
console.log(petsSet.size); // -> 2
```

#### Weitere Beispiele:
```javascript
let fruitSet = new Set(["apple", "banana", "apple"]); // -> {"apple", "banana"}
let colorSet = new Set(["red", "blue", "red", "green"]); // -> {"red", "blue", "green"}
let citySet = new Set(["Berlin", "Paris", "Berlin"]); // -> {"Berlin", "Paris"}
```

## Überprüfen auf Vorhandensein von Elementen

Mit der **has**-Methode kann man prüfen, ob ein bestimmtes Element im Set existiert.

```javascript
let petsSet = new Set(["cat", "dog"]); // -> {"cat", "dog"}
console.log(petsSet.has("cat")); // -> true
console.log(petsSet.has("shark")); // -> false
```

#### Weitere Beispiele:
```javascript
let numSet = new Set([1, 2, 3]);
console.log(numSet.has(2)); // -> true
console.log(numSet.has(5)); // -> false

let letterSet = new Set(["a", "b", "c"]);
console.log(letterSet.has("b")); // -> true
console.log(letterSet.has("z")); // -> false
```

## Hinzufügen, Löschen und Leeren von Elementen

Man kann mit den Methoden `add`, `delete` und `clear` auf die Elemente eines Sets zugreifen.

```javascript
petsSet.add("shark");
petsSet.add("hamster");
console.log(petsSet.size); // -> 4
petsSet.delete("dog"); // -> true
console.log(petsSet.size); // -> 3
petsSet.clear();
console.log(petsSet.size); // -> 0
```

#### Weitere Beispiele:
```javascript
let fruitSet = new Set(["apple", "banana"]);
fruitSet.add("orange");
fruitSet.delete("banana");
console.log(fruitSet.size); // -> 2

let bookSet = new Set(["Harry Potter", "LOTR"]);
bookSet.add("Narnia");
bookSet.clear();
console.log(bookSet.size); // -> 0
```

## Iterieren durch Set-Elemente

Das **forEach**-Verfahren ermöglicht das Durchlaufen aller Set-Elemente, wobei jedes Element als **Wert** und **Schlüssel** (identisch) übergeben wird.

```javascript
let petsSet = new Set(["cat", "dog", "hamster"]); 
petsSet.forEach(value => console.log(value)); // -> cat -> dog -> hamster
```

#### Weitere Beispiele:
```javascript
let countries = new Set(["Germany", "France", "Italy"]);
countries.forEach(country => console.log(country));

let numbers = new Set([10, 20, 30]);
numbers.forEach(num => console.log(num));

let foods = new Set(["pizza", "pasta", "sushi"]);
foods.forEach(food => console.log(food));
```

### Iteratoren und die `values`-Methode

Mit der `values`-Methode wird ein **Iterator** zurückgegeben, mit dem man das Set-Element für Element durchgehen kann.

```javascript
let petsSet = new Set(["cat", "dog", "hamster"]);
let petsIterator = petsSet.values();
console.log(petsIterator.next().value); // -> cat
console.log(petsIterator.next().value); // -> dog
console.log(petsIterator.next().value); // -> hamster
```

#### Weitere Beispiele:
```javascript
let lettersSet = new Set(["a", "b", "c"]);
let letterIterator = lettersSet.values();
console.log(letterIterator.next().value); // -> "a"
console.log(letterIterator.next().value); // -> "b"
console.log(letterIterator.next().value); // -> "c"
```

## Der Spread-Operator in Sets

Mit dem **Spread-Operator** (`...`) kann man die Elemente eines Sets in ein Array umwandeln.

```javascript
let petsSet = new Set(["cat", "dog", "hamster"]);
let petsArray = [...petsSet]; // -> ["cat", "dog", "hamster"]
console.log(petsArray instanceof Array); // -> true
```

#### Weitere Beispiele:
```javascript
let numSet = new Set([1, 2, 3]);
let numArray = [...numSet]; // -> [1, 2, 3]

let charSet = new Set(["x", "y", "z"]);
let charArray = [...charSet]; // -> ["x", "y", "z"]

let animalSet = new Set(["lion", "tiger", "bear"]);
let animalArray = [...animalSet]; // -> ["lion", "tiger", "bear"]
```

## Fazit

Sets sind besonders nützlich, wenn eine Sammlung **einzigartiger, ungeordneter Werte** benötigt wird. Sie bieten eine einfache und effiziente Möglichkeit, Daten zu speichern und zu manipulieren, ohne sich um die Reihenfolge zu kümmern oder doppelte Werte zu verwalten.
