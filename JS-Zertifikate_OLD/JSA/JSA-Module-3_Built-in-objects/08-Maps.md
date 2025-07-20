
# JavaScript Maps – Einführung und Anwendungsbeispiele

## Was ist eine Map?

In JavaScript ist eine **Map** eine Sammlung von **Schlüssel-Wert-Paaren**. Sie ist flexibel in der Art der gespeicherten Daten, da sowohl die Schlüssel als auch die Werte jeglichen Datentyp annehmen können. 

Maps sind besonders nützlich, wenn eine Sammlung benötigt wird, in der man durch Schlüssel-Wert-Zuordnungen auf Werte zugreifen möchte.

### Wichtige Eigenschaften einer Map:
- **Schlüssel-Wert-Paare**: Jedes Element in einer Map hat einen eindeutigen Schlüssel und einen zugeordneten Wert.
- **Flexible Schlüssel**: Im Gegensatz zu Objekten können in einer Map Schlüssel auch Datentypen wie Funktionen oder Objekte sein.
- **Einzigartige Schlüssel**: Ein Schlüssel kann nur einmal vorkommen. Falls ein neuer Wert für einen bereits existierenden Schlüssel hinzugefügt wird, überschreibt dieser den alten Wert.

## Erstellen einer Map

### Leere Map

Eine Map kann ohne Argumente erstellt und später mit Schlüsseln und Werten gefüllt werden.

```javascript
let emptyMap = new Map();
console.log(emptyMap.size); // -> 0
```

#### Weitere Beispiele:
```javascript
let usersMap = new Map();
let productsMap = new Map();
let countriesMap = new Map();
```

### Map mit Elementen erstellen

Man kann ein Array von Arrays als Argument übergeben, wobei jedes Array ein Schlüssel-Wert-Paar darstellt.

```javascript
let petsMap = new Map([["cats", 1], ["dogs", 2], ["hamsters", 5]]);
console.log(petsMap.size); // -> 3
```

#### Weitere Beispiele:
```javascript
let fruitCountMap = new Map([["apple", 5], ["banana", 10]]);
let studentScoresMap = new Map([["Alice", 90], ["Bob", 85]]);
let cityPopulationMap = new Map([["Berlin", 3000000], ["Paris", 2200000]]);
```

## Überprüfen auf Vorhandensein eines Schlüssels

Mit der **has**-Methode kann man prüfen, ob ein bestimmter Schlüssel in der Map existiert.

```javascript
console.log(petsMap.has("dogs")); // -> true
console.log(petsMap.has("sharks")); // -> false
```

#### Weitere Beispiele:
```javascript
console.log(fruitCountMap.has("apple")); // -> true
console.log(studentScoresMap.has("Eve")); // -> false
console.log(cityPopulationMap.has("Paris")); // -> true
```

## Arbeiten mit Elementen

Mit den Methoden `set`, `get`, `delete` und `clear` kann man die Elemente einer Map verwalten.

```javascript
petsMap.set("hamsters", 6);
console.log(petsMap.get("hamsters")); // -> 6
petsMap.delete("hamsters");
console.log(petsMap.get("hamsters")); // -> undefined
petsMap.clear();
console.log(petsMap.size); // -> 0
```

#### Weitere Beispiele:
```javascript
fruitCountMap.set("orange", 3);
console.log(fruitCountMap.get("orange")); // -> 3
fruitCountMap.delete("banana");
console.log(fruitCountMap.has("banana")); // -> false
fruitCountMap.clear();
console.log(fruitCountMap.size); // -> 0
```

## Iterieren durch Map-Elemente

Die **forEach**-Methode ermöglicht das Durchlaufen aller Map-Elemente. Sie gibt den Wert und den zugehörigen Schlüssel zurück.

```javascript
petsMap.forEach((value, key) => console.log(`${key} : ${value}`)); // -> cats : 1 -> dogs : 2
```

#### Weitere Beispiele:
```javascript
fruitCountMap.forEach((count, fruit) => console.log(`${fruit} : ${count}`));
studentScoresMap.forEach((score, student) => console.log(`${student} : ${score}`));
cityPopulationMap.forEach((population, city) => console.log(`${city} : ${population}`));
```

## Iteratoren: `values`, `keys` und `entries`

### Werte abrufen

Mit `values` erhalten wir alle Werte der Map.

