# **Aufgaben**

**Primitive Typen & Operatoren**

1.  **Warenkorb-Summe:** Deklariere drei Variablen für drei verschiedene Produktpreise (z.B. `19.99`, `4.50`, `12.00`). Berechne die Gesamtsumme und gib sie aus.
2.  **Rest der Division:** Deklariere eine Variable mit der Anzahl der Schüler (`27`) und eine weitere mit der Anzahl der Teams (`4`). Berechne, wie viele Schüler übrig bleiben, wenn so viele 4er-Teams wie möglich gebildet werden. Gib den Rest aus.
3.  **Temperatur-Umrechner:** Erstelle eine Variable für eine Temperatur in Celsius (`25.0`). Rechne diese Temperatur in Fahrenheit um mit der Formel `F = C * 9/5 + 32` und gib das Ergebnis aus.
4.  **Euro und Cent:** Eine Variable enthält den Preis `7.89`. Zerlege diesen Preis in zwei Ganzzahl-Variablen: eine für die vollen Euros (`7`) und eine für die Cents (`89`). Gib beide Werte getrennt aus. (Tipp: Nutze Typumwandlung und den Modulo-Operator).
5.  **Freizeitpark-Zutritt:** Eine Person darf nur auf die Achterbahn, wenn sie mindestens 14 Jahre alt ist **UND** größer als 1.50m ist, **ODER** wenn sie einen VIP-Pass hat. Erstelle Variablen für `alter`, `groesse` und `hatVipPass`. Prüfe die Bedingung und gib `true` oder `false` aus.

**String-Methoden**

6.  **Formelle Anrede:** Erstelle Variablen für `vorname` ("max") und `nachname` ("mustermann"). Formatiere beide Namen so, dass der erste Buchstabe groß und der Rest klein ist. Gib dann eine formelle Begrüßung aus: "Guten Tag, Max Mustermann."
7.  **E-Mail-Bereinigung:** Eine Variable `email` enthält die Eingabe `"  test@example.com   "`. Bereinige die E-Mail von allen führenden und folgenden Leerzeichen und gib die bereinigte E-Mail in Kleinbuchstaben aus.
8.  **Dateinamen-Prüfung:** Ein Dateiname wird in einer Variable `datei` gespeichert (z.B. "Urlaubsbild.JPG"). Prüfe, ob der Dateiname (unabhängig von Groß-/Kleinschreibung) auf ".jpg" endet. Gib `true` oder `false` aus.
9.  **Benutzer-ID erstellen:** Erstelle eine Benutzer-ID aus einem Vornamen und einem Nachnamen. Die ID soll aus den ersten drei Buchstaben des Vornamens und den ersten fünf Buchstaben des Nachnamens bestehen, alles in Kleinbuchstaben. Beispiel: "Robert" und "Langemann" wird zu "roblange".
10. **CSV-Daten parsen:** Ein Datensatz liegt als String vor: `Artikel:Druckerpatrone;Preis:49.95;Status:Lagernd`. Extrahiere die Werte "Druckerpatrone", "49.95" und "Lagernd" und gib sie einzeln und beschriftet aus. (Tipp: Nutze `split`).
11. **Domain extrahieren:** Gegeben ist eine E-Mail-Adresse in einer Variable. Extrahiere nur den Domain-Teil der Adresse. Beispiel: aus "max.mustermann@https://www.google.com/search?q=google.com" soll "https://www.google.com/search?q=google.com" extrahiert werden.
12. **Wörter zensieren:** Gegeben ist ein Satz: "Der Referent sprach über Politik und Geld." Ersetze die Wörter "Politik" und "Geld" durch Sternchen (`"*******"`) und gib den neuen Satz aus.

**Komplexe Typen**

