# Inheritance allows one class to acquire attributes and methods from another class
# The child can use the functionality of parent and can also add its own functionality

# Animal class
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()

