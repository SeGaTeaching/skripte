# Übungs-Set: Verzweigungen (if, else, switch)

## **Aufgaben**

### **Grundlagen**

1.  **Bestanden oder nicht?** Prüfe, ob eine erreichte Punktzahl (`>= 50`) zum Bestehen ausreicht und gib "Bestanden" oder "Durchgefallen" aus.
2.  **Versandkostenfrei:** Ein Online-Shop bietet kostenlosen Versand für Bestellungen über 50 €. Prüfe einen Warenkorbwert und gib aus, ob der Versand kostenlos ist oder nicht.
3.  **Wochenende:** Prüfe, ob ein eingegebener Wochentag ("Samstag" oder "Sonntag") ein Wochenendtag ist.
4.  **Gültige E-Mail?** Prüfe, ob eine eingegebene Zeichenkette das "@"-Zeichen enthält, um eine sehr grundlegende E-Mail-Validierung durchzuführen.
5.  **Ticket-Verkauf:** Ein Ticket kostet 15 €. Kinder unter 12 Jahren zahlen nur 8 €. Schreibe ein Programm, das nach dem Alter fragt und den korrekten Preis ausgibt.
6.  **Lagerbestand:** Prüfe, ob der Lagerbestand eines Produkts (`> 0`) ist. Gib "Auf Lager" oder "Ausverkauft" aus.
7.  **Login-Prüfung:** Prüfe, ob ein eingegebener Benutzername `admin` **und** ein Passwort `12345` lautet. Gib "Login erfolgreich" oder "Falsche Daten" aus.

### **`if-elif-else` & Logik**

8.  **Notensystem:** Wandle eine Punktzahl in eine Note um: 90-100 = "A", 80-89 = "B", 70-79 = "C", 60-69 = "D", unter 60 = "F".
9.  **Schaltjahr-Rechner:** Prüfe, ob ein eingegebenes Jahr ein Schaltjahr ist. Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist, außer es ist durch 100 teilbar, es sei denn, es ist auch durch 400 teilbar.
10. **Paket-Gewicht:** Berechne die Versandkosten basierend auf dem Gewicht: bis 2kg = 5€, 2kg bis 5kg = 8€, über 5kg = 12€.
11. **Rabatt-System:** Ein Kunde erhält 10% Rabatt, wenn er entweder ein "Student" ist **oder** der Bestellwert über 100€ liegt. Prüfe beide Bedingungen.
12. **Dreiecks-Typen:** Nimm drei Seitenlängen eines Dreiecks entgegen. Bestimme, ob das Dreieck gleichseitig (alle Seiten gleich), gleichschenklig (zwei Seiten gleich) oder ungleichseitig (keine Seite gleich) ist.
13. **Geldautomat:** Simuliere eine Abhebung. Eine Abhebung ist nur möglich, wenn der gewünschte Betrag das Kontoguthaben nicht übersteigt **und** der Betrag ein Vielfaches von 10 ist.
14. **Jahreszeiten:** Gib zu einem eingegebenen Monat ("Januar", "Februar", ..., "Dezember") die passende Jahreszeit (Winter, Frühling, Sommer, Herbst) aus. Dies ist ein idealer Anwendungsfall für `switch-case`.
15. **HTTP-Statuscodes:** Gib zu einem eingegebenen Code (z.B. 200, 301, 404, 500) die Bedeutung aus ("OK", "Moved Permanently", "Not Found", "Internal Server Error"). Auch dies ist ein idealer Anwendungsfall für `switch-case`.

### **Verschachtelte Logik & Kombinationen**

