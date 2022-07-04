# DOM
- Document Object Model (API)
- It is an interface for changing the content of a page

# Functions
- Traditional: `function name() {}`
- Function expression: `function () {}`
    - They are anonymous functions
- Arrow function: `() => {}`
    - They are compact and anonymous functions

# Promises
- Object that encapsulates the result of an asynchronous operation
  let asynchronous methods return values like synchronous methods
  "I promise to return something in the future"
- State can either be 'resolved' or 'rejected'
```Javascript
const promise = new Promise(async_func(resolve, reject))
promise.then(value => console.log(value)).catch(error => console.log(error))
```

# Async
- Makes a function return a Promise
- But does not have resolve or reject callbacks
```Javascript
async function loadFile() {if (fileLoaded) return 'File Loaded'}
loadFile().the(value => console.log(value)).catch(error => console.log(error))
```
# Await
- Makes an async function wait for a promise
- Await is only valid inside an async function
- Eliminates the use of methods like then() and catch()
```Javascript
async function loadFile() {if (fileLoaded) return 'File Loaded'}
async function startProcess(){let message = await loadFile()}
```
