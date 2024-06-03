# Parameterized Constructor
class Details:
    def __init__(self, animal, group) -> None:
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


# Default Constructor
class Details:
    def __init__(self) -> None:
        self.animal = "Crab"
        self.group = "Crustaceans"

obj1 = Details()
print(obj1.animal, "belongs to the", obj1.group, "group.")


# Simulating Constructor Overloading using Default Arguments
class Details:
    def __init__(self, animal="Crab", group="Crustaceans"):
        self.animal = animal
        self.group = group

obj1 = Details()
obj2 = Details("Lion", "Mammals")
print(obj1.animal, "belongs to the", obj1.group, "group.")
print(obj2.animal, "belongs to the", obj2.group, "group.")


# Inheritance and Constructors
class Animal:
    def __init__(self, animal):
        self.animal = animal

class Details(Animal):
    def __init__(self, animal, group):
        super().__init__(animal)
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")
