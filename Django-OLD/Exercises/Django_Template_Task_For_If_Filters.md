
# Aufgabe: Anwenden von For Loops, If Statements und Filtern in Django Templates

## Aufgabe
Erstelle eine Django-Webseite, die eine Liste von Büchern mit ihren Titeln, Autoren und Erscheinungsjahren anzeigt. Die Webseite soll folgende Anforderungen erfüllen:

1. **Daten filtern**: 
   - Titel der Bücher sollen in **Großbuchstaben** angezeigt werden.
   - Autoren sollen im **Title Case** formatiert werden.

2. **Jahre anzeigen**:
   - Zeige nur Bücher an, die nach dem Jahr 2000 veröffentlicht wurden.

3. **Zählen**:
   - Zähle die Anzahl der Bücher, die die Bedingung erfüllen, und zeige sie am Anfang der Liste an.

4. **Zusätzliche Informationen**:
   - Wenn kein Buch angezeigt werden kann, soll eine Meldung wie „Keine Bücher verfügbar“ erscheinen.

---

## Vorgaben
Die Daten sind vorgegeben und sollen in der View bereitgestellt werden:

### **Code für `views.py`**
```python
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        {"title": "The Road", "author": "Cormac McCarthy", "year": 2006},
        {"title": "The Hunger Games", "author": "Suzanne Collins", "year": 2008},
        {"title": "Normal People", "author": "Sally Rooney", "year": 2018},
    ]
```

---

## Anforderungen an das Template
Das Template `books.html` soll folgende Logik umsetzen:

1. **Titel formatieren**: Verwende den `upper`-Filter, um Titel in Großbuchstaben anzuzeigen.
2. **Autoren formatieren**: Verwende den `title`-Filter, um die Namen der Autoren zu formatieren.
3. **Bedingung**: Nutze ein `{% if %}`-Statement, um Bücher nach 2000 zu filtern.
4. **Schleife**: Verwende `{% for %}`, um durch die Bücherliste zu iterieren.
5. **Zusammenfassung**: Zeige die Anzahl der Bücher, die angezeigt werden, mit dem `length`-Filter an.

---

## Beispiel für die HTML-Ausgabe
Die folgende Ausgabe wird bei korrekt umgesetzter Lösung erwartet:

### **Wenn Bücher vorhanden sind:**
```
Gefundene Bücher: 3
- THE ROAD von Cormac McCarthy (2006)
- THE HUNGER GAMES von Suzanne Collins (2008)
- NORMAL PEOPLE von Sally Rooney (2018)
```

### **Wenn keine Bücher gefunden werden (z.B., wenn alle nach 2020 veröffentlicht wären):**
```
Keine Bücher verfügbar.
```

---

## Hinweise
- Nutze `{% for %}`- und `{% if %}`-Statements, um die Daten zu filtern und darzustellen.
- Wende die Filter wie `upper`, `title` und `length` an.
- Die Datenstruktur (`books`) ist vorgegeben; finde heraus, wie du auf die Attribute zugreifen kannst.

---

## Aufgabe: Template erstellen
Erstelle ein Template `books.html`, das die oben beschriebenen Anforderungen erfüllt.

---

## URL-Konfiguration
Stelle sicher, dass deine View in der `urls.py` konfiguriert ist:
```python
from django.urls import path
from .views import books_view

urlpatterns = [
    path('books/', books_view, name='books'),
]
```

---

### Viel Erfolg!
