
# JSA Class-based Approach

## 2.0.1 Classes

JavaScript has several methods for creating objects. These methods prior to the introduction of **classes** (in ECMAScript 6) were **classless**, including approaches like object literals and constructor functions. 

### Why Introduce Classes in JavaScript?

There are two main reasons why classes were introduced:

1. **Simplified Inheritance**: Before classes, inheritance in JavaScript was done using **prototypes**, which were often unintuitive and required practice to grasp. Classes offer a cleaner, easier-to-read syntax for inheritance.
  
2. **Cross-language Familiarity**: Most object-oriented languages, like Java, Python, and C#, use classes. By introducing classes in JavaScript, developers familiar with these languages can easily adapt to JavaScript.

### What is a Class in JavaScript?

A **class** in JavaScript serves as a **template** for creating objects. When we define a class, we outline the methods and properties that objects based on the class will have. 

A key component of a class is the **constructor**. The constructor is a method invoked when creating an object based on the class, and it’s responsible for initializing object properties. 

Example:

```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    // Method to calculate area
    area() {
        return this.width * this.height;
    }

    // Method to calculate perimeter
    perimeter() {
        return 2 * (this.width + this.height);
    }
}

// Create rectangles
let smallRectangle = new Rectangle(2, 4);
let largeRectangle = new Rectangle(10, 20);

console.log(smallRectangle.area()); // Output: 8
console.log(largeRectangle.perimeter()); // Output: 60
```

---

## 2.1 Class Declaration

### 2.1.1 Class Declaration

To declare a class, use the `class` keyword. Let’s work through an example:

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // Method to say hello
    sayHello() {
        return `Hello, my name is ${this.name}`;
    }

    // Method to check if person is an adult
    isAdult() {
        return this.age >= 18;
    }
}

let person1 = new Person("Alice", 25);
let person2 = new Person("Bob", 15);

console.log(person1.sayHello()); // Output: Hello, my name is Alice
console.log(person2.isAdult());  // Output: false
```

### Refactoring Constructor Functions into Classes

Before classes, constructor functions were used. Let’s look at how we can refactor a constructor function into a class:

#### Constructor Function Example:
```javascript
function Vehicle(id, latitude, longitude) {
    this.id = id;
    this.latitude = latitude;
    this.longitude = longitude;
    this.status = "available";
}

let vehicle1 = new Vehicle("V100", 52.52, 13.405);
```

#### Refactored into Class:
```javascript
class Vehicle {
    constructor(id, latitude, longitude) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.status = "available";
    }

    getInfo() {
        return `Vehicle ${this.id} is at (${this.latitude}, ${this.longitude}).`;
    }
}

let vehicle1 = new Vehicle("V100", 52.52, 13.405);
console.log(vehicle1.getInfo());  // Output: Vehicle V100 is at (52.52, 13.405).
```

---

### 2.1.2 Class Expressions

Classes in JavaScript can be **anonymous** or **named** when used in **expressions**. Here’s an example:

```javascript
let Animal = class {
    constructor(type, sound) {
        this.type = type;
        this.sound = sound;
    }

    makeSound() {
        return `${this.type} makes a ${this.sound} sound.`;
    }
};

let dog = new Animal("Dog", "bark");
console.log(dog.makeSound());  // Output: Dog makes a bark sound.
```

---

## 2.1.3 The `instanceof` Operator

The `instanceof` operator checks whether an object is an instance of a particular class:

```javascript
let car = new Vehicle("C123", 51.1657, 10.4515);
console.log(car instanceof Vehicle);  // Output: true
```

---

## Class Inheritance

In JavaScript, you can **extend** a class by using the `extends` keyword. Let’s see an example of inheritance:

```javascript
class Employee {
    constructor(name, position) {
        this.name = name;
        this.position = position;
    }

    describe() {
        return `${this.name} works as a ${this.position}.`;
    }
}

class Manager extends Employee {
    constructor(name, department) {
        super(name, "Manager");
        this.department = department;
    }

    describe() {
        return `${this.name} manages the ${this.department} department.`;
    }
}

let emp1 = new Employee("John", "Developer");
let mgr1 = new Manager("Jane", "IT");

console.log(emp1.describe());  // Output: John works as a Developer.
console.log(mgr1.describe());  // Output: Jane manages the IT department.
```

---

## Conclusion

JavaScript classes provide a powerful yet simple structure to organize code. By using classes, you can easily create objects, define methods, and inherit from other classes, making code reusable and maintainable. The syntax of JavaScript classes is similar to other OOP languages, making it a familiar choice for developers transitioning into JavaScript.

