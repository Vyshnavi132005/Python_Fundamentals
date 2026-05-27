class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Ram", 50000)

print(emp.name)
print(emp.salary)