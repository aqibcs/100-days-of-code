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


# Decorators with Arguments
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


# Multiple Decorators
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


# Class-based Decorators
class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class-based decorator")
        return self.func(*args, **kwargs)

@ClassDecorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Built-in Decorators
# @staticmethod
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.static_method()


# @classmethod
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

MyClass.class_method()


# @property
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)
print(obj.value)
obj.value = 20
print(obj.value)
