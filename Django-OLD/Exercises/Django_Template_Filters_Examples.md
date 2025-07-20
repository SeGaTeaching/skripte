
# Django Template Filters: Praxisbeispiele

## 1. Beispiel-Dictionary in der View
Definiere in der View ein Dictionary, das alle benötigten Daten enthält, um die Filterbeispiele im Template darzustellen.

### **Code für `views.py`**
```python
from django.shortcuts import render

def filter_examples_view(request):
    context = {
        "name": "John Doe",
        "items": ["apple", "banana", "cherry"],
        "my_list": ["first_item", "second_item", "third_item"],
        "words": ["Django", "Templates", "Filters", "are", "powerful"],
        "string": "Django Templates Filters are powerful",
        "numbers": [1, 2, 3, 4, 5, 6]
    }
    return render(request, 'filters_example.html', context)
```

---

## 2. HTML-Vorlage mit Filter-Beispielen
In der Vorlage werden alle Filter mit den Daten aus dem Dictionary angewendet. Jede Sektion zeigt ein spezifisches Beispiel.

### **Code für `filters_example.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Template Filters</title>
</head>
<body>
    <h1>Django Template Filters Beispiele</h1>

    <section>
        <h2>1. Großbuchstaben (upper)</h2>
        <p>Original: {{ name }}</p>
        <p>Upper: {{ name | upper }}</p>
    </section>

    <section>
        <h2>2. Kleinbuchstaben (lower)</h2>
        <p>Original: {{ name }}</p>
        <p>Lower: {{ name | lower }}</p>
    </section>

    <section>
        <h2>3. Kapitalisierung (title)</h2>
        <p>Original: {{ name }}</p>
        <p>Title: {{ name | title }}</p>
    </section>

    <section>
        <h2>4. Länge einer Liste (length)</h2>
        <p>Liste: {{ items }}</p>
        <p>Länge: {{ items | length }}</p>
    </section>

    <section>
        <h2>5. Erstes Element (first)</h2>
        <p>Liste: {{ my_list }}</p>
        <p>Erstes Element: {{ my_list | first }}</p>
    </section>

    <section>
        <h2>6. Letztes Element (last)</h2>
        <p>Liste: {{ my_list }}</p>
        <p>Letztes Element: {{ my_list | last }}</p>
    </section>

    <section>
        <h2>7. Liste verbinden (join)</h2>
        <p>Wörter: {{ words }}</p>
        <p>Verbunden: {{ words | join:", " }}</p>
    </section>

    <section>
        <h2>8. Wortanzahl (wordcount)</h2>
        <p>String: "{{ string }}"</p>
        <p>Wörter: {{ string | wordcount }}</p>
    </section>

    <section>
        <h2>9. Liste slicen (slice)</h2>
        <p>Nummern: {{ numbers }}</p>
        <p>Slice [1:3]: {{ numbers | slice:"1:3" }}</p>
    </section>
</body>
</html>
```

---

## 3. Zusammenfassung
Diese Vorlage zeigt:
1. Die Verwendung von Django-Filtern.
2. Dynamisches Laden von Daten aus der View.
3. Strukturierte Abschnitte zur Präsentation im Unterricht.

- **URL-Konfiguration**: Verknüpfe die View mit einer URL.
```python
from django.urls import path
from .views import filter_examples_view

urlpatterns = [
    path('filters/', filter_examples_view, name='filter_examples'),
]
```

Nutze diese Beispiele im Unterricht, um die Leistungsfähigkeit von Django Template Filters zu demonstrieren.
