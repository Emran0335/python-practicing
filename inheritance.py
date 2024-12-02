# Inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent) in this way Child class inherits parent class.
#               clss Sub(Super) means child class knonwn as Sub class and Parent class as Super

class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm a motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("specific use: road trip and racing")


c = Car()
c.general_usage()
c.specific_usage()


# mv old_filename new_filename
# To update(rename) an existing file in the terminal.

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    # pass to demonstrate the attributes of Parent class
    def speak(self):
        print(f"{self.name}'s sound is woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}'s sound is meow")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name}'s sound is squeek")


dog = Dog("Spike")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.eat()
dog.sleep()
dog.speak()


cat.eat()
cat.sleep()
cat.speak()

mouse.eat()
mouse.sleep()
mouse.speak()


# inheritance is finished