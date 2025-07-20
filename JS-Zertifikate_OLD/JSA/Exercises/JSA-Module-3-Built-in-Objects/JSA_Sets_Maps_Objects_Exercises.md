
# JavaScript Sets, Maps, and Objects – Übungsaufgaben

Hier sind 15 Aufgaben zu den Themen **Sets**, **Maps** und **Objects**. Diese Aufgaben sind so gestaltet, dass die Lernenden die Methoden und Eigenschaften anwenden müssen, ohne dass die Lösungsmethoden direkt aus der Aufgabenstellung hervorgehen.

## Aufgaben

### Aufgabe 1
Erstelle ein Set mit den Werten `["apple", "banana", "cherry", "apple", "date"]`. 
- Füge zwei weitere Früchte hinzu.
- Entferne dann eine beliebige Frucht.
- Überprüfe, ob das Set die Frucht `"banana"` enthält.
- Gib die Größe des Sets aus.

### Aufgabe 2
Erstelle eine Map namens `cityPopulation` mit den Werten `[["Berlin", 3_500_000], ["Paris", 2_200_000], ["London", 9_000_000]]`. 
- Füge zwei neue Städte hinzu.
- Ändere die Population von Paris.
- Überprüfe, ob "Madrid" in der Map enthalten ist.

### Aufgabe 3
Erstelle ein Objekt `book` mit den Eigenschaften `title: "1984"`, `author: "George Orwell"`, und `copies: 500`.
- Erhöhe den Wert von `copies` um 100.
- Entferne das `author`-Feld.
- Füge ein neues Feld `publisher` hinzu mit dem Wert `"Secker & Warburg"`.

### Aufgabe 4
Erstelle ein Set `numbers` mit den Werten `[1, 2, 3, 4, 5]`. 
- Füge drei weitere Zahlen hinzu.
- Verwandle das Set in ein Array und sortiere es absteigend.

### Aufgabe 5
Erstelle eine Map `productPrices` mit `[["apple", 1.5], ["banana", 2.0], ["cherry", 2.5]]`. 
- Erhöhe den Preis von "banana" um 0.5.
- Entferne "apple".
- Erstelle ein Array aus allen Werten.

### Aufgabe 6
Erstelle ein Objekt `user` mit den Eigenschaften `username: "jsmith"`, `email: "jsmith@example.com"`, `age: 30`.
- Ändere `age` zu 31.
- Füge eine neue Eigenschaft `isActive: true` hinzu.
- Erstelle ein Array mit allen Schlüssel-Wert-Paaren.

### Aufgabe 7
Erstelle ein Set mit den Werten `[10, 20, 30, 40, 50]`. 
- Überprüfe, ob das Set die Zahl 25 enthält.
- Füge die Zahl 25 hinzu und überprüfe erneut.

### Aufgabe 8
Erstelle eine Map `movieRatings` mit `[["Inception", 4.5], ["Interstellar", 4.7], ["Memento", 4.3]]`. 
- Füge einen weiteren Film hinzu.
- Gib alle Filme mit einer Bewertung über 4.4 aus.

### Aufgabe 9
Erstelle ein Objekt `car` mit den Eigenschaften `brand: "Tesla"`, `model: "Model S"`, `year: 2020`. 
- Aktualisiere das `year` auf 2021.
- Füge eine neue Eigenschaft `isElectric: true` hinzu.
- Erstelle ein Array mit allen Werten.

### Aufgabe 10
Erstelle ein Set `colors` mit den Werten `["red", "green", "blue"]`. 
- Füge `"yellow"` und `"blue"` hinzu.
- Überprüfe die Länge des Sets und gib die Farben als Array zurück.

### Aufgabe 11
Erstelle eine Map `inventory` mit `[["apple", 10], ["banana", 5], ["cherry", 12]]`. 
- Erhöhe den Bestand von "cherry" um 3.
- Entferne alle Einträge, die weniger als 10 haben.

### Aufgabe 12
Erstelle ein Objekt `employee` mit den Eigenschaften `name: "John Doe"`, `position: "Developer"`, `salary: 50000`.
- Erhöhe `salary` um 5000.
- Füge `department: "IT"` hinzu.
- Gib alle Schlüssel des Objekts aus.

### Aufgabe 13
Erstelle ein Set `letters` mit den Werten `["a", "b", "c", "d"]`. 
- Entferne den Buchstaben "c".
- Füge "e" und "f" hinzu.
- Gib das Set als Array sortiert aus.

### Aufgabe 14
Erstelle eine Map `countries` mit `[["Germany", "Berlin"], ["France", "Paris"], ["Spain", "Madrid"]]`.
- Ändere die Hauptstadt von "Spain" zu "Barcelona".
- Füge ein weiteres Land hinzu.
- Überprüfe, ob "Italy" in der Map enthalten ist.

### Aufgabe 15
Erstelle ein Objekt `person` mit den Eigenschaften `firstName: "Alice"`, `lastName: "Smith"`, `age: 28`.
- Erhöhe das Alter um 1.
- Erstelle eine neue Eigenschaft `fullName` aus den Werten von `firstName` und `lastName`.
- Gib das Objekt als Array mit allen Eigenschaften aus.

## Lösungen und Erklärungen

### Lösung 1
```javascript
let fruitSet = new Set(["apple", "banana", "cherry", "apple", "date"]);
fruitSet.add("kiwi");
fruitSet.add("mango");
fruitSet.delete("cherry");
console.log(fruitSet.has("banana")); // true
console.log(fruitSet.size); // 4
```

### Lösung 2
```javascript
let cityPopulation = new Map([["Berlin", 3500000], ["Paris", 2200000], ["London", 9000000]]);
cityPopulation.set("Rome", 2800000);
cityPopulation.set("Madrid", 3200000);
cityPopulation.set("Paris", 2300000);
console.log(cityPopulation.has("Madrid")); // true
```

### Lösung 3
```javascript
let book = { title: "1984", author: "George Orwell", copies: 500 };
book.copies += 100;
delete book.author;
book.publisher = "Secker & Warburg";
console.log(book); // { title: '1984', copies: 600, publisher: 'Secker & Warburg' }
```

### Lösung 4
```javascript
let numbers = new Set([1, 2, 3, 4, 5]);
numbers.add(6);
numbers.add(7);
numbers.add(8);
let sortedArray = [...numbers].sort((a, b) => b - a);
console.log(sortedArray); // [8, 7, 6, 5, 4, 3, 2, 1]
```

### Lösung 5
```javascript
let productPrices = new Map([["apple", 1.5], ["banana", 2.0], ["cherry", 2.5]]);
productPrices.set("banana", 2.5);
productPrices.delete("apple");
let pricesArray = [...productPrices.values()];
console.log(pricesArray); // [2.5, 2.5]
```

### Lösung 6
```javascript
let user = { username: "jsmith", email: "jsmith@example.com", age: 30 };
user.age = 31;
user.isActive = true;
let userEntries = Object.entries(user);
console.log(userEntries); // [["username", "jsmith"], ["email", "jsmith@example.com"], ["age", 31], ["isActive", true]]
```

### Lösung 7
```javascript
let numberSet = new Set([10, 20, 30, 40, 50]);
console.log(numberSet.has(25)); // false
numberSet.add(25);
console.log(numberSet.has(25)); // true
```
