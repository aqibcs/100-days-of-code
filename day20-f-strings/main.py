# Using f-strings for Mathematical Operations:
num1 = 10
num2 = 20
result = num1 * num2
print(f"The result of {num1} multiplied by {num2} is {result}.")


# Using f-strings for Dictionary Values:
person = {'name': 'Alice', 'Age': 20}
print(f"{person['name']} is {person['Age']} years old.")


# Formatting Dates with f-strings (using datetime module):
from datetime import datetime

current_date = datetime.now()
print(f"Today's date is {current_date:%Y-%m-%d}.")


# Formatting Multiple Variables with f-strings:
name = 'Alice'
age = 25
city = 'New York'
print(f"Hello, my name is {name}, I'm {age} years old, and I live in {city}.")