16. **Schere, Stein, Papier:** Nimm die Eingaben von zwei Spielern entgegen und bestimme den Gewinner nach den bekannten Regeln (Schere schlägt Papier, Papier schlägt Stein, Stein schlägt Schere). Berücksichtige auch ein Unentschieden.
17. **BMI-Rechner & Auswertung:** Berechne den Body-Mass-Index (`BMI = Gewicht / Größe²`). Gib anschließend eine Bewertung basierend auf dem BMI aus: \< 18.5 = "Untergewicht", 18.5 - 24.9 = "Normalgewicht", 25 - 29.9 = "Übergewicht", \>= 30 = "Adipositas".
18. **Passwort-Stärke:** Prüfe ein eingegebenes Passwort auf folgende Kriterien:
      * Mindestens 8 Zeichen lang
      * Muss mindestens eine Zahl enthalten
      * Muss mindestens einen Großbuchstaben enthalten
        Gib eine entsprechende Meldung aus, ob das Passwort "sicher" ist oder welche Regel verletzt wurde.
19. **Tarif-Rechner:** Ein Handytarif kostet 10€ Grundgebühr. Darin sind 100 Freiminuten enthalten. Jede weitere Minute kostet 0,20€. Berechne die Monatsrechnung basierend auf den verbrauchten Minuten.
20. **Reisekosten:** Eine Firma erstattet Reisekosten. Für Reisen unter 100km gibt es 0.30€ pro km. Für Reisen von 100km oder mehr gibt es 0.25€ pro km. Zusätzlich gibt es eine Tagespauschale von 20€, wenn die Reise mehr als 8 Stunden gedauert hat. Berechne die Gesamterstattung.

---

<div style="page-break-after: always;"></div>

---

## **Lösungen**

### 🐍 Python Lösungen

```python
# 1. Bestanden oder nicht?
punkte = 65
if punkte >= 50:
    print("Bestanden")
else:
    print("Durchgefallen")

# 2. Versandkostenfrei
warenkorb = 60.50
if warenkorb > 50:
    print("Versand ist kostenlos.")
else:
    print("Versandkosten fallen an.")

# 3. Wochenende
tag = "Sonntag"
if tag == "Samstag" or tag == "Sonntag":
    print("Es ist Wochenende!")
else:
    print("Es ist ein Wochentag.")

# 4. Gültige E-Mail?
email = "test@example.com"
if "@" in email:
    print("Die E-Mail könnte gültig sein.")
else:
    print("Die E-Mail enthält kein @-Zeichen.")
    
# 5. Ticket-Verkauf
alter = 10
if alter < 12:
    print("Der Ticketpreis beträgt 8€.")
else:
    print("Der Ticketpreis beträgt 15€.")
    
# 6. Lagerbestand
bestand = 0
if bestand > 0:
    print("Auf Lager")
else:
    print("Ausverkauft")

# 7. Login-Prüfung
username = "admin"
password = "12345"
if username == "admin" and password == "12345":
    print("Login erfolgreich")
else:
    print("Falsche Daten")

# 8. Notensystem
score = 85
if score >= 90:
    print("Note: A")
elif score >= 80:
    print("Note: B")
elif score >= 70:
    print("Note: C")
elif score >= 60:
    print("Note: D")
else:
    print("Note: F")

# 9. Schaltjahr-Rechner
jahr = 2024
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")

# 10. Paket-Gewicht
gewicht = 3.5
if gewicht < 2:
    print("Versandkosten: 5€")
elif gewicht <= 5:
    print("Versandkosten: 8€")
else:
    print("Versandkosten: 12€")

# 11. Rabatt-System
kundentyp = "Student"
bestellwert = 80.0
if kundentyp == "Student" or bestellwert > 100:
    print("10% Rabatt gewährt.")
else:
    print("Kein Rabatt.")

# 12. Dreiecks-Typen
a, b, c = 7, 7, 5
if a == b and b == c:
    print("Gleichseitiges Dreieck")
elif a == b or a == c or b == c:
    print("Gleichschenkliges Dreieck")
else:
    print("Ungleichseitiges Dreieck")
    
# 13. Geldautomat
kontostand = 500
abhebung = 120
if abhebung <= kontostand and abhebung % 10 == 0:
    print("Abhebung erfolgreich.")
else:
    print("Abhebung nicht möglich.")

# 14. Jahreszeiten (mit match-case)
monat = "März"
match monat:
    case "Dezember" | "Januar" | "Februar":
        print("Winter")
    case "März" | "April" | "Mai":
        print("Frühling")
    case "Juni" | "Juli" | "August":
        print("Sommer")
    case "September" | "Oktober" | "November":
        print("Herbst")
    case _:
        print("Ungültiger Monat")

# 15. HTTP-Statuscodes (mit Dictionary als switch-Alternative)
status_code = 404
bedeutungen = {
    200: "OK",
    301: "Moved Permanently",
    404: "Not Found",
    500: "Internal Server Error"
}
print(bedeutungen.get(status_code, "Unbekannter Code"))

# 16. Schere, Stein, Papier
p1 = "Stein"
p2 = "Schere"
if p1 == p2:
    print("Unentschieden!")
elif (p1 == "Stein" and p2 == "Schere") or \
     (p1 == "Schere" and p2 == "Papier") or \
     (p1 == "Papier" and p2 == "Stein"):
    print("Spieler 1 gewinnt!")
else:
    print("Spieler 2 gewinnt!")

# 17. BMI-Rechner & Auswertung
gewicht_kg = 75
groesse_m = 1.80
bmi = gewicht_kg / (groesse_m ** 2)
print(f"Dein BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Kategorie: Untergewicht")
elif bmi < 25:
    print("Kategorie: Normalgewicht")
elif bmi < 30:
    print("Kategorie: Übergewicht")
else:
    print("Kategorie: Adipositas")

# 18. Passwort-Stärke
passwort_test = "Pass123"
hat_mindestlaenge = len(passwort_test) >= 8
hat_zahl = any(char.isdigit() for char in passwort_test)
hat_grossbuchstaben = any(char.isupper() for char in passwort_test)
if hat_mindestlaenge and hat_zahl and hat_grossbuchstaben:
    print("Passwort ist sicher.")
else:
    print("Passwort ist unsicher.")

# 19. Tarif-Rechner
minuten = 150
grundgebuehr = 10.0
rechnung = grundgebuehr
if minuten > 100:
    zusatzminuten = minuten - 100
    rechnung += zusatzminuten * 0.20
print(f"Monatsrechnung: {rechnung:.2f}€")

# 20. Reisekosten
km = 120
stunden = 9
erstattung = 0.0
if km < 100:
    erstattung = km * 0.30
else:
    erstattung = km * 0.25
if stunden > 8:
    erstattung += 20
print(f"Gesamterstattung: {erstattung:.2f}€")
```

