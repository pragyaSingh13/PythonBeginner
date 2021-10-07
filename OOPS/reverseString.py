class TestClass:
    name = "Krishan"
    def reverseString(obj):
        value=""
        for data in obj.name:
            value = data+value
        return value
    
obj1 = TestClass()
print(obj1.reverseString())

