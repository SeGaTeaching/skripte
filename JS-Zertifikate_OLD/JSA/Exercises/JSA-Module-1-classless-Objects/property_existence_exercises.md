
# JavaScript Exercises: Property Existence Test and Enumeration

## Aufgaben

### Aufgabe 1
Erstelle ein Objekt `book` mit den Eigenschaften `title`, `author`, und `year`. 
Überprüfe, ob die Eigenschaft `publisher` existiert und füge sie hinzu, falls nicht.

### Aufgabe 2
Gegeben ist das folgende Objekt `user`:
```javascript
let user = { 
    name: "Alice", 
    email: "alice@example.com"
};
```
Schreibe eine Bedingung, die sicherstellt, dass du auf die Eigenschaft `email.domain` zugreifst, ohne einen Fehler zu verursachen.

### Aufgabe 3
Verwende den Operator `in`, um zu prüfen, ob die Eigenschaft `address` in einem Objekt `company` vorhanden ist. 
Falls ja, gib die Adresse in der Konsole aus.

### Aufgabe 4
Erstelle ein Objekt `car` mit den Eigenschaften `brand`, `model` und `year`. 
Verwende eine `for...in` Schleife, um alle Eigenschaftsnamen und -werte des Objekts auszugeben.

### Aufgabe 5
Verwende `Object.keys`, um alle `Properties` eines Objekts `person` in ein Array zu speichern und gib das Array in der Konsole aus.

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
let book = {
    title: "JavaScript Guide",
    author: "John Doe",
    year: 2021
};

if (!book.publisher) {
    book.publisher = "Unknown Publisher";
}
console.log(book.publisher); // Output: "Unknown Publisher"
```

### Lösung zu Aufgabe 2
```javascript
let user = { 
    name: "Alice", 
    email: "alice@example.com"
};

if (user && user.email) {
    console.log(user.email.domain); // Output: undefined
}
```

### Lösung zu Aufgabe 3
```javascript
let company = {
    name: "Tech Corp",
    address: "123 Tech Street"
};

if ("address" in company) {
    console.log(company.address); // Output: "123 Tech Street"
}
```

### Lösung zu Aufgabe 4
```javascript
let car = {
    brand: "Tesla",
    model: "Model 3",
    year: 2020
};

for (let key in car) {
    console.log(\`\${key}: \${car[key]}\`);
    // Output:
    // brand: Tesla
    // model: Model 3
    // year: 2020
}
```

### Lösung zu Aufgabe 5
```javascript
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
};

let keys = Object.keys(person);
console.log(keys); // Output: ["firstName", "lastName", "age"]
```
