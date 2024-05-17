# Enumerate a dictionary's keys and values
person = {'name': 'Aqib', 'age': 21, 'city': 'Peshawar'}
for index, (key, value) in enumerate(person.items()):
    print(f'Key: {key}, Value: {value}, Index: {index}')


# Enumerate a list of tuples
coordinates = [(10, 20), (30, 40), (50, 60)]
for index, (x, y) in enumerate(coordinates):
    print(f'Index: {index}, X: {x}, Y: {y}')


# Enumerate lines in a file
with open('example.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
        print(f'Line {index}: {line.strip()}')