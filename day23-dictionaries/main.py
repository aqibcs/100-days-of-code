# 1.Accessing Dictionary items:
# Accessing single values
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
print(info['name']) # Output: Aqib

print(info.get('age')) # Output: 21

# Accessing multiple values
print(info.values()) # Output: dict_values(['Aqib', 21, True])

# Accessing keys
print(info.keys())  # Output: dict_keys(['name', 'age', 'eligible'])

# Accessing key-value pairs
print(info.items()) # Output: dict_items([('name', 'Aqib'), ('age', 21), ('eligible', True)])


# 2.Dictionary Methods
# Update method
info = {'name': 'Aqib', 'age': 21, 'eligible': True}
info.update({'age': 22}) # Update age value
info.update({'DOB': 2002}) # Add new key-value pairs
print(info) # Output: {'name': 'Aqib', 'age': 22, 'eligible': True, 'DOB': 2002}

# Removing items
info.clear()
print(info) # Output: {}

info = {'name': 'Aqib', 'age': 21, 'eligible': True}
info.pop('eligible') # Remove 'eligible' key
print(info) # Output: {'name': 'Aqib', 'age': 21}

info = {'name': 'Aqib', 'age': 21, 'DOB': 2002, 'eligible': True}
info.popitem() # Remove last key-value pair
print(info) # Output: {'name': 'Aqib', 'age': 21, 'DOB': 2001}

# Using del keyword
del info['age']
print(info)  # Output: {'name': 'Aqib', 'eligible': True}