
# 3.1.8 String in JavaScript

Der `String`-Konstruktor entspricht dem primitiven String-Typ und ermöglicht die einfache Manipulation von Zeichenketten. Er stellt eine Vielzahl von Methoden bereit, die für die tägliche Arbeit mit Strings sehr nützlich sind.

## 3.1.9 Strings in JavaScript

Strings können in JavaScript in einfachen (`'`), doppelten (`"`) oder Backticks (`\``) Anführungszeichen angegeben werden. Backticks erlauben zusätzlich das Einfügen von Variablen durch Template Literals.

### Beispiel 1: Verwendung von Template Literals

```javascript
let name = "Alice";
let age = 25;
let message = `Hi, ${name}! You are ${age} years old.`;
console.log(message); // -> Hi, Alice! You are 25 years old.
```

### Beispiel 2: Strings mit unterschiedlichen Anführungszeichen

```javascript
let doubleQuoted = "This is a string";
let singleQuoted = 'This is also a string';
let backticks = `This is a template literal`;
console.log(doubleQuoted, singleQuoted, backticks);
```

### Beispiel 3: Escapen von Zeichen

```javascript
let quote = 'He said, "Hello!"';
let escape = "It's a beautiful day.";
console.log(quote);  // -> He said, "Hello!"
console.log(escape); // -> It's a beautiful day.
```

## 3.1.10 String Konstruktor

Der `String`-Konstruktor kann zur expliziten Erstellung von String-Objekten verwendet werden, obwohl dies in der Regel nicht empfohlen wird. Die Länge eines Strings kann mit der `length`-Eigenschaft abgefragt werden.

### Beispiel 4: Verwendung der `length`-Eigenschaft

```javascript
let str = "Hello, World!";
console.log(str.length);  // -> 13
console.log("".length);   // -> 0
```

### Beispiel 5: Überprüfung von String-Längen

```javascript
let strings = [undefined, "", "abc", "JavaScript", 123];
strings.forEach(s => {
    s && s.length && console.log(s);
});
// -> "abc", "JavaScript"
```

## 3.1.11 String als Array von Zeichen

Ein String kann wie ein Array von Zeichen behandelt werden, wobei jedes Zeichen über seinen Index angesprochen werden kann.

### Beispiel 6: Zugriff auf Zeichen eines Strings

```javascript
let title = "JavaScript";
console.log(title[0]); // -> J
console.log(title.charAt(0)); // -> J
```

## 3.1.12 Groß- und Kleinschreibung

Die Methoden `toLowerCase()` und `toUpperCase()` ermöglichen das Umwandeln von Zeichenketten in Klein- oder Großbuchstaben.

### Beispiel 7: Groß-/Kleinschreibung umwandeln

```javascript
let greeting = "Hello, World!";
console.log(greeting.toUpperCase()); // -> HELLO, WORLD!
console.log(greeting.toLowerCase()); // -> hello, world!
```

## 3.1.13 Aufteilen von Strings

Die Methode `split()` teilt eine Zeichenkette in ein Array von Teilstrings, basierend auf einem angegebenen Trennzeichen.

### Beispiel 8: Zeichenkette aufteilen

```javascript
let ipAddress = "192.168.1.1";
let parts = ipAddress.split(".");
console.log(parts); // -> ["192", "168", "1", "1"]
```

## 3.1.14 Ersetzen von Teilstrings

Die Methode `replaceAll()` ersetzt alle Vorkommen eines bestimmten Teilstrings durch einen anderen.

### Beispiel 9: Ersetzen von Zeichenketten

```javascript
let text = "Hello, Hello!";
let newText = text.replaceAll("Hello", "Hi");
console.log(newText); // -> Hi, Hi!
```

## 3.1.15 Suchen von Teilstrings

Die Methoden `includes()`, `indexOf()` und `lastIndexOf()` helfen beim Suchen von Teilstrings.

### Beispiel 10: Suchen nach Teilstrings

```javascript
let text = "Find me here, here and here.";
console.log(text.includes("here"));         // -> true
console.log(text.indexOf("here"));          // -> 9
console.log(text.lastIndexOf("here"));      // -> 23
```

## 3.1.16 Kopieren von Teilstrings

Die Methoden `substr()`, `substring()` und `slice()` ermöglichen das Kopieren von Teilstrings aus einer Zeichenkette.

### Beispiel 11: Kopieren von Teilstrings

```javascript
let text = "JavaScript is fun!";
console.log(text.substr(0, 10));   // -> JavaScript
console.log(text.substring(0, 10)); // -> JavaScript
console.log(text.slice(0, 10));    // -> JavaScript
```

## 3.1.17 Auffüllen von Strings

Mit den Methoden `padStart()` und `padEnd()` können Strings auf eine bestimmte Länge erweitert werden.

### Beispiel 12: Padding von Strings

```javascript
let num = "5";
console.log(num.padStart(3, "0"));  // -> 005
console.log(num.padEnd(3, "0"));    // -> 500
```

## 3.1.18 Trimmen von Strings

Die Methoden `trim()`, `trimStart()` und `trimEnd()` entfernen Leerzeichen am Anfang oder Ende eines Strings.

### Beispiel 13: Trimmen von Strings

```javascript
let city = "  New York  ";
console.log(city.trim());       // -> "New York"
console.log(city.trimStart());  // -> "New York  "
console.log(city.trimEnd());    // -> "  New York"
```

## 3.1.19 Vergleichen von Strings

Strings können mit Vergleichsoperatoren (`<`, `>`, `==`, usw.) verglichen werden.

### Beispiel 14: Vergleichen von Strings

```javascript
console.log("apple" < "banana");  // -> true
console.log("2" < "10");          // -> false
```

### Beispiel 15: Vergleichen von Strings mit `localeCompare()`

```javascript
console.log("Österreich".localeCompare("Deutschland", "de")); // -> 1
console.log("Berlin".localeCompare("Bremen", "de"));          // -> -1
```

## Zusammenfassung

- Strings können in JavaScript in verschiedenen Anführungszeichen definiert werden.
- Methoden wie `toUpperCase()`, `split()`, `replaceAll()` und `indexOf()` erleichtern die Manipulation von Zeichenketten.
- Methoden wie `padStart()`, `trim()` und `localeCompare()` bieten zusätzliche Funktionalitäten, um Strings in spezifische Formate zu bringen oder sie zu vergleichen.
