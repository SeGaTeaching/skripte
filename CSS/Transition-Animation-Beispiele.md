
# Anspruchsvolle Transitions & Animations Vorlagen

---

## 1. Glatte Übergänge mit Farbwechsel, Skalierung und Rotation

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background-color: #3498db;
      transition: background-color 1s ease, transform 1s ease;
    }

    .box:hover {
      background-color: #e74c3c;
      transform: scale(1.2) rotate(15deg);
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

### Erklärung:
- **Transition auf mehrere Eigenschaften**: Sowohl `background-color` als auch `transform` werden gleichzeitig animiert.
- **Skalierung und Rotation**: Beim Hover wird die Box größer und leicht gedreht.

---

## 2. Slide-In Menü mit Verzögerter Transition

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    .menu {
      width: 200px;
      height: 50px;
      background-color: #2ecc71;
      transition: transform 0.5s ease-in-out 0.3s, background-color 0.2s ease;
      transform: translateX(-250px);
    }

    .menu:hover {
      transform: translateX(0);
      background-color: #27ae60;
    }
  </style>
</head>
<body>
  <div class="menu"></div>
</body>
</html>
```

### Erklärung:
- **Transformations-Transition mit Delay**: Das Menü schiebt sich nach einer kleinen Verzögerung ins Bild.
- **Transition von Hintergrundfarbe und Bewegung**: Beim Hover wird sowohl die Position als auch die Farbe geändert.

---

## 3. Pulsierender Button mit endloser Animation

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    @keyframes pulse {
      0% {
        transform: scale(1);
        background-color: #1abc9c;
      }
      50% {
        transform: scale(1.1);
        background-color: #16a085;
      }
      100% {
        transform: scale(1);
        background-color: #1abc9c;
      }
    }

    .button {
      padding: 20px 40px;
      background-color: #1abc9c;
      color: white;
      font-size: 18px;
      border: none;
      cursor: pointer;
      animation: pulse 2s infinite;
    }
  </style>
</head>
<body>
  <button class="button">Pulsieren</button>
</body>
</html>
```

### Erklärung:
- **Keyframe-Animation**: Die Schaltfläche pulsiert kontinuierlich und ändert dabei leicht ihre Größe und Farbe.
- **Unendliche Wiederholung**: Die Animation wird durch `infinite` endlos wiederholt.

---

## 4. Flip Card mit 3D-Effekten

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    .card {
      width: 200px;
      height: 300px;
      perspective: 1000px;
    }

    .inner-card {
      width: 100%;
      height: 100%;
      transition: transform 0.8s;
      transform-style: preserve-3d;
      position: relative;
    }

    .card:hover .inner-card {
      transform: rotateY(180deg);
    }

    .front, .back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
    }

    .front {
      background-color: #f39c12;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: white;
    }

    .back {
      background-color: #e74c3c;
      transform: rotateY(180deg);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: white;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="inner-card">
      <div class="front">
        Vorderseite
      </div>
      <div class="back">
        Rückseite
      </div>
    </div>
  </div>
</body>
</html>
```

### Erklärung:
- **3D-Transition**: Beim Hover dreht sich die Karte um 180 Grad, wodurch eine flüssige 3D-Flip-Animation entsteht.
- **`backface-visibility`**: Stellt sicher, dass die Rückseite der Karte nur sichtbar wird, wenn sie nach vorne gedreht ist.

---

## 5. Fortschrittsbalken mit animiertem Füllstand

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    .progress-bar {
      width: 100%;
      background-color: #ecf0f1;
      border-radius: 25px;
      overflow: hidden;
    }

    .progress {
      height: 30px;
      background-color: #2ecc71;
      width: 0;
      border-radius: 25px;
      animation: load 5s ease-in-out forwards;
    }

    @keyframes load {
      0% {
        width: 0;
      }
      100% {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <div class="progress-bar">
    <div class="progress"></div>
  </div>
</body>
</html>
```

### Erklärung:
- **Keyframe-Animation**: Der Fortschrittsbalken wächst kontinuierlich von 0% auf 100%.
- **`forwards`**: Sorgt dafür, dass die Animation nach Abschluss in ihrem letzten Zustand verbleibt.

---

## 6. Text-Schreibanimation

### HTML
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <style>
    .typing {
      font-family: monospace;
      font-size: 24px;
      white-space: nowrap;
      overflow: hidden;
      border-right: 2px solid;
      width: 0;
      animation: typing 3.5s steps(30, end), blink-caret 0.5s step-end infinite;
    }

    @keyframes typing {
      from { width: 0; }
      to { width: 100%; }
    }

    @keyframes blink-caret {
      50% { border-color: transparent; }
    }
  </style>
</head>
<body>
  <div class="typing">Dies ist eine Schreibanimation!</div>
</body>
</html>
```

### Erklärung:
- **Schreibmaschineneffekt**: Der Text wird Buchstabe für Buchstabe angezeigt.
- **Zwei Keyframe-Animationen**: Eine für das Tippen, eine für das Blinken des Cursors.

---
