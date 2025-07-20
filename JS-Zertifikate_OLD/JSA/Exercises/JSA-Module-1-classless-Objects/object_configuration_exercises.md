
# JavaScript Exercises: Property and Object Configuration

## Aufgaben

### Aufgabe 1
Erstelle ein Objekt `laptop` mit der Eigenschaft `brand`. Verwende `Object.defineProperty`, um eine neue Eigenschaft `model` hinzuzufügen, 
die nicht konfigurierbar und nicht überschreibbar ist. Versuche, den Wert von `model` zu ändern und ihn anschließend zu löschen.

### Aufgabe 2
Erstelle ein Objekt `movie` und verwende `Object.defineProperty`, um die Eigenschaft `title` hinzuzufügen, 
die nicht aufzählbar, aber schreibbar und konfigurierbar ist. Verwende `Object.keys` und `Object.getOwnPropertyNames`, 
um die vorhandenen Eigenschaften zu untersuchen.

### Aufgabe 3
Erstelle ein Objekt `planet` mit der Eigenschaft `name`. Verwende `Object.preventExtensions` und überprüfe mit `Object.isExtensible`, 
ob dem Objekt neue Eigenschaften hinzugefügt werden können.

### Aufgabe 4
Erstelle ein Objekt `album` mit der Eigenschaft `title`. Verwende `Object.seal`, um das Objekt zu versiegeln. 
Versuche, die Eigenschaft `title` zu löschen und eine neue Eigenschaft `artist` hinzuzufügen. Gib das Objekt aus.

### Aufgabe 5
Erstelle ein Objekt `game` mit den Eigenschaften `name` und `genre`. Verwende `Object.freeze`, um das Objekt einzufrieren. 
Versuche, den Wert von `name` zu ändern und eine neue Eigenschaft `platform` hinzuzufügen. Gib den Status des Objekts aus, 
um zu überprüfen, ob es gefroren ist.

---

## Lösungen

### Lösung zu Aufgabe 1
```javascript
let laptop = { brand: "TechBrand" };
Object.defineProperty(laptop, "model", {
    value: "X200",
    writable: false,
    configurable: false
});

laptop.model = "X300"; // Keine Änderung, da writable: false
delete laptop.model; // Kein Effekt, da configurable: false
console.log(laptop.model); // Output: "X200"
```

### Lösung zu Aufgabe 2
```javascript
let movie = {};
Object.defineProperty(movie, "title", {
    value: "Inception",
    enumerable: false,
    writable: true,
    configurable: true
});

console.log(Object.keys(movie)); // Output: []
console.log(Object.getOwnPropertyNames(movie)); // Output: ["title"]
```

### Lösung zu Aufgabe 3
```javascript
let planet = { name: "Earth" };
Object.preventExtensions(planet);
console.log(Object.isExtensible(planet)); // Output: false
planet.size = "Large"; // Keine Änderung, da Objekt nicht erweiterbar ist
console.log(planet); // Output: { name: "Earth" }
```

### Lösung zu Aufgabe 4
```javascript
let album = { title: "Greatest Hits" };
Object.seal(album);
delete album.title; // Kein Effekt, da das Objekt versiegelt ist
album.artist = "Various"; // Keine Änderung, da keine neuen Eigenschaften hinzugefügt werden können
console.log(album); // Output: { title: "Greatest Hits" }
```

### Lösung zu Aufgabe 5
```javascript
let game = { name: "Adventure Quest", genre: "RPG" };
Object.freeze(game);

game.name = "Mystery Quest"; // Keine Änderung, da das Objekt gefroren ist
game.platform = "PC"; // Keine Änderung, da keine neuen Eigenschaften hinzugefügt werden können
console.log(game); // Output: { name: "Adventure Quest", genre: "RPG" }

console.log(Object.isFrozen(game)); // Output: true
```

