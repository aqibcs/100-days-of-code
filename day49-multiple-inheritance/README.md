# Multiple Inheritance in Python
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.


## Syntax
In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.
```python
class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body
```

In this example, the `ChildClass` inherits attributes and methods from all three parent classes: `ParentClass1`, `ParentClass2`, and `ParentClass3`.

# Method Resolution Order (MRO)
In the case of multiple inheritance, Python follows a **method resolution order (MRO)** to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods. Python uses the **C3 linearization** algorithm for this purpose.

To inspect the MRO of a class, You can use the `__mro__` attribute or the `mro()` method:
```python
print(ChildClass.__mro__)
# or
print(ChildClass.mro())
```

## Example
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# Creating an instance of Dog
dog = Dog(name="Buddy", breed="Golden Retriever", fur_color="Golden")

# Using attributes and methods from both parent classes
print(dog.name)       # Buddy (from Mammal, also assigned by Animal)
print(dog.species)    # Dog (from Animal)
print(dog.fur_color)  # Golden (from Mammal)
dog.make_sound()      # Bark! (overridden in Dog)

# Inspecting the MRO
print(Dog.__mro__)
```
In this example, the `Dog` class inherits from both the `Animal` and `Mammal` classes, so it can use attributes and methods from both parent classes. The `make_sound` method is overridden in the `Dog` class to provide a specific implementation for dogs.

## Potential Issue with Multiple Inheritance
While multiple inheritance can be very powerful, it can also lead to potential issues such as the **diamond problem**. This occurs when a class inherits from two classes that both inherit from a common base class. Python handles this issue using the C3 linearization algorithm to create a consistent MRO.

### For Example:
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()  # Output: B
print(D.__mro__)
```
In this case, the MRO ensures that `B` is checked before `C`, even though both `B` and `C` inherit from `A`.
