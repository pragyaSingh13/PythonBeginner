
class Demo:
    def div(self,a,b):
            print(a/b)

    def disp(self):
        print("Whatever")

obj = Demo()
try:
    obj.div(10,0)
except Exception as ref:
   print("Divison not possible", ref)
finally:
    print("ieufg")

obj.disp()
