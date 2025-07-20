
# JavaScript JSON

**JSON** (JavaScript Object Notation) ist ein textbasiertes Datenformat, das primär für den Datenaustausch über Netzwerke verwendet wird. 
In JavaScript wird JSON verwendet, um Daten effizient zu speichern und zu übertragen. JSON hat sich durch seine Einfachheit etabliert und wird in vielen anderen Sprachen genutzt.

---

## 1. JSON.stringify()

Die Methode `JSON.stringify()` wandelt JavaScript-Objekte in ein JSON-Format (also einen String) um.

### Beispiel
```javascript
let person = {
    name: "Maria",
    alter: 30,
    stadt: "Berlin"
};
let personJSON = JSON.stringify(person);
console.log(typeof personJSON); // -> string
console.log(personJSON); // -> {"name":"Maria","alter":30,"stadt":"Berlin"}
```

#### Zusatzbeispiel 1
```javascript
let buch = {
    titel: "JavaScript für Einsteiger",
    seiten: 400,
    autoren: ["Max Mustermann", "Lisa Müller"]
};
let buchJSON = JSON.stringify(buch);
console.log(buchJSON); // -> {"titel":"JavaScript für Einsteiger","seiten":400,"autoren":["Max Mustermann","Lisa Müller"]}
```

#### Zusatzbeispiel 2
```javascript
let auto = {
    marke: "Tesla",
    modell: "Model 3",
    elektrisch: true
};
let autoJSON = JSON.stringify(auto);
console.log(autoJSON); // -> {"marke":"Tesla","modell":"Model 3","elektrisch":true}
```

---

## 2. JSON.parse()

Die Methode `JSON.parse()` konvertiert JSON-Strings zurück in JavaScript-Objekte.

### Beispiel
```javascript
let daten = '{"id":"AB12345","position":{"long":10.1234,"lat":52.1234}}';
let objekt = JSON.parse(daten);
console.log(typeof objekt); // -> object
console.log(objekt.position.long); // -> 10.1234
```

#### Zusatzbeispiel 1
```javascript
let einstellungenJSON = '{"thema":"dunkel","sprache":"de","benachrichtigungen":true}';
let einstellungen = JSON.parse(einstellungenJSON);
console.log(einstellungen.thema); // -> dunkel
console.log(einstellungen.sprache); // -> de
```

#### Zusatzbeispiel 2
```javascript
let profilJSON = '{"nutzername":"janedoe","punkte":1500}';
let profil = JSON.parse(profilJSON);
console.log(profil.nutzername); // -> janedoe
console.log(profil.punkte); // -> 1500
```

---

## 3. JSON mit Arrays und Objekten

JSON unterstützt das Speichern von Arrays und Objekten.

### Beispiel: Array von Objekten
```javascript
let users = [
    { "name": "Anna", "alter": 25 },
    { "name": "Ben", "alter": 30 }
];
let usersJSON = JSON.stringify(users);
console.log(usersJSON); // -> [{"name":"Anna","alter":25},{"name":"Ben","alter":30}]
```

#### Zusatzbeispiel 1
```javascript
let produkte = [
    { "name": "Laptop", "preis": 800 },
    { "name": "Tablet", "preis": 400 }
];
let produkteJSON = JSON.stringify(produkte);
console.log(produkteJSON); // -> [{"name":"Laptop","preis":800},{"name":"Tablet","preis":400}]
```

#### Zusatzbeispiel 2
```javascript
let kurse = [
    { "titel": "Mathe", "stunden": 20 },
    { "titel": "Informatik", "stunden": 30 }
];
let kurseJSON = JSON.stringify(kurse);
console.log(kurseJSON); // -> [{"titel":"Mathe","stunden":20},{"titel":"Informatik","stunden":30}]
```

---

## 4. Fehlerquellen und Zyklen in JSON

Zyklen in Objekten können zu Fehlern führen.

### Beispiel
```javascript
let obj = {};
obj.self = obj; // zyklische Referenz
try {
    JSON.stringify(obj); // Fehler: Zyklen können nicht in JSON konvertiert werden
} catch (error) {
    console.log("Fehler:", error.message);
}
```

---

Dieses Skript gibt Ihnen und Ihren Schülern einen fundierten Überblick über die JSON-Methoden `stringify` und `parse` in JavaScript mit zusätzlichen Beispielen.
