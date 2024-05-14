# Joining Sets
Sets in python more or less work in the same way as sets in mathematics.
We can perform operations like union and intersection on the sets just like in mathematics.

## 1. union() and update():
The `union()` and `update()` methods prints all items that are present in the two sets.
The `union()` methods returns a new set whereas `update()` method add items into the existing set from another set.


### Example:
```python
cities = {"Islamabad", "Berlin", "New York"}
cities2 = {"Islamabad", "Kabul", "Karachi"}
cities3 = cities.union(cities2)
print(cities3)
```

### Output:
```bash
{'Berlin', 'New York', 'Kabul', 'Karachi', 'Islamabad'}
```

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Karachi"}
cities2 = {"Islamabad", "Kabul", "Karachi", "Lahore"}
cities.update(cities2)
print(cities)
```

### Output:
```bash
{'Islamabad', 'Berlin', 'Kabul', 'New York', 'Karachi', 'Lahore'}
```

## 2. intersection and intersection_update():
The `intersection()` and `intersection_update()` methods prints only items that similar to both the sets.
The `intersection()` method returns a new set whereas `intersection_update()` method updates into the existing set from another set.

### Example:
```python
cities = {"Islamabad", "Berlin", "New York"}
cities2 = {"Islamabad", "Kabul", "Karachi"}
cities.intersection(cities2)
print(cities)
```

### Output:
```bash
{'Berlin', 'Islamabad', 'New York'}
```

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Delhi"}
cities2 = {"Islamabad", "Kabul", "Karachi", "Berlin"}
cities.intersection_update(cities2)
print(cities)
```

### Output:
```bash
{'Islamabad', 'Berlin'}
```


## 3. symmetric_difference and symmetric_difference_update():
The `symmetric_diiferenc` and `symmetric_difference_update()` methods prints only items that are not similar to both the sets.
The `symmetric_difference` methods returns a new whereas   `symmetric_difference_update()` method update into the existing set from another set.

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Delhi"}
cities2 = {"Islamabad", "Kabul", "Karachi", "Berlin"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```

### Ouput:
```bash
{'New York', 'Kabul', 'Karachi', 'Delhi'}
```

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Delhi"}
cities2 = {"Islamabad", "Kabul", "Karachi", "Berlin"}
cities.symmetric_difference_update(cities2)
print(cities)
```

### Output:
```bash
{'Karachi', 'Kabul', 'New York', 'Delhi'}
```

## 4. difference() and difference_update():
The `difference()` and `difference_update()` methods prints only items that are only present in the original set and not in both the sets.
The `difference()` methods returns a new set whereas `difference_update()` method updates into the existing set from another set.

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Delhi"}
cities2 = {"Islamabad", "Kabul", "Karachi"}
cities3 = cities.difference(cities2)
print(cities3)
```

### Output:
```bash
{'Berlin', 'New York', 'Delhi'}
```

### Example:
```python
cities = {"Islamabad", "Berlin", "New York", "Delhi"}
cities2 = {"Islamabad", "Kabul", "Karachi"}
print(cities.difference(cities2))
```
### Output:
```bash
{'Delhi', 'New York', 'Berlin'}
```