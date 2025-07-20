
# Statische Mitglieder in JavaScript-Klassen

## 2.5.1 Statische Mitglieder
Neben den regulären Methoden und Eigenschaften, die in JavaScript-Klassen definiert werden, können wir auch statische Methoden und Eigenschaften erstellen. Diese sind nicht Teil des erstellten Objekts, sondern nur mit der Klasse selbst verbunden.

### Beispiel 1: Statische Methode in der AlmostEmptyClass
```javascript
class AlmostEmptyClass {
    constructor(sth) {
        console.log(sth);
    }

    sayHi() {
        console.log("Hi!");
    }

    static sayHello() {
        console.log("Hello!");
    }
}

let almostEmptyObject = new AlmostEmptyClass(120); // 120
almostEmptyObject.sayHi(); // -> Hi!
almostEmptyObject.sayHello(); // -> error
AlmostEmptyClass.sayHello(); // -> Hello!
```

In diesem Beispiel kann die statische Methode `sayHello` nicht über das erstellte Objekt `almostEmptyObject` aufgerufen werden. Stattdessen wird sie direkt über die Klasse `AlmostEmptyClass` aufgerufen.

### Zusätzliche Beispiele:

#### Beispiel 2: Statische Methode in der `MathUtils`-Klasse
```javascript
class MathUtils {
    static add(a, b) {
        return a + b;
    }

    static subtract(a, b) {
        return a - b;
    }
}

console.log(MathUtils.add(5, 3)); // -> 8
console.log(MathUtils.subtract(5, 3)); // -> 2
```

Hier sehen wir eine Utility-Klasse `MathUtils`, die statische Methoden für mathematische Operationen enthält. Diese Methoden sind nicht an Instanzen der Klasse gebunden.

#### Beispiel 3: Statische Methode zur Validierung in einer `User`-Klasse
```javascript
class User {
    constructor(username, email) {
        this.username = username;
        this.email = email;
    }

    static isValidEmail(email) {
        return email.includes("@");
    }
}

console.log(User.isValidEmail("test@example.com")); // -> true
console.log(User.isValidEmail("testexample.com")); // -> false
```

Die Methode `isValidEmail` prüft, ob eine gegebene E-Mail-Adresse gültig ist. Da dies eine logische Funktion ist, die nicht von einer Instanz abhängig ist, wird sie als statische Methode implementiert.

## Statische Methoden als Hilfsmethoden
Statische Methoden eignen sich besonders gut für Hilfsmethoden, die sich auf die Klasse selbst und nicht auf eine Instanz beziehen. Ein gutes Beispiel ist das Vergleichen von Objekten einer Klasse.

### Beispiel 4: Statische Methode zum Vergleich von Fahrzeugen
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.status = "unavailable";
    }

    static isSameId(v1, v2) {
        return v1.id === v2.id;
    }
}

let vehicle1 = new Vehicle({ id: "AL1024", latitude: 59.367628, longitude: 18.213423 });
let vehicle2 = new Vehicle({ id: "AL1024", latitude: 0, longitude: 0 });
let vehicle3 = new Vehicle({ id: "AL1026", latitude: 59.367628, longitude: 18.213423 });

console.log(Vehicle.isSameId(vehicle1, vehicle2)); // -> true
console.log(Vehicle.isSameId(vehicle1, vehicle3)); // -> false
```

Die statische Methode `isSameId` vergleicht zwei Instanzen der `Vehicle`-Klasse basierend auf ihrer `id`. Da diese Methode auf Klassenebene definiert ist, kann sie ohne ein Objekt der Klasse aufgerufen werden.

### Statische Methoden nach der Klassendefinition
Statische Methoden können auch nach der Deklaration der Klasse hinzugefügt werden.

```javascript
Vehicle.isSameId = function(v1, v2) {
    return v1.id === v2.id;
};
```

Dieser Code zeigt, dass wir eine statische Methode auch außerhalb des Klassenkörpers definieren können.

## Fazit
Statische Methoden und Eigenschaften sind nicht an Instanzen von Klassen gebunden, sondern an die Klasse selbst. Sie eignen sich hervorragend für Hilfsmethoden und andere Logik, die nicht von individuellen Objekten abhängt. Die Nutzung von `static` erleichtert es, solche Methoden in JavaScript zu definieren.
