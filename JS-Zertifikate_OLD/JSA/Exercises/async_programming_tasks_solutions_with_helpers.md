# Aufgaben zu Asynchronem Programmieren in JavaScript

### Übungsaufgaben
**Aufgabe 1:** Erstelle eine Funktion `fetchData`, die eine HTTP-Anfrage simuliert und nach 2 Sekunden eine zufällige Zahl zurückgibt. Verwende `setTimeout`. Überprüfe das Ergebnis mit einer Callback-Funktion.

**Aufgabe 2:** Erstelle eine Funktion `waitAndGreet`, die nach einer Verzögerung von 3 Sekunden einen Namen entgegennimmt und eine Begrüßung zurückgibt. Verwende Promises und nutze `then`, um die Begrüßung anzuzeigen.

**Aufgabe 3:** Schreibe eine Funktion, die eine zufällige Zahl als Promise zurückgibt. Verwende `async` und `await`, um die Zahl abzurufen und sie im Konsolenlog auszugeben.

**Aufgabe 4:** Implementiere eine Funktion `loadData`, die nacheinander drei asynchrone Aufgaben ausführt: Daten abrufen, verarbeiten und anzeigen. Verwende Promises und `async/await`, um sicherzustellen, dass jede Aufgabe auf die vorherige wartet.

**Aufgabe 5:** Erstelle eine Funktion `calculateSumAsync`, die zwei Zahlen asynchron addiert und das Ergebnis zurückgibt. Verwende `Promise`. Nutze `async/await`, um das Ergebnis der Summe zu erhalten.

**Aufgabe 6:** Schreibe eine Funktion, die eine Reihe von Nachrichten nacheinander ausgibt, indem du `setTimeout` in einer Schleife mit steigender Verzögerung verwendest. Verwende `Promise` und `async/await`, um die Nachrichten mit der Verzögerung anzuzeigen.

**Aufgabe 7:** Erstelle eine Funktion `delayedMultiply`, die zwei Zahlen akzeptiert, nach 2 Sekunden deren Produkt zurückgibt und einen Fehler erzeugt, wenn eine Eingabe keine Zahl ist. Verwende Promises und `catch`, um den Fehler zu behandeln.

**Aufgabe 8:** Erstelle eine `async` Funktion `retryFetch` die bis zu dreimal eine fehlerhafte HTTP-Anfrage wiederholt und dann entweder das Ergebnis oder eine Fehlermeldung zurückgibt.

**Aufgabe 9:** Erstelle eine Funktion `parallelFetch` die drei simulierte HTTP-Anfragen parallel ausführt und die Ergebnisse in einem Array zurückgibt. Verwende Promises und `Promise.all`.

**Aufgabe 10:** Schreibe eine Funktion, die eine asynchrone Operation wiederholt, bis eine Bedingung erfüllt ist (z.B. eine Zahl über 90 erzeugt). Verwende `async` und `await` für die Wiederholung.

**Aufgabe 11:** Erstelle eine `fetchAndProcessData` Funktion, die Daten aus einer API abruft und verarbeitet, aber einen Fehler wirft, wenn die Daten leer sind. Verwende `try/catch`, um den Fehler abzufangen und eine Nachricht im Fehlerfall anzuzeigen.

**Aufgabe 12:** Erstelle eine `fetchDataWithTimeout` Funktion, die nach 3 Sekunden abbricht, wenn keine Antwort von einer HTTP-Anfrage vorliegt. Verwende Promises, `setTimeout` und `Promise.race`.


---

### Hilfsfunktionen

```javascript
// Simulierte asynchrone Funktionen zur Verwendung in den Aufgaben

// Simuliert eine Datenanforderung mit einer zufälligen Zahl als Ergebnis
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simuliere Erfolg oder Fehler mit 80% Wahrscheinlichkeit auf Erfolg
            Math.random() > 0.2 ? resolve(Math.random()) : reject("Fehler: Netzwerkfehler");
        }, 1000);
    });
}

// Simuliert die Verarbeitung von Daten
function processData(data) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(`Verarbeitete Daten: ${data}`), 1000);
    });
}

// Simuliert die Anzeige von Daten
function displayData(data) {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(data);
            resolve("Angezeigt");
        }, 500);
    });
}

// Simuliert eine Funktion zur Erzeugung einer Zufallszahl
function getRandomNumber() {
    return new Promise((resolve) => {
        setTimeout(() => resolve(Math.floor(Math.random() * 100)), 500);
    });
}
```


---

### Lösungen
**Lösung zu Aufgabe 1:**

```javascript
function fetchData(callback) { setTimeout(() => { callback(Math.random()); }, 2000); } fetchData(result => console.log(result));
```

**Lösung zu Aufgabe 2:**

```javascript
function waitAndGreet(name) { return new Promise(resolve => { setTimeout(() => resolve(`Hallo, ${name}!`), 3000); }); } waitAndGreet('Max').then(console.log);
```

**Lösung zu Aufgabe 3:**

```javascript
async function getRandomNumber() { const number = await new Promise(resolve => resolve(Math.random())); console.log(number); } getRandomNumber();
```

**Lösung zu Aufgabe 4:**

```javascript
async function loadData() { await fetchData(); await processData(); await displayData(); } loadData();
```

**Lösung zu Aufgabe 5:**

```javascript
function calculateSumAsync(a, b) { return new Promise(resolve => resolve(a + b)); } async function sum() { const result = await calculateSumAsync(5, 7); console.log(result); } sum();
```

**Lösung zu Aufgabe 6:**

```javascript
async function sequentialMessages() { for (let i = 1; i <= 3; i++) { await new Promise(resolve => setTimeout(resolve, i * 1000)); console.log(`Message ${i}`); } } sequentialMessages();
```

**Lösung zu Aufgabe 7:**

```javascript
function delayedMultiply(a, b) { return new Promise((resolve, reject) => { if (typeof a === 'number' && typeof b === 'number') { setTimeout(() => resolve(a * b), 2000); } else { reject('Invalid input'); } }); } delayedMultiply(3, 4).then(console.log).catch(console.error);
```

**Lösung zu Aufgabe 8:**

```javascript
async function retryFetch() { for (let i = 0; i < 3; i++) { try { return await fetchData(); } catch (error) { console.log(`Attempt ${i + 1} failed`); } } throw new Error('All attempts failed'); }
```

**Lösung zu Aufgabe 9:**

```javascript
function parallelFetch() { return Promise.all([fetchData(), fetchData(), fetchData()]).then(console.log); }
```

**Lösung zu Aufgabe 10:**

```javascript
async function repeatUntilCondition() { let number; do { number = await getRandomNumber(); console.log(number); } while (number <= 90); } repeatUntilCondition();
```

**Lösung zu Aufgabe 11:**

```javascript
async function fetchAndProcessData() { try { const data = await fetchData(); if (!data) throw new Error('No data'); process(data); } catch (error) { console.error('Error:', error.message); } }
```

**Lösung zu Aufgabe 12:**

```javascript
function fetchDataWithTimeout() { const fetchPromise = fetchData(); const timeoutPromise = new Promise((_, reject) => setTimeout(() => reject('Timeout'), 3000)); return Promise.race([fetchPromise, timeoutPromise]); } fetchDataWithTimeout().catch(console.error);
```

