# from abc import ABC, abstractmethod

# class Animal(ABC):

#     def eat(self):
#         print("Animal Eating")

#     @abstractmethod
#     def run(self):
#         print("Animal Running")

#     def sleep(self):
#         print("Animal Sleeping")

# class Dog(Animal):

#     def bark(self):
#         print("Dog Barking")

#     def run(self):
#         print("Dog Running")
#         super().run()

# jack = Dog()

# jack.run()

# Abstract class can have abstract methods and concrete methods. Abstract methods are methods that are declared but not implemented. Concrete methods are methods that are implemented. Abstract class can have both abstract and concrete methods. Abstract class can not be instantiated. Abstract class can have constructor. Abstract class can have static methods, final methods, and static variables. Abstract class can extend only one class but it can implement multiple interfaces. Abstract class can have final methods which will force the subclass not to change the body of the method. Abstract class can have static methods which will force the subclass to provide the body of the method. Abstract class can have static variables which will be common to all the instances (or objects) of the class.

# Abstraction

# Abstraction is the process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.

# Abstraction lets you focus on what the object does instead of how it does it.

# Abstraction can be achieved with either abstract classes or interfaces.

# Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).

# Abstract method: can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).

# To access the abstract class, it must be inherited from another class, and its body is provided by the subclass.

# Example

# Create a parent class called Animal, with a method called animal_sound:


class Animal:

    def animal_sound(self):
        print("The animal makes a sound")


# Create a child class called Piglet, inherit the properties from the Animal class:


class Piglet(Animal):
    pass


# Create an object called oink:

oink = Piglet()

# Call the method animal_sound on the object oink:

oink.animal_sound()

# Output:

# The animal makes a sound
