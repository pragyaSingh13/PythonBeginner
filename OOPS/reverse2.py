class Test:
    def reverseIt(obj,name):
        value = ""
        for data in name:
            value = data+value
            return value

ob = Test()
ob.name = "Pragya"
print(ob.reverseIt(ob.name))

