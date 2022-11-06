# from abc import ABC, abstractmethod


# class AbstractClass(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def some_method():
#         pass
#     def need_something(self):
#         print("I need something")


# ac = AbstractClass("class")

# print(ac)


class Demo:

    def check(self):
        return " Demo's check "

    def display(self):
        print(self.check(), end="")


class Demo_Derived(Demo):

    def check(self):
        return " Derived's check "


Demo().display()
Demo_Derived().display()