<div style="page-break-after: always;"></div>

###  JavaScript Lösungen

```javascript
// 1. Bestanden oder nicht?
let punkte = 65;
if (punkte >= 50) {
    console.log("Bestanden");
} else {
    console.log("Durchgefallen");
}

// 2. Versandkostenfrei
let warenkorb = 60.50;
if (warenkorb > 50) {
    console.log("Versand ist kostenlos.");
} else {
    console.log("Versandkosten fallen an.");
}

// 3. Wochenende
let tag = "Sonntag";
if (tag === "Samstag" || tag === "Sonntag") {
    console.log("Es ist Wochenende!");
} else {
    console.log("Es ist ein Wochentag.");
}

// 4. Gültige E-Mail?
let email = "test@example.com";
if (email.includes("@")) {
    console.log("Die E-Mail könnte gültig sein.");
} else {
    console.log("Die E-Mail enthält kein @-Zeichen.");
}

// 5. Ticket-Verkauf
let alter = 10;
if (alter < 12) {
    console.log("Der Ticketpreis beträgt 8€.");
} else {
    console.log("Der Ticketpreis beträgt 15€.");
}

// 6. Lagerbestand
let bestand = 0;
if (bestand > 0) {
    console.log("Auf Lager");
} else {
    console.log("Ausverkauft");
}

// 7. Login-Prüfung
let username = "admin";
let password = "12345";
if (username === "admin" && password === "12345") {
    console.log("Login erfolgreich");
} else {
    console.log("Falsche Daten");
}

// 8. Notensystem
let score = 85;
if (score >= 90) {
    console.log("Note: A");
} else if (score >= 80) {
    console.log("Note: B");
} else if (score >= 70) {
    console.log("Note: C");
} else if (score >= 60) {
    console.log("Note: D");
} else {
    console.log("Note: F");
}

// 9. Schaltjahr-Rechner
let jahr = 2024;
if ((jahr % 4 === 0 && jahr % 100 !== 0) || (jahr % 400 === 0)) {
    console.log(`${jahr} ist ein Schaltjahr.`);
} else {
    console.log(`${jahr} ist kein Schaltjahr.`);
}

// 10. Paket-Gewicht
let gewicht = 3.5;
if (gewicht < 2) {
    console.log("Versandkosten: 5€");
} else if (gewicht <= 5) {
    console.log("Versandkosten: 8€");
} else {
    console.log("Versandkosten: 12€");
}

// 11. Rabatt-System
let kundentyp = "Student";
let bestellwert = 80.0;
if (kundentyp === "Student" || bestellwert > 100) {
    console.log("10% Rabatt gewährt.");
} else {
    console.log("Kein Rabatt.");
}

// 12. Dreiecks-Typen
let a = 7, b = 7, c = 5;
if (a === b && b === c) {
    console.log("Gleichseitiges Dreieck");
} else if (a === b || a === c || b === c) {
    console.log("Gleichschenkliges Dreieck");
} else {
    console.log("Ungleichseitiges Dreieck");
}

// 13. Geldautomat
let kontostand = 500;
let abhebung = 120;
if (abhebung <= kontostand && abhebung % 10 === 0) {
    console.log("Abhebung erfolgreich.");
} else {
    console.log("Abhebung nicht möglich.");
}

// 14. Jahreszeiten
let monat = "März";
switch (monat) {
    case "Dezember": case "Januar": case "Februar":
        console.log("Winter");
        break;
    case "März": case "April": case "Mai":
        console.log("Frühling");
        break;
    case "Juni": case "Juli": case "August":
        console.log("Sommer");
        break;
    case "September": case "Oktober": case "November":
        console.log("Herbst");
        break;
    default:
        console.log("Ungültiger Monat");
}

// 15. HTTP-Statuscodes
let statusCode = 404;
switch (statusCode) {
    case 200:
        console.log("OK");
        break;
    case 301:
        console.log("Moved Permanently");
        break;
    case 404:
        console.log("Not Found");
        break;
    case 500:
        console.log("Internal Server Error");
        break;
    default:
        console.log("Unbekannter Code");
}

// 16. Schere, Stein, Papier
let p1 = "Stein";
let p2 = "Schere";
if (p1 === p2) {
    console.log("Unentschieden!");
} else if ((p1 === "Stein" && p2 === "Schere") ||
           (p1 === "Schere" && p2 === "Papier") ||
           (p1 === "Papier" && p2 === "Stein")) {
    console.log("Spieler 1 gewinnt!");
} else {
    console.log("Spieler 2 gewinnt!");
}

// 17. BMI-Rechner & Auswertung
let gewicht_kg = 75;
let groesse_m = 1.80;
let bmi = gewicht_kg / (groesse_m ** 2);
console.log(`Dein BMI: ${bmi.toFixed(2)}`);
if (bmi < 18.5) {
    console.log("Kategorie: Untergewicht");
} else if (bmi < 25) {
    console.log("Kategorie: Normalgewicht");
} else if (bmi < 30) {
    console.log("Kategorie: Übergewicht");
} else {
    console.log("Kategorie: Adipositas");
}

// 18. Passwort-Stärke
let passwort_test = "Pass123";
let hatMindestlaenge = passwort_test.length >= 8;
let hatZahl = /\d/.test(passwort_test);
let hatGrossbuchstaben = /[A-Z]/.test(passwort_test);
if (hatMindestlaenge && hatZahl && hatGrossbuchstaben) {
    console.log("Passwort ist sicher.");
} else {
    console.log("Passwort ist unsicher.");
}

// 19. Tarif-Rechner
let minuten = 150;
const grundgebuehr = 10.0;
let rechnung = grundgebuehr;
if (minuten > 100) {
    let zusatzminuten = minuten - 100;
    rechnung += zusatzminuten * 0.20;
}
console.log(`Monatsrechnung: ${rechnung.toFixed(2)}€`);

// 20. Reisekosten
let km = 120;
let stunden = 9;
let erstattung = 0.0;
if (km < 100) {
    erstattung = km * 0.30;
} else {
    erstattung = km * 0.25;
}
if (stunden > 8) {
    erstattung += 20;
}
console.log(`Gesamterstattung: ${erstattung.toFixed(2)}€`);
```

