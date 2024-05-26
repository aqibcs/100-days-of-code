# Lambda Functions in Python
In Python, a `lambda` function is a small anonymous function defined using the `lambda` keyword. Lambda functions are often used when a small function is needed for a short period of time and are commonly used as arguments to higher-order functions, such as `map`, `filter`, and `reduce`.
### Syntax:
```python
lambda arguments: expression
```
A lambda function can take any number of arguments, but it can only have one expression. The expression is evaluated and returned.

## Basic Example:
Here is a comparison between a regular function and a lambda function that both double the input:
```python
# Regular function to double the input
def double(x):
    return x * 2

# Lambda function to double the input
double_lambda = lambda x: x * 2

# Using the functions
print(double(5))         # Output: 10
print(double_lambda(5))  # Output: 10
```
## Lambda Function with Multiple Arguments
Lambda functions can take multiple arguments just like regular functions. Here is an example:

```python
# Regular function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
multiply_lambda = lambda x, y: x * y

# Using the functions
print(multiply(5, 3))         # Output: 15
print(multiply_lambda(5, 3))  # Output: 15
```

## Using Lambda Functions with Higher-Order Functions
Lambda functions are often used with higher-order functions like `map`, `filter`, and `reduce`.

## Example with `map`
```python
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
```

## Example with `filter`
```python
# Regular function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Using filter with a regular function
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

# Using filter with a lambda function
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_lambda)  # Output: [2, 4]
```

## Example with `reduce`
```python
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
```

## Lambda Functions with Single Expressions
Although lambda functions are limited to a single expression, they can perform complex operations within that expression. For example:

```python
# Lambda function to calculate the product of two numbers and print the result
print_product = lambda x, y: print(f'{x} * {y} = {x * y}')

# Using the lambda function
print_product(5, 3)  # Output: 5 * 3 = 15
```