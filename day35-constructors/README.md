# Constructors
A constructor is a special method in a class that is used to create and initialize an object of that class. It is invoked automatically when an object of the class is created. The main purpose of a constructor is to initialize or assign values to the data members of the class. A constructor cannot return any value.

## Syntax of Python Constructor
```python
def __init__(self):
    # initialization
```
`__init__ ` is one of the reserved methods in Python. In Object-Oriented Programming, it is known as a constructor.

## Type of Constructors in Python
1. Parameterized Constructor
2. Default Constructor

### Parameterized Constructor:
When the constructor accepts arguments along with `self`, it is known as a parameterized constructor. These arguments can be used inside the class to assign values to the data members.

#### Example:
```python
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
```

### Default Constructor
When the constructor doesn't accept any arguments from the object and has only one argument, `self`, in the constructor, it is known as a default constructor.

#### Example:
```python
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()
```
## Additional Concept
### More About `self`
`self` refers to the instance of the class. It is used to access variables that belong to the class. When a method is called, the instance is passed as the first argument.

### Constructor Overloading
Python does not support constructor overloading; however, you can simulate it using default arguments:
```python
class Details:
    def __init__(self, animal="Crab", group="Crustaceans"):
        self.animal = animal
        self.group = group

obj1 = Details()
obj2 = Details("Lion", "Mammals")
print(obj1.animal, "belongs to the", obj1.group, "group.")
print(obj2.animal, "belongs to the", obj2.group, "group.")
```

### Inheritance and Constructors
When using inheritance, the constructor of the parent class can be called in the child class using `super()`:
```python
class Animal:
    def __init__(self, animal):
        self.animal = animal

class Details(Animal):
    def __init__(self, animal, group):
        super().__init__(animal)
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
```