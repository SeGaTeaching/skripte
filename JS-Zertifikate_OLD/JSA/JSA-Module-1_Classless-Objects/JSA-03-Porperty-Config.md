
# Property and Object Configuration in JavaScript: Detailed Guide

## 1.8.1 Property Configuration
Properties in JavaScript objects have configuration attributes: `writable`, `enumerable`, and `configurable`. These attributes determine if and how the properties can be modified.

### Example: Using Object.getOwnPropertyDescriptor
The `Object.getOwnPropertyDescriptor` method allows us to retrieve configuration details of a property.

```javascript
let contact = {
    firstName: "David",
    lastName: "Taylor",
    get fullName() { return \`\${this.firstName} \${this.lastName}\`; }
};

let desc = Object.getOwnPropertyDescriptor(contact, "firstName");
console.log(desc); // Output: { value: "David", writable: true, enumerable: true, configurable: true }
```

### Example: Setting Property Configuration with Object.defineProperty
The `Object.defineProperty` method can create or modify properties with specific configurations.

```javascript
let contact = {};
Object.defineProperty(contact, "_age", {
    value: 36,
    writable: true,
    enumerable: false,
    configurable: true
});

console.log(Object.keys(contact)); // Output: []
console.log(contact._age); // Output: 36
```

### Modifying Property Attributes
To change an existing property, use `Object.defineProperty`. For example, to make `_age` read-only:

```javascript
Object.defineProperty(contact, "_age", {
    writable: false
});

contact._age = 50; // No effect
console.log(contact._age); // Output: 36
```

### Using Object.getOwnPropertyNames
To retrieve all properties regardless of enumerability:

```javascript
let enumKeys = Object.keys(contact);
let allKeys = Object.getOwnPropertyNames(contact);
console.log(enumKeys); // Output: []
console.log(allKeys); // Output: ["_age"]
```

## 1.8.2 Object Configuration
Object-level configuration methods control the entire object’s extensibility, seal, and freeze states.

### Example: Preventing Extensions with Object.preventExtensions
```javascript
let book = { title: "1984" };
Object.preventExtensions(book);
book.author = "George Orwell"; // No effect
console.log(book); // Output: { title: "1984" }
```

### Example: Sealing an Object with Object.seal
```javascript
Object.seal(book);
delete book.title; // No effect
book.title = "Animal Farm"; // This works, properties are still writable
console.log(book.title); // Output: "Animal Farm"
```

### Example: Freezing an Object with Object.freeze
```javascript
Object.freeze(book);
book.title = "1984"; // No effect, properties are not writable anymore
console.log(book.title); // Output: "Animal Farm"
```

### Checking Object State
Methods are available to check whether an object is extensible, sealed, or frozen:

```javascript
console.log(Object.isExtensible(book)); // Output: false
console.log(Object.isSealed(book));     // Output: true
console.log(Object.isFrozen(book));     // Output: true
```

## Summary
- **Property Configuration**: Use `writable`, `enumerable`, and `configurable` to control access and modification of properties.
- **Object-Level Configuration**: Use `preventExtensions`, `seal`, and `freeze` to enforce restrictions on the entire object.
