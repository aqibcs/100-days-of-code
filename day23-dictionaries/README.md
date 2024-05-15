# Python Dictionaries
`Dictionaries` are ordered collection of data items. They store multiple items in a single variable.
`Dictionary` items are key-value pairs that are separated by commas and enclosed by curly brackets {}.

### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info)
```
### Output:
```bash
{'name': 'Aqib', 'age': 21, 'eligible': True}
```

## Accessing Dictionary items:
### 1. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning key either in square brackets or by using get methods.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info)
print(info.get('eligible'))
```
#### Output:
```bash
Aqib
True
```

### 2. Accessing multiple values:
We can print all the values in the dictionary using values() method.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info.values())
```
#### Output:
```bash
dict_values(['Aqib', 21, True])
```

### 3. Accessing keys:
We can print all the keys in the dictionary using keys() method.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info.keys())
```
#### Output:
```bash
dict_keys(['name', 'age', 'eligible'])
```
### 4. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info.items())
```
#### Output:
```bash
dict_items([('name': 'Aqib', 'age': 21, 'eligible': True)])
```

# Dictionary Methods
Dictionary uses several built-in methods for manipulation. They are listed below.

## Update():
The `update()` method updates the values of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info)
info.update({'age': 22})
info.update({'DOB': 2002})
print(info)
```
### Output:
```bash
{'name': 'Aqib', 'age': 21, 'eligible': True}
{'name': 'Aqib', 'age': 22, 'eligible': True, 'DOB': 2002}
```
## Removing items from dictionary:
There are a few methods that we can use to remove items from dictionary.

### clear():
The `clear()` method removes all the items from the list.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
info.clear()
print(info)
```
#### Output:
```bash
{}
```
### pop():
The `pop()` method removes the key-value pair whose key is passed as a parameter.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
info.pop('eligible')
print(info)
```
#### Output:
```bash
{'name': 'Aqib', 'age': 21}
```

### popitem():
The `popitem()` method removes the last key-value pair from the dictionary.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True, 'DOB': 2002}
info.popitem()
print(info)
```
#### Output:
```bash
{'name': 'Aqib', 'age': 21, 'eligible': True}
```

### del:
We can also use the `del` keyword to remove a dictionary item.

#### Example:
```python
info = {'name': 'Aqib', 'age': 21, 'eligible': True, 'DOB': 2002}
del info
print(info)
```
#### Output:
```bash
NameError: name 'info' is not defined
```