1.  **Wochentage (Liste/Array):** Erstelle eine Liste/ein Array mit den ersten drei Wochentagen ("Montag", "Dienstag", "Mittwoch"). Gib dann nur das zweite Element ("Dienstag") auf der Konsole aus.
2.  **Auto-Steckbrief (Dictionary/Map):** Erstelle ein Dictionary/eine Map, um ein Auto zu beschreiben. Es soll die Schlüssel "marke", "modell" und "baujahr" mit entsprechenden Werten enthalten. Gib nur den Wert für den Schlüssel "modell" aus.
3.  **Gästeliste bearbeiten (Liste/Array):** Erstelle eine Gästeliste mit drei Namen. Gib die Liste aus. Ersetze dann den ersten Namen in der Liste durch einen neuen Namen. Gib die Liste erneut aus, um die Änderung zu zeigen.

---
<div style="page-break-after: always;"></div>
---

### **Lösungen**

### 🐍 Python Lösungen

```python
# Aufgabe 1
p1, p2, p3 = 19.99, 4.50, 12.00
summe = p1 + p2 + p3
print(f"1. Gesamtsumme: {summe:.2f} €")

# Aufgabe 2
schueler = 27
teamsize = 4
rest = schueler % teamsize
print(f"2. Übrige Schüler: {rest}")

# Aufgabe 3
celsius = 25.0
fahrenheit = celsius * 9/5 + 32
print(f"3. Temperatur in Fahrenheit: {fahrenheit}°F")

# Aufgabe 4
preis_float = 7.89
euros = int(preis_float)
cents = round((preis_float - euros) * 100)
print(f"4. Volle Euros: {euros}, Cents: {cents}")

# Aufgabe 5
alter, groesse, hat_vip_pass = 15, 1.60, False
darf_fahren = (alter >= 14 and groesse > 1.50) or hat_vip_pass
print(f"5. Darf fahren? {darf_fahren}")

# Aufgabe 6
vorname = "max"
nachname = "mustermann"
vorname_formatiert = vorname.capitalize()
nachname_formatiert = nachname.capitalize()
print(f"6. Guten Tag, {vorname_formatiert} {nachname_formatiert}.")

# Aufgabe 7
email = "  test@example.com   "
bereinigt = email.strip().lower()
print(f"7. Bereinigte E-Mail: {bereinigt}")

# Aufgabe 8
datei = "Urlaubsbild.JPG"
endet_mit_jpg = datei.lower().endswith(".jpg")
print(f"8. Endet mit .jpg? {endet_mit_jpg}")

# Aufgabe 9
vorname, nachname = "Robert", "Langemann"
user_id = vorname[0:3].lower() + nachname[0:5].lower()
print(f"9. Benutzer-ID: {user_id}")

# Aufgabe 10
datensatz = "Artikel:Druckerpatrone;Preis:49.95;Status:Lagernd"
teile = datensatz.split(';')
artikel = teile[0].split(':')[1]
preis = teile[1].split(':')[1]
status = teile[2].split(':')[1]
print(f"10. Artikel: {artikel}, Preis: {preis}, Status: {status}")

# Aufgabe 11
email_full = "max.mustermann@google.com"
domain = email_full.split('@')[1]
print(f"11. Domain: {domain}")

# Aufgabe 12
satz = "Der Referent sprach über Politik und Geld."
zensiert = satz.replace("Politik", "*******").replace("Geld", "*******")
print(f"12. Zensierter Satz: {zensiert}")

# Aufgabe 13
wochentage = ["Montag", "Dienstag", "Mittwoch"]
print(f"13. Zweiter Wochentag: {wochentage[1]}")

# Aufgabe 14
auto = {"marke": "VW", "modell": "Golf", "baujahr": 2021}
print(f"14. Modell: {auto['modell']}")

# Aufgabe 15
gaeste = ["Anna", "Bernd", "Clara"]
print(f"15. Alte Liste: {gaeste}")
gaeste[0] = "Anton"
print(f"15. Neue Liste: {gaeste}")
```

### ☕ Java Lösungen

