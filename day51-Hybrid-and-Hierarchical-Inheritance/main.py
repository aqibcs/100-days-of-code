# Hybrid Inheritance Example
class Human:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):

    def __init__(self, name, age, address) -> None:
        super().__init__(name, age)
        self.address = address

    def show_details(self):
        super().show_details()
        print("Address:", self.address)


class Program:

    def __init__(self, program_name, duration) -> None:
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):

    def __init__(self, name, age, address, program) -> None:
        super().__init__(name, age, address)
        self.program = program

    def show_details(self):
        super().show_details()
        self.program.show_details()


# Create a Program object
program = Program("Computer Science", "4 Years")
# Create a Student object
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Hierarchical Inheritance Example
class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def show_details(self):
        print("Name:", self.name)


class Dog(Animal):

    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.breed = breed

    def show_details(self):
        super().show_details()
        print("Species: Dog")
        print("Breed:", self.breed)


class Cat(Animal):

    def __init__(self, name, color) -> None:
        super().__init__(name)
        self.color = color

    def show_details(self):
        super().show_details()
        print("Species: Cat")
        print("Color:", self.color)


dog = Dog("Max", "Golden Retriever")
# Display details
dog.show_details()
print()
# Create a Cat object
cat = Cat("Luna", "Black")
# Display the details
cat.show_details()
