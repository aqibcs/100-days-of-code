# Introduction to Loops
Sometimes a programmer want to execute a group of statements a cerian number of times. This can be done using loops. Based on this loops are further classified into following main types:
- for loop
- while loop

## The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets, and dictionaries.

### Example: iterating over a string:
```python
name = "aqib"
for i in name:
    print(i, end=" ")
```

### Example: iterating over List:
```python
colors = ['green', 'blue', 'red', 'orange']
for i in colors:
    print(i)
```

## range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

### Example:
```python
for k in range(5):
    print(k)
```

### Output:
```bash
0
1
2
3
4
```
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

### Example:
```python
for k in range(4, 9):
    print(k)
```

### Output:
```bash
4
5
6
7
8
```