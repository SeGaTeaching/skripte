
# JavaScript Parameter Handling Techniques

## 4.1.1 Default Parameter Values

With ES6, functions can now have default parameter values, which simplifies handling missing arguments.

### Example: Greeting Function with Default Value

```javascript
function greetings(name = 'anonymous') {
    console.log(`Hi, ${name}!`);
}

greetings();           // -> Hi, anonymous!
greetings('Alice');    // -> Hi, Alice!
```

In this example, if we call `greetings()` without arguments, the default value 'anonymous' is used. If we provide a name, such as 'Alice', it overrides the default.

### Additional Examples

```javascript
function sayHello(name = 'Friend') {
    console.log(`Hello, ${name}!`);
}

sayHello();             // -> Hello, Friend!
sayHello('Bob');        // -> Hello, Bob!

function introduce(name = 'Guest', age = 18) {
    console.log(`${name} is ${age} years old.`);
}

introduce();            // -> Guest is 18 years old.
introduce('Carol');     // -> Carol is 18 years old.
introduce('Dave', 25);  // -> Dave is 25 years old.
```

By assigning defaults, we make functions more robust to missing parameters and reduce the need for conditional checks.

## 4.1.2 The Rest Parameter

The `...rest` parameter aggregates all arguments into an array. This is especially helpful when the function needs to accept a flexible number of arguments.

### Example: Logging Multiple Arguments

```javascript
function logArguments(...args) {
    console.log(`Arguments count: ${args.length}`);
    args.forEach((arg, index) => console.log(`Argument ${index + 1}: ${arg}`));
}

logArguments(1, 2, 3);         // -> Arguments count: 3
                               //    Argument 1: 1
                               //    Argument 2: 2
                               //    Argument 3: 3

logArguments('a', 'b');        // -> Arguments count: 2
                               //    Argument 1: a
                               //    Argument 2: b
```

### Additional Examples

```javascript
function calculateSum(...numbers) {
    return numbers.reduce((sum, number) => sum + number, 0);
}

console.log(calculateSum(10, 20, 30));    // -> 60
console.log(calculateSum(5, 5, 5, 5));    // -> 20

function greetAll(greeting, ...names) {
    names.forEach(name => console.log(`${greeting}, ${name}!`));
}

greetAll('Hello', 'Alice', 'Bob');       // -> Hello, Alice!
                                         //    Hello, Bob!
```

Rest parameters must be the last in the parameter list, and only one `...rest` parameter can exist per function.

## 4.1.3 The Spread Operator

The spread operator, `...`, is used to expand an array into individual elements. It's especially helpful when calling functions that expect separate arguments.

### Example: Passing Array Elements as Arguments

```javascript
function displayInfo(name, age, city) {
    console.log(`${name} is ${age} years old and lives in ${city}.`);
}

let person = ['Alice', 30, 'New York'];
displayInfo(...person);          // -> Alice is 30 years old and lives in New York.
```

### Additional Examples

```javascript
function multiply(a, b, c) {
    return a * b * c;
}

let numbers = [2, 3, 4];
console.log(multiply(...numbers));       // -> 24

function findMax(...values) {
    return Math.max(...values);
}

console.log(findMax(5, 10, 15, 20));     // -> 20
console.log(findMax(...[7, 14, 21, 3])); // -> 21
```

The spread operator is useful not only for function arguments but also for combining arrays and objects.

### Combining Arrays and Objects

```javascript
let fruits = ['apple', 'banana'];
let moreFruits = ['cherry', ...fruits, 'date'];
console.log(moreFruits);                // -> ['cherry', 'apple', 'banana', 'date']

let defaults = { theme: 'dark', language: 'en' };
let settings = { ...defaults, language: 'fr' };
console.log(settings);                  // -> { theme: 'dark', language: 'fr' }
```

By utilizing the spread and rest parameters, we can make our functions and data structures more flexible and efficient.

---
# JavaScript: Simulating Named Parameters

JavaScript does not support named parameters directly. However, by passing a single object with properties as arguments, we can simulate named parameters, making function calls clearer and more flexible.

## 4.1.4 Simulating Named Parameters

