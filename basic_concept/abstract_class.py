from abc import ABC, abstractmethod

class ParentAbstract(ABC):
    @abstractmethod
    def method(self):
        pass

class ChildClass(ParentAbstract):
    def __init__(self, name):
        self.name = name

    def method(self):
        print("method")

    def print_name(self):
        print(self.name)


# obj1 = ParentAbstract()
child_obj = ChildClass("test")
child_obj.print_name()