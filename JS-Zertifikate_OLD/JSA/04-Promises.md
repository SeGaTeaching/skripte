
# Promises in Asynchronous JavaScript

## 4.3.4 Understanding Promises

### The Problem with Callbacks

Callback functions, while effective, can lead to "callback hell" when handling multiple asynchronous events that depend on one another. This results in deeply nested code that is hard to read and maintain.

### What is a Promise?

A **Promise** is an object that represents the eventual result (or failure) of an asynchronous operation. It has three possible states:

- **Pending**: The initial state, neither fulfilled nor rejected.
- **Fulfilled**: The operation was completed successfully.
- **Rejected**: The operation failed.

Promises provide a more structured way to handle asynchronous actions, enabling better code readability and easier management.

### Creating a Promise

We create a promise using the `Promise` constructor and an executor function, which takes two callbacks as arguments: `resolve` and `reject`.

#### Example 1: Basic Promise

```javascript
let p = new Promise((resolve, reject) => {
    resolve("Data Loaded");
});

p.then((result) => console.log(result));  // Output: Data Loaded
```

### Explanation

- **Promise Creation**: A promise `p` is created, and `resolve` is immediately called with "Data Loaded".
- **then Method**: `then` is used to access the promise’s result once it is fulfilled.

---

### Example 2: Promise with a Delay

Here, `setTimeout` creates a delay before resolving.

```javascript
let delayedPromise = new Promise((resolve) => {
    setTimeout(() => {
        resolve("Resolved after 2 seconds");
    }, 2000);
});

delayedPromise.then((message) => console.log(message));
```

### Explanation

The promise resolves after 2 seconds, simulating an asynchronous operation.

---

### Example 3: Handling Errors with `catch`

Using `catch`, we handle errors in the promise.

```javascript
let errorPromise = new Promise((resolve, reject) => {
    reject("Something went wrong");
});

errorPromise
    .then((data) => console.log(data))
    .catch((error) => console.log(`Error: ${error}`));
```

### Explanation

The `catch` method captures and handles rejected promises, allowing for graceful error management.

---

### Example 4: Chaining Promises

Promises can be chained, allowing sequential execution of asynchronous tasks.

```javascript
let chainPromise = new Promise((resolve) => {
    resolve(1);
});

chainPromise
    .then((result) => result * 2)
    .then((result) => result * 3)
    .then((result) => console.log(result));  // Output: 6
```

### Explanation

Each `then` in the chain modifies the result, showing the ease of chaining in promises.

---

### Example 5: Using `finally` with Promises

`finally` is executed regardless of whether the promise is fulfilled or rejected.

```javascript
let finalPromise = new Promise((resolve) => {
    setTimeout(() => resolve("Promise Settled"), 1000);
});

finalPromise
    .then((result) => console.log(result))
    .finally(() => console.log("Operation complete"));
```

### Explanation

The `finally` method runs after the promise settles, irrespective of the outcome, making it useful for cleanup tasks.

---

## Advanced Promise Methods

### `Promise.all`

Executes after all promises in an array are fulfilled.

```javascript
let p1 = new Promise(resolve => setTimeout(() => resolve(1), 1000));
let p2 = new Promise(resolve => setTimeout(() => resolve(2), 2000));
let p3 = new Promise(resolve => setTimeout(() => resolve(3), 3000));

Promise.all([p1, p2, p3]).then(results => console.log(results));  // Output: [1, 2, 3]
```

### `Promise.race`

Executes when the first promise in an array is fulfilled.

```javascript
Promise.race([p1, p2, p3]).then(result => console.log(result));  // Output: 1
```

### Explanation

- `Promise.all` waits for all promises to resolve, while `Promise.race` resolves or rejects as soon as the first promise settles.

## Practical Example: Fetching Data

This example shows using `fetch` with promises to handle HTTP requests:

```javascript
const value = 200;
fetch(`http://localhost:3000/json?value=${value}`)
    .then(response => response.json())
    .then(data => {
        console.log(`server: ${value} * ${value} = ${data.square} (${data.time}ms)`);
    })
    .catch(error => console.log(`Error: ${error}`));
