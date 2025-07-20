
# JavaScript Built-in Objects: JSON, Math, and RegExp

Built-in objects in JavaScript go beyond simple constructors for data types; they bring additional functionalities.
In this guide, we'll explore the essential built-in objects in JavaScript: JSON, Math, and RegExp.

---

## 1. JSON

**JSON (JavaScript Object Notation)** is a lightweight text-based format commonly used for data interchange.
JSON is easy for humans to read and write and easy for machines to parse and generate.

### JSON.stringify()

The `JSON.stringify()` method converts JavaScript objects into a JSON string format. This is useful for data storage or transmission.

#### Example 1
```javascript
let person = {
    name: "Alice",
    age: 25,
    city: "New York"
};
let personJSON = JSON.stringify(person);
console.log(typeof personJSON); // -> string
console.log(personJSON); // -> {"name":"Alice","age":25,"city":"New York"}
```

#### Additional Example 2
```javascript
let user = {
    username: "john_doe",
    loggedIn: true,
    preferences: { theme: "dark", language: "en" }
};
let userJSON = JSON.stringify(user);
console.log(typeof userJSON); // -> string
console.log(userJSON); // -> {"username":"john_doe","loggedIn":true,"preferences":{"theme":"dark","language":"en"}}
```

#### Additional Example 3
```javascript
let cart = {
    items: ["apple", "banana", "cherry"],
    total: 15.0,
    discount: null
};
let cartJSON = JSON.stringify(cart);
console.log(typeof cartJSON); // -> string
console.log(cartJSON); // -> {"items":["apple","banana","cherry"],"total":15.0,"discount":null}
```

### JSON.parse()

The `JSON.parse()` method parses a JSON string and converts it back into a JavaScript object.

#### Example 1
```javascript
let data = '{"id":"AK12113","position":{"longitude":59.358615,"latitude":17.947589}}';
let vehicle = JSON.parse(data);
console.log(typeof vehicle); // -> object
console.log(vehicle.position.latitude); // -> 17.947589
```

#### Additional Example 2
```javascript
let settingsJSON = '{"theme":"dark","showAds":false,"volume":80}';
let settings = JSON.parse(settingsJSON);
console.log(settings.theme); // -> dark
console.log(settings.showAds); // -> false
console.log(settings.volume); // -> 80
```

#### Additional Example 3
```javascript
let profileJSON = '{"username":"janedoe","status":"active","score":1500}';
let profile = JSON.parse(profileJSON);
console.log(profile.username); // -> janedoe
console.log(profile.status); // -> active
console.log(profile.score); // -> 1500
```

---

## 2. Math

The `Math` object is a built-in object that has properties and methods for mathematical constants and functions. 

### Common Math Methods

#### Math.ceil(), Math.floor(), Math.round()

- `Math.ceil()` rounds up to the nearest integer.
- `Math.floor()` rounds down to the nearest integer.
- `Math.round()` rounds to the nearest integer.

#### Example 1
```javascript
console.log(Math.ceil(5.4)); // -> 6
console.log(Math.floor(5.4)); // -> 5
console.log(Math.round(5.4)); // -> 5
```

#### Additional Example 2
```javascript
console.log(Math.ceil(-1.7)); // -> -1
console.log(Math.floor(-1.7)); // -> -2
console.log(Math.round(-1.7)); // -> -2
```

#### Additional Example 3
```javascript
console.log(Math.ceil(0.01)); // -> 1
console.log(Math.floor(0.01)); // -> 0
console.log(Math.round(0.01)); // -> 0
```

---