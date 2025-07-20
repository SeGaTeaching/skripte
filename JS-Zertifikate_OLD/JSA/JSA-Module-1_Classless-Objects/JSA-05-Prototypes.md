
# Understanding Prototypes in JavaScript: Detailed Guide

## 1.10.1 What are Prototypes?
JavaScript uses prototypes to enable inheritance and the sharing of properties and methods among objects.

### Example: Basic Prototype Chain
```javascript
let point = { x: 0, y: 0 };
let coloredPoint = { color: "red" };
coloredPoint.__proto__ = point;

console.log(coloredPoint.x); // Output: 0
console.log(Object.getOwnPropertyNames(coloredPoint)); // Output: ["color"]
```

## 1.10.2 Using the __proto__ Property
Setting the prototype directly via `__proto__` is discouraged, but it helps illustrate the concept.

### Example: Inheriting Methods with __proto__
```javascript
let figure = {
    getType: function() {
        return this.type ? this.type : "unknown";
    }
};

let circle = {
    type: "circle",
    center: { x: 0, y: 0 },
    radius: 100
};

circle.__proto__ = figure;
console.log(circle.getType()); // Output: "circle"
```

## 1.10.3 Using Object.setPrototypeOf
Use `Object.setPrototypeOf` to set an object’s prototype in a recommended way.

```javascript
Object.setPrototypeOf(circle, figure);
let proto = Object.getPrototypeOf(circle);
console.log(circle.getType()); // Output: "circle"
```

## 1.10.4 Using Object.create
`Object.create` creates a new object with a specified prototype.

### Example: Creating an Object with a Prototype
```javascript
let circle = Object.create(figure);
circle.type = "circle";
circle.center = { x: 0, y: 0 };
circle.radius = 100;
console.log(circle.getType()); // Output: "circle"
```

## 1.10.5 Using Constructors for Prototypes
Constructor functions allow creating objects with shared prototypes.

### Example: Constructor Functions
```javascript
function Figure() {
    this.getType = function() {
        return this.type ? this.type : "unknown";
    };
}

function Circle(center, radius) {
    this.type = "circle";
    this.center = center;
    this.radius = radius;
}
Circle.prototype = new Figure();

let myCircle = new Circle({ x: 0, y: 0 }, 50);
console.log(myCircle.getType()); // Output: "circle"
```

### Adding Methods to the Prototype
```javascript
Circle.prototype.sayHi = function() {
    console.log("Hi from Circle!");
};
myCircle.sayHi(); // Output: "Hi from Circle!"
```

## 1.10.6 Extending Built-in Prototypes
Prototypes allow modifying built-in objects.

### Example: Adding a Method to String
```javascript
String.prototype.sayHello = function() {
    console.log("Hello from String!");
};
"example".sayHello(); // Output: "Hello from String!"
```

---

Prototypes are powerful in JavaScript, enabling inheritance and extending built-in objects. 
Using modern ES6 classes often simplifies prototype management, making JavaScript code more readable.
