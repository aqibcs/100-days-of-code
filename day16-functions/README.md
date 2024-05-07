# Python Function
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of function:
1. Built-in functions
2. User-defined functions

## Built-in functions:
These function are defined and pre-coded in python. Some examples of built-in functions are as follows:
- min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), print(), etc.

## User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

### Syntax:
```python
def function_name(parameters):
    pass
    # Code and Statements
```
- Create a function using the def keyword, followed by a function name, followed by a parenthesis (()), and a colon(:).
- Any parameters and arguments should be placed within the parenthesis.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

## Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

### Example:
```python
def name(first_name, last_name):
    print("Hello,", first_name, last_name)

name("Same", "Wilson")
```

### Output:
```bash
Hello, Same Wilson
```