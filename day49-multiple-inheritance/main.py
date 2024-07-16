# Example of Multiple Inheritance in Python


# Base classes
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


# Derived class using multiple inheritance
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
print(dog.name)  # Buddy (from Mammal, also assigned by Animal)
print(dog.species)  # Dog (from Animal)
print(dog.fur_color)  # Golden (from Mammal)
dog.make_sound()  # Bark! (overridden in Dog)

# Inspecting the MRO
print(Dog.__mro__)
# or
print(Dog.mro())


# Potential Issue with Multiple Inheritance (Diamond Problem)
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


# Creating an instance of D
d = D()
d.method()  # Output: B
print(D.__mro__)
# or
print(D.mro())