```

### Explanation

`fetch` returns a promise, which we handle using `then` for success and `catch` for errors. This approach provides a clean, readable structure for handling HTTP requests.

---

### Final Notes

Using promises allows for more readable, maintainable code and can handle multiple asynchronous actions with clarity. Promises are crucial in JavaScript for any operation that doesn’t complete instantly.


# Async/Await in JavaScript

## 4.3.5 A Simpler Approach to Promises

### What is Async/Await?

The `async` and `await` keywords in JavaScript offer a simplified approach to handling promises. This structure resembles synchronous code, making it easier to read and manage, especially when dealing with multiple asynchronous operations.

- **`async`**: Marks a function as asynchronous, allowing the use of `await` inside it.
- **`await`**: Pauses the execution of the `async` function until the promise is resolved, returning the final result.

### Basic Example of Async/Await

Let's look at a basic example to understand how `async` and `await` work together.

```javascript
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Data fetched"), 1000);
    });
}

async function getData() {
    console.log("Fetching data...");
    const result = await fetchData();
    console.log(result);
}

getData();
console.log("Operation started");
```

### Explanation

1. **Function Creation**: `fetchData` returns a promise that resolves after 1 second.
2. **Using Async/Await**: `await` pauses `getData` until `fetchData` is fulfilled, so "Data fetched" appears only after 1 second.

### Console Output

```
Fetching data...
Operation started
Data fetched
```

---

## Example 1: Sequential Async Operations

With async/await, sequential operations become straightforward.

```javascript
function delay(value, time) {
    return new Promise(resolve => setTimeout(() => resolve(value), time));
}

async function sequentialOperations() {
    const first = await delay("First", 1000);
    console.log(first);

    const second = await delay("Second", 2000);
    console.log(second);

    const third = await delay("Third", 1000);
    console.log(third);
}

sequentialOperations();
```

### Explanation

Each `await` pauses execution until the previous promise resolves, ensuring sequential order.

### Output

```
First
Second
Third
```

---

## Example 2: Fetching Data with Async/Await

The `fetch` API works seamlessly with async/await for HTTP requests.

```javascript
async function fetchData() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

fetchData();
```

### Explanation

- **Error Handling**: Using `try...catch`, we handle errors in a clean and readable way.

### Output

```
{ id: 1, title: "Sample Title", body: "Sample Body", ... }
```

---

## Example 3: Using Multiple Await Statements in a Loop

Async/await also works effectively within loops, allowing sequential asynchronous calls.

```javascript
const fetchPost = async (id) => {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
    return await response.json();
};

async function fetchPosts() {
    for (let i = 1; i <= 3; i++) {
        const post = await fetchPost(i);
        console.log(`Post ${i}:`, post);
    }
}

fetchPosts();
```

### Explanation

Each `await` inside the loop waits for the promise to resolve, fetching each post sequentially.

---

## Example 4: Parallel Execution with Promise.all

Using `Promise.all`, we can perform asynchronous tasks in parallel with async/await.

```javascript
async function parallelFetch() {
    const [post1, post2, post3] = await Promise.all([
        fetchPost(1),
        fetchPost(2),
        fetchPost(3),
    ]);
    console.log(post1, post2, post3);
}

parallelFetch();
```

### Explanation

`Promise.all` allows us to fetch all posts simultaneously, reducing wait time compared to sequential execution.

---

## Example 5: Handling Rejected Promises with Async/Await

Using `try...catch`, we can manage rejected promises more gracefully.

```javascript
function fetchWithError() {
    return new Promise((_, reject) => {
        setTimeout(() => reject("Fetch failed"), 1000);
    });
}

async function handleError() {
    try {
        await fetchWithError();
    } catch (error) {
        console.error("Caught an error:", error);
    }
}

handleError();
```

### Explanation

The `try...catch` block catches errors, preventing unhandled promise rejections.

---

## Example 6: Using Async/Await for Conditional Async Operations

Async functions can be used conditionally.

```javascript
async function conditionalFetch(fetchData) {
    if (fetchData) {
        const data = await fetchData();
        console.log("Data:", data);
    } else {
        console.log("No data to fetch");
    }
}

conditionalFetch(() => delay("Conditional Data", 1000));
```

---

## Final Notes

The `async/await` syntax provides a clean, readable structure to work with asynchronous code in JavaScript, making it simpler to maintain than traditional promise chains.
