# Default Arguments Example:
# Define a function with default arguments
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# call the function without specifying the greeting
greet_user("Alice")


# Keyword Arguments Example:
# Define a function with keyword arguments
def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Call the function using keyword arguments
print_details(name="Alice", age=25, city="New York")


# Required Arguments Example:
# Define a function with required arguments
def add_numbers(a, b):
    return a + b

# Call the function with the correct number of arguments
result = add_numbers(5, 10)
print("Sum: ", result)

# This will raise an error because the required number of arguments is missing
# add_numbers(5)


# Variable-length Arguments (Arbitrary Arguments) Example:
# Define a function with arbitrary arguments
def print_names(*names):
    for name in names:
        print(name)

# Call the function with multiple arguments
print_names("Alice", "Bob", "Charlie", "David")


# Keyword Arbitrary Arguments Example:
# Define a function with keyword arbitrary arguments
def print_person_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments
print_person_details(name="Alice", age=30, city="New York")


# Return Statement Example:
def calculate_square(number):
    return number * number

# Call the function and store the result
result = calculate_square(4)
print("Square:", result)
