
# JavaScript Debugging und Testen

## Einführung in das Debugging von JavaScript-Code

JavaScript bietet zahlreiche Werkzeuge zur Analyse und Behebung von Fehlern. Das folgende Beispiel nutzt ein einfaches Programm mit mehreren Funktionen und zeigt, wie man den Code Schritt für Schritt debuggen kann. 

Das Beispiel-HTML-Dokument enthält JavaScript-Code, der drei Funktionen definiert und den Debugging-Prozess demonstriert.

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>JavaScript Debugging Beispiele</title>
</head>
<body>
  <h1>JavaScript Debugging</h1>
  <p>Öffne die Entwicklertools und gehe Schritt für Schritt durch den Code.</p>

  <script>
    function addiere(a, b) {
      debugger;  // Halte hier an, um die Parameterwerte zu prüfen
      return a + b;
    }

    function berechneQuadrat(x) {
      let ergebnis = x * x;
      debugger;  // Halte hier an, um das Ergebnis zu prüfen
      return ergebnis;
    }

    function hauptfunktion() {
      console.log("Programm gestartet");
      let zahl1 = 3;
      let zahl2 = 4;
      let summe = addiere(zahl1, zahl2); // Step into, um in die Funktion zu gehen
      let quadrat = berechneQuadrat(summe); // Step over, um zur nächsten Zeile zu springen
      console.log("Quadrat der Summe: " + quadrat);
      debugger;  // Halte hier an, um den Call Stack zu prüfen
    }

    hauptfunktion(); // Starte die Programmausführung

  </script>
</body>
</html>
```

## Erklärung der Debugging-Schritte anhand des Beispiels

### 6.2.1 Testen und Debuggen des Codes
   - **Konsole verwenden**: Öffne die Konsole, um sicherzustellen, dass „Programm gestartet“ korrekt ausgegeben wird.
   - **Breakpoints setzen**: Der `debugger`-Befehl in der Funktion `addiere` hält das Programm an, bevor die Addition ausgeführt wird, sodass du die Werte von `a` und `b` überprüfen kannst.

### 6.2.2 Debugging
   - Gehe in den „Sources“-Tab der Entwicklertools und finde die JavaScript-Datei. Der `debugger`-Befehl in `berechneQuadrat` stoppt die Ausführung, sodass du überprüfen kannst, ob die Berechnung des Quadrats korrekt ist.

### 6.2.3 Schrittweise Programmausführung
   - Verwende „Step over“ auf den Zeilen `let summe = addiere(zahl1, zahl2);` und `let quadrat = berechneQuadrat(summe);`, um die Funktionsaufrufe Schritt für Schritt zu beobachten, ohne in die Funktionen hineinzugehen.

### 6.2.4 Vorbereitung der Umgebung und ein Beispiel
   - Bereite das HTML-Dokument vor und öffne die Entwicklertools. Nutze die „Console“ und den „Sources“-Tab, um den Code zu untersuchen.

### 6.2.5 Verwendung des `debugger`-Statements
   - **Debugging** der Funktion `addiere`:
     - Wenn das Programm an der Zeile `debugger;` anhält, überprüfe die Variablenwerte `a` und `b`.
     - Dies hilft sicherzustellen, dass die Funktion die erwarteten Eingaben verarbeitet.
   
   - **Debugging** der Funktion `berechneQuadrat`:
     - Nachdem die Addition abgeschlossen ist, überprüft der nächste `debugger`-Stopp die Variable `ergebnis` nach der Berechnung des Quadrats.

### 6.2.6 Fortsetzen der Ausführung
   - Nach der Überprüfung der Variablenwerte kannst du die Ausführung fortsetzen, indem du auf „Resume“ klickst. Das Programm läuft weiter bis zum nächsten `debugger`-Statement.

### 6.2.7 Arbeiten ohne das `debugger`-Statement
   - Setze manuell Breakpoints, indem du auf die Zeilennummern im „Sources“-Tab klickst. Dies ist hilfreich, wenn du bestimmte Zeilen überprüfen möchtest, ohne den `debugger`-Befehl direkt in den Code zu schreiben.

### 6.2.8 Step over
   - „Step over“ springt über die Funktion `berechneQuadrat`, sodass du zur nächsten Zeile gelangen kannst, ohne in die Berechnung selbst hineinzugehen. Dies ist hilfreich, wenn du nur das Endergebnis überprüfen möchtest.

### 6.2.9 Step into
   - Verwende „Step into“ bei `addiere(zahl1, zahl2)`, um in die Funktion `addiere` zu gelangen und die Details der Berechnung zu beobachten.

### 6.2.10 Call stack
   - Der `debugger`-Befehl im letzten Teil der `hauptfunktion` stoppt das Programm. Der „Call stack“ zeigt dir, dass die `hauptfunktion` die `addiere`- und `berechneQuadrat`-Funktionen aufgerufen hat.
   - So kannst du nachvollziehen, wie der Programmfluss durch die Funktionen geführt wurde.

### 6.2.11 Step out
   - Wenn du in der Funktion `addiere` oder `berechneQuadrat` bist, kannst du „Step out“ verwenden, um zur aufrufenden Funktion zurückzukehren und die restlichen Teile der `hauptfunktion` auszuführen.

## Beispiel-Debugging im Browser

1. **HTML-Datei öffnen**: Lade die Datei im Browser und öffne die Entwicklertools.
2. **Debugger nutzen**: Verwende die Schritte, um durch den Code zu navigieren und die Werte der Variablen und den Programmfluss zu beobachten.
3. **Konsole beobachten**: Verwende `console.log()`-Ausgaben, um sicherzustellen, dass die Ausgaben korrekt sind und der Ablauf dem erwarteten entspricht.

Diese Vorgehensweise ermöglicht ein tiefes Verständnis für das Debuggen und die Funktion der einzelnen Befehle. Viel Erfolg beim Erklären im Unterricht!
