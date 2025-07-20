
# Übungsaufgaben zu Strings in JavaScript

## Aufgaben

### Aufgabe 1
Gegeben ist der String: `"JavaScript is fun and challenging!"`. Ersetze das Wort "challenging" mit dem Wort "rewarding", schneide den ersten Teil bis einschließlich "fun" ab, und wandle den restlichen Text in Großbuchstaben um.

### Aufgabe 2
Du hast den String: `"123-456-789"`. Extrahiere die drei Zahlenblöcke und addiere sie als Ganzzahlen.

### Aufgabe 3
Ein Benutzer gibt eine E-Mail-Adresse ein, zum Beispiel `"user@example.com"`. Schreibe eine Funktion, die den Benutzernamen (den Teil vor dem `@`) und die Domain (den Teil nach dem `@`) separat extrahiert und als Objekt zurückgibt.

### Aufgabe 4
Du erhältst eine Liste von Sätzen in einem einzigen String, getrennt durch Punkte: `"Hello. How are you? Have a great day."`. Teile den String in einzelne Sätze auf, entferne alle Fragezeichen und Punkte, und gib die Anzahl der Wörter in jedem Satz aus.

### Aufgabe 5
Schreibe eine Funktion, die den String `"   JavaScript   "` sowohl am Anfang als auch am Ende trimmt, die Buchstaben des Strings in Kleinbuchstaben umwandelt und jedes Wort durch einen Bindestrich (`-`) trennt.

### Aufgabe 6
Gegeben ist der String: `"apple, banana, cherry"`. Wandle diesen String in eine Liste (Array) um, entferne die Leerzeichen, füge am Ende des Arrays `"grape"` hinzu und gib das Array als String zurück, wobei die Elemente durch Semikolon (`;`) getrennt sind.

### Aufgabe 7
Du hast einen String mit einer Telefonnummer, bei der die Zahlen durch Leerzeichen getrennt sind: `"4 9 5 2 3 6"`. Füge die Zahlen zu einem String ohne Leerzeichen zusammen und formatiere die Telefonnummer so, dass sie in Dreierblöcken getrennt wird (z.B. `"495-236"`).

### Aufgabe 8
Gegeben ist der String: `"Learning JavaScript is fun, but challenging."`. Schreibe eine Funktion, die den String so modifiziert, dass alle Wörter, die mit einem Vokal (a, e, i, o, u) beginnen, durch ihre Länge ersetzt werden. Beispiel: `"Learning 10 fun, but challenging."`

### Aufgabe 9
Extrahiere die letzten drei Zeichen des Strings `"Programming"` und gib sie dreimal hintereinander wiederholt zurück, ohne dass Leerzeichen zwischen den Zeichen erscheinen.

### Aufgabe 10
Gegeben ist der String `"Basketball is a team sport."`. Wandle diesen String so um, dass die Buchstaben in der ersten Hälfte des Strings in Großbuchstaben und die Buchstaben in der zweiten Hälfte in Kleinbuchstaben umgewandelt werden.

### Aufgabe 11
Du erhältst eine Zeichenkette `"aaaabbbbccccdddd"`. Schreibe eine Funktion, die die Häufigkeit jedes Zeichens zählt und ein Objekt mit den Buchstaben als Schlüssel und der Anzahl ihrer Vorkommen als Wert zurückgibt.

### Aufgabe 12
Gegeben ist der String `"ABCDEFGH"`. Füge nach jedem zweiten Buchstaben einen Bindestrich (`-`) ein, aber füge am Ende des Strings keinen Bindestrich hinzu.

### Aufgabe 13
Du erhältst eine Textdatei, die mit dem String `"Error: The file was not found. Error: Access denied."` beginnt. Schreibe eine Funktion, die alle Vorkommen des Wortes `"Error"` entfernt und die verbleibenden Sätze in einem Array zurückgibt.

### Aufgabe 14
Ein Benutzer gibt ein Passwort mit mindestens 8 Zeichen ein. Erstelle eine Funktion, die überprüft, ob das Passwort mindestens eine Zahl, einen Großbuchstaben und ein Sonderzeichen enthält. Wenn nicht, gibt die Funktion einen entsprechenden Hinweis aus.