### Example: Using an Object to Pass Parameters by Name

By using object destructuring in the function definition, we can refer to specific properties directly.

```javascript
function getFile({url, name, mime}) {
    console.log(`url: ${url}, name: ${name}, mime: ${mime}`);
    // Further processing of the file retrieval can be done here
}

let params = {name: 'test.json', url: 'https://localhost/files', mime: 'application/json'};
getFile(params);  // -> url: https://localhost/files, name: test.json, mime: application/json
```

In this example, we pass a single `params` object containing `url`, `name`, and `mime`. The function can access each by name, regardless of order.

### Additional Examples with Named Parameters

1. **Flexible Function Calls with Optional Parameters**

   ```javascript
   function createUser({username, email, role = 'guest'}) {
       console.log(`User: ${username}, Email: ${email}, Role: ${role}`);
   }

   createUser({username: 'jdoe', email: 'jdoe@example.com'});   // -> User: jdoe, Email: jdoe@example.com, Role: guest
   createUser({username: 'asmith', email: 'asmith@example.com', role: 'admin'}); // -> User: asmith, Email: asmith@example.com, Role: admin
   ```

   By using an object with a default `role`, we handle missing properties while still being able to access them by name.

2. **Simulating Optional Configurations**

   ```javascript
   function configureServer({host = 'localhost', port = 8080, secure = false}) {
       console.log(`Server running on ${host}:${port}, Secure: ${secure}`);
   }

   configureServer({host: '192.168.1.1', secure: true});  // -> Server running on 192.168.1.1:8080, Secure: true
   configureServer({port: 3000});                         // -> Server running on localhost:3000, Secure: false
   ```

   Here, `host`, `port`, and `secure` parameters allow configuration options with sensible defaults.

### Key Benefits of Simulating Named Parameters

- **Clarity:** It is clear which argument corresponds to which parameter without needing a specific order.
- **Flexibility:** We can omit optional parameters or reorder arguments without changing how the function operates.
- **Defaults:** Combined with default parameter values, it becomes simpler to handle undefined values.

This approach is particularly useful in complex functions with many optional parameters or configuration options.

### Using Default Values with Named Parameters

Combining named parameters with default values ensures flexibility and safety against undefined properties.

```javascript
function sendRequest({method = 'GET', url, data = null, headers = {}}) {
    console.log(`Method: ${method}, URL: ${url}, Data: ${data}, Headers: ${JSON.stringify(headers)}`);
}

sendRequest({url: 'https://api.example.com/data'});  // -> Method: GET, URL: https://api.example.com/data, Data: null, Headers: {}
sendRequest({method: 'POST', url: 'https://api.example.com/data', data: {id: 1}, headers: {'Content-Type': 'application/json'}});  
// -> Method: POST, URL: https://api.example.com/data, Data: [object Object], Headers: {"Content-Type":"application/json"}
```

This approach mimics named parameters, allowing us to pass configurations in any order while still having meaningful defaults.
---

# JavaScript Closures

A closure is a mechanism that binds a function to its lexical environment, storing the variables it references from its surrounding scope.

## 4.1.5 Closure Explained

Closures allow a function to "remember" the variables in its environment, even after the function that created it has finished executing.

### Example: Persistent Counter

```javascript
function getCounter() {
    let count = 0;
    return function () {
        return ++count;
    }
}

let counter = getCounter();
console.log(counter()); // -> 1
console.log(counter()); // -> 2
console.log(counter()); // -> 3
```

In this example, `getCounter` defines `count` within its scope. When `counter` (the returned function) is called, it remembers the value of `count`, incrementing it each time.

### Additional Examples and Explanations

1. **Maintaining Private Data**

   ```javascript
   function createSecret(secret) {
       return function() {
           return secret;
       }
   }

   let reveal = createSecret("Hidden message");
   console.log(reveal());   // -> Hidden message
   ```

   Here, `secret` is private to `createSecret` but remains accessible to the returned function due to closure. Each instance of `createSecret` keeps its own `secret`.

