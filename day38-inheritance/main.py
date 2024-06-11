# Single Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# create an instance of Dog
dog = Dog()
print(dog.speak())
print(dog.bark())


print("=======================")
# Multiple Inheritance
class Animal:
    def speak(self):
        return "Animal Speaks"

class Pet:
    def play(self):
        return "Pet plays"

class Dog(Animal, Pet):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
dog = Dog()
print(dog.speak())
print(dog.play())
print(dog.bark())


print("=======================")
# Multilevel Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Mammal(Animal):
    def walk(self):
        return "Mammal walks"

class Dog(Mammal):
    def bark(self):
        return "Dog barks"

# create an instance of Dog
dog = Dog()
print(dog.speak())
print(dog.walk())
print(dog.bark())


print("=======================")
# Hierarchical Inheritance
class Animal:
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

class Cat(Animal):
    def meow(self):
        return "Cat meows"

# Create an instance of Dog and Cat
dog = Dog()
cat = Cat()

print(dog.speak())
print(dog.bark())
print(cat.speak())
print(cat.meow())


print("=======================")
# Hybrid Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Pet:
    def play(self):
        return "Pet plays"

class Dog(Animal, Pet):
    def bark(self):
        return "Dog barks"

class Cat(Animal):
    def meow(self):
        return "Cat meows"

class Bulldog(Dog):
    def guard(self):
        return "Bulldog guards"

# Create instances of Dog, Cat, and Bulldog
dog = Dog()
cat = Cat()
bulldog = Bulldog()

print(dog.speak())
print(dog.play())
print(dog.bark())
print(cat.speak())
print(cat.meow())
print(bulldog.speak())
print(bulldog.play())
print(bulldog.bark())
print(bulldog.guard())
