# Regular function to double the input
def double(x):
    return x * 2

# Lambda function to double the input
double_lambda = lambda x: x * 2

# Using the functions
print(double(5))         # Output: 10
print(double_lambda(5))  # Output: 10


# Regular function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
multiply_lambda = lambda x, y: x * y

# Using the functions
print(multiply(5, 3))         # Output: 15
print(multiply_lambda(5, 3))  # Output: 15


# Regular function to square a number
def square(x):
    return x ** 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map with a regular function
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using map with a lambda function
squared_numbers_lambda = list(map(lambda x: x ** 2, numbers))
print(squared_numbers_lambda)  # Output: [1, 4, 9, 16, 25]


# Regular function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Using filter with a regular function
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

# Using filter with a lambda function
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_lambda)  # Output: [2, 4]


from functools import reduce

# Regular function to add two numbers
def add(x, y):
    return x + y

# Using reduce with a regular function
sum_numbers = reduce(add, numbers)
print(sum_numbers)  # Output: 15

# Using reduce with a lambda function
sum_numbers_lambda = reduce(lambda x, y: x + y, numbers)
print(sum_numbers_lambda)  # Output: 15
