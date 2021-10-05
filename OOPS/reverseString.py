class TestClass:
    def getName(self):
        name = input("Enter your name:")
        return name

    def reverseName(self,nameStr):
        newStr = ""
        x=len(nameStr)
        x = x-1
        while(x>=0):
            newStr+= nameStr[x]
            x-=1
        return newStr

obj1 = TestClass()
name  = obj1.getName()
print(name)
print(obj1.reverseName(name))


