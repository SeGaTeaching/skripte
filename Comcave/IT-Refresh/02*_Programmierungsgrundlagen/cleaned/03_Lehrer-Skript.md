
## 🏗️ **KAPITEL 3: Struktogramme (Nassi-Shneiderman-Diagramme)**

*(Geschätzte Dauer: 1 voller Unterrichtstag)*

-----

### **📝 SKRIPT (für Präsentation / Notebook)**

#### **3.1 Was ist ein Struktogramm?**

Nachdem wir unsere Logik als textuellen Pseudocode geplant haben, nutzen wir nun eine visuelle Methode: das **Struktogramm**.

**Analogie: Der LEGO®-Bauplan**
Stellt euch vor, Pseudocode ist eine textliche Bauanleitung. Ein Struktogramm ist der dazugehörige Bauplan aus LEGO®-Steinen. Jeder Baustein (Sequenz, Verzweigung, Schleife) hat eine feste Form und kann nur auf logisch sinnvolle Weise mit anderen Bausteinen zusammengesteckt werden. Das verhindert von Anfang an chaotische Konstruktionen ("Spaghetti-Code").

**Definition**
Ein Struktogramm (nach Nassi-Shneiderman) ist eine grafische Darstellung eines Algorithmus, die vollständig auf Verbindungspfeile verzichtet. Der gesamte Algorithmus wird als ein großes Rechteck dargestellt, das in kleinere Blöcke für die einzelnen logischen Schritte unterteilt wird.

#### **3.2 Die Bausteine eines Struktogramms**

Jede logische Struktur hat ihre eigene, feste Form.

| Baustein | Form | Beschreibung |
| :--- | :--- | :--- |
| **Sequenz** | ▭ | Ein einfaches Rechteck für eine oder mehrere nacheinander auszuführende Anweisungen. |
| **Selektion (Wenn-Dann)** | ◸...◹ | Ein Block mit der Bedingung oben und dem "Ja"-Zweig darunter. |
| **Selektion (Wenn-Dann-Sonst)** | ◸...◹\<br\>◺...◿ | Wie oben, aber mit einem zusätzlichen "Nein"-Zweig. |
| **Fallauswahl (Switch)** | ◫ | Ein mehrfach geteilter Block für eine `switch-case`-Anweisung. |
| **Kopfgesteuerte Schleife (While)** | ⫢ | Die Schleifenbedingung steht oben. Der innere Block wird wiederholt, solange die Bedingung wahr ist. |
| **Fußgesteuerte Schleife (Do-While)** | ⫣ | Der innere Block wird mindestens einmal ausgeführt, bevor die Bedingung am Ende geprüft wird. |

-----

