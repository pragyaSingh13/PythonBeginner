class ParentClass:
    name = "Pragya"
    def printName(self):
        last = "Singh"
        print("",last)

class ChildClass(ParentClass):
    name="qpwdih"
    def printName(self):
        print("From Parent Class",super().name)
obj1 = ChildClass()
obj1.printName()


