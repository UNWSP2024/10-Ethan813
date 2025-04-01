# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it is called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.

class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed
    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
    def get_speed(self):
        return self.speed
car1 = Car(2022, 'Porsche_718_Cayman_GT4_RS',0)

for number in range(5):
    car1.accelerate()
    print(car1.get_speed())
#I wasn't sure what this meant "The call the brake method." so i just did it five times like accelerate.
for number in range(5):
    car1.brake()
    print(car1.get_speed())
#ethan collins 4/1/2025 zooooooooooom