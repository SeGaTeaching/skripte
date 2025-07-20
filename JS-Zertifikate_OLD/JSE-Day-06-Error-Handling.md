
# JavaScript Fehler und Ausnahmebehandlung

## 6.1.1 Weitere Details zu JavaScript-Fehlern und -Ausnahmen

JavaScript hat verschiedene Fehlerarten, die auftreten können. Zu den häufigsten gehören:

- **SyntaxError**: Tritt auf, wenn der Code gegen die Syntaxregeln von JavaScript verstößt.
  - Beispiel 1: Ein fehlendes Anführungszeichen.
    ```javascript
    console.log("Hallo Welt);  // SyntaxError: Das schließende Anführungszeichen fehlt
    ```
  - Beispiel 2: Ein fehlender Operator zwischen zwei Variablen.
    ```javascript
    let a = 5 let b = 10;  // SyntaxError: Es fehlt ein Semikolon oder Operator zwischen den Variablen
    ```

- **ReferenceError**: Dieser Fehler tritt auf, wenn auf eine nicht definierte oder nicht deklarierte Variable zugegriffen wird.
  - Beispiel 1: Zugriff auf eine Variable, die nie definiert wurde.
    ```javascript
    console.log(nichtDefiniert);  // ReferenceError: nichtDefiniert ist nicht definiert
    ```
  - Beispiel 2: Zugriff auf eine lokale Variable außerhalb ihres Gültigkeitsbereichs.
    ```javascript
    function test() {
      let lokaleVariable = 10;
    }
    console.log(lokaleVariable);  // ReferenceError: lokaleVariable ist nicht definiert
    ```

- **TypeError**: Tritt auf, wenn ein Vorgang auf einen Wert des falschen Datentyps angewendet wird.
  - Beispiel 1: Verwendung einer Funktion auf einem Datentyp, der diese Funktion nicht unterstützt.
    ```javascript
    let zahl = 100;
    zahl.toUpperCase();  // TypeError: toUpperCase ist für Zahlen nicht definiert
    ```
  - Beispiel 2: Zugriff auf eine Eigenschaft eines undefined-Werts.
    ```javascript
    let obj = null;
    console.log(obj.name);  // TypeError: Kann die Eigenschaft 'name' von null nicht lesen
    ```

- **RangeError**
  - Beispiel 1: Die Methode toFixed() wird verwendet, um eine Zahl auf eine bestimmte Anzahl von Dezimalstellen zu runden. Der zulässige Bereich für Dezimalstellen liegt zwischen 0 und 100. Wenn eine Zahl außerhalb dieses Bereichs verwendet wird, tritt ein RangeError auf.
    ```javascript
    try {
      let zahl = 1.2345;
      console.log(zahl.toFixed(200)); // Versuch, 200 Dezimalstellen anzugeben
    } catch (error) {
        console.log("RangeError: " + error.message); // Ausgabe: RangeError: toFixed() argument must be between 0 and 100
    }
    ```
  - Beispiel 2: In JavaScript gibt es eine maximale Anzahl von Elementen, die ein Array haben kann (abhängig von der Umgebung, meist etwa 2^32 - 1). Wenn versucht wird, ein Array mit einer Länge darüber zu erstellen, wird ein RangeError geworfen.
    ```javascript
    try {
      let arr = new Array(1e12); // Versuch, ein sehr großes Array zu erstellen
    } catch (error) {
      console.log("RangeError: " + error.message); // Ausgabe: RangeError: Invalid array length
    }
    ```


## 6.1.2 Das try...catch Statement

Das `try...catch`-Statement ermöglicht das Abfangen von Fehlern, sodass der Code weiterhin ausgeführt wird.

**Syntax:**
```javascript
try {
  // Code, der potenziell Fehler erzeugen könnte
} catch (fehler) {
  // Fehlerbehandlungscode
}
```

**Beispiele:**

- Beispiel 1: Abfangen eines ReferenceErrors
  ```javascript
  try {
    console.log(variableNichtDefiniert);
  } catch (error) {
    console.log("Ein Fehler ist aufgetreten: " + error.message); // Ausgabe: Ein Fehler ist aufgetreten: variableNichtDefiniert ist nicht definiert
  }
  ```

- Beispiel 2: Umgang mit einer Division durch Null
  ```javascript
  function division(a, b) {
    try {
      if (b === 0) throw new Error("Division durch Null ist nicht erlaubt.");
      return a / b;
    } catch (error) {
      console.log("Fehler: " + error.message);
    }
  }
  
  console.log(division(4, 0));  // Ausgabe: Fehler: Division durch Null ist nicht erlaubt.
  ```

## 6.1.3 Bedingte Ausnahmebehandlung

Mit bedingter Ausnahmebehandlung können Sie bestimmte Fehlertypen unterschiedlich behandeln.

**Beispiele:**

