# Instance vs class variables
In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

## Class Variables
Class variables are attributes that are shared across all instances of a class. They are defined directly within the class, but outside any instance methods. They are typically used to store data that should be consistent across all instances of a class.

### Usage:
Class variables are useful for keeping track of data that is common to all objects, like counting the number of instances created or setting a common configuration that affects all instances.

### Example:
```python
class MyClass:
    # This is a class variable
    class_variable = 0
    
    def __init__(self):
        # Modify the class variable
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable()  # Output: 2
obj2.print_class_variable()  # Output: 2
```

### Explanation:
- **`class_variable`** is defined at the class level.
- Each time a new instance is created, **`class_variable`** is incremented.
- Since **`class_variable`** is shared, calling **`print_class_variable`** on any instance outputs the same value.

## Instance Variables
Instance variables are attributes that are specific to each instance of a class. They are usually initialized within the **`__init__`** method and are prefixed with **`self`**.

### Usage:
Instance variables are attributes that are specific to each instance of a class. They are usually initialized within the **`__init__`** method and are prefixed with self.

### Example:
```python
class MyClass:
    def __init__(self, name):
        # This is an instance variable
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name()  # Output: John
obj2.print_name()  # Output: Jane
```
### Explanation:
- **`name`** is an instance variable.
- Each instance (**`obj1`** and **`obj2`**) has its own value for **`name`**.
- Calling **`print_name`** on each instance outputs the respective name.

## Key Differences
1. **Scope:**
    - Class variables are shared across all instances of a class.
    - Instance variables are unique to each instance.

2. **Declaration:**
    - Class variables are declared inside the class but outside any method.
    - Instance variables are declared inside the `__init__` method or any other instance method, prefixed with `self`.

3. **Access:**
    - Class variables can be accessed using the class name or an instance:
**`ClassName.variable`** or **`instance.variable`**.
    - Instance variable are accessed through an instance:
**`instance.variable`**.

# Example to Illustrate Both
Here's a combined example showing both class and instance variable:
```python
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

emp1.print_details()  # Output: Name: Alice, Salary: 70000, Company: TechCorp
emp2.print_details()  # Output: Name: Bob, Salary: 80000, Company: TechCorp
```
### Explanation:
- **`company_name`** is a class variable, shared by all instances.
- **`name`** and **`salary`** are instance variables, unique to each **`Employee`**.

# Conclusion
Understanding the distinction between class variables and instance variables is crucial for managing shared versus instance-specific data. Class variables are useful for data that should be consistent across all instances, while instance variables are tailored to the unique needs of each instance. This understanding helps in writing more efficient, readable, and maintainable code.