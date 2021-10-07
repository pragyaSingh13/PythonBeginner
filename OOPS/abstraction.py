from abc import ABC, abstractmethod

class TV(ABC):
    name = "xyz"
    @abstractmethod
    def jadu(self):
        pass
    def abc(self):
        print("Welcome")

class Samsung(TV):
    def jadu(self):
        print("This is jadu")

obj2 = Samsung()
print(obj2.name)
obj2.jadu()
obj2.abc()
