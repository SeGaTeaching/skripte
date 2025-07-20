
# JavaScript Objects – Einführung und Anwendungsbeispiele

## Was ist ein Objekt?

Ein **Objekt** in JavaScript ist eine Sammlung von **Schlüssel-Wert-Paaren**, die verwendet werden kann, um Daten strukturiert zu speichern. Obwohl wir Objekte bereits oft verwendet haben, betrachten wir sie hier als **zusammengesetzte Datenstruktur**, die in verschiedenen Situationen sehr nützlich ist.

### Vergleich mit anderen Strukturen:
- **Array**: Eine Sammlung, bei der Werte durch ihre Position (Index) identifiziert werden. Die Reihenfolge der Elemente ist wichtig.
- **Set**: Eine Sammlung ohne Index, die nur einzigartige Werte speichert.
- **Map**: Eine Sammlung, die Schlüssel-Wert-Paare speichert, ähnlich wie ein Set, aber ohne strikte Reihenfolge der Elemente.

## Erstellen eines Objekts

Ein Objekt kann mithilfe von **Literalen** oder dem `Object`-Konstruktor erstellt werden. Das einfachste und häufigste Verfahren ist die Literalnotation.

```javascript
let anotherPetsObj = { "snakes": 1, "cats": 3, "dogs": 2 };
```

#### Weitere Beispiele:
```javascript
let fruitCount = { "apples": 10, "bananas": 5, "oranges": 7 };
let cityPopulation = { "Berlin": 3000000, "Paris": 2200000, "Tokyo": 14000000 };
let carStock = { "sedan": 20, "SUV": 10, "truck": 5 };
```

## Hinzufügen, Ändern und Löschen von Eigenschaften

Zum Hinzufügen oder Ändern von Eigenschaften verwendet man die **Punktnotation** oder die **Klammernotation**.

```javascript
console.log(anotherPetsObj.snakes); // -> 1
anotherPetsObj.snakes = 2;
console.log(anotherPetsObj.snakes); // -> 2
delete anotherPetsObj.snakes;
console.log(anotherPetsObj.snakes); // -> undefined
anotherPetsObj.snakes = 0;
console.log(anotherPetsObj.snakes); // 0
```

#### Weitere Beispiele:
```javascript
fruitCount.apples = 12;
console.log(fruitCount.apples); // -> 12
delete fruitCount.bananas;

cityPopulation["Paris"] = 2300000;
console.log(cityPopulation["Paris"]); // -> 2300000
delete cityPopulation["Tokyo"];
```

## Durchlaufen von Objekten

Mit den statischen Methoden `Object.keys`, `Object.values` und `Object.entries` kann man die **Schlüssel**, **Werte** und **Schlüssel-Wert-Paare** eines Objekts erhalten und durchlaufen.

```javascript
Object.keys(anotherPetsObj).forEach(key => console.log(key)); // -> snakes -> cats -> dogs
Object.values(anotherPetsObj).forEach(value => console.log(value)); // -> 1 -> 3 -> 2
Object.entries(anotherPetsObj).forEach(entry => console.log(entry)); // -> ["snakes", 1] -> ["cats", 3] -> ["dogs", 2]
```

#### Weitere Beispiele:
```javascript
Object.keys(cityPopulation).forEach(city => console.log(city));
Object.values(fruitCount).forEach(count => console.log(count));
Object.entries(carStock).forEach(entry => console.log(entry));
```

### for...in Schleife

Die **for...in Schleife** ermöglicht das Durchlaufen von Objekten ähnlich wie bei `forEach`, aber sie ist speziell für Objekte optimiert.

```javascript
for (let key in anotherPetsObj) {
    console.log(key); // -> snakes -> cats -> dogs
    console.log(anotherPetsObj[key]); // -> 1 -> 3 -> 2
}
```

#### Weitere Beispiele:
```javascript
for (let fruit in fruitCount) {
    console.log(fruit);
    console.log(fruitCount[fruit]);
}

for (let city in cityPopulation) {
    console.log(city);
    console.log(cityPopulation[city]);
}
```

## Der Spread-Operator für Objekte

Der **Spread-Operator** (`...`) kann verwendet werden, um die Eigenschaften eines Objekts in ein anderes Objekt zu kopieren.

```javascript
let petsObj = { "cats": 1, "dogs": 3, "hamsters": 2 };
let newPetsObj = { ...petsObj, "sharks": 1 }; // -> {cats: 1, dogs: 3, hamsters: 2, sharks: 1}
```

#### Weitere Beispiele:
```javascript
let additionalFruit = { "pears": 4, "grapes": 12 };
let fruitStock = { ...fruitCount, ...additionalFruit };

let extendedPopulation = { "London": 9000000, ...cityPopulation };

let vehicleTypes = { "motorcycle": 8, ...carStock };
```

## JSON – Datenübertragung mit Objekten

Die Datenstruktur von Objekten ist so praktisch, dass sie oft für die **Datenübertragung** im JSON-Format verwendet wird, einem textbasierten Format, das speziell für den Datenaustausch entwickelt wurde. Mehr zu JSON folgt im nächsten Abschnitt.

## Fazit

JavaScript-Objekte sind vielseitig und nützlich, wenn es um die Speicherung strukturierter Daten in **Schlüssel-Wert-Paaren** geht. Sie bieten effiziente Möglichkeiten zur Verwaltung, Bearbeitung und Iteration von Daten.
