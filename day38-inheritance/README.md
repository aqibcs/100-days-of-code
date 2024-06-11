# Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

## Python Inheritance Syntax
```python
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
  ```
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

## Types of inheritance:
1. [Single inheritance](#single-inheritance)
2. [Multiple inheritance](#multiple-inheritance)
3. [Multilevel inheritance](#multilevel-inheritance)
4. [Hierarchical Inheritance](#hierarchical-inheritance)
5. [Hybrid Inheritance](#hybrid-inheritance)

### Single Inheritance:
Single inheritance means a class is derived from only one base class. Here's an example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
my_dog = Dog()
my_dog.speak()  # Output: Animal speaks
my_dog.bark()   # Output: Dog barks
```
### Multiple Inheritance:
Multiple inheritance means a class is derived from more than one base class.
Here's an example:
```python
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

# Creating an instance of C
my_object = C()
my_object.method_a()  # Output: Method A
my_object.method_b()  # Output: Method B
my_object.method_c()  # Output: Method C
```

### Multilevel Inheritance:
Multilevel inheritance means a class is derived from another class.
Here's an example:
```python
class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(B):
    def method_c(self):
        print("Method C")

# Creating an instance of C
my_object = C()
my_object.method_a()  # Output: Method A
my_object.method_b()  # Output: Method B
my_object.method_c()  # Output: Method C
```

### Hierarchical Inheritance:
Hierarchical inheritance means multiple derived classes are created from a single base class.
Here's an example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating instances of Dog and Cat
my_dog = Dog()
my_cat = Cat()
my_dog.speak()  # Output: Animal speaks
my_dog.bark()   # Output: Dog barks
my_cat.speak()  # Output: Animal speaks
my_cat.meow()   # Output: Cat meows
```

### Hybrid Inheritance:
Hybrid inheritance is a combination of two or more types of inheritance.
Here's an example:
```python
class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

# Creating an instance of D
my_object = D()
my_object.method_a()  # Output: Method A
my_object.method_b()  # Output: Method B
my_object.method_c()  # Output: Method C
my_object.method_d()  # Output: Method D
```