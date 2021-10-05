class Parent:
    def __init__(self,a):
        print("Constructor 1 ",a)

class Child(Parent):
    def __init__(self,a):
        super().__init__(a)
    
obj1 = Child(12)