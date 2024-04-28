# Day-5: Variables and Data Types

## What is Variable?
A variable is like a container that holds data, much like how our kitchen containers hold sugar, salt, etc. Creating a variable is akin to creating a placeholder in memory and assigning it a value. In Python, it's as easy as writing:
```python
a = 1
b = True
c = "Aqib"
d = None
```
These are four variables of different data types.

## What is a Date Type?
A data type specifies the type of value a variable holds. This is necessary in programming to perform various operations without causing errors. In Python, we can print the type of any object using the `type` function:
```python
a = 1
print(type(a))

b = "1"
print(type(b))
```
By default, python provides the following built-in data types:

1. Numeric data: int, float, complex
    - int: 3, -9, 0
    - float: 2.23, -9.34, 0.2
    - complex: 6 + 2i

2. Text data: str
    - str: "Hello World!", "Python Programming"

3. Boolean data:
    - Boolean data consists of values True or False.

4. Sequenced data: list, tuple
**List:**  A list is an ordered collection of data with elements separated by commas and enclosed within square brackets. Lists are mutable and can be modified after creation.
### Example:
```python
list1 = [2, 4.1, [-3, 7], ["apple", "banana"]]
print(list1)
```
### Output:
```bash
[2, 4.1, [-3, 7], ["apple", "banana"]]
```

**Tuple:** A tuple is an ordered collection of data with elements separated by commas and enclosed within parentheses. Tuples are immutable and cannot be modified after creation.
### Example:
```python
tuple1 = (("parrot", "sparrow"), ("lion", "tiger"))
print(tuple1)
```
### Output:
```bash
(("parrot", "sparrow"), ("lion", "tiger"))
```

5. Mapped data: dict
**dict:** A dictionary is an unordered collection of data containing a key:value pair, The key:value pairs are enclosed within curly brackets.
### Example:
```python
dict1 = {"name": "Aqib", "age": 22, "canVote": True}
print(dict1)
```
### Output:
```bash
{"name": "Aqib", "age": 22, "canVote": True}
```

