#with operators
import operator
x=10
y=20

def add(a,b):
    print("addition",operator.add(a,b))

def sub(a,b):
    print("subtraction",operator.sub(a,b))

def mul(a,b):
    print("multiplication",operator.mul(a,b))

def div(a,b):
    print("division",operator.floordiv(b,a))

def mod(a,b):
    print("modulus",operator.mod(a,b))


add(x,y)
sub(x,y)
mul(x,y)
div(x,y)
mod(x,y)