### **2-Tage-Lehrplan: Netzwerkprogrammierung & REST-APIs in Python (PCPP-1 Vorbereitung)**

**Tutor-Projekt (Demonstration):** API-Client für eine öffentliche Buch-Datenbank (z.B. Open Library API)
**Schüler-Projekt (Übungen):** API-Client für "JSONPlaceholder" (ein kostenloser Fake-API-Service zum Testen)

---

### **Tag 1: Grundlagen der Kommunikation & Datenformate**

An diesem Tag legen wir das Fundament des Datenaustauschs. Wir beginnen ganz unten bei den Sockets, um zu verstehen, wie Netzwerkkommunikation prinzipiell funktioniert. Danach fokussieren wir uns auf die universellen Sprachen des Internets – die Datenformate JSON und XML.

**Block 1: Netzwerk-Grundlagen & Low-Level-Sockets (ca. 2.5 Stunden)**
* **Lernziele:**
    * Die Grundbegriffe der Netzwerktechnik (Sockets, Ports, Protokolle, Client/Server) verstehen.
    * Den grundlegenden Aufbau einer HTTP-Anfrage kennen.
    * Mit dem `socket`-Modul eine manuelle, Low-Level-Verbindung zu einem Webserver herstellen und eine rohe HTTP-Antwort empfangen.
    * Die Notwendigkeit und Vorteile von High-Level-Bibliotheken wie `requests` erkennen.
* **Themen:**
    1.  **Das Internet verstehen:** Client, Server, IP-Adressen, Ports und Protokolle (TCP/IP, HTTP).
    2.  **Sockets:** Die "Steckdosen" des Netzwerks.
    3.  **HTTP 101:** Der Aufbau einer einfachen `GET`-Anfrage.
    4.  **Praxis mit dem `socket`-Modul:** Manuelles Senden einer HTTP-Anfrage und Empfangen der rohen Antwort.
* **Tutor-Projekt (Buch-API):** Der Tutor nutzt das `socket`-Modul, um eine rohe HTTP-Anfrage an `example.com` zu senden und die zurückgegebene HTML-Seite in der Konsole auszugeben, um den Prozess zu demonstrieren.
* **Übungs-Set 1:** Enthält 5-8 Programmieraufgaben, bei denen die Schüler mit Sockets experimentieren, z.B. Verbindungen zu verschiedenen Ports herstellen oder den Header einer HTTP-Antwort manuell parsen.

---

**Block 2: Das Lingua Franca des Webs: JSON (ca. 3 Stunden)**
* **Lernziele:**
    * Die Syntax und die Datentypen von JSON (string, number, boolean, array, object, null) sicher beherrschen.
    * Die Analogie zwischen Python (`dict`, `list`) und JSON (`object`, `array`) verstehen.
    * Das `json`-Modul verwenden, um Python-Objekte in JSON-Strings zu serialisieren (`dumps`) und JSON-Strings in Python-Objekte zu deserialisieren (`loads`).
    * Mit verschachtelten JSON-Daten umgehen können.
* **Themen:**
    1.  **Was ist JSON?** (JavaScript Object Notation): Aufbau, Regeln, Vorteile.
    2.  **Serialisierung:** Von Python-Dictionary zu JSON-String mit `json.dumps()`.
    3.  **Deserialisierung:** Von JSON-String zu Python-Dictionary mit `json.loads()`.
    4.  **Umgang mit JSON-Dateien:** Laden aus (`json.load()`) und Speichern in (`json.dump()`) Dateien.
* **Tutor-Projekt (Buch-API):** Der Tutor nimmt einen Beispiel-JSON-String von der Buch-API, deserialisiert ihn in ein Python-Dictionary und greift auf einzelne Werte (Titel, Autor) zu. Anschließend wird ein Python-Dictionary (ein neues Buch) in einen JSON-String serialisiert.
* **Übungs-Set 2:** Enthält 5-8 Programmieraufgaben rund um JSON. Die Schüler arbeiten mit Beispiel-JSON-Daten des **JSONPlaceholder**-Projekts (z.B. einen Blog-Post parsen und dessen Titel ändern).

---

**Block 3: Das klassische Datenformat: XML (ca. 2.5 Stunden)**
* **Lernziele:**
    * Die grundlegende Struktur von XML (Tags, Attribute, Baumstruktur) verstehen.
    * Das `xml.etree.ElementTree`-Modul nutzen, um XML-Daten zu parsen.
    * Gezielt auf bestimmte Elemente und deren Attribute in einem XML-Dokument zugreifen können.
* **Themen:**
    1.  **Was ist XML?** (eXtensible Markup Language): Aufbau, Vergleich mit JSON.
    2.  **XML als Baum:** Das Konzept von Wurzel-, Eltern- und Kind-Elementen.
    3.  **Parsen von XML:** Mit `ElementTree.parse()` eine Datei einlesen.
    4.  **Navigation im Baum:** Mit `.find()` und `.findall()` nach Elementen suchen.
