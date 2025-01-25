#!/usr/bin/node

// Define the function to add two integers
const add = (a, b) => a + b;

// Convert arguments to integers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Print the result of addition
console.log(add(a, b));
