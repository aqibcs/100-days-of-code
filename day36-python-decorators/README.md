# Python Decorators Guide

## Table of Contents
1. [Introduction to Decorators](#introduction-to-decorators)
2. [Basic Decorator Syntax](#basic-decorator-syntax)
3. [Decorators with Arguments](#decorators-with-arguments)
4. [Multiple Decorators](#multiple-decorators)
5. [Built-in Decorators](#built-in-decorators)
    - [@staticmethod](#staticmethod)
    - [@classmethod](#classmethod)
    - [@property](#property)
6. [Practical Examples](#practical-examples)
    - [Logging Decorator](#logging-decorator)
    - [Authorization Decorator](#authorization-decorator)
    - [Caching Decorator](#caching-decorator)
7. [Conclusion](#conclusion)

## Introduction to Decorators
Decorators are functions that modify the behavior of other functions or methods. They are commonly used for cross-cutting concerns like logging, access control, and caching.

## Basic Decorator Syntax
A basic decorator is a function that takes another function and extends its behavior.

```python
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")

greet()
```
#### Output:
```bash
Before the function call
Hello, World!
After the function call
```
## Decorators with Arguments
Decorators can accept arguments by adding another layer of functions.

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()
```
#### Output:
```bash
Hello!
Hello!
Hello!
```

## Multiple Decorators
You can apply multiple decorators to a single function.
```python
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()
```
#### Output:
```bash
Decorator One
Decorator Two
Hello!
```

## Built-in Decorators
### @staticmethod
Defines a method that does not operate on an instance of the class.
```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.static_method()
```
#### Output:
```bash
This is a static method.
```

### @classmethod
Define method that operates on the class itself.
```python
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

MyClass.class_method()
```
#### Output:
```bash
This is a class method of MyClass.
```

### @property
Allows you to define methods that can be accessed like attributes.
```python
class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value)
        self._value = new_value

obj = MyClass(10)
print(obj.value)
obj.value = 20
print(obj.value)
```
#### Output:
```bash
10
20
```
## Conclusion
Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.