> ### 👨‍🏫 **VISUALISIERUNG & DEMO (Live via Teams)**
>
> #### **Tool-Empfehlung**
>
> Für die Erstellung von Struktogrammen ist der **Struktog-Editor** ideal.
>
>   * **Webseite:** [https://struktog.de](https://www.google.com/search?q=https://struktog.de)
>   * **Warum?** Es ist ein kostenloses, online-basiertes Tool, das speziell für diesen Zweck entwickelt wurde. Es bietet die korrekten Blöcke an und zwingt dich dazu, die Regeln einzuhalten, was didaktisch sehr wertvoll ist. Du kannst deine erstellten Diagramme als Bild exportieren.
>
> **Dein Vorgehen im Unterricht:**
> Teile deinen Bildschirm mit dem geöffneten Struktog-Editor und baue die folgenden Beispiele live mit den Schülern zusammen.
>
> -----
>
> #### **Beispiel 1: Ticketpreis-Kalkulator (Sequenz & Selektion)**
>
> **Anleitung zur Erstellung im Struktog-Editor:**
>
> 1.  Füge einen neuen Anweisungs-Block (Sequenz) ein für die Eingabe: `EINGABE von alter`.
> 2.  Füge darunter einen Verzweigungs-Block (Selektion `if-else`) ein.
> 3.  Trage in das Bedingungsfeld der Verzweigung ein: `alter < 16 ODER alter >= 65`.
> 4.  Klicke in den "Ja"-Zweig (links) und füge eine Anweisung ein: `SETZE preis AUF 9.00`.
> 5.  Klicke in den "Nein"-Zweig (rechts) und füge eine Anweisung ein: `SETZE preis AUF 12.00`.
> 6.  Füge unterhalb des gesamten Verzweigungs-Blocks eine letzte Anweisung ein: `AUSGABE von preis`.
>
> -----
>
> #### **Beispiel 2: Notendurchschnitt (Sequenz & Schleife)**
>
> **Anleitung zur Erstellung im Struktog-Editor:**
>
> 1.  Beginne mit zwei Anweisungen in einem Sequenz-Block: `SETZE notenliste AUF [...]` und `SETZE gesamtsumme AUF 0`.
> 2.  Füge darunter eine kopfgesteuerte Schleife (`while` oder `for-each`) ein.
> 3.  Trage in den Schleifenkopf ein: `FÜR jede note IN notenliste`.
> 4.  Klicke in den Körper der Schleife und füge die Anweisung ein: `SETZE gesamtsumme AUF gesamtsumme + note`.
> 5.  Füge nach der Schleife einen weiteren Sequenz-Block mit den letzten beiden Anweisungen ein: `SETZE anzahl AUF ...` und `SETZE durchschnitt AUF ...`.
> 6.  Beende mit der Anweisung `AUSGABE von durchschnitt`.
>
> -----
>
> #### **Beispiel 3: FizzBuzz (Verschachtelte Logik)**
>
> **Anleitung zur Erstellung im Struktog-Editor:**
>
> 1.  Füge eine `for`-Schleife als äußersten Block ein. Bedingung: `FÜR zahl VON 1 BIS 100`.
> 2.  Klicke in den Körper der `for`-Schleife und füge dort eine `if-else`-Verzweigung ein.
> 3.  Bedingung für diese erste Verzweigung: `zahl durch 3 teilbar UND zahl durch 5 teilbar`.
> 4.  Fülle den "Ja"-Zweig mit der Anweisung: `AUSGABE von "FizzBuzz"`.
> 5.  Klicke nun in den "Nein"-Zweig. Füge hier eine **weitere, verschachtelte `if-else`-Verzweigung** ein.
> 6.  Bedingung für die zweite Verzweigung: `zahl durch 3 teilbar`.
> 7.  Fülle den "Ja"-Zweig mit `AUSGABE von "Fizz"` und den "Nein"-Zweig mit einer **dritten, verschachtelten `if-else`-Verzweigung**.
> 8.  Bedingung für die dritte Verzweigung: `zahl durch 5 teilbar`.
> 9.  Fülle deren "Ja"-Zweig mit `AUSGABE von "Buzz"` und den "Nein"-Zweig mit `AUSGABE von zahl`.

-----

> ### 🗣️ **MANUSKRIPT LEHRER (Stichpunkte)**
>
>   * **Einstieg & Analogie:**
>
>       * "Wir haben unsere Pläne als Text geschrieben. Aber ein Bild sagt mehr als tausend Worte. Stellen wir uns vor, wir bauen mit LEGO. Ein Struktogramm gibt uns feste Bausteine, die nur auf eine logische Weise zusammenpassen."
>
>   * **Tool-Vorstellung:**
>
>       * Zeige die Webseite `struktog.de`.
>       * *Kernbotschaft:* "Dieses Tool ist unser Sicherheitsnetz. Es lässt uns gar nicht erst unstrukturierte, chaotische Pläne erstellen. Wir sind gezwungen, sauber zu arbeiten."
>
>   * **Live-Demos:**
>
>       * Führe die Schüler durch die Erstellung der Beispiele. Kommentiere jeden Klick.
>       * *Interaktion:* "Für die Altersprüfung, welchen Baustein brauchen wir jetzt?" -\> "Richtig, eine Verzweigung." "Und was kommt in die Bedingung?"
>       * Betone bei FizzBuzz: "Seht ihr, wie wir die Entscheidungen ineinander schachteln? Das Diagramm macht die Hierarchie der Logik sofort sichtbar."
>
>   * **Überleitung:**
>
>       * "Struktogramme sind fantastisch, um die logische Struktur zu erzwingen. Manchmal will man aber den allgemeinen *Fluss* eines Programms darstellen, vielleicht auch mit Sprüngen oder parallelen Pfaden. Dafür gibt es eine zweite, flexiblere Methode, die wir uns als Nächstes ansehen: den Programmablaufplan."