### Aufgabe 15
Schreibe eine Funktion, die den String `"   spaces    everywhere   "` so umformatiert, dass die doppelten Leerzeichen durch einfache Leerzeichen ersetzt werden und der String insgesamt getrimmt wird.

---

## Lösungen

### Lösung 1
```javascript
let str = "JavaScript is fun and challenging!";
let result = str.replace("challenging", "rewarding").slice(17).toUpperCase();
console.log(result);  // -> REWARDING!
```

### Lösung 2
```javascript
let str = "123-456-789";
let numbers = str.split("-").map(Number);
let sum = numbers.reduce((a, b) => a + b, 0);
console.log(sum);  // -> 1368
```

### Lösung 3
```javascript
function extractEmailDetails(email) {
    let [username, domain] = email.split("@");
    return { username, domain };
}
console.log(extractEmailDetails("user@example.com"));
// -> { username: "user", domain: "example.com" }
```

### Lösung 4
```javascript
const text = "Hello. How are you? Have a great day.";

// Aufteilen des Strings in Sätze und Entfernen von Satzzeichen
const sentences = text.split(/[.?!]/).filter(sentence => sentence.trim() !== "");

// Zählen der Wörter in jedem Satz und Ausgabe
const wordCounts = sentences.map(sentence => {
  const words = sentence.trim().split(/\s+/); // Wörter zählen
  return words.length;
});

console.log(wordCounts);
```

### Lösung 5
```javascript
function formatString(str) {
    return str.trim().toLowerCase().split(" ").join("-");
}
console.log(formatString("   JavaScript   "));  // -> "javascript"
```

### Lösung 6
```javascript
let fruits = "apple, banana, cherry".split(",").map(fruit => fruit.trim());
fruits.push("grape");
let result = fruits.join(";");
console.log(result);  // -> "apple;banana;cherry;grape"
```

### Lösung 7
```javascript
let phone = "4 9 5 2 3 6".replace(/\s/g, "");
let formattedPhone = phone.match(/.{1,3}/g).join("-");
console.log(formattedPhone);  // -> "495-236"
```

### Lösung 8
```javascript
function replaceVowelWords(str) {
    return str.split(" ").map(word => /^[aeiou]/i.test(word) ? word.length : word).join(" ");
}
console.log(replaceVowelWords("Learning JavaScript is fun, but challenging."));
// -> "Learning JavaScript 10 fun, but challenging."
```

### Lösung 9
```javascript
let str = "Programming";
let lastThree = str.slice(-3);
console.log(lastThree.repeat(3));  // -> "inginging"
```

### Lösung 10
```javascript
let str = "Basketball is a team sport.";
let middle = Math.floor(str.length / 2);
let result = str.slice(0, middle).toUpperCase() + str.slice(middle).toLowerCase();
console.log(result);  // -> "BASKETBALL IS A team sport."
```

### Lösung 11
```javascript
function countChars(str) {
    return [...str].reduce((acc, char) => {
        acc[char] = acc[char] ? acc[char] + 1 : 1;
        return acc;
    }, {});
}
console.log(countChars("aaaabbbbccccdddd"));
// -> {a: 4, b: 4, c: 4, d: 4}
```

### Lösung 12
```javascript
let str = "ABCDEFGH";
let result = str.match(/.{1,2}/g).join("-");
console.log(result);  // -> "AB-CD-EF-GH"
```

### Lösung 13
```javascript
function removeErrors(str) {
    return str.split("Error:").filter(Boolean).map(s => s.trim());
}
console.log(removeErrors("Error: The file was not found. Error: Access denied."));
// -> ["The file was not found.", "Access denied."]
```

### Lösung 14
```javascript
function validatePassword(password) {
    let hasNumber = /\d/.test(password);
    let hasUppercase = /[A-Z]/.test(password);
    let hasSpecialChar = /[!@#$%^&*]/.test(password);
    
    if (password.length >= 8 && hasNumber && hasUppercase && hasSpecialChar) {
        return "Password is valid";
    } else {
        return "Password must be at least 8 characters long, contain a number, an uppercase letter, and a special character.";
    }
}
console.log(validatePassword("Password1!"));  // -> "Password is valid"
```

### Lösung 15
```javascript
function removeExtraSpaces(str) {
    return str.replace(/\s+/g, " ").trim();
}
console.log(removeExtraSpaces("   spaces    everywhere   "));
// -> "spaces everywhere"
```
