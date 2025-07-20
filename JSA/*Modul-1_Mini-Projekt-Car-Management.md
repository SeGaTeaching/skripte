# Mini-Projekt: Fahrzeugverwaltungssystem

## Ziel des Projekts

In diesem Mini-Projekt entwickelst du ein einfaches, aber strukturiertes **Fahrzeugverwaltungssystem** in JavaScript. Ziel ist es, die bisher erlernten Konzepte zur Objekterstellung, Methodendefinition, Vererbung, Zugriffskontrolle und Datenkapselung **in einem praxisnahen Szenario** umzusetzen.

Du wirst:
- mehrere Fahrzeuge als Objekte modellieren,
- Methoden definieren, die spezifisches Verhalten abbilden,
- zwischen allgemeinen und spezialisierten Eigenschaften unterscheiden,
- mindestens eine Vererbungsstruktur abbilden,
- zwischen verschiedenen Erzeugungsmethoden bewusst wählen (Factory, Literal, `Object.create`, etc.),
- Konzepte wie `this`, Getter/Setter und Property Attributes reflektieren und ggf. gezielt einsetzen.

---

## Rahmenbedingungen

Das Mini-Projekt ist **nicht als Copy-Paste-Aufgabe** gedacht. Stattdessen sollst du bewusst designen, planen und implementieren. Du entscheidest, **welche Konstrukte du einsetzt und warum**.

Die Umsetzung erfolgt **in mehreren Phasen**, die du Schritt für Schritt erarbeiten und dokumentieren kannst.

---

## Projektszenario

Stell dir vor, du sollst ein kleines Verwaltungssystem für einen Fuhrpark entwickeln. Der Fuhrpark besteht aus verschiedenen Fahrzeugtypen (z. B. Autos, LKWs, Fahrräder), die jeweils bestimmte Eigenschaften und Methoden besitzen.

### Beispieleigenschaften (Daten):
- Hersteller / Marke
- Baujahr
- Kilometerstand
- Betriebsbereit: true/false
- Kraftstofftyp / elektrische Reichweite

### Beispielspezifische Methoden (Verhalten):
- `start()` – gibt eine Startmeldung aus
- `inspect()` – gibt Fahrzeugstatus zurück
- `drive(km)` – erhöht den Kilometerstand

Es können allgemeine Methoden für alle Fahrzeuge existieren – aber auch spezialisierte pro Typ.

---

## Projektaufgaben

### Phase 1: Grundstruktur mit Objektliteralen
- Erstelle mindestens **zwei Fahrzeuge** als Objektliteral (z. B. Auto und Fahrrad).
- Gib jedem Objekt sinnvolle Eigenschaften und mindestens **eine Methode**.
- Nutze `this` korrekt innerhalb der Methoden.

### Phase 2: Factory Function oder `Object.create`
- Erstelle eine **Factory Function** oder verwende `Object.create()` für wiederverwendbare Objekterzeugung.
- Erzeuge mindestens **drei Fahrzeuge** mit dieser Technik.
- Dokumentiere Unterschiede zur Objektliteral-Methode.

### Phase 3: Zugriff kontrollieren
- Verwende bei mindestens einem Fahrzeug **Getter und/oder Setter** für abgeleitete oder geschützte Werte (z. B. Reichweite).
- Nutze bei einem Objekt bewusst `Object.defineProperty()` oder `Object.freeze()`.

### Phase 4: Erweiterung durch Vererbung
- Baue ein Vererbungskonzept:
  - Ein generisches `Vehicle`-Objekt mit Standardmethoden.
  - Spezifische Fahrzeuge (z. B. `Car`, `Truck`) erben davon.
- Entscheide selbst, ob du `Object.create`, Prototypen oder `class`/`extends` nutzt.

---

## Erweiterungsideen

- Plane Tankvorgänge oder Serviceintervalle ein.
- Implementiere eine kleine Sammlung (Array) und filtere Fahrzeuge nach Zustand.
- Speichere Fahrzeuge sortiert nach Typ in einem Objekt oder per Map.
- Implementiere ein einfaches „Kilometerlimit“ (z. B. für Leasingfahrzeuge).

---

## Lernziele

Dieses Mini-Projekt hilft dir, die folgenden Konzepte praktisch zu festigen:
- Objekterstellungstechniken in JavaScript
- Verwendung von `this` in Methoden
- Nutzung von Prototypen und Vererbung
- Getter/Setter, Property Attributes, Zugriffsschutz
- Strukturierte Planung eines objektorientierten Entwurfs

---

## Hinweise zur Bearbeitung

- Das Projekt ist **nicht als reine Codelösung** gedacht.
- Du sollst **eigene Designentscheidungen treffen** und bewusst reflektieren.
- Der Fokus liegt auf **tieferem Verständnis**, nicht auf möglichst kurzer Umsetzung.

👉 Viel Erfolg – und denke daran: Sauberer, strukturierter Code ist genauso wichtig wie funktionierender Code.

