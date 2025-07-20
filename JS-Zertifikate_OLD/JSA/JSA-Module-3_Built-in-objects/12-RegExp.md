
# JavaScript Reguläre Ausdrücke (RegExp)

Der `RegExp` Konstruktor in JavaScript wird verwendet, um reguläre Ausdrücke zu erstellen, die Muster für Textsuche und -validierung darstellen.
Dieses Skript bietet eine Einführung in die grundlegenden Konzepte und Methoden.

---

## 1. Grundlagen von Regulären Ausdrücken

Ein **regulärer Ausdruck** (Regular Expression, RegExp) ist ein Suchmuster, das aus Zeichen und Metazeichen besteht.

### Beispiel
```javascript
let text = "Ich lerne JavaScript";
let regex = /JavaScript/;
console.log(regex.test(text)); // -> true
```

#### Zusatzbeispiel 1
```javascript
let satz = "Lernen ist wichtig";
let muster = /wichtig/;
console.log(muster.test(satz)); // -> true
```

#### Zusatzbeispiel 2
```javascript
let phrase = "JavaScript ist mächtig.";
let expression = /einfach/;
console.log(expression.test(phrase)); // -> false
```

---

## 2. Erstellung von RegExp

Reguläre Ausdrücke können auf zwei Arten erstellt werden:
- Mit dem `RegExp` Konstruktor.
- Mit dem Literal-Syntax durch Schrägstriche.

### Beispiel: Konstruktor und Literal
```javascript
let regex1 = new RegExp("abc");
let regex2 = /abc/;
console.log(regex1.test("abcdef")); // -> true
console.log(regex2.test("123abc")); // -> true
```

#### Zusatzbeispiel 1
```javascript
let regex1 = new RegExp("123");
let regex2 = /123/;
console.log(regex1.test("abc123")); // -> true
console.log(regex2.test("keine Zahl hier")); // -> false
```

#### Zusatzbeispiel 2
```javascript
let regex1 = new RegExp("hallo");
let regex2 = /hallo/;
console.log(regex1.test("hallo welt")); // -> true
console.log(regex2.test("Hallo Welt")); // -> false (case-sensitive)
```

---

## 3. Methoden: `test` und `exec`

### Methode `test()`

Die Methode `test()` prüft, ob ein String mit einem Muster übereinstimmt. Sie gibt `true` oder `false` zurück.

#### Beispiel
```javascript
let regex = /c.t/;
console.log(regex.test("cat")); // -> true
console.log(regex.test("cut")); // -> true
console.log(regex.test("ct")); // -> false
```

#### Zusatzbeispiel 1
```javascript
let regex = /s.n/;
console.log(regex.test("sun")); // -> true
console.log(regex.test("sin")); // -> true
console.log(regex.test("song")); // -> false
```

#### Zusatzbeispiel 2
```javascript
let regex = /h.t/;
console.log(regex.test("hat")); // -> true
console.log(regex.test("hit")); // -> true
console.log(regex.test("hotdog")); // -> true
```

---

### Methode `exec()`

Die Methode `exec()` gibt bei einem Treffer ein Array mit Informationen zurück.

#### Beispiel
```javascript
let regex = /c.t/;
console.log(regex.exec("haircut")); // -> ["cut", index: 4, input: "haircut", groups: undefined]
console.log(regex.exec("ct")); // -> null
```

#### Zusatzbeispiel 1
```javascript
let regex = /h.t/;
console.log(regex.exec("hat")); // -> ["hat", index: 0, input: "hat", groups: undefined]
console.log(regex.exec("hotdog")); // -> ["hot", index: 0, input: "hotdog", groups: undefined]
```

#### Zusatzbeispiel 2
```javascript
let regex = /f.o/;
console.log(regex.exec("foo")); // -> ["foo", index: 0, input: "foo", groups: undefined]
console.log(regex.exec("faro")); // -> ["fo", index: 1, input: "faro", groups: undefined]
```

---

## 4. Methoden des String Konstruktors mit RegExp

JavaScript's String-Methoden wie `search`, `match` und `replace` unterstützen ebenfalls reguläre Ausdrücke.

### Beispiel
```javascript
let str = "Hund und Katze";
let regex = /Katze/;
console.log(str.search(regex));  // -> 9
console.log(str.replace(regex, "Vogel")); // -> Hund und Vogel
console.log(str.match(regex)); // -> ["Katze", index: 9, input: "Hund und Katze", groups: undefined]
```

#### Zusatzbeispiel 1
```javascript
let text = "Das Wetter ist schön.";
let pattern = /schön/;
console.log(text.search(pattern)); // -> 14
console.log(text.replace(pattern, "kalt")); // -> Das Wetter ist kalt.
```

#### Zusatzbeispiel 2
```javascript
let phrase = "RegExp ist mächtig.";
let reg = /mächtig/;
console.log(phrase.match(reg)); // -> ["mächtig", index: 11, input: "RegExp ist mächtig.", groups: undefined]
console.log(phrase.replace(reg, "nützlich")); // -> RegExp ist nützlich.
```

---

Das vollständige Dokument enthält viele Beispiele und bietet einen fundierten Überblick über reguläre Ausdrücke in JavaScript.
