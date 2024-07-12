class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# Create an instance of Animal
generic_animal = Animal(name="Generic Animal", species="Unknown")
print(f"{generic_animal.name} is a {generic_animal.species}")
generic_animal.make_sound()  # Output: Sound made by the animal

# Create an instance of Dog
my_dog = Dog(name="Buddy", breed="Golden Retriever")
print(f"{my_dog.name} is a {my_dog.species} of breed {my_dog.breed}")
my_dog.make_sound()  # Output: Bark!
