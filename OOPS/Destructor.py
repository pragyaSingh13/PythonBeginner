class Demo:
    def printData(self):
        print("Inside a function")
    def __init__(self):
        print("Object Created")       
    def __del__(self):
        #to get the name of the class
        class_name = self.__class__.__name__
        print(class_name,"Deleted")

obj1 = Demo()
obj1.printData()
