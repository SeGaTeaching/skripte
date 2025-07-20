# Erstellung eines Django Projekts

## Ziel
- Einrichtung einer Arbeitsumgebung
- Django Projekt erstellen
- Erste eigene Seite anzeigen im Browser
- Einblick in die MVT Architektur

## 1. Einrichtung einer virtuellen Arbeitsumgebung
### Grund:
- Projekte isolieren
- Umbgebung hat eigene Abhängigkeiten, Versionen und Bibliotheken -> Vermeidung von Konflikten

### Virtuelle Umgebung erstellen

Linux, macOS:
 ```bash
python3 -m venv myenv
```

Windows:
 ```bash
python -m venv myenv
```

### Virtuelle Umgebung aktivieren
Linux, macOS:
 ```bash
source myenv/bin/activate
```

Windows:
 ```bash
   myenv\Scripts\activate
```

### Django installieren
in der virtuellen Umgebung, zu erkennen an dem (virutal-Env-Name) vor dem Pfad
```bash
pip install django

# oder für bestimmte Version
pip install django==3.2.9

# check ob django installiert
python -m django --version
```

## 2. Erstellen eines Django Projekts
- nach Installation von Django evt. in IDE wie Visual Studio Code wechseln
- ggf. nochmal environment dort aktivieren

### Standard Befehl für Erstellen eines Projekts
#### A: mit seperaten Projekt-Ordner
```bash
django-admin startproject myproject
```
erstellt eine Ordnerstruktur, welche ungefähr so auschaut ausschaut
```bash
myproject/                # Hauptprojektordner
├── manage.py             # Kommandozeilentool für Django-Befehle
├── myproject/            # Projekt-Settings und Hauptkonfigurationsordner
│   ├── __init__.py       # Markiert diesen Ordner als Python-Paket
│   ├── settings.py       # Konfigurationsdatei des Projekts (z.B. Datenbank, Apps, Middleware)
│   ├── urls.py           # Haupt-Routing-Datei für das Projekt
│   ├── asgi.py           # ASGI-Serverkonfiguration für asynchrone Webanwendungen
│   └── wsgi.py           # WSGI-Serverkonfiguration für das Deployment
└── __pycache__/          # Cache-Ordner für kompilierte Python-Dateien (automatisch generiert)
```

#### B: ODER direkt im aktuellen Ordner mit Punkt '.' am Ende
```bash
django-admin startproject myproject .
```

Ordnerstruktur
```bash
./                      # Aktueller Ordner, in dem das Projekt erstellt wurde
├── manage.py           # Kommandozeilentool für Django-Befehle
├── myproject/          # Projekt-Settings und Hauptkonfigurationsordner
│   ├── __init__.py     # Markiert diesen Ordner als Python-Paket
│   ├── settings.py     # Konfigurationsdatei des Projekts (z.B. Datenbank, Apps, Middleware)
│   ├── urls.py         # Haupt-Routing-Datei für das Projekt
│   ├── asgi.py         # ASGI-Serverkonfiguration für asynchrone Webanwendungen
│   └── wsgi.py         # WSGI-Serverkonfiguration für das Deployment
└── __pycache__/        # Cache-Ordner für kompilierte Python-Dateien (automatisch generiert)
```

|                  | Ohne Punkt am Ende des Befehls (A)                 | Mit Punkt am Ende des Befehls (B)               |
|------------------|----------------------------------------------------|-------------------------------------------------|
| **Vorteile**     | - Bessere Struktur                                 | - Ordnerstruktur bleibt kompakt                 |
|                  | - Trennung von Konfiguration und Quellcode         | - Ideal für isolierte Projekte                  |
|                  | - Flexibler für größere Projekte                   | - Weniger Pfade                                 |
| **Nachteile**    | - Zusätzliche Ordnerstruktur                       | - Unübersichtlich bei mehreren Apps             |
|                  | - Verwaltung von Pfaden                            | - Weniger Flexibilität für zusätzliche Dateien  |

