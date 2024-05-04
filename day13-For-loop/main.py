# Iterating over string
name = "Aqib"
for i in name:
    print(i)

# Iterating over List
colors = ['green', 'blue', 'red', 'orange']
for i in colors:
    print(i)


# Looping from 0 to 10 with a step of 2
for i in range(0, 10, 2):
    print(i)


# Loop from 10 to 0 in reverse
for i in range(10, 0, -1):
    print(i)

# Nested Loop to create a multiplication table
for i in range(1, 5):
    for j in range(1, 5):
        print(i * j, end="\t")
    print()


"""Example: Using Enumerate:
The enumerate() function can be used within a for loop 
to get both the index and the value of items in a sequence."""
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
