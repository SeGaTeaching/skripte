
# Klassen-Deklaration in JavaScript

## 2.1.1 Klassen-Deklaration
Um eine Klasse zu definieren, betrachten wir ein Szenario mit einem Transportunternehmen, das verschiedene Fahrzeuge verwendet. Jedes Fahrzeug hat eine eindeutige ID, einen Status ("frei", "beschäftigt", "nicht verfügbar"), geografische Positionen (Längengrad und Breitengrad) und eine Zeit der letzten Positionsaktualisierung.

### Beispiel 1: Konstruktor-Funktion
```javascript
let Vehicle = function(id, latitude, longitude) {
    this.setPosition = function(latitude, longitude) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    };
    this.id = id;
    this.status = "unavailable";
    this.time = Date.now();
    this.latitude = latitude;
    this.longitude = longitude;
};
let vehicle1 = new Vehicle("AL1024", 59.358615, 17.947589);
vehicle1.setPosition(59.367647, 18.213451);
console.log(vehicle1);
```

Im obigen Beispiel haben wir die Funktion `Vehicle` definiert, die als Konstruktor dient. Die Funktion initialisiert die Eigenschaften `id`, `status`, `time`, `latitude` und `longitude` sowie die Methode `setPosition`.

### Verbesserte Version
Um Redundanzen zu vermeiden, können wir die Methode `setPosition` bereits beim Initialisieren des Objekts aufrufen.

```javascript
let Vehicle = function(id, latitude, longitude) {
    this.setPosition = function(latitude, longitude) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    };
    this.id = id;
    this.status = "unavailable";
    this.setPosition(latitude, longitude);
};
```

### Verwenden von Objekten für Parameterübergabe
Statt einzelne Argumente zu übergeben, können wir ein Objekt mit den erforderlichen Feldern erstellen. Dies reduziert die Fehleranfälligkeit, insbesondere bei ähnlichen Parametern wie Längen- und Breitengrad.

```javascript
let Vehicle = function(initialData) {
    let { id, latitude, longitude } = initialData;
    this.setPosition = function(latitude, longitude) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    };
    this.id = id;
    this.status = "unavailable";
    this.setPosition(latitude, longitude);
};
let vehicle1 = new Vehicle({ id: "AL1024", latitude: 59.367647, longitude: 18.213451 });
let vehicle2 = new Vehicle({ longitude: 18.213423, latitude: 59.367628, id: "AL1024" });
```

### Destrukturierung von Parametern im Konstruktor
Eine Verbesserung des obigen Codes besteht darin, Destrukturierung direkt im Funktionsparameter zu verwenden.

```javascript
let Vehicle = function({ id, latitude, longitude }) {
    this.setPosition = function({ latitude, longitude }) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    };
    this.getPosition = function() {
        return {
            latitude: this.latitude,
            longitude: this.longitude
        };
    };
    this.id = id;
    this.status = "unavailable";
    this.setPosition({ latitude, longitude });
};
let vehicle1 = new Vehicle({ id: "AL1024", latitude: 59.367647, longitude: 18.213451 });
let vehicle2 = new Vehicle({ longitude: 18.213423, latitude: 59.367628, id: "AL1024" });
```

## 2.1.2 Klassen-Deklaration
Mit JavaScript können wir Klassen mit dem Schlüsselwort `class` definieren. Der folgende Code zeigt, wie wir die `Vehicle`-Funktion in eine Klasse umwandeln können:

### Beispiel 1: Klasse `Vehicle`
```javascript
class Vehicle {
    constructor({ id, latitude, longitude }) {
        this.id = id;
        this.status = "unavailable";
        this.setPosition({ latitude, longitude });
    }

    setPosition({ latitude, longitude }) {
        this.time = Date.now();
        this.longitude = longitude;
        this.latitude = latitude;
    }

    getPosition() {
        return {
            latitude: this.latitude,
            longitude: this.longitude
        };
    }
}

let vehicle1 = new Vehicle({ id: "AL1024", latitude: 59.367647, longitude: 18.213451 });
let vehicle2 = new Vehicle({ longitude: 18.213423, latitude: 59.367628, id: "AL1024" });
```

Im obigen Beispiel haben wir die Methoden `setPosition` und `getPosition` aus dem Konstruktor entfernt und direkt im Klassenkörper definiert.

### Beispiel 2: Instanz einer Klasse
```javascript
class AlmostEmptyClass {
    constructor(sth) {
        console.log(sth);
    }
    sayHi() {
        console.log("Hi!");
    }
}
let almostEmptyObject = new AlmostEmptyClass(120);
almostEmptyObject.sayHi();
```

## 2.1.3 Der Operator `instanceof`
Mit dem Operator `instanceof` können wir überprüfen, ob ein Objekt eine Instanz einer bestimmten Klasse ist.

### Beispiel 1:
```javascript
console.log(vehicle1 instanceof Vehicle); // -> true
console.log(vehicle1 instanceof Object);  // -> true
```

Jedes Objekt, das von einer Klasse abgeleitet ist, ist auch eine Instanz der Klasse `Object`, da alle Klassen in JavaScript implizit von `Object` erben.

### Beispiel 2: Funktionsausdruck einer Klasse
```javascript
let AlmostEmptyClass = class {
    constructor(sth) {
        console.log(sth);
    }
    sayHi() {
        console.log("Hi!");
    }
};
let almostEmptyObject = new AlmostEmptyClass(120);
almostEmptyObject.sayHi();
```

## Fazit
In JavaScript können wir Klassen mit dem Schlüsselwort `class` definieren. Funktionen und Klassen sind in JavaScript erstklassige Objekte, was bedeutet, dass sie als Argumente übergeben, zurückgegeben und in Variablen gespeichert werden können. Der `instanceof` Operator hilft uns zu überprüfen, ob ein Objekt zu einer bestimmten Klasse gehört.
