# Inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent) in this way Child class inherits parent class.

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
    pass            # pass to demonstrate the attributes of Parent class

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Spike")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.eat()
dog.sleep()

cat.eat()
cat.sleep()

mouse.eat()
mouse.sleep()
    
    