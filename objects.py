
# object = A 'bundle' of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a 'class' to create many objects

# class = (blueprint) used to design the structue and layout of an object.


class Car:
    # dunder method(constructor - similar to function) means double underscore
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You can drive the car {self.model}")

    def stop(self):
        print(f"You can stop the car {self.model}")

# methods are actions that an object can perform.
# these methods are identical for each object.


# self is called twice automatically
# slef is the object instance that is going to be created from the class(car1, ... etc.)
car1 = Car("Mustang", 2024, "red", False)  # self is here car1.
car2 = Car("Corvette", 2025, "blue", True)  # self is here car2.
car3 = Car("Charger", 2026, "yellow", True)  # self is here car3.


print(car1.model)  # dot is known as attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()

print(car2.model)  # dot is known as attribute access operator
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()

print(car3.model)  # dot is known as attribute access operator
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.drive()
car3.stop()
