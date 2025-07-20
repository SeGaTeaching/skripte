
# Asynchronous Programming in JavaScript

## 4.3.1 Introduction to Asynchronous Programming

This section introduces **asynchronous programming** in JavaScript, with a focus on using the `XMLHttpRequest` object and the `fetch` method. We provide a simple server setup using Node.js and Express to demonstrate these concepts in practice.

Below is the sample server setup:

```javascript
var express = require("express");
var cors = require("cors");
var app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors({ origin: '*' }));

const sleep = (waitTimeInMs) => new Promise(resolve => setTimeout(resolve, waitTimeInMs));

app.get("/", (req, res, next) => {
  res.send(`<!DOCTYPE html><html><body><h1>Sample Site</h1></body></html>`);
});

app.get("/json", async (req, res, next) => {
  const time = Math.floor(Math.random() * 1000) + 1000;
  let square = req.query.value || 0;
  square *= square;
  await sleep(time);
  res.json({
    'time': time,
    'square': square
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

### Server Description

- **Endpoint**: Runs on `http://localhost:3000`.
- **Main Functionality**:
  - An empty HTML page for demonstration.
  - A JSON endpoint (`/json`) that takes a `value` parameter, squares it, and returns the result with a random delay between 1000 to 2000 milliseconds.
  
### How to Use
Start the server and access `http://localhost:3000` in your browser. You can then test `XMLHttpRequest` and `fetch` examples directly from the console.

## 4.3.2 Why Do We Need Asynchronous Techniques?

### Synchronous vs Asynchronous Execution

- **Synchronous Execution**: Tasks are executed one after the other, waiting for each task to finish before starting the next. While simple and intuitive, this approach can cause delays when waiting for external data, like a database query.
- **Asynchronous Execution**: Allows certain tasks to start before the previous tasks complete. This can be beneficial when tasks involve waiting for external resources.

Consider the following synchronous example:

```javascript
let showInfo = result => {
  let info = "the arguments are equal";
  if(result > 0) {
    info = "the first argument is greater";
  } else if (result < 0) {
    info = "the second argument is greater";
  }
  console.log(info);
}

let compareSync = (a, b, fn) => {
  let r = a - b;
  fn(r);
}

console.log("start");
compareSync(10, 5, showInfo);
console.log("end");
```

### Explanation

In this code:
- `showInfo` displays a message based on the `result`.
- `compareSync` calculates the difference and calls `showInfo`.

**Output**:

```
start
the first argument is greater
end
```

Since the code executes in sequence, it’s a synchronous example.

### Asynchronous Example with `setTimeout`

Let’s make the function asynchronous using `setTimeout`:

```javascript
let showInfo = result => {
  let info = "the arguments are equal";
  if(result > 0) {
    info = "the first argument is greater";
  } else if (result < 0) {
    info = "the second argument is greater";
  }
  console.log(info);
}

let compareAsync = (a, b, fn) => {
  let r = a - b;
  setTimeout(fn, 1000, r);
}

console.log("start");
compareAsync(10, 5, showInfo);
console.log("end");
```

**Output**:

```
start
end
the first argument is greater
```

### Explanation of the Asynchronous Behavior

In `compareAsync`, the function ends immediately after calling `setTimeout`, allowing the program to proceed with `console.log("end")`. After 1000 milliseconds, the function `showInfo` runs and logs the result.

This demonstrates **asynchronicity**, where function execution timing depends on events rather than strict code order.

# Callback Functions in Asynchronous JavaScript

## 4.3.3 Understanding Callback Functions

### Overview

In asynchronous programming, callback functions are an essential concept. They allow us to handle responses from processes that take time to complete, such as retrieving data from a server.

In this section, we explore how JavaScript handles asynchronous data retrieval using callback functions, focusing on the `XMLHttpRequest` object.

### What is a Callback Function?

A **callback function** is a function passed into another function as an argument. The callback is then invoked within the outer function to complete some kind of action. This pattern is especially useful in asynchronous operations, where we don’t want the code execution to stop while waiting for a response.

### Example: Using XMLHttpRequest with a Callback

