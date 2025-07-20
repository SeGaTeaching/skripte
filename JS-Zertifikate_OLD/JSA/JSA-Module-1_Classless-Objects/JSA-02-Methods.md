
# Methods in JavaScript: Detailed Guide

## 1.7.1 Declaring Methods in Objects
In JavaScript, methods are properties of objects that are functions. Methods allow objects to perform actions.

### Example: Method Declaration and Invocation
```javascript
let circle = {
    radius: 100,
    center: { x: 0, y: 0 },
    getType: function() {
        return "circle";
    }
};

// Simplified method syntax
let circleSimplified = {
    radius: 100,
    center: { x: 0, y: 0 },
    getType() {
        return "circle";
    }
};

// Invoking methods
console.log(circle.getType()); // Using dot notation
console.log(circle["getType"]()); // Using bracket notation
```

## 1.7.2 Using the `this` Keyword
The `this` keyword refers to the object the method is called on, allowing methods to access other properties of the same object.

### Example: Using `this` to Access Object Properties
```javascript
let circle = {
    radius: 100,
    center: { x: 0, y: 0 },
    getType() {
        return typeof this.radius === "number" ? "circle" : "unknown";
    }
};

console.log(circle.getType());

let figure = { ...circle };
delete circle.radius;
console.log(figure.getType()); // Output will be "circle"
```

### Pitfall: Using Object Names Instead of `this`
Avoid directly using object names within methods; use `this` to prevent errors when copying or modifying objects.

```javascript
let circle = {
    radius: 100,
    getType() {
        return typeof this.radius === "number" ? "circle" : "unknown";
    }
};

let figure = { ...circle };
delete circle.radius;
console.log(figure.getType()); // "circle" because of `this`
```

## 1.7.3 `this` in Nested Objects
When a method is nested within another object, `this` refers to the immediate object.

### Example: Using `this` in Nested Objects
```javascript
let circle = {
    radius: 100,
    center: {
        x: 0,
        y: 0,
        show() {
            console.log(`${this.x}, ${this.y}`);
        }
    }
};

circle.center.show(); // Output: "0, 0"
```

### Limitation: Accessing Parent Object from Nested Objects
`this` does not allow direct access to parent properties. Instead, pass necessary data as arguments:

```javascript
let circle = {
    radius: 100,
    center: {
        x: 0,
        y: 0,
        show(radius) {
            console.log(`Center: (${this.x}, ${this.y}), Radius: ${radius}`);
        }
    }
};

circle.center.show(circle.radius); // Output: "Center: (0, 0), Radius: 100"
```

## 1.7.4 Getters and Setters
Getters and setters are methods that let you define computed properties and manage data access. 

### Example: Using Getters and Setters
```javascript
let contact = {
    _tel: "207-662-5412",
    get tel() {
        return this._tel;
    },
    set tel(value) {
        this._tel = value;
    }
};

console.log(contact.tel); // "207-662-5412"
contact.tel = "100-100-1000";
console.log(contact.tel); // "100-100-1000"
```

### Complex Example: Aggregated Getters and Validation
```javascript
let person = {
    _age: 30,
    firstName: "Alice",
    lastName: "Smith",
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },
    get age() {
        return this._age;
    },
    set age(value) {
        if (value > 0) this._age = value;
    }
};

console.log(person.fullName); // "Alice Smith"
person.age = -10; // Invalid age, so age remains 30
console.log(person.age); // "30"
person.age = 25; // Valid age
console.log(person.age); // "25"
```

### Usage Notes
- Getters are called as properties, not methods: `object.property`.
- Setters must take exactly one parameter.
- Use getters and setters for encapsulation, data validation, and computed properties.
