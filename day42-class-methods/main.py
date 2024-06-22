# Example 1: Creating a Factory Method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @classmethod
    def from_string(cls, car_string):
        make, model, year = car_string.split('-')
        return cls(make, model, int(year))

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


# Using the factory method
car_str = "Toyota-Corolla-2020"
car = Car.from_string(car_str)
car.display_info()