<div style="page-break-after: always;"></div>

### ☕ Java Lösungen

```java
import java.util.regex.Pattern;

public class UebungenVerzweigungen {
    public static void main(String[] args) {
        // 1. Bestanden oder nicht?
        int punkte = 65;
        if (punkte >= 50) {
            System.out.println("Bestanden");
        } else {
            System.out.println("Durchgefallen");
        }

        // 2. Versandkostenfrei
        double warenkorb = 60.50;
        if (warenkorb > 50) {
            System.out.println("Versand ist kostenlos.");
        } else {
            System.out.println("Versandkosten fallen an.");
        }

        // 3. Wochenende
        String tag = "Sonntag";
        if (tag.equals("Samstag") || tag.equals("Sonntag")) {
            System.out.println("Es ist Wochenende!");
        } else {
            System.out.println("Es ist ein Wochentag.");
        }

        // 4. Gültige E-Mail?
        String email = "test@example.com";
        if (email.contains("@")) {
            System.out.println("Die E-Mail könnte gültig sein.");
        } else {
            System.out.println("Die E-Mail enthält kein @-Zeichen.");
        }

        // 5. Ticket-Verkauf
        int alter = 10;
        if (alter < 12) {
            System.out.println("Der Ticketpreis beträgt 8€.");
        } else {
            System.out.println("Der Ticketpreis beträgt 15€.");
        }

        // 6. Lagerbestand
        int bestand = 0;
        if (bestand > 0) {
            System.out.println("Auf Lager");
        } else {
            System.out.println("Ausverkauft");
        }

        // 7. Login-Prüfung
        String username = "admin";
        String password = "12345";
        if (username.equals("admin") && password.equals("12345")) {
            System.out.println("Login erfolgreich");
        } else {
            System.out.println("Falsche Daten");
        }

        // 8. Notensystem
        int score = 85;
        if (score >= 90) {
            System.out.println("Note: A");
        } else if (score >= 80) {
            System.out.println("Note: B");
        } else if (score >= 70) {
            System.out.println("Note: C");
        } else if (score >= 60) {
            System.out.println("Note: D");
        } else {
            System.out.println("Note: F");
        }

        // 9. Schaltjahr-Rechner
        int jahr = 2024;
        if ((jahr % 4 == 0 && jahr % 100 != 0) || (jahr % 400 == 0)) {
            System.out.println(jahr + " ist ein Schaltjahr.");
        } else {
            System.out.println(jahr + " ist kein Schaltjahr.");
        }

        // 10. Paket-Gewicht
        double gewicht = 3.5;
        if (gewicht < 2) {
            System.out.println("Versandkosten: 5€");
        } else if (gewicht <= 5) {
            System.out.println("Versandkosten: 8€");
        } else {
            System.out.println("Versandkosten: 12€");
        }
        
        // 11. Rabatt-System
        String kundentyp = "Student";
        double bestellwert = 80.0;
        if (kundentyp.equals("Student") || bestellwert > 100) {
            System.out.println("10% Rabatt gewährt.");
        } else {
            System.out.println("Kein Rabatt.");
        }

        // 12. Dreiecks-Typen
        int a = 7, b = 7, c = 5;
        if (a == b && b == c) {
            System.out.println("Gleichseitiges Dreieck");
        } else if (a == b || a == c || b == c) {
            System.out.println("Gleichschenkliges Dreieck");
        } else {
            System.out.println("Ungleichseitiges Dreieck");
        }

        // 13. Geldautomat
        double kontostand = 500;
        double abhebung = 120;
        if (abhebung <= kontostand && abhebung % 10 == 0) {
            System.out.println("Abhebung erfolgreich.");
        } else {
            System.out.println("Abhebung nicht möglich.");
        }

        // 14. Jahreszeiten
        String monat = "März";
        switch (monat) {
            case "Dezember", "Januar", "Februar":
                System.out.println("Winter");
                break;
            case "März", "April", "Mai":
                System.out.println("Frühling");
                break;
            case "Juni", "Juli", "August":
                System.out.println("Sommer");
                break;
            case "September", "Oktober", "November":
                System.out.println("Herbst");
                break;
            default:
                System.out.println("Ungültiger Monat");
                break;
        }

        // 15. HTTP-Statuscodes
        int statusCode = 404;
        switch (statusCode) {
            case 200:
                System.out.println("OK");
                break;
            case 301:
                System.out.println("Moved Permanently");
                break;
            case 404:
                System.out.println("Not Found");
                break;
            case 500:
                System.out.println("Internal Server Error");
                break;
            default:
                System.out.println("Unbekannter Code");
                break;
        }

        // 16. Schere, Stein, Papier
        String p1 = "Stein";
        String p2 = "Schere";
        if (p1.equals(p2)) {
            System.out.println("Unentschieden!");
        } else if ((p1.equals("Stein") && p2.equals("Schere")) ||
                   (p1.equals("Schere") && p2.equals("Papier")) ||
                   (p1.equals("Papier") && p2.equals("Stein"))) {
            System.out.println("Spieler 1 gewinnt!");
        } else {
            System.out.println("Spieler 2 gewinnt!");
        }

        // 17. BMI-Rechner & Auswertung
        double gewichtKg = 75;
        double groesseM = 1.80;
        double bmi = gewichtKg / (groesseM * groesseM);
        System.out.printf("Dein BMI: %.2f\n", bmi);
        if (bmi < 18.5) {
            System.out.println("Kategorie: Untergewicht");
        } else if (bmi < 25) {
            System.out.println("Kategorie: Normalgewicht");
        } else if (bmi < 30) {
            System.out.println("Kategorie: Übergewicht");
        } else {
            System.out.println("Kategorie: Adipositas");
        }

        // 18. Passwort-Stärke
        String passwortTest = "Pass123";
        boolean hatMindestlaenge = passwortTest.length() >= 8;
        boolean hatZahl = Pattern.compile(".*[0-9].*").matcher(passwortTest).matches();
        boolean hatGrossbuchstaben = !passwortTest.equals(passwortTest.toLowerCase());
        if (hatMindestlaenge && hatZahl && hatGrossbuchstaben) {
            System.out.println("Passwort ist sicher.");
        } else {
            System.out.println("Passwort ist unsicher.");
        }

        // 19. Tarif-Rechner
        int minuten = 150;
        double grundgebuehr = 10.0;
        double rechnung = grundgebuehr;
        if (minuten > 100) {
            int zusatzminuten = minuten - 100;
            rechnung += zusatzminuten * 0.20;
        }
        System.out.printf("Monatsrechnung: %.2f€\n", rechnung);

        // 20. Reisekosten
        double km = 120;
        int stunden = 9;
        double erstattung = 0.0;
        if (km < 100) {
            erstattung = km * 0.30;
        } else {
            erstattung = km * 0.25;
        }
        if (stunden > 8) {
            erstattung += 20;
        }
        System.out.printf("Gesamterstattung: %.2f€\n", erstattung);
    }
}
```