2. **Counter with Initial Value**

   ```javascript
   function createCounter(start = 0) {
       let count = start;
       return function() {
           return ++count;
       }
   }

   let countFromFive = createCounter(5);
   console.log(countFromFive()); // -> 6
   console.log(countFromFive()); // -> 7
   
   let countFromTen = createCounter(10);
   console.log(countFromTen());  // -> 11
   ```

   Here, each counter starts from a different initial value, demonstrating how closures can encapsulate unique data.

### Advanced Example: Emulating Private Properties

Closures are often used to simulate private variables in JavaScript objects.

```javascript
function getPoint() {
    function inc(n) {
        return ++n;
    }
    return {
        x: 10,
        y: 20,
        incX: function() {
            this.x = inc(this.x);
        },
        incY: function() {
            this.y = inc(this.y);
        }
    };
}

let point = getPoint();
console.log(point);     // -> {x: 10, y: 20, incX: ƒ, incY: ƒ}
point.incX();
console.log(point);     // -> {x: 11, y: 20, incX: ƒ, incY: ƒ}
```

The `inc` function is local to `getPoint` and not directly accessible outside it. However, `incX` and `incY` use `inc` within the object, which keeps `inc` private.

### Benefits of Using Closures

- **Data Privacy:** Encapsulate data, creating private variables accessible only to specific functions.
- **Persistent State:** Allows maintaining state across function calls.
- **Functional Design:** Common in functional programming and callbacks, closures enable flexible, modular code.

### Common Use Cases

1. **Event Handlers**

   ```javascript
   function setupEventListener(element, message) {
       element.addEventListener('click', function() {
           console.log(message);
       });
   }

   let button = document.createElement('button');
   setupEventListener(button, "Button clicked!");
   button.click();  // -> Button clicked!
   ```

   The closure in the click event handler remembers `message` even after `setupEventListener` finishes.

2. **Delayed Execution with setTimeout**

   ```javascript
   function delayedMessage(msg, delay) {
       setTimeout(function() {
           console.log(msg);
       }, delay);
   }

   delayedMessage("Hello after 1 second", 1000); // -> Hello after 1 second
   ```

   The message is printed after a delay, with the closure keeping `msg` in memory.

Closures in JavaScript make it possible to maintain state between function calls, creating more flexible and efficient code.
---


# JavaScript IIFE (Immediately Invoked Function Expression)

An IIFE (Immediately Invoked Function Expression) is a JavaScript pattern that allows us to create and call a function immediately after defining it. This is useful when we need a function to execute only once or to encapsulate variables.

## 4.1.6 IIFE Explained

### Basic Structure of an IIFE

```javascript
(function(){
    // Code to execute immediately
})();
```

### Example: Self-Invoking Function

```javascript
(function(msg){
    console.log(msg);
})('test IIFE');  // -> test IIFE
```

Here, an anonymous function is defined and immediately called with the argument `'test IIFE'`. This approach keeps `msg` within the function scope, preventing it from entering the global namespace.

### Why Use IIFEs?

1. **Encapsulation**: Variables defined in an IIFE are not accessible outside the function, which avoids polluting the global namespace.
2. **One-Time Execution**: IIFEs are ideal for functions that should only run once, such as initialization logic.

### Additional Examples

1. **Preventing Global Variable Conflicts**

   ```javascript
   (function () {
       let localVar = "I'm local to the IIFE";
       console.log(localVar);
   })();

   // Trying to access localVar here would result in an error
   console.log(typeof localVar);  // -> undefined
   ```

   By using an IIFE, we limit `localVar` to the function scope, preventing accidental access or modification.

2. **Simple Math Operations**

   ```javascript
   let result = (function(x, y) {
       return x + y;
   })(5, 10);

   console.log(result);  // -> 15
   ```

   This IIFE calculates the sum of `x` and `y` without storing unnecessary variables in the global scope.

### Example: Encapsulation for Complex Operations

```javascript
(function () {
    let a = 10;
    let b = 20;
    let result;
    let multiply = function (x, y) {
        return x * y;
    };
    result = multiply(a, b);
    console.log(result);  // -> 200
})();

// result is not accessible here
console.log(typeof result);  // -> undefined
```

In this example, `a`, `b`, `result`, and `multiply` are confined to the IIFE, preventing them from cluttering the global scope.

