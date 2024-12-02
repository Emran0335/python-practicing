
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


# class variables = Shared among all instances(created objects) of a class
#                   Defined outside the constructor(def __init__(self))
#                   Allow you to share data among all objects created from that class

# instance variables have their own version.
# but class variables shared among all instances(objects created)

class Bird:
    wings = 2   # class variables

    def __init__(self, name, isPopular):
        self.name = name                # instance variable
        self.isPopular = isPopular      # instance variable

    def speak(selt):
        print(f"The {selt.name} can speak")


crow = Bird("Crow", True)

print(crow.name)
crow.speak()


class Student:

    # class variables
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # instances variables
        self.name = name
        self.age = age
        # self refers to the instance or object we are currently working with
        Student.num_students += 1


student1 = Student("Emran", 36)
student2 = Student("Hossain", 35)
student3 = Student("Sadifa", 3)
student4 = Student("Nusaiba", 3)

print(student1.name)
print(student2.name)
print(student3.name)

print(student1.age)
print(student2.age)
print(student3.age)

# But it is not a good practice.
print(student1.class_year)
print(student2.class_year)
print(student3.class_year)

# The good practice is to access class variable by the name of the class
print(Student.class_year)  # it is more explicit
print(Student.num_students)
# Number of students is 4 because it three instances(student-objects) are created.


# selt = student1 or student2 or student3. So, self refers to the object(instance)
# def __init__(self, name, age):
#     # instances variables
#     student1.name = name
#     student1.age = age
#     # self refers to the instance or object we are currently working with



# git branch -M main
# -M means modified. So, it will modified the branch to main.