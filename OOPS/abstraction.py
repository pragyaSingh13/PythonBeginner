from abc import ABC, abstractmethod

class TV(ABC):
    @abstractmethod
    def jadu(self):
        pass
    def abc(obj):
        print("Welcome")

class Samsung(TV):
    def jadu(obj):
        print("This is jadu")


obj2 = Samsung()
obj2.jadu()
obj2.abc()
