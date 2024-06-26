# Example of using dir()
x = [1, 2, 3]
print(dir(x))


# Example of using __dict__
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.__dict__)


# Example integration introspection tools
x = [1, 2, 3]

# Using dir()
print("Attributes and methods of x:")
print(dir(x))


# Using __dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print("\nInstance attributes of p:")
print(p.__dict__)

# Using help()
print("\nHelp documentation for list:")
help(list)