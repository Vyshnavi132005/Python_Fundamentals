class Parent:

    def display(self):
        print("Parent Method")

class Child(Parent):

    def display(self):
        print("Child Method")

obj = Child()

obj.display()