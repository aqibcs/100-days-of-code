# Python Sets
Sets are unordered collection od data items. They store multiple items in a single variable.
Set items are separated by commas and enclosed within curly brackets { }. Sets are unchangeable, meaning you cannot change items of the set once created.
Sets do not contain duplicate items.

### Example:
```python
info = {"Carla", 19, False, 5.9, 19}
print(info)
```

### Output
```bash
{False, 19, 5.9, 'Carla'}
```
Here we see that items of set occur in random order and hence they cannot be accessed using index number.
Also, sets do no allow duplicate values.

### Example:
```python
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
```

### Output:
```bash
False
Carla
19
5.9
```