# Basic Method Overriding
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

# Create instances of each class
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()



# Overriding with 'super()'
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")
        return super().sound()

class Cat(Animal):
    def sound(self):
        print("The cat meows")
        return super().sound()

# Create instances of each class
dog = Dog()
cat = Cat()

# Call the sound method on each instance
dog.sound()
cat.sound()


# Combining Overriding with initialization
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        print(f"{self.name} the {self.breed} barks")

# Create an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.sound()