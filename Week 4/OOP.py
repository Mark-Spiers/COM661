import math
import random

class Circle():

    def __init__(self, radius, circle_x, circle_y):
        self.__radius = radius
        self.__center_x = circle_x
        self.__center_y = circle_y

    def area(self):
        pi = math.pi
        return pi * (self.__radius * self.__radius)

    def circumference(self):
        pi = math.pi
        return 2 * pi * self.__radius

    def get_top(self):
        return self.__center_y + self.__radius

    def get_right(self):
        return self.__center_x + self.__radius

Circ = Circle(4, 5, 6)
print(Circ.area())

print(Circ.circumference())

print(Circ.get_top())

print(Circ.get_right())


class Car():

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self, speed_step):
        self.__speed += speed_step

    def breake(self, reduce_speed_step):
        self.__speed -= reduce_speed_step

    def get_speed(self):
        return self.__speed



def snake_eyes():
    die1 = 0
    die2 = 0
    counter = 0
    for i in range(1, 501):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)

        if die1 == die2:
            counter += 1

    print("Number of times snake eyes ir rolled is:", counter)

snake_eyes()
