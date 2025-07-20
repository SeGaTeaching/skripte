
# Klassen vs. Konstruktoren in JavaScript

## 2.6.1 Klassen vs. Konstruktoren
In JavaScript sind Klassen sehr ähnlich zu Konstruktorfunktionen, da sie größtenteils nur syntaktischen Zucker über die bestehende Prototypen-basierte Vererbung darstellen. Syntaktischer Zucker ist ein Konzept in der Programmierung, bei dem eine Funktion der Sprache für die Bequemlichkeit des Programmierers eingeführt wird, aber durch eine Transformation des Codes eliminiert werden könnte.

### Vergleich von Klassen und Konstruktoren
Hier sind zwei funktional identische Beispiele, eines mit Klassen und das andere mit Konstruktorfunktionen geschrieben:

### Beispiel 1: Klassen in JavaScript
```javascript
class TestClass {
    constructor(arg) {
        this.arg = arg;
        console.log(this.arg);
    }

    showSth() {
        console.log("I'm prototyped!");
    }

    static showSth() {
        console.log("Hi, I'm static!");
    }
}

let test = new TestClass("Hello");
test.showSth(); // -> I'm prototyped!
TestClass.showSth(); // -> Hi, I'm static!
console.log(test instanceof TestClass);
```

In diesem Beispiel haben wir sowohl eine Prototyp-Methode (`showSth`) als auch eine statische Methode (`showSth`). Die Prototyp-Methode ist an die Instanz der Klasse gebunden, während die statische Methode an die Klasse selbst gebunden ist.

### Beispiel 2: Konstruktorfunktion in JavaScript
```javascript
let Test = function(arg) {
    this.arg = arg;
    console.log(this.arg);
};

Test.prototype.showSth = function() {
    console.log("I'm prototyped!");
};

Test.showSth = function() {
    console.log("Hi, I'm static!");
};

let test = new Test("Hello");
test.showSth(); // -> I'm prototyped!
Test.showSth(); // -> Hi, I'm static!
console.log(test instanceof Test);
```

Dieses Beispiel zeigt, dass der gleiche Effekt mit Konstruktorfunktionen erreicht werden kann. Die `showSth`-Methode, die an die Instanz gebunden ist, wird über das Prototyp-Objekt hinzugefügt. Die statische Methode wird direkt auf dem Konstruktor definiert.

### Zusätzliche Beispiele:

#### Beispiel 3: Klassen-basierte Implementierung einer `Person`
```javascript
class Person {
    constructor(name) {
        this.name = name;
    }

    greet() {
        console.log(`Hello, my name is ${this.name}`);
    }

    static species() {
        return "Homo sapiens";
    }
}

let person = new Person("Alice");
person.greet(); // -> Hello, my name is Alice
console.log(Person.species()); // -> Homo sapiens
```

#### Beispiel 4: Konstruktor-basierte Implementierung einer `Person`
```javascript
let Person = function(name) {
    this.name = name;
};

Person.prototype.greet = function() {
    console.log(`Hello, my name is ${this.name}`);
};

Person.species = function() {
    return "Homo sapiens";
};

let person = new Person("Alice");
person.greet(); // -> Hello, my name is Alice
console.log(Person.species()); // -> Homo sapiens
```

Wie wir sehen können, sind die Ergebnisse in beiden Implementierungen identisch.

### Prototypbasierte Methode
Es ist erwähnenswert, dass die Methoden, die im Prototyp eines Objekts definiert sind, für alle Instanzen dieses Objekts geteilt werden. Dies spart Speicherplatz, da die Methode nicht für jede Instanz neu erstellt wird.

Ein gewöhnliches Beispiel dafür könnte so aussehen:

```javascript
let Test = function(arg) {
    this.arg = arg;
    this.showSth = function() {
        console.log("I'm prototyped!");
    };
    console.log(this.arg);
};

Test.showSth = function() {
    console.log("Hi, I'm static!");
};
```

### Entscheidung zwischen Klassen und Konstruktoren
Die Wahl zwischen der Verwendung von Klassen und Konstruktoren ist oft subjektiv. Beide bieten die gleichen Funktionen und Möglichkeiten. Wenn du alleine arbeitest, kannst du einfach die Methode wählen, die dir angenehmer ist. In einem Team kann es jedoch wichtig sein, einen einheitlichen Ansatz zu verfolgen. Zudem könnten bestimmte Frameworks oder Bibliotheken (wie React) vorschreiben, eine bestimmte Methode zu verwenden.

## Fazit
Klassen und Konstruktorfunktionen in JavaScript bieten die gleichen Möglichkeiten, aber Klassen bieten eine syntaktisch bequemere Möglichkeit, Prototypen-basierte Vererbung zu nutzen. Die Wahl zwischen beiden hängt oft von den persönlichen Vorlieben oder den Anforderungen eines Projekts ab.
