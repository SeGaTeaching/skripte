
# 3.1.3 Boolean in JavaScript

Der `Boolean`-Konstruktor in JavaScript ist eine Funktion, die es uns ermöglicht, Objekte zu erstellen, die einem booleschen primitiven Typ entsprechen. Wie bei allen primitiven Datentypen gibt es auch hier einen entsprechenden Konstruktor, der als Klasse fungiert. `Boolean` kann auf verschiedene Weisen verwendet werden.

## Verwendung von Boolean

1. **Autoboxing**: Der primitive boolesche Wert wird automatisch in das entsprechende Objekt umgewandelt, wenn Methoden aufgerufen werden.
2. **Mit `new` Operator**: Man kann explizit ein neues Boolean-Objekt erstellen, indem man den `new` Operator verwendet.

### Beispiel 1: Erstellen eines Boolean-Objekts

```javascript
let boolObj1 = new Boolean();
let boolObj2 = new Boolean(true);
let str1 = boolObj1.toString();
let bool2 = boolObj2.valueOf();
console.log(`str1 : ${typeof str1} : ${str1}`); // -> str1 : string : false
console.log(`bool2 : ${typeof bool2} : ${bool2}`); // -> bool2 : boolean : true
```

- `boolObj1` enthält den Standardwert `false`, da kein Argument übergeben wurde.
- `boolObj2` enthält den explizit übergebenen Wert `true`.

Die Methoden `toString()` und `valueOf()` können verwendet werden, um den Wert im Objekt als String bzw. als primitiven booleschen Wert zu erhalten.

### Beispiel 2: Verwendung von Autoboxing mit primitiven Booleans

```javascript
let bool1 = false;
let str1 = bool1.toString();
let bool2 = bool1.valueOf();
console.log(`str1 : ${typeof str1} : ${str1}`); // -> str1 : string : false
console.log(`bool2 : ${typeof bool2} : ${bool2}`); // -> bool2 : boolean : false
```

Hier wird das primitive `false` durch Autoboxing in ein temporäres Boolean-Objekt umgewandelt, um die Methoden `toString()` und `valueOf()` auszuführen.

## Boolean ohne den `new` Operator

Man kann den Boolean-Konstruktor auch ohne den `new` Operator verwenden, um ein Argument in einen booleschen Wert umzuwandeln.

### Beispiel 3: Boolean ohne `new` Operator

```javascript
let bool1 = Boolean(false);
let bool2 = Boolean(1);
let bool3 = Boolean("");
console.log(`bool1 : ${typeof bool1} : ${bool1}`); // -> bool1 : boolean : false
console.log(`bool2 : ${typeof bool2} : ${bool2}`); // -> bool2 : boolean : true
console.log(`bool3 : ${typeof bool3} : ${bool3}`); // -> bool3 : boolean : false
```

Hier konvertieren wir verschiedene Werte in ihre booleschen Entsprechungen:
- `false` bleibt `false`.
- `1` wird zu `true`, da jede positive Zahl in JavaScript als `true` gilt.
- Ein leerer String `""` wird zu `false`, da leere Werte als "falsy" betrachtet werden.

## Zusätzliche Beispiele

### Beispiel 4: Überprüfung von "truthy" und "falsy" Werten

```javascript
let falsyValues = [false, null, undefined, NaN, "", 0, -0, 0n];
falsyValues.forEach(value => {
    console.log(`${value} is falsy: `, Boolean(value) === false);
});

let truthyValues = [true, {}, [], "hello", 1, -1, 42n];
truthyValues.forEach(value => {
    console.log(`${value} is truthy: `, Boolean(value) === true);
});
```

In diesem Beispiel prüfen wir, welche Werte als "falsy" (d.h. sie werden zu `false` konvertiert) und welche als "truthy" (d.h. sie werden zu `true` konvertiert) gelten.

### Beispiel 5: Konvertierung von Werten zu Boolean für logische Überprüfungen

```javascript
function checkValue(value) {
    if (Boolean(value)) {
        console.log(`${value} is true`);
    } else {
        console.log(`${value} is false`);
    }
}

checkValue(0);      // -> 0 is false
checkValue("test");  // -> test is true
checkValue(null);    // -> null is false
checkValue(100);     // -> 100 is true
```

Hier verwenden wir den `Boolean`-Konstruktor, um verschiedene Werte auf ihre "truthy" oder "falsy" Natur zu überprüfen.

## Zusammenfassung

- Der `Boolean`-Konstruktor dient zur Erstellung von Objekten, die einem booleschen primitiven Wert entsprechen.
- Verwende `toString()` und `valueOf()` für die Konvertierung eines Boolean-Objekts in einen String oder einen primitiven booleschen Wert.
- Durch **Autoboxing** wird ein primitiver Boolean in ein temporäres Objekt umgewandelt, wenn Methoden aufgerufen werden.
- Der `Boolean`-Konstruktor kann auch ohne den `new` Operator verwendet werden, um Werte in ihre booleschen Entsprechungen zu konvertieren.
- "Falsy" Werte in JavaScript sind: `false`, `null`, `undefined`, `NaN`, `""`, `0`, `-0`, `0n`.
- Alle anderen Werte gelten als "truthy".