- Beispiel 1: Behandlung von SyntaxError und ReferenceError
  ```javascript
  try {
    eval("console.log('Hallo");  // SyntaxError wegen eines nicht geschlossenen Strings
  } catch (error) {
    if (error instanceof SyntaxError) {
      console.log("Syntaxfehler gefunden: " + error.message);
    } else {
      console.log("Ein unbekannter Fehler ist aufgetreten.");
    }
  }
  ```

- Beispiel 2: Unterscheidung zwischen TypeError und ReferenceError
  ```javascript
  try {
    let obj = undefined;
    console.log(obj.name);  // TypeError
  } catch (error) {
    if (error instanceof TypeError) {
      console.log("Typfehler: " + error.message);
    } else if (error instanceof ReferenceError) {
      console.log("Referenzfehler: " + error.message);
    } else {
      console.log("Ein anderer Fehler ist aufgetreten.");
    }
  }
  ```

## 6.1.4 Die finally-Anweisung

Der `finally`-Block wird unabhängig davon ausgeführt, ob ein Fehler auftritt oder nicht. Er eignet sich gut für Bereinigungscode.

**Syntax:**
```javascript
try {
  // Code, der Fehler erzeugen könnte
} catch (error) {
  // Fehlerbehandlung
} finally {
  // Code, der immer ausgeführt wird
}
```

**Beispiele:**

- Beispiel 1: Fehlerbehandlung mit finally
  ```javascript
  try {
    throw new Error("Ein Testfehler");
  } catch (error) {
    console.log("Fehler abgefangen: " + error.message);
  } finally {
    console.log("Der finally-Block wird immer ausgeführt.");
  }
  ```

- Beispiel 2: Bereinigung von Ressourcen
  ```javascript
  function datenbankZugriff() {
    try {
      console.log("Verbindung zur Datenbank hergestellt.");
      throw new Error("Verbindungsfehler"); // Simulierter Fehler
    } catch (error) {
      console.log("Fehler: " + error.message);
    } finally {
      console.log("Verbindung zur Datenbank wird geschlossen.");
    }
  }
  
  datenbankZugriff();
  ```

## 6.1.5 Warum sollte man den finally-Block verwenden?

Der `finally`-Block ist nützlich, um sicherzustellen, dass bestimmte Aktionen unabhängig von Fehlern ausgeführt werden, wie z.B. das Schließen von Ressourcen.

**Beispiele:**

- Beispiel 1: 
  ```javascript
  function datenVerarbeiten() {
    try {
      // Code, der fehlerhaft sein könnte
      console.log("Daten werden verarbeitet...");
      throw new Error("Fehler bei der Datenverarbeitung");
    } catch (error) {
      console.log(error.message);
    } finally {
      console.log("Verbindung zur Datenbank wird geschlossen.");
    }
  }

  datenVerarbeiten();
  ```

- Beispiel 2: Log-Ausgabe nach einem Versuch, selbst bei Erfolg
  ```javascript
  try {
    console.log("Berechnung wird durchgeführt.");
  } finally {
    console.log("Der finally-Block wird immer ausgeführt, unabhängig vom Erfolg.");
  }
  ```

## 6.1.6 Die throw-Anweisung und benutzerdefinierte Fehler

Mit `throw` können Sie eigene Fehler definieren und auslösen, um spezifische Bedingungen zu signalisieren.

**Syntax:**
```javascript
throw new Error("Fehlermeldung");
```

**Beispiele:**

- Beispiel 1: Benutzerdefinierter Fehler bei ungültigem Benutzer
  ```javascript
  function checkBenutzer(name) {
    if (!name) {
      throw new Error("Name darf nicht leer sein.");
    }
    console.log("Benutzername: " + name);
  }

  try {
    checkBenutzer("");  // Löst den Fehler aus
  } catch (error) {
    console.log("Fehler: " + error.message);  // Ausgabe: Fehler: Name darf nicht leer sein.
  }
  ```

- Beispiel 2: Fehlerauslösung bei einer ungültigen Zahl
  ```javascript
  function validateNumber(num) {
    if (typeof num !== 'number') {
      throw new TypeError("Die Eingabe muss eine Zahl sein.");
    }
    console.log("Die Zahl ist gültig.");
  }

  try {
    validateNumber("fünf");  // Löst den Fehler aus
  } catch (error) {
    console.log("Fehler: " + error.message);  // Ausgabe: Fehler: Die Eingabe muss eine Zahl sein.
  }
  ```
- Beispiel 3:
  ```javascript
    function checkAlter(alter) {
    if (alter < 18) {
      throw new Error("Das Alter muss mindestens 18 sein.");
    } else {
      console.log("Zugriff gewährt.");
    }
  }

  try {
    checkAlter(16);
  } catch (error) {
    console.log("Fehler: " + error.message);
  }
  ```
