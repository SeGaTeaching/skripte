 
# 3.1.20 Date in JavaScript

Der `Date`-Konstruktor in JavaScript dient sowohl zur Speicherung von Datum als auch von Zeit. Im Gegensatz zu den vorher besprochenen primitiven Typen stellt `Date` kein primitives Objekt dar. Es speichert die Zeit als einen Zeitstempel, der die Anzahl der Millisekunden seit dem 1. Januar 1970, 00:00:00 UTC, repräsentiert.

## 3.1.21 Zeitzonen und Timestamp

### Beispiel 1: Erstellen eines `Date`-Objekts

```javascript
let date1 = new Date(0);
let date2 = new Date(1000 * 60 * 60 * 10); // 10 Stunden später
console.log(date1.toUTCString());  // -> Thu, 01 Jan 1970 00:00:00 GMT
console.log(date2.toUTCString());  // -> Thu, 01 Jan 1970 10:00:00 GMT
```

In diesem Beispiel wird ein `Date`-Objekt mit einem Zeitstempel von 0 Millisekunden erstellt, das den 1. Januar 1970 darstellt. Das zweite Objekt wird mit 10 Stunden (in Millisekunden) erstellt.

### Beispiel 2: Zeitzonen-Offset berechnen

```javascript
console.log(date2.getTimezoneOffset());   // -> 0
console.log(date2.toLocaleString());      // -> 01/01/1970, 10:00:00
console.log(date2.toISOString());         // -> 1970-01-01T10:00:00.000Z
```

Diese Methode zeigt, wie der Zeitzonen-Offset und die Lokale Zeit mit verschiedenen Methoden abgefragt werden kann.

## 3.1.22 Aktuelle Zeit

Das `Date`-Objekt kann verwendet werden, um die aktuelle Zeit zu erhalten. Der Konstruktor kann ohne Argumente aufgerufen werden, was die aktuelle Zeit zurückgibt.

### Beispiel 3: Aktuelle Zeit abrufen

```javascript
let now = new Date();
console.log(now.toLocaleString());  // -> aktuelle Zeit im lokalen Format
```

Die statische Methode `Date.now()` gibt den aktuellen Zeitstempel zurück.

### Beispiel 4: Verwendung von `Date.now()`

```javascript
let nowTimestamp = Date.now();
let nowObj = new Date(nowTimestamp);
console.log(`Zeitstempel: ${nowTimestamp}, Datum: ${nowObj}`);
```

## 3.1.23 Zeitangaben mit Komponenten

Ein Datum kann auch durch die Angabe einzelner Komponenten wie Jahr, Monat, Tag usw. erstellt werden.

### Beispiel 5: Datum mit Jahr und Monat erstellen

```javascript
let date1 = new Date(2022, 0);  // Januar 2022
let date2 = new Date(2022, 11, 25);  // 25. Dezember 2022
console.log(date1.toLocaleString());  // -> 01/01/2022, 00:00:00
console.log(date2.toLocaleString());  // -> 25/12/2022, 00:00:00
```

## 3.1.24 Zeitangaben mit Datumszeichenfolgen

Die Erstellung eines `Date`-Objekts durch die Übergabe von Datumszeichenfolgen kann in verschiedenen Formaten erfolgen.

### Beispiel 6: ISO 8601 Format

```javascript
let date1 = new Date("2020-07-08");
let date2 = new Date("2020-07-08T10:20:00");
console.log(date1.toLocaleString());  // -> 08/07/2020, 00:00:00
console.log(date2.toLocaleString());  // -> 08/07/2020, 10:20:00
```

Hier wird das ISO-Format verwendet, um die Zeit darzustellen. Ohne `Z` am Ende ist die Zeit lokal, mit `Z` ist sie in UTC.

## 3.1.25 Praktische Verwendung von Zeitstempeln

Mit der Methode `getTime()` kann der Zeitstempel eines bestimmten Datums in Millisekunden abgefragt werden. Diese Methode kann z.B. verwendet werden, um die Zeit zwischen zwei Zeitpunkten zu berechnen.

### Beispiel 7: Berechnung der Millisekunden zwischen zwei Daten

```javascript
let date1 = new Date(2020, 6, 8, 10, 20, 0);
let date2 = new Date(2020, 6, 9, 10, 20, 0);
console.log(date2.getTime() - date1.getTime());  // -> 86400000 (Millisekunden in einem Tag)
```

## 3.1.26 Zugriff auf einzelne Zeitkomponenten

Die `Date`-Objekte bieten eine Vielzahl von Methoden, um auf einzelne Komponenten wie Jahr, Monat, Tag usw. zuzugreifen.

### Beispiel 8: Zugriff auf Jahr, Monat und Tag

```javascript
let date = new Date("2020-07-08T10:20:00");
console.log(date.getFullYear());  // -> 2020
console.log(date.getMonth());     // -> 6 (Juli, da Monate ab 0 gezählt werden)
console.log(date.getDate());      // -> 8
```

Es gibt auch Methoden, um diese Werte zu ändern, z.B. `setFullYear()`, `setMonth()`, etc.

### Beispiel 9: Ändern der Stunden

```javascript
let date = new Date("2020-07-08T10:20:00");
date.setHours(15);
console.log(date.getHours());  // -> 15
```

## 3.1.27 Umwandlung von Zeitangaben in Strings

Es gibt mehrere Methoden, um das Datum und die Uhrzeit eines `Date`-Objekts in einen String umzuwandeln.

### Beispiel 10: `toLocaleDateString` und `toLocaleTimeString`

```javascript
let date = new Date("2020-07-08T10:20:00");
console.log(date.toLocaleDateString());  // -> 08/07/2020
console.log(date.toLocaleTimeString());  // -> 10:20:00
```

Diese Methoden geben das Datum oder die Zeit im lokalen Format des Systems zurück.

## Zusammenfassung

- `Date`-Objekte speichern Zeit als einen Zeitstempel, der Millisekunden seit dem 1. Januar 1970 darstellt.
- Zeitzonen und UTC-Zeitformate spielen eine wichtige Rolle bei der Verarbeitung von Zeiten.
- Der `Date`-Konstruktor akzeptiert verschiedene Formate und kann durch Zeitstempel, Komponenten oder Zeichenfolgen erstellt werden.
- Mit Methoden wie `getTime()`, `toLocaleString()`, `getFullYear()` kann man auf verschiedene Zeitformate zugreifen und sie bearbeiten.
