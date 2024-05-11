# Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

### Example:
```python
countries = ("Pakistan", "Japan", "Italy", "England")
temp = list(countries)
temp.append("Germany")
temp.pop(2)
temp[1] = "Bangladesh"
countries = tuple(temp)
print(countries)
```

### Output:
```bash
('Pakistan', 'Bangladesh', 'England', 'Germany')
```
Thus, we convert the tuple to a list, manipulate items of the list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.

### Example:
```python
countries = ("Pakistan", "Japan", "Italy", "England")
countries2 = ("China", "Afghanistan")
Asia = countries + countries2
print(Asia)
```

### Output:
```bash
('Pakistan', 'Japan', 'Italy', 'England', 'China', 'Afghanistan')
```

# Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods. They are explained below:

## Count() Method:
The count() method of Tuple returns the number of times the given element appears in the tuple.

### Syntax:
```python
tuple.count(element)
```

### Example:
```python
Tuple1 = (0, 1, 2, 3, 2, 3, 3, 2, 1, 2)
res = Tuple1.count(2)
print('Count of 2 in Tuple1 is:', res)
```
### Output:
```bash
Count of 2 in Tuple1 is: 4
```

## Index() method
The index() method returns the first occurrence of the given element from the tuple.

### Syntax:
```python
tuple.index(element, start, end)
```
**Note:** This method raises a ValueError if the element is not found is the tuple.

### Example:
```python
Tuple = (0, 1, 3, 4, 3, 2, 4, 2)
res = Tuple.index(2)
print('First occurrence of 2 is', res)
```

### Output:
```bash
First occurrence of 2 is 5
```