class demo:
    firstname =""
    lastname=""

    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    def display(self):
        print("FirstName ",str(self.firstname))
        print("LastName ",str(self.lastname))

obj = demo("Pragya"," Singh")

obj.display()