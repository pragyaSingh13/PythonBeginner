from abc import ABC, abstractmethod

class TV(ABC):
    name = "xyz"
    @abstractmethod
    def jadu(self):
        pass
    @abstractmethod
    def abc(self):
       pass

class Samsung(TV):
    def abc(self):
        print("This is jadu")
    def jadu(self):
        print("This is another jadu")

obj2 = Samsung()
print(obj2.name)
obj2.jadu()
obj2.abc()