### Use Cases of IIFEs

1. **Module Pattern**

   IIFEs are often used to create module patterns, where functionality is encapsulated but can still be accessed in a controlled way.

   ```javascript
   let counterModule = (function() {
       let count = 0;
       return {
           increment: function() { return ++count; },
           decrement: function() { return --count; },
           getCount: function() { return count; }
       };
   })();

   console.log(counterModule.getCount());  // -> 0
   counterModule.increment();
   console.log(counterModule.getCount());  // -> 1
   ```

   Here, `count` remains private but can be manipulated through the module’s public methods.

2. **Initialization Code**

   ```javascript
   (function() {
       // Initialization logic
       console.log("Application initialized");
   })();
   ```

   This code block runs once to set up configurations or variables, without leaving behind any unnecessary global variables.

IIFEs provide an excellent way to isolate code, prevent global variable conflicts, and execute code immediately without cluttering the global scope.
---


# JavaScript Forwarding Calls: `apply`, `call`, and `bind`

In JavaScript, we can control the `this` context of functions with methods like `apply`, `call`, and `bind`. These methods allow us to specify the object that `this` should refer to inside a function.

## Understanding `this`

The value of `this` depends on where and how a function is called. In methods, `this` usually refers to the object that owns the method.

### Example: Using `this` in Object Methods

```javascript
let point = {
    x: 100,
    y: 200,
    show: function() {
        console.log(`${this.x}:${this.y}`);
    }
};

point.show();  // -> 100:200
```

The `show` method accesses `x` and `y` using `this`, which refers to the `point` object.

## Behavior of `this` in Functions

In strict mode, `this` in a regular function defaults to `undefined`. Outside strict mode, it defaults to the global object (`window` in browsers).

### Examples: Strict vs. Non-Strict Mode

```javascript
'use strict';
function showThisStrict() {
    console.log(this);  // -> undefined
}

function showThisNonStrict() {
    console.log(this);  // -> Window (or global object)
}

showThisStrict();
showThisNonStrict();
```

## `call` and `apply`

Both `call` and `apply` allow us to specify `this` for a function call.

### `call` Example: Setting `this`

```javascript
let point = { x: 100, y: 200 };

function showPoint(msg) {
    console.log(`${msg} [${this.x}:${this.y}]`);
}

showPoint.call(point, "Location");  // -> Location [100:200]
```

Here, `this` refers to `point` because `call` set `this` to `point`. We also passed `"Location"` as an argument.

### `apply` Example: Passing Arguments as an Array

The only difference between `call` and `apply` is how arguments are passed.

```javascript
showPoint.apply(point, ["Location"]);  // -> Location [100:200]
```

The `apply` method takes arguments in an array, whereas `call` accepts arguments as a list.

### Additional Examples: Passing Multiple Arguments

```javascript
function introduce(greeting, name) {
    console.log(`${greeting}, ${name}! I am at [${this.x}, ${this.y}].`);
}

introduce.call(point, "Hello", "Alice");    // -> Hello, Alice! I am at [100, 200].
introduce.apply(point, ["Hi", "Bob"]);      // -> Hi, Bob! I am at [100, 200].
```

## `bind`: Creating a Bound Function

`bind` returns a new function where `this` is permanently set to the specified object. Unlike `call` and `apply`, it does not execute the function immediately.

### Example: Using `bind`

```javascript
let displayPoint = showPoint.bind(point, "Bound Location");
displayPoint();  // -> Bound Location [100:200]
```

With `bind`, we create a new function (`displayPoint`) that is permanently linked to `point`.

### More Examples with `bind`

1. **Binding Without Arguments**

   ```javascript
   let showOnlyPoint = showPoint.bind(point);
   showOnlyPoint("Coordinate");   // -> Coordinate [100:200]
   ```

   Here, we bind `point` to `showPoint`, allowing us to pass arguments when calling `showOnlyPoint`.

2. **Using `bind` for Event Listeners**

   ```javascript
   let button = document.createElement('button');
   button.textContent = "Show Point";
   button.onclick = showOnlyPoint;  // Bound to point

   document.body.appendChild(button);
   ```

   In this example, the `button` triggers `showOnlyPoint`, which will display the coordinates with `point` as `this`.