* **Tutor-Projekt (Buch-API):** Der Tutor parst eine einfache XML-Datei, die eine Sammlung von Büchern darstellt, und extrahiert die Titel aller Bücher.
* **Übungs-Set 3:** Enthält 5-8 Programmieraufgaben zu XML, z.B. das Parsen einer einfachen XML-Struktur und das Extrahieren spezifischer Informationen.

---

### **Tag 2: Entwicklung eines modernen API-Clients**

An diesem Tag bauen wir auf den Grundlagen auf und verwenden die Industriestandard-Bibliothek `requests`, um einen sauberen und robusten Client für eine moderne REST-API zu entwickeln. Der Fokus liegt auf der praktischen Anwendung der HTTP-Methoden.

**Block 4: Der `requests`-Client & Daten abrufen (GET) (ca. 3 Stunden)**
* **Lernziele:**
    * Die `requests`-Bibliothek als High-Level-Alternative zu Sockets verstehen und nutzen.
    * Eine `GET`-Anfrage an eine REST-API senden.
    * Das `Response`-Objekt analysieren: Status-Code, Header und Inhalt (`.json()`, `.text`).
    * Mit Query-Parametern die Anfrage filtern und anpassen.
* **Themen:**
    1.  **Vorstellung von `requests`:** Warum es der De-facto-Standard ist.
    2.  **Die `GET`-Anfrage:** `requests.get()`.
    3.  **Analyse der Antwort:** `.status_code` (200, 404 etc.), `.headers`, `.text`, `.json()`.
    4.  **Parameter übergeben:** Das `params`-Argument von `get()`.
* **Tutor-Projekt (Buch-API):** Der Tutor schreibt einen Client, der mit `requests.get()` Informationen zu einem bestimmten Buch von der Open Library API abruft und den Titel und Autor aus der JSON-Antwort anzeigt.
* **Übungs-Set 4:** Enthält 5-8 Programmieraufgaben. Die Schüler nutzen `requests`, um mit ihrem **JSONPlaceholder**-Projekt zu interagieren: alle Posts abrufen (`/posts`), einen spezifischen Post abrufen (`/posts/1`), und Kommentare zu einem Post abrufen (`/posts/1/comments`).

---

**Block 5: Daten verändern mit POST, PUT & DELETE (ca. 2.5 Stunden)**
* **Lernziele:**
    * Die Bedeutung der HTTP-Methoden `POST` (erstellen), `PUT` (aktualisieren) und `DELETE` (löschen) verstehen.
    * Lernen, wie man mit `requests` Daten im Body einer Anfrage sendet (Payload).
    * Eine Ressource auf einem Server erstellen, ändern und löschen können.
* **Themen:**
    1.  **CRUD-Operationen und HTTP-Methoden.**
    2.  **`POST`-Anfragen:** Eine neue Ressource erstellen mit `requests.post()`.
    3.  **`PUT`-Anfragen:** Eine bestehende Ressource komplett ersetzen mit `requests.put()`.
    4.  **`DELETE`-Anfragen:** Eine Ressource löschen mit `requests.delete()`.
    5.  **Payload senden:** Das `json`-Argument in den `requests`-Methoden.
* **Tutor-Projekt (Buch-API):** Der Tutor demonstriert die Funktionsweise von `POST`, `PUT` und `DELETE`, indem er die Anfragen an einen Test-Endpunkt sendet und die (simulierte) Erfolgsantwort des Servers anzeigt.
* **Übungs-Set 5:** Enthält 5-8 Programmieraufgaben. Die Schüler nutzen die echten Endpunkte von **JSONPlaceholder**, um einen neuen Post zu erstellen, dessen Inhalt zu aktualisieren und ihn anschließend wieder zu löschen.

---

**Block 6: Robuste Clients & Fehlerbehandlung (ca. 2.5 Stunden)**
* **Lernziele:**
    * Einen API-Client schreiben, der robust auf Fehler reagiert.
    * Typische Netzwerkfehler (z.B. Timeouts, Verbindungsfehler) mit `try-except` abfangen.
    * HTTP-Status-Codes systematisch auswerten, um zwischen Erfolg und verschiedenen Arten von Fehlern zu unterscheiden.
    * Best Practices wie die Verwendung von Timeouts kennenlernen.
* **Themen:**
    1.  **Die Realität: Nichts funktioniert immer.**
    2.  **Fehler in `requests`:** Die `requests.exceptions`-Hierarchie.
    3.  **Netzwerkfehler abfangen:** `try-except` für `ConnectionError`, `Timeout` etc.
    4.  **HTTP-Fehler behandeln:** Systematische Prüfung des `status_code`.
    5.  **Timeouts setzen:** Das `timeout`-Argument.
* **Tutor-Projekt (Buch-API):** Der Tutor refaktorisiert seinen Client, um alle API-Aufrufe in `try-except`-Blöcke zu packen und auf verschiedene Status-Codes (200, 404, 500) unterschiedlich zu reagieren.
* **Übungs-Set 6:** Enthält 5-8 Programmieraufgaben. Die Schüler erweitern ihren **JSONPlaceholder**-Client um eine robuste Fehlerbehandlung, z.B. was passiert, wenn sie versuchen, einen Post abzurufen, der nicht existiert.