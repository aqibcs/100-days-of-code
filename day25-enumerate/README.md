# Enumerate function in python
The `enumerate` function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string)
and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

### Example:
```python
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
### Output:
```bash
0 apple
1 banana
2 mango
```
The `enumerate` function returns a tuple containing the index and value of each element in the sequence.
You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

# Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:
### Example:
```python
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```
### Output:
```bash
1 apple
2 banana
3 mango
```
The `enumerate` function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:
### Example:
```python
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
```
### Output:
```bash
1: apple
2: banana
3: mango
```
In addition to lists, you can use the enumerate function with any other sequence type in Python,
such as tuples and strings. Here's an example with a tuple:
### Example:
```python
# Loop over a tuple and print the index and value of each element
colors = ('red', 'blue', 'orange')
for index, color in enumerate(colors):
    print(index, color)
```

### Example with a string:
```python
# Loop over a string and print the index and value of each character
s = 'Hello'
for index, c in enumerate(s):
    print(index, c)
```
