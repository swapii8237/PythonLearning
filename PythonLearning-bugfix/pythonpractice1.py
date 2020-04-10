class Employee:
    def __init__(self, name, age,salary):
     self.name = name
     self.age = age
     self.salary = 20000
     
E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1. 
print("Employee name: ",E1.name)
print("Employee age: ",E1.age)
print("Employee salary: ",E1.salary)