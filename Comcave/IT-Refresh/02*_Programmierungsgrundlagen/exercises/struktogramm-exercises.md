## Übungsaufgaben: Komplexe Struktogramme

### **Problemstellung 1: Login-Versuche**
**Situation:** Ein Benutzer soll sich mit einem Passwort anmelden. Aus Sicherheitsgründen hat er dafür aber nur **drei Versuche**.

**Aufgabe:** Entwirf einen Algorithmus, der den Benutzer nach einem Passwort fragt. Wenn das Passwort falsch ist, soll die Anzahl der verbleibenden Versuche ausgegeben und die Abfrage wiederholt werden. Wenn das Passwort korrekt ist oder die drei Versuche aufgebraucht sind, soll das Programm mit einer entsprechenden Erfolgs- oder Fehlermeldung beendet werden. Das korrekte Pass

---
### **Problemstellung 2: Notendurchschnitt mit Validierung**
**Situation:** Ein Lehrer möchte den Notendurchschnitt seiner Klasse berechnen. Er möchte die Noten nacheinander eingeben. Das Programm soll dabei ungültige Noten (kleiner als 1 oder größer als 6) erkennen und ignorieren. Die Eingabe soll beendet werden, wenn der Lehrer die Zahl `0` eingibt.

**Aufgabe:** Erstelle ein Struktogramm für ein Programm, das Noten entgegennimmt, bis eine `0` eingegeben wird. Ungültige Noten sollen mit einer Fehlermeldung übersprungen werden. Am Ende soll der Durchschnitt der gültigen Noten berechnet und ausgegeben werden. Es muss auch der Fall bedacht werden, dass gar keine gültige Note eingegeben wurde.

---
### **Problemstellung 3: Einfacher Warenkorb**
**Situation:** Ein Kunde in einem kleinen Online-Shop legt Artikel in seinen Warenkorb, indem er nacheinander deren Preise eingibt. Wenn er fertig ist, gibt er eine `0` ein, um zum Bezahlvorgang zu gelangen. Der Shop bietet einen Rabatt von 10% an, wenn der Gesamtwert aller Artikel 100€ übersteigt.

**Aufgabe:** Modelliere den gesamten Prozess als Struktogramm. Der Algorithmus soll Preise sammeln, bis die Eingabe beendet wird. Anschließend soll er prüfen, ob ein Rabatt gewährt wird, den Endpreis berechnen und eine finale Abrechnung (Zwischensumme, Rabatt, Endpreis) ausgeben.


---
---

## Lösungen

### **Lösung zu Problemstellung 1: Login-Versuche**

Das Struktogramm kombiniert eine Schleife mit einer Zählvariable und einer finalen Überprüfung nach der Schleife.

**Beschreibung des Struktogramms:**
1.  **Anweisungs-Block (Sequenz):**
    * `SETZE versuche AUF 0`
    * `SETZE login_erfolgreich AUF FALSCH`
2.  **Kopfgesteuerte Schleife (while):**
    * **Bedingung:** `versuche < 3 UND login_erfolgreich == FALSCH`
    * **Schleifenkörper:**
        * Anweisung: `EINGABE von passwort`
        * **Verzweigungs-Block (if-else):**
            * **Bedingung:** `passwort == "Admin123"`
            * **Ja-Zweig:** Anweisung: `SETZE login_erfolgreich AUF WAHR`
            * **Nein-Zweig:** Anweisung: `SETZE versuche AUF versuche + 1`
3.  **Verzweigungs-Block (if-else) nach der Schleife:**
    * **Bedingung:** `login_erfolgreich == WAHR`
    * **Ja-Zweig:** Anweisung: `AUSGABE von "Login erfolgreich!"`
    * **Nein-Zweig:** Anweisung: `AUSGABE von "Zu viele Fehlversuche. Zugang gesperrt."`

---
### **Lösung zu Problemstellung 2: Notendurchschnitt mit Validierung**

Dieses Struktogramm nutzt eine Endlosschleife mit `break` und `continue` (realisiert durch `if-else`) und einer finalen Prüfung gegen Division durch Null.

**Beschreibung des Struktogramms:**
1.  **Anweisungs-Block (Sequenz):**
    * `SETZE summe_noten AUF 0`
    * `SETZE anzahl_noten AUF 0`
2.  **Kopfgesteuerte Schleife (while):**
    * **Bedingung:** `WAHR` (Dies erzeugt eine Endlosschleife)
    * **Schleifenkörper:**
        * Anweisung: `EINGABE von note`
        * **Verzweigungs-Block (if-else):**
            * **Bedingung:** `note == 0`
            * **Ja-Zweig:** Anweisung: `SCHLEIFE VERLASSEN` (break)
            * **Nein-Zweig:**
                * **Innerer Verzweigungs-Block (if-else):**
                    * **Bedingung:** `note >= 1 UND note <= 6`
                    * **Ja-Zweig:**
                        * Anweisung: `SETZE summe_noten AUF summe_noten + note`
                        * Anweisung: `SETZE anzahl_noten AUF anzahl_noten + 1`
                    * **Nein-Zweig:** Anweisung: `AUSGABE von "Ungültige Note!"`
3.  **Verzweigungs-Block (if-else) nach der Schleife:**
    * **Bedingung:** `anzahl_noten > 0`
    * **Ja-Zweig:**
        * Anweisung: `SETZE durchschnitt AUF summe_noten / anzahl_noten`
        * Anweisung: `AUSGABE von "Durchschnitt: " + durchschnitt`
    * **Nein-Zweig:** Anweisung: `AUSGABE von "Keine gültigen Noten eingegeben."`

---
### **Lösung zu Problemstellung 3: Einfacher Warenkorb**

Dieses Struktogramm ist dem Verkaufsautomaten sehr ähnlich. Es sammelt Daten in einer Schleife und verarbeitet das Ergebnis danach.

**Beschreibung des Struktogramms:**
1.  **Anweisungs-Block (Sequenz):**
    * `SETZE gesamtsumme AUF 0`
2.  **Kopfgesteuerte Schleife (while):**
    * **Bedingung:** `WAHR`
    * **Schleifenkörper:**
        * Anweisung: `EINGABE von preis`
        * **Verzweigungs-Block (nur if):**
            * **Bedingung:** `preis == 0`
            * **Ja-Zweig:** Anweisung: `SCHLEIFE VERLASSEN` (break)
        * Anweisung: `SETZE gesamtsumme AUF gesamtsumme + preis`
3.  **Anweisungs-Block (Sequenz) nach der Schleife:**
    * `AUSGABE von "Zwischensumme: " + gesamtsumme`
4.  **Verzweigungs-Block (if-else):**
    * **Bedingung:** `gesamtsumme > 100`
    * **Ja-Zweig:**
        * Anweisung: `SETZE rabatt AUF gesamtsumme * 0.10`
        * Anweisung: `SETZE endpreis AUF gesamtsumme - rabatt`
        * Anweisung: `AUSGABE von "Rabatt (10%): " + rabatt`
    * **Nein-Zweig:**
        * Anweisung: `SETZE endpreis AUF gesamtsumme`
5.  **Anweisungs-Block (Sequenz):**
    * `AUSGABE von "Endpreis: " + endpreis`