## Summary of Differences

- `call`: Invokes the function, accepting a list of arguments.
- `apply`: Invokes the function, accepting arguments as an array.
- `bind`: Returns a new function with `this` set to the specified context, without invoking it.

## Special Considerations for Arrow Functions

Arrow functions do not have their own `this`. Instead, they inherit `this` from their lexical scope (the scope in which they were defined). Thus, `apply`, `call`, and `bind` do not affect `this` in arrow functions.

### Example: Arrow Function `this`

```javascript
let globalObj = { x: 5, y: 10 };

let arrowFunc = () => console.log(this);
arrowFunc.call(globalObj);  // -> Window (in browser) or global object
```

Here, `this` remains bound to the outer scope, regardless of `call`, `apply`, or `bind`.

---


# JavaScript First-Class Functions

JavaScript treats functions as "first-class citizens." This means functions can be treated like any other variable: they can be assigned to variables, passed as arguments, or returned from other functions.

## 4.1.8 Understanding First-Class Functions

### 1. Assigning Functions to Variables

A function can be assigned to a variable and then called using that variable.

```javascript
let sum = function(a, b) {
    return a + b;
};

console.log(sum(10, 20));  // -> 30
```

This example creates an anonymous function assigned to `sum`. This type of function is called a "function expression."

### Additional Examples

```javascript
let greet = function(name) {
    return `Hello, ${name}!`;
};

console.log(greet("Alice"));  // -> Hello, Alice!
console.log(greet("Bob"));    // -> Hello, Bob!
```

### 2. Passing Functions as Arguments

Functions can be passed as arguments to other functions, enabling flexible design patterns like callbacks.

```javascript
function executeOperation(operation, firstArg, secondArg) {
    return operation(firstArg, secondArg);
}

console.log(executeOperation(sum, 10, 20));  // -> 30
```

In this example, `executeOperation` accepts a function (`operation`) and two arguments (`firstArg`, `secondArg`). It executes the function passed in.

### Additional Example: Passing Functions

```javascript
function calculate(op, x, y) {
    return op(x, y);
}

let multiply = function(a, b) {
    return a * b;
};

console.log(calculate(multiply, 5, 6));  // -> 30
console.log(calculate(sum, 8, 12));      // -> 20
```

### 3. Returning Functions

Functions can also return other functions. This technique enables the creation of customized functions.

```javascript
function getMultiplyBy(multiplier) {
    return function(a) {
        return a * multiplier;
    };
}

let multiplyBy3 = getMultiplyBy(3);
console.log(multiplyBy3(2));    // -> 6

console.log(getMultiplyBy(5)(10));  // -> 50
```

In this example, `getMultiplyBy` returns a function that multiplies any input by the specified multiplier. Calling `getMultiplyBy(3)` returns a function that multiplies by 3.

### Additional Examples of Returning Functions

1. **Creating Adders**

   ```javascript
   function getAdder(increment) {
       return function(x) {
           return x + increment;
       };
   }

   let addFive = getAdder(5);
   console.log(addFive(10));   // -> 15
   console.log(addFive(20));   // -> 25
   ```

   Here, `getAdder` returns a function that adds a specified increment to any input.

2. **Customizable Greeter**

   ```javascript
   function createGreeter(greeting) {
       return function(name) {
           return `${greeting}, ${name}!`;
       };
   }

   let sayHello = createGreeter("Hello");
   let sayGoodbye = createGreeter("Goodbye");

   console.log(sayHello("Alice"));     // -> Hello, Alice!
   console.log(sayGoodbye("Bob"));     // -> Goodbye, Bob!
   ```

   By returning functions, we create reusable, customizable functions.

### Benefits of First-Class Functions

- **Higher-Order Functions**: First-class functions enable higher-order functions, which are functions that accept or return other functions.
- **Modularity**: Functions can be created in one place and used elsewhere, promoting modular design.
- **Callbacks**: Passing functions as arguments enables the creation of callback patterns commonly used in asynchronous code.

JavaScript's first-class functions provide flexibility in coding, allowing for creative and efficient patterns.
---


