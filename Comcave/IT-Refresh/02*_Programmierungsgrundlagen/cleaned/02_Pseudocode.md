02
# ✍️ **Kapitel 2: Pseudocode (Die Brückensprache)**

---

## **2.1 Was ist Pseudocode und warum ist er nützlich?**

Nachdem wir im letzten Kapitel gelernt haben, Probleme logisch zu zerlegen, brauchen wir nun eine Methode, um unsere Lösungspläne aufzuschreiben. Hier kommt der **Pseudocode** ins Spiel.

**Analogie: Das Rezept des Chefkochs**
Ein Gedanke ("Ich will einen Schokoladenkuchen backen") ist noch kein Plan. Ein detailliertes Rezept hingegen schon. Pseudocode ist das Rezept für den Programmierer:

  * Es ist detaillierter und strukturierter als eine bloße Idee.
  * Es ist aber flexibler und verständlicher als eine starre chemische Formel (der finale Programmcode).

**Definition**
Pseudocode ist ein informelles Werkzeug zur Planung von Algorithmen. Er ist eine Brückensprache, eine Kombination aus menschlicher Sprache und Programmiersprache. Ziel ist es, die Logik eines Programms klar und verständlich darzustellen, ohne sich um die exakte Syntax einer bestimmten Programmiersprache kümmern zu müssen.

**Der Nutzen von Pseudocode**

  * **Planung:** Er hilft, komplexe Abläufe zu strukturieren, bevor man programmiert. Logikfehler findet man so viel schneller als im fertigen Code.
  * **Kommunikation:** Er erleichtert die Erklärung von Algorithmen gegenüber Teammitgliedern oder weniger technischen Personen.
  * **Dokumentation:** Guter Pseudocode kann später als Kommentar direkt in den finalen Programmcode übernommen werden und erklärt die Absicht hinter dem Code.

-----

#### **2.2 Unser Pseudocode-Standard**

Es gibt keinen weltweit gültigen Standard für Pseudocode. Für unseren Kurs legen wir aber einen gemeinsamen Stil fest, damit unsere Pläne für jeden im Team klar verständlich sind.

**Unsere Schlüsselwörter (immer in GROSSBUCHSTABEN)**

| Schlüsselwort | Bedeutung |
| :--- | :--- |
| `START` / `ENDE` | Markiert den Anfang und das Ende des Programms. |
| `EINGABE von [Variable]` | Fordert eine Eingabe vom Benutzer an und speichert sie. |
| `AUSGABE von [Variable/Text]`| Gibt einen Wert oder Text auf dem Bildschirm aus. |
| `SETZE [Variable] AUF [Wert]`| Weist einer Variable einen Wert zu. |
| `WENN...DANN...SONST` | Leitet eine bedingte Anweisung ein (`if-else`). |
| `SOLANGE...MACHE` | Leitet eine kopfgesteuerte Schleife ein (`while`). |

**Unsere Grundregeln**

1. **Eine Anweisung pro Zeile:** Jeder Schritt ist eine eigene Zeile.
2. **Einrückungen zeigen Struktur:** Code-Blöcke innerhalb von Bedingungen oder Schleifen werden eingerückt.
3.  **Klartext statt Code:** Wir beschreiben die Logik verständlich.
      * **Gut:** `WENN zahl ungerade ist DANN`
      * **Schlecht:** `WENN zahl % 2 != 0 DANN`

-----

## **2.3 Pseudocode in Aktion**

**Beispiel 1: Einfache Sequenz (Flächenberechnung)**

```
START
  AUSGABE von "Bitte die Höhe des Rechtecks eingeben:"
  EINGABE von hoehe

  AUSGABE von "Bitte die Breite des Rechtecks eingeben:"
  EINGABE von breite

  SETZE flaeche AUF hoehe * breite
  AUSGABE von "Die Fläche beträgt: " + flaeche
ENDE
```

**Beispiel 2: Selektion (Altersprüfung)**

```
START
  AUSGABE von "Bitte gib dein Alter ein:"
  EINGABE von alter

  WENN alter < 18 DANN
    AUSGABE von "Zugang für Minderjährige verweigert."
  SONST
    AUSGABE von "Zugang gewährt."
  ENDEWENN
ENDE
```

**Beispiel 3: Iteration (Countdown)**

```
START
  SETZE zaehler AUF 10

  SOLANGE zaehler > 0 MACHE
    AUSGABE von zaehler
    SETZE zaehler AUF zaehler - 1
  ENDESOLANGE

  AUSGABE von "Start!"
ENDE
```