```javascript
let petValuesIterator = petsMap.values();
console.log(petValuesIterator.next().value); // -> 1
console.log(petValuesIterator.next().value); // -> 2
```

#### Weitere Beispiele:
```javascript
let fruitValuesIterator = fruitCountMap.values();
console.log(fruitValuesIterator.next().value);

let studentScoresIterator = studentScoresMap.values();
console.log(studentScoresIterator.next().value);

let cityPopulationIterator = cityPopulationMap.values();
console.log(cityPopulationIterator.next().value);
```

### Schlüssel abrufen

Mit `keys` erhalten wir alle Schlüssel der Map.

```javascript
let petKeysIterator = petsMap.keys();
console.log(petKeysIterator.next().value); // -> cats
```

#### Weitere Beispiele:
```javascript
let fruitKeysIterator = fruitCountMap.keys();
console.log(fruitKeysIterator.next().value);

let studentNamesIterator = studentScoresMap.keys();
console.log(studentNamesIterator.next().value);

let cityNamesIterator = cityPopulationMap.keys();
console.log(cityNamesIterator.next().value);
```

### `entries` Methode für Schlüssel-Wert-Paare

Die `entries`-Methode gibt ein Iterator-Objekt zurück, das alle Schlüssel-Wert-Paare liefert.

```javascript
let petEntriesIterator = petsMap.entries();
console.log(petEntriesIterator.next().value); // -> ["cats", 1]
```

#### Weitere Beispiele:
```javascript
let fruitEntriesIterator = fruitCountMap.entries();
console.log(fruitEntriesIterator.next().value);

let studentEntriesIterator = studentScoresMap.entries();
console.log(studentEntriesIterator.next().value);

let cityEntriesIterator = cityPopulationMap.entries();
console.log(cityEntriesIterator.next().value);
```

## Die for...of Schleife

Die **for...of Schleife** ermöglicht das Durchlaufen von Maps und anderen Sammlungen.

```javascript
for (let [key, value] of petsMap) {
    console.log(`${key}: ${value}`);
}
```

#### Weitere Beispiele:
```javascript
for (let [fruit, count] of fruitCountMap) {
    console.log(`${fruit}: ${count}`);
}

for (let [student, score] of studentScoresMap) {
    console.log(`${student}: ${score}`);
}

for (let [city, population] of cityPopulationMap) {
    console.log(`${city}: ${population}`);
}
```

## Der Spread-Operator in Maps

Mit dem **Spread-Operator** (`...`) kann man die Elemente einer Map in ein Array umwandeln.

```javascript
let petsArray = [...petsMap];
console.log(petsArray instanceof Array); // -> true
```

#### Weitere Beispiele:
```javascript
let fruitArray = [...fruitCountMap];
let studentArray = [...studentScoresMap];
let cityArray = [...cityPopulationMap];
```

## Fazit

Maps sind besonders nützlich, wenn eine Sammlung **Schlüssel-Wert-Paare** mit flexiblen Schlüsseln und Werten benötigt wird. Sie bieten eine strukturierte Möglichkeit, Daten zu speichern und zu manipulieren, wobei jeder Schlüssel einzigartig ist.

## Mehrere Elemente hinzufügen

### forEach oder for-loop

```javascript
let mySet = new Set();
let elementsToAdd = ["apple", "banana", "cherry"];

elementsToAdd.forEach(element => mySet.add(element));
console.log(mySet); // -> {"apple", "banana", "cherry"}
```

```javascript
let myMap = new Map();
let pairsToAdd = [["apple", 1], ["banana", 2], ["cherry", 3]];

pairsToAdd.forEach(([key, value]) => myMap.set(key, value));
console.log(myMap); // -> Map { "apple" => 1, "banana" => 2, "cherry" => 3 }
```

### Spread Operator

```javascript
let initialSet = new Set(["apple"]);
let additionalElements = ["banana", "cherry"];
let mySet = new Set([...initialSet, ...additionalElements]);
console.log(mySet); // -> {"apple", "banana", "cherry"}
```

```javascript
let initialMap = new Map([["apple", 1]]);
let additionalPairs = [["banana", 2], ["cherry", 3]];
let myMap = new Map([...initialMap, ...additionalPairs]);
console.log(myMap); // -> Map { "apple" => 1, "banana" => 2, "cherry" => 3 }
```