# Example 1: Concatenating Tuples
# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate the two tuples
concatenating_tuple = tuple1 + tuple2
print(concatenating_tuple)


# Example 2: Accessing Tuple Elements
# Define a tuple
my_tuple = ('apple', 'banana', 'cherry', 'date')

# Access elements by index
first_element = my_tuple[0]
last_element = my_tuple[-1]

print("First element:", first_element)
print("Last element: ", last_element)


# Example 3: Slicing Tuples
# Define a tuple
number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice the tuple to get a subset
subset_tuple = number_tuple[2:7]
print(subset_tuple)


# Examples for count() Method:
Tuple3 = ('Apple', 'banana', 'cherry', 'banana', 'apple')
count_banana = Tuple3.count('banana')
print('Count of banana in Tuple3 is:', count_banana)


# Examples for index() Method:
Tuple4 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
index_f = Tuple4.index('f')
print("Index of f in Tuple4 is:", Tuple4)
