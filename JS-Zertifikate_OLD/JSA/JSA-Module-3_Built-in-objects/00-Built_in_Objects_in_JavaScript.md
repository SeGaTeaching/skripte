
# 3.0.1 Built-in Objects in JavaScript

In JavaScript haben wir gelernt, eigene Objekte durch Techniken wie Literale, Konstruktoren oder Klassen zu definieren und zu erstellen. Die Struktur dieser Objekte – also ihre Eigenschaften und Methoden – wird dabei durch die aktuellen Anforderungen bestimmt.

## Standard Built-in Objects

JavaScript bietet eine Vielzahl vordefinierter Objekte, die häufig benötigte Funktionalitäten bereitstellen. Diese Objekte werden als **built-in objects** (eingebaute Objekte) bezeichnet. Beispiele sind:

- `Math` für mathematische Berechnungen
- `JSON` für die Umwandlung von Objekten in ein übertragbares Format

### Unterscheidung zwischen Objekten und Klassen

Viele dieser eingebauten Objekte sind normale Objekte. Sie werden verwendet, indem der Objektname und die zugehörige Methode oder Eigenschaft aufgerufen werden, z.B. `JSON.stringify`.

Jedoch sind nicht alle eingebauten Elemente einfache Objekte. Einige dieser **built-in objects** sind in Wirklichkeit Klassen oder Funktionen, wie z.B. `Object` oder `Date`. Da jedoch in JavaScript alles außer den primitiven Datentypen als Objekt betrachtet wird, hat sich die Bezeichnung "built-in objects" für alle Elemente durchgesetzt.

### Nutzen der eingebauten Objekte

Die eingebauten Objekte erleichtern uns die Programmierung erheblich, da sie viele Funktionalitäten als Methoden und Eigenschaften zur Verfügung stellen. Wichtig dabei ist es, zu verstehen, ob eine Methode oder Eigenschaft statisch ist oder auf einer Instanz eines Objekts arbeitet.

## Unterschied zwischen statischen und Instanzmethoden

Zur Erinnerung ein Beispiel:

```javascript
class AlmostEmptyClass { 
    constructor(sth) { 
        console.log(sth); 
    }; 

    sayHi() { 
        console.log("Hi!") 
    }; 

    static sayHello() { 
        console.log("Hello!") 
    }; 
}; 

let almostEmptyObject = new AlmostEmptyClass(120); // 120 
almostEmptyObject.sayHi(); // -> Hi! 
almostEmptyObject.sayHello(); // Fehler
AlmostEmptyClass.sayHello(); // -> Hello!
```

In diesem Beispiel ist `sayHi` eine **Instanzmethode** (sie wird auf einer Instanz des Objekts aufgerufen), während `sayHello` eine **statische Methode** ist (sie wird direkt auf der Klasse aufgerufen).

Das Verständnis dieses Unterschieds ist entscheidend, um die eingebauten Objekte korrekt zu verwenden.

### Beispiel: Das `Number`-Objekt

Das `Number`-Objekt wird genutzt, um Zahlen als Objekte zu behandeln:

```javascript
let n = new Number(100.123);
let fixed = n.toFixed(2); // Ausgabe: '100.12'
let test1 = Number.isInteger(100); // Ausgabe: true
let test2 = n.isInteger(100); // Fehler: n.isInteger ist keine Funktion
```

- `toFixed` ist eine **Instanzmethode**, die auf dem Objekt `n` aufgerufen wird, das mit dem `Number`-Konstruktor erstellt wurde.
- `isInteger` ist eine **statische Methode**, die direkt auf der `Number`-Klasse verwendet wird.

## Kategorien von Built-in Objects

Die eingebauten Objekte können grob in drei Gruppen eingeteilt werden:

1. **Objekte für primitive Datentypen**:
    - `Boolean`
    - `Number`
    - `String`
    - `Date`

2. **Objekte für zusammengesetzte Datentypen**:
    - `Array`
    - `Set`
    - `Map`
    - `Object`

3. **Hilfsobjekte für häufige Aufgaben**:
    - `JSON`
    - `Math`
    - `RegExp`

Diese Gruppierung basiert auf der praktischen Nützlichkeit der Objekte und ist keine offizielle Klassifikation.

## Fazit

Was wir bisher gelernt haben, ermöglicht es uns, die eingebauten Objekte in JavaScript zu nutzen. Wir sollten in der Lage sein:

- Methoden und Eigenschaften von Objekten korrekt zu verwenden,
- zwischen statischen und Instanzmethoden zu unterscheiden,
- die Dokumentation für eingebauten Objekte zu verstehen.

Für weiterführende Informationen sind die Seiten der **MDN Web Docs** eine exzellente Ressource.
