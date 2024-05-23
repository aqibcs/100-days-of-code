# Example 1: Local and Global Variables
"""In this example, we will see how local and global variables are defined and accessed."""
# Global variable
count = 0


def increment():
    # Local variable
    count = 1
    print("Inside increment(), local count:", count)


def decrement():
    # Local variable
    count = -1
    print("Inside decrement(), local count:", count)


increment()  # Output: Inside increment(), local count: 1
decrement()  # Output: Inside decrement(), local count: -1
print("Outside functions, global count:", count)  # Output: Outside functions, global count: 0


# Example 2: Using the `global` Keyword
"""This example demonstrates how to use the `global` keyword to modify a global variable within a function."""
# Global variable
total = 100


def add_to_total(amount):
    global total
    total += amount
    print("Inside add_to_total(), global total:", total)


add_to_total(50)  # Output: Inside add_to_total(), global total: 150
print("Outside add_to_total(), global total:", total)  # Output: Outside add_to_total(), global total: 150


# Example 3: global with Multiple Variables
"""This example shows how to use the `global` keyword with multiple variables."""
# Global variables
a = 10
b = 20


def update_globals():
    global a, b
    a = 15
    b = 30
    print("Inside update_globals(), a:", a, "b:", b)


update_globals()  # Output: Inside update_globals(), a: 15 b: 30
print("Outside update_globals(), a:", a, "b:", b)  # Output: Outside update_globals(), a: 15 b: 30