```java
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class UebungenKapitel2 {
    public static void main(String[] args) {
        // Aufgabe 1
        double p1 = 19.99, p2 = 4.50, p3 = 12.00;
        double summe = p1 + p2 + p3;
        System.out.printf("1. Gesamtsumme: %.2f €\n", summe);

        // Aufgabe 2
        int schueler = 27;
        int teamsize = 4;
        int rest = schueler % teamsize;
        System.out.println("2. Übrige Schüler: " + rest);

        // Aufgabe 3
        double celsius = 25.0;
        double fahrenheit = celsius * 9.0/5.0 + 32; // 9.0/5.0 für Gleitkommadivision
        System.out.println("3. Temperatur in Fahrenheit: " + fahrenheit + "°F");

        // Aufgabe 4
        double preisFloat = 7.89;
        int euros = (int) preisFloat;
        int cents = (int) Math.round((preisFloat - euros) * 100);
        System.out.println("4. Volle Euros: " + euros + ", Cents: " + cents);
        
        // Aufgabe 5
        int alter = 15;
        double groesse = 1.60;
        boolean hatVipPass = false;
        boolean darfFahren = (alter >= 14 && groesse > 1.50) || hatVipPass;
        System.out.println("5. Darf fahren? " + darfFahren);

        // Aufgabe 6
        String vorname = "max";
        String nachname = "mustermann";
        String vornameFormatiert = vorname.substring(0, 1).toUpperCase() + vorname.substring(1).toLowerCase();
        String nachnameFormatiert = nachname.substring(0, 1).toUpperCase() + nachname.substring(1).toLowerCase();
        System.out.println("6. Guten Tag, " + vornameFormatiert + " " + nachnameFormatiert + ".");

        // Aufgabe 7
        String email = "  test@example.com   ";
        String bereinigt = email.trim().toLowerCase();
        System.out.println("7. Bereinigte E-Mail: " + bereinigt);

        // Aufgabe 8
        String datei = "Urlaubsbild.JPG";
        boolean endetMitJpg = datei.toLowerCase().endsWith(".jpg");
        System.out.println("8. Endet mit .jpg? " + endetMitJpg);

        // Aufgabe 9
        String vornameUser = "Robert";
        String nachnameUser = "Langemann";
        String userId = (vornameUser.substring(0, 3) + nachnameUser.substring(0, 5)).toLowerCase();
        System.out.println("9. Benutzer-ID: " + userId);
        
        // Aufgabe 10
        String datensatz = "Artikel:Druckerpatrone;Preis:49.95;Status:Lagernd";
        String[] teile = datensatz.split(";");
        String artikel = teile[0].split(":")[1];
        String preis = teile[1].split(":")[1];
        String status = teile[2].split(":")[1];
        System.out.println("10. Artikel: " + artikel + ", Preis: " + preis + ", Status: " + status);
        
        // Aufgabe 11
        String emailFull = "max.mustermann@google.com";
        String domain = emailFull.split("@")[1];
        System.out.println("11. Domain: " + domain);

        // Aufgabe 12
        String satz = "Der Referent sprach über Politik und Geld.";
        String zensiert = satz.replace("Politik", "*******").replace("Geld", "*******");
        System.out.println("12. Zensierter Satz: " + zensiert);

        // Aufgabe 13
        String[] wochentage = {"Montag", "Dienstag", "Mittwoch"};
        System.out.println("13. Zweiter Wochentag: " + wochentage[1]);

        // Aufgabe 14
        Map<String, String> auto = new HashMap<>();
        auto.put("marke", "VW");
        auto.put("modell", "Golf");
        auto.put("baujahr", "2021");
        System.out.println("14. Modell: " + auto.get("modell"));
        
        // Aufgabe 15
        String[] gaeste = {"Anna", "Bernd", "Clara"};
        System.out.println("15. Alte Liste: " + Arrays.toString(gaeste));
        gaeste[0] = "Anton";
        System.out.println("15. Neue Liste: " + Arrays.toString(gaeste));
    }
}
```