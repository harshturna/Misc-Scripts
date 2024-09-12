const once = (func) => {
    let hasRun = false;
    let result;

    return (...args) => {
        if (!hasRun) {
            hasRun = true;
            result = func(...args);
        }
        return result;
    };
};

// usage

const greetOnce = once((name) => `Hello, ${name}!`);

console.log(greetOnce("Alice")); // Outputs: Hello, Alice!
console.log(greetOnce("Bob"));   // Still outputs: Hello, Alice!
