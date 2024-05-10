# Python Lists:
- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets[].
- Lists are changeable meaning we can alter them after creation.

### Example 1:
```python
lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = ["blue", "red", "green"]
print(lst1)
print(lst2)
```

### Output:
```bash
[1, 2, 2, 3, 5, 4, 6, 7]
["blue", "red", "green"]
```

# List Comprehension
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

## Syntax:
List = [Expression(item) for item in iterable if Condition]

**Expression**: It is the item which is being iterated.

**Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

**Condition**: Condition checks if the item should be added to the new list or not. 

### Example 1: Accepts items with the small letter “o” in the new list 
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```
### Output:
```
['Milo', 'Bruno', 'Rosa']
 ```

### Example 2: Accepts items which have more than 4 letters
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```
### Output:
```
['Sarah', 'Bruno', 'Anastasia']
```