# JavaScript Decorating Functions (Wrappers, Higher-Order Functions)

Decorators, or decorating functions, are higher-order functions that add extra behavior to existing functions without modifying them directly.

## 4.1.9 Decorating Functions Explained

A higher-order function takes another function as an argument or returns one. When a function wraps another and changes its behavior, it becomes a decorator.

### Basic Example of a Decorator

Consider a simple function `funA` that returns the sum of two numbers.

```javascript
let funA = function(a, b) {
    return a + b;
};

let decor = function(fn) {
    return function(arg1, arg2) {
        let result = fn(arg1, arg2);
        console.log(`result ${result}`);
        return result;
    };
};

let funB = decor(funA);
console.log(funA(3, 4)); // -> 7
funB(3, 4);              // -> result 7
```

The decorator `decor` wraps `funA`, adding a console message with the result. `funB` now performs the addition and logs the output.

### Use Case: Caching Results (Memoization)

Decorators can optimize functions by caching results. Below, we decorate a `factorial` function to store previously calculated results.

```javascript
let factorial = function (n) {
    return n > 1 ? factorial(n - 1) * n : 1;
};

let memoize = function(fn) {
    let cache = new Map();
    return function(n) {
        if (cache.has(n)) {
            console.log(`... found ${n} -> ${cache.get(n)}`);
            return cache.get(n);
        }
        let result = fn(n);
        cache.set(n, result);
        console.log(`... calc ${n} -> ${result}`);
        return result;
    };
};

let factorialCached = memoize(factorial);
factorialCached(5);  // -> ... calc 5 -> 120
factorialCached(5);  // -> ... found 5 -> 120
```

### More Examples of Decorators

1. **Timing Execution with `console.time`**

   ```javascript
   let timerDecorator = function(fn) {
       return function(...args) {
           console.time('Execution Time');
           let result = fn(...args);
           console.timeEnd('Execution Time');
           return result;
       };
   };

   let timedFactorial = timerDecorator(factorial);
   timedFactorial(5);  // -> Execution Time: (time in ms)
   ```

   This decorator adds a timer to measure function execution, making it useful for profiling.

2. **Debouncing**

   Debounce limits the rate at which a function executes. Useful for events like resizing a window.

   ```javascript
   function debounce(fn, delay) {
       let timeoutId;
       return function(...args) {
           clearTimeout(timeoutId);
           timeoutId = setTimeout(() => fn(...args), delay);
       };
   }

   window.onresize = debounce(() => console.log("Resized!"), 300);
   ```

   Only the last call after the delay will execute, ignoring intermediate calls.

3. **Throttling**

   Throttle limits how often a function can run within a given time frame.

   ```javascript
   function throttle(fn, interval) {
       let lastTime = 0;
       return function(...args) {
           let now = Date.now();
           if (now - lastTime >= interval) {
               fn(...args);
               lastTime = now;
           }
       };
   }

   let throttledResize = throttle(() => console.log("Resized!"), 1000);
   window.onresize = throttledResize;
   ```

   This example ensures `onresize` fires at most once every second.

### Benefits of Using Decorators

- **Code Reusability**: Decouples extra functionality from the core logic, making it reusable.
- **Optimization**: Memoization, debounce, and throttle improve performance in specific cases.
- **Extensibility**: Allows adding new behavior without altering the original function.

Decorators play a significant role in functional programming and are powerful for managing repeated patterns.
---

```javascript
// Basic Fibonacci function (without memoization)
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Memoization decorator for caching results
function memoize(fn) {
    const cache = new Map();
    return function(n) {
        if (cache.has(n)) {
            console.log(`... found ${n} -> ${cache.get(n)}`);
            return cache.get(n);
        }
        const result = fn(n);
        cache.set(n, result);
        console.log(`... calc ${n} -> ${result}`);
        return result;
    };
}

// Decorating the Fibonacci function with memoization
const memoizedFibonacci = memoize(fibonacci);

// Testing the memoized Fibonacci function
for (let i = 0; i < 10; i++) {
    console.log(`Fibonacci(${i}) = ${memoizedFibonacci(i)}`);
}
```