Here’s a step-by-step example using `XMLHttpRequest` to retrieve data from a server asynchronously:

```javascript
const value = 200;
let request = new XMLHttpRequest();

// Defining a callback function to handle the response
let responseLoaded = () => {
    if (request.status === 200) {
        const resp = JSON.parse(request.responseText);
        console.log(`server: ${value} * ${value} = ${resp.square} (${resp.time}ms)`);
    }
}

// Attaching the callback to the request's 'load' event
request.onload = responseLoaded;
request.open('GET', `http://localhost:3000/json?value=${value}`);
request.send();

console.log(`browser: ${value} * ${value} = ${value * value}`);
```

### Explanation

1. **Initialization**: We create an instance of `XMLHttpRequest` using `new XMLHttpRequest()`.
2. **Defining the Callback**: The `responseLoaded` function acts as a callback, processing the server’s response.
3. **Attaching the Callback**: We set `request.onload = responseLoaded;` so that once the data is loaded, the callback function executes.
4. **Sending the Request**: The `request.send()` method initiates the asynchronous request, allowing the rest of the code to execute without waiting.

### Output

```
browser: 200 * 200 = 40000
server: 200 * 200 = 40000 (1577ms)
```

The **first message** appears immediately, calculated by the browser. The **second message** comes from the server response after a short delay.

## Additional Example: Simplified Callback Functions

### Example: Asynchronous Square Calculation

This example uses `setTimeout` to simulate a delayed operation:

```javascript
let squareAsync = (num, callback) => {
    setTimeout(() => {
        let result = num * num;
        callback(result);
    }, 1000); // Delays by 1 second
}

squareAsync(5, (result) => {
    console.log(`The square is: ${result}`);
});
```

### Explanation

1. **Function Definition**: `squareAsync` accepts two parameters – the number to square (`num`) and a callback function.
2. **Asynchronous Operation**: Inside `squareAsync`, `setTimeout` delays the squaring calculation by 1000ms.
3. **Callback Invocation**: The callback function receives the result and logs it.

### Output

```
The square is: 25
```

This example demonstrates how **callback functions** can handle delayed responses.

## Using `addEventListener` with Callback Functions

Instead of setting `request.onload`, we can use `addEventListener` to attach the callback:

```javascript
request.addEventListener("load", () => {
    if (request.status === 200) {
        const resp = JSON.parse(request.responseText);
        console.log(`server: ${value} * ${value} = ${resp.square} (${resp.time}ms)`);
    }
});
```

### Explanation

- The `addEventListener` method binds the callback function to the "load" event.
- This approach offers flexibility as multiple callbacks can be added to the same event.

### Final Example: Nested Callbacks (Callback Hell)

When callbacks depend on each other, they can become deeply nested, leading to “callback hell.” Here’s an example:

```javascript
function fetchData(callback) {
    setTimeout(() => {
        console.log("Data fetched");
        callback();
    }, 1000);
}

function processData(callback) {
    setTimeout(() => {
        console.log("Data processed");
        callback();
    }, 1000);
}

function displayData() {
    setTimeout(() => {
        console.log("Data displayed");
    }, 1000);
}

// Executing nested callbacks
fetchData(() => {
    processData(() => {
        displayData();
    });
});
```

### Explanation

In this example, each function waits for the previous one to complete. Although it achieves the task, this approach can become unwieldy in complex code.

### Output

```
Data fetched
Data processed
Data displayed
```

This structure illustrates how nested callbacks can quickly become challenging to manage, motivating the use of **Promises** or **Async/Await** for better readability.

Using `setTimeout` with a callback allows us to simulate a delayed greeting message.

```javascript
function greetUser(name, callback) {
    setTimeout(() => {
        callback(`Hello, ${name}!`);
    }, 2000);
}

greetUser("Alice", (message) => {
    console.log(message);
});
```

```javascript
function calculate(a, b, operation) {
    return operation(a, b);
}

function add(x, y) {
    return x + y;
}

function multiply(x, y) {
    return x * y;
}

console.log(calculate(5, 10, add)); // Output: 15
console.log(calculate(5, 10, multiply)); // Output: 50
```