# Introduction to Object-Oriented Programming
In programming, there are two primary approaches to written code:
1. Procedural Programming
2. Object-oriented Programming (OOP)

Up until now, we have primarily followed the `"Procedural programming"` approach. In this session, we will delve into Object-Oriented Programming (OOP), a powerful paradigm that allows us to model real-world concepts using classes and objects.

## Understanding Object-Oriented Programming
The basic idea of OOP in python is to use classes and objects to represent real-world entities and concepts. This approach offers a more organized and modular way of writing code, making it easier to manage and extend.

### Classes and Objects:
- **Class:** A class is a blueprint or template for creating objects. It defines the properties (attributes) and methods (functions) that an object of that class will have. For example, a `Person` class might define properties like `name` and `age`, and methods like `speak()` and `walk()`.

- **Object:** An object is an instance of a class. Each object contains its own data and methods. For instance, if you create two instance of the `Person` class, each instance (object) will have its own unique `name` and `age` but will share the same methods for `speak()` and `walk()`.

### Key Features of OOP
1. #### Encapsulation:
Encapsulation means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This concept helps protect the object's data from being modified unexpectedly, ensuring a controlled and predictable interaction with the object's properties.
```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    
    def speak(self):
        print(f"My name is {self.__name} and I am {self.__age} years old.")

    def set_age(self, age):
        self.__age = age
```
2. #### Inheritance:
Inheritance allows new classes to be created that inherit the properties and methods of an existing class. This promotes code reuse and makes it easy to create new classes that have similar functionality to existing ones.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")
```
3. #### Polymorphism:
Polymorphism allows objects of different classes to be treated as if they were objects of a common class. This provides greater flexibility in code and makes it easier to write functions and methods that can work with multiple types of objects.
```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)
```
### Summary
# Introduction to Object-Oriented Programming

In programming, there are two primary approaches to writing code:
1. Procedural Programming
2. Object-Oriented Programming (OOP)

Up until now, we have primarily followed the "Procedural Programming" approach. In this session, we will delve into Object-Oriented Programming (OOP), a powerful paradigm that allows us to model real-world concepts using classes and objects.

## Understanding Object-Oriented Programming

The basic idea of OOP in Python is to use classes and objects to represent real-world entities and concepts. This approach offers a more organized and modular way of writing code, making it easier to manage and extend.

### Classes and Objects

- **Class:** A class is a blueprint or template for creating objects. It defines the properties (attributes) and methods (functions) that an object of that class will have. For example, a `Person` class might define properties like `name` and `age`, and methods like `speak()` and `walk()`.
  
- **Object:** An object is an instance of a class. Each object contains its own data and methods. For instance, if you create two instances of the `Person` class, each instance (object) will have its own unique `name` and `age` but will share the same methods for `speak()` and `walk()`.

### Key Features of OOP

1. **Encapsulation:** 
   Encapsulation means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This concept helps protect the object's data from being modified unexpectedly, ensuring a controlled and predictable interaction with the object's properties.

   ```python
   class Person:
       def __init__(self, name, age):
           self.__name = name  # Private attribute
           self.__age = age    # Private attribute
       
       def speak(self):
           print(f"My name is {self.__name} and I am {self.__age} years old.")

       def set_age(self, age):
           self.__age = age
   ```

2. **Inheritance:** 
   Inheritance allows new classes to be created that inherit the properties and methods of an existing class. This promotes code reuse and makes it easy to create new classes that have similar functionality to existing ones.

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age
       
       def speak(self):
           print(f"My name is {self.name} and I am {self.age} years old.")
   
   class Student(Person):
       def __init__(self, name, age, student_id):
           super().__init__(name, age)
           self.student_id = student_id
       
       def study(self):
           print(f"{self.name} is studying.")
   ```

3. **Polymorphism:** 
   Polymorphism allows objects of different classes to be treated as if they were objects of a common class. This provides greater flexibility in code and makes it easier to write functions and methods that can work with multiple types of objects.

   ```python
   class Cat:
       def speak(self):
           print("Meow")
   
   class Dog:
       def speak(self):
           print("Bark")
   
   def animal_sound(animal):
       animal.speak()
   
   cat = Cat()
   dog = Dog()
   
   animal_sound(cat)  # Output: Meow
   animal_sound(dog)  # Output: Bark
   ```

### Summary
Object-Oriented Programming in Python allows developers to model real-world concepts and entities using classes and objects. It promotes encapsulation to protect data, inheritance to reuse code, and polymorphism to create flexible and adaptable code. By leveraging these features, developers can write more organized, maintainable, and scalable code.