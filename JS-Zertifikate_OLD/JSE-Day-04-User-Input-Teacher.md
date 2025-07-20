
# User Input in JavaScript: alert, prompt, and confirm

## 1. Introduction to User Input

JavaScript provides various ways to interact with the user. These include `alert`, `prompt`, and `confirm`, which allow displaying messages and receiving input from the user.

## 2. `alert()`

The `alert()` method displays a simple message. It is useful for giving information or warnings to the user. The message is shown in a modal window that the user must acknowledge to continue.

**Syntax:**
```javascript
alert("This is a message!");
```

**Examples:**
```javascript
// Simple message
alert("Welcome to our website!");

// Message with a variable
let username = "Alice";
alert("Hello, " + username + "! Welcome back.");
```

**Exercise:**
1. Create a message that reminds the user to save their inputs.
2. Display a message with dynamic text that greets a person by their name.

## 3. `prompt()`

The `prompt()` method displays an input field and prompts the user to enter something. The return value is the user's input. If the user clicks "Cancel," `null` is returned.

**Syntax:**
```javascript
let name = prompt("What is your name?");
```

**Examples:**
```javascript
// Simple input
let age = prompt("How old are you?");
alert("You are " + age + " years old.");

// Input with a default value
let favoriteColor = prompt("What is your favorite color?", "Blue");
alert("Your favorite color is " + favoriteColor + ".");
```

**Exercise:**
1. Ask the user for their age and calculate the year they were born.
2. Create a small program that asks for the user's name and then greets them nicely.

## 4. `confirm()`

The `confirm()` method displays a window with a message and the buttons "OK" and "Cancel." The return value is a boolean: `true` if the user clicks "OK" and `false` if they click "Cancel."

**Syntax:**
```javascript
let response = confirm("Do you want to proceed?");
```

**Examples:**
```javascript
// Simple confirmation
let deleteFile = confirm("Are you sure you want to delete this file?");
if (deleteFile) {
  alert("The file will be deleted.");
} else {
  alert("The file was not deleted.");
}

// Confirmation with a condition
let wantsNewsletter = confirm("Would you like to subscribe to our newsletter?");
if (wantsNewsletter) {
  alert("Thank you for subscribing to our newsletter!");
} else {
  alert("Maybe next time.");
}
```

**Exercise:**
1. Create a prompt that asks the user if they want to log into the website. Show a corresponding message depending on whether they choose "OK" or "Cancel."
2. Ask the user if they want to cancel an operation and either proceed or cancel based on their response.

## 5. Combining `alert`, `prompt`, and `confirm`

The three methods can be combined to create a simple interactive program.

**Example Program:**
```javascript
alert("Welcome to our program!");

let name = prompt("What is your name?");
let age = prompt("How old are you, " + name + "?");

if (confirm("May I save this data?")) {
  alert("Thank you, " + name + "! Your data has been saved.");
} else {
  alert("Don't worry, " + name + ". Your data has not been saved.");
}
```

**Exercise:**
1. Create a program that asks the user about their favorite activities and then shows a confirmation to save those activities.
2. Develop a small survey that asks the user about their favorite movie, book, and food, and then summarizes at the end.

This provides a solid foundation for teaching students various methods of user interaction in JavaScript. Good luck with your lesson!

```javascript
function startGuessingGame(range) {
  // Zufällige Zahl zwischen 1 und dem angegebenen Bereich generieren
  const randomNumber = Math.floor(Math.random() * range) + 1;
  let attempts = 0;
  let guess = 0;

  alert(`Willkommen zum Zahlenratespiel! Versuche, die Zahl zwischen 1 und ${range} zu erraten.`);

  // Solange raten, bis die richtige Zahl erraten wurde
  while (guess !== randomNumber) {
    // Benutzereingabe einholen
    guess = parseInt(prompt("Gib eine Zahl ein:"), 10);
    attempts++;

    // Eingabe überprüfen und Hinweise geben
    if (isNaN(guess)) {
      alert("Bitte gib eine gültige Zahl ein.");
    } else if (guess < randomNumber) {
      alert("Zu niedrig! Versuch es nochmal.");
    } else if (guess > randomNumber) {
      alert("Zu hoch! Versuch es nochmal.");
    } else {
      alert(`Glückwunsch! Du hast die Zahl ${randomNumber} in ${attempts} Versuchen erraten.`);
    }
  }
}

// Spiel starten, mit einem benutzerdefinierten Bereich, z. B. 1 bis 100
startGuessingGame(100);
```
