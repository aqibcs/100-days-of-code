class BaseClass:
    def base_method(self):
        print("BaseClass method called")

class DerivedClass1(BaseClass):
    def derived1_method(self):
        print("DerivedClass1 method called")

class DerivedClass2(DerivedClass1):
    def derived2_method(self):
        print("DerivedClass2 method called")

# Creating an object of DerivedClass2
obj = DerivedClass2()
obj.base_method()
obj.derived1_method()
obj.derived2_method()