### Eigene App anlegen
**Was ist eine Django-App?**: 
Eine App in Django ist ein Teilprojekt, das eine spezifische Funktionalität erfüllt. Zum Beispiel könnte man für eine Webseite eine Blog-App, eine Benutzer-App und eine E-Commerce-App haben. Ein Django-Projekt besteht meist aus mehreren Apps.

- ggf in Ordner wechseln in welcher die `manage.py` sich befindet
```bash
python manage.py startapp myapp
```

OrdnerStruktur jetzt:
```bash
myproject/                
├── manage.py             
├── myproject/            
│   ├── __init__.py       
│   ├── settings.py       
│   ├── urls.py           
│   ├── asgi.py           
│   └── wsgi.py           
├── __pycache__/          
└── myapp/                # Neuer App-Ordner
    ├── migrations/       # Ordner für Datenbankmigrationen der App
    │   └── __init__.py   # Markiert den Migrationsordner als Python-Paket
    ├── __init__.py       # Markiert diesen Ordner als Python-Paket
    ├── admin.py          # Datei zur Registrierung der Modelle im Django-Admin
    ├── apps.py           # App-Konfigurationsdatei
    ├── models.py         # Definiert die Datenbankmodelle der App
    ├── tests.py          # Tests für die App
    ├── views.py          # Views für die App, um Logik für Anfragen bereitzustellen
    └── urls.py           # Optional: URL-Routing-Datei für die App (muss ggf. erstellt werden)
```
### Erstellte App in der `settings.py` im `myproject` Ordner registrieren
```python
#... schnipp
INSTALLED_APPS = [
    # My Apps
    'myapp',              # App registrieren innerhalb der INSTALLED_APPS Liste
    
    # Default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#... schnipp
```

### Entwicklungsserver starten
Nachdem das Projekt installiert ist (App anlegen ist optional für diesen Schritt) starte den Development Server um die erfolgreiche Installation zu überprüfen
```bash
python manage.py runserver
```
- Die Seite ist nun über den URL http://127.0.0.1:8000 im Browser erreichbar
- ggf. kann über den Befehl ein anderer Port als 8000 angegeben werden
- um den Server zu beenden in der Konsole <STRG>+C drücken


## 3. Eigene Seite erstellen (Routing)
- einen 'intro/' Pfad anlegen und diesen mit vordefiniertem Text ausgeben

### Pfad erstellen / handeln

**A. die `urls.py` im `myproject` Ordner wie folgt ergänzen**
```python
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', include('myapp.urls')),
]
```
- importiere `include` von `django.urls`  -> siehe zweite Zeile
- in der Liste 'urlpatterns' ergänze folgende Zeile:
  `path('intro/', include('myapp.urls')),`
- das 'leitet' den einkommenden request auf diesem Pfad an die `urls.py` im `myapp` Ordner weiter


**B. `urls.py` im `myapp` Ordner**
- im `myapp` Ordner eine Datei `urls.py` erstellen und wie folgt ergänzen
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
- `path` Funktion von `django.urls` importieren
- `views` Modul von `myapp` importieren
- 'urlpatterns' Liste erstellen und 'path Funktion darin ausführen
-> Eingehender request über '/intro/' wird an das `views` Modul übergeben

### Request Verarbeiten und ServerAntwort ausgeben

**C. `views.py` im `myapp` Ordner öffnen und wie folt ergänzen**
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Intro</h1><p>Hallo ich bin erfolgreich aufgerufen</p>')
```
- `HttpResponse` von `django.http` importieren
- Funktion `index` mit `request` als Argument anlegen, welche eine HttpResponse zurückgibt


### Webseite besuchen
- ggf. Server noch einmal starten
```python
python manage.py runserver
```
- folgenden Link im Browser aufrufen: http://127.0.0.1:8000/intro/