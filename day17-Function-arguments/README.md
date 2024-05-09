# Function Arguments and return statement
There are four types of arguments that we can provide in a function:
- Default Arguments
- Keyword Arguments
- Variable Length Arguments
- Required Arguments

## Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provide in the function call for that argument.

### Example:
```python
def name(first_name, middle_name = "Jhon", last_name = "Whatson"):
    print("Hello,", first_name, middle_name, last_name)

name("Amy")
```
### Output
```bash
Hello, Amy Jhon Whatson
```

## Keyword arguments:
We can provide arguments with key = value, this way interpreter recognizes the arguments by the parameter name.

Hence, the order in which the arguments are passed does not matter.
### Example:
```python
def name(first_name, middle_name, last_name):
    print("Hello,", first_name, middle_name, last_name)

name(middle_name = "Peter", last_name = "Wesker", first_name = "Jade")
```
### Output:
```bash
Hello, Jade Peter Wesker
```

## Required arguments:
In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

**Example 1:**  When number of arguments passed does not match to the actual function definition.

```python
def name(first_name, middle_name, last_name):
    print("Hello,", first_name, middle_name, last_name)

name("Peter", "Quill")
```
### Output:
```bash
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'last_name'
```

**Example 1:** when number of arguments passed matches to the actual function definition.
```python
def name(first_name, middle_name, last_name):
    print("Hello,", first_name, middle_name, last_name)

name("Peter", "Ego", "Quill")
```
### Output:
```bash
Hello, Peter Ego Quill
```

## Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

### Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

#### Example:
```python
def name(*name):
    print("Hello," name[0], name[1], name[2])

print("James", "Buchanan", "Barnes")
```
#### Output:
```bash
Hello,  James Buchanan Barnes
```

### Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

#### Example:
```python
def name(**name):
    print("Hello,", name["first_name"], name["middle_name"], name["last_name"])

name(middle_name = "Buchanan", last_name = "Barnes", first_name = "Jame")
```
#### Output:
```bash
Hello, James Buchanan Barnes
```

## Return statement:
The return statement is used to return the value of the expression back to the calling function.

#### Example:
```python
def name(first_name, middle_name, last_name):
    return "Hello, " + first_name + " " + middle_name + " " + last_name

print(name("james", "Buchanan", "Barnes"))
```

#### Output:
```bash
Hello, James Buchanan Barnes
```