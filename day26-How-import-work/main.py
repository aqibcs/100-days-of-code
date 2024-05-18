# Importing and using the random module for generating random numbers:
import  random

# Generate a random integer between 1 and 10 inclusive
random_number = random.randint(1, 10)
print(random_number)


# Importing and using the datetime module to work with dates and times:
from  datetime import datetime

# Get the current date and time
now = datetime.now()
print(now)

# Format the current date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)


"""Importing a custom module from another file in the same directory:
Suppose you have a file named my_module.py with the following contents:"""
import  module

module.greet("Aqib") # Output: Hello, Aqib!
result = module.square(5)
print(result) # Output: 25