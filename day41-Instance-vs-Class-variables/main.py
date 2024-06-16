class Employee:
    # Class variable
    company_name = "TechCorp"
    
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
    
    def print_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company_name}")

emp1 = Employee("Alice", 70000)
emp2 = Employee("Bob", 80000)

emp1.print_details()
emp2.print_details()