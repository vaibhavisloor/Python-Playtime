from turtle import Turtle
import random

colors = [
    "yellow",
    "orange",
    "red",
    "pink",
    "purple",
    "blue",
    "green",
    "brown",
    "black"
]

y_coords = [-200,-150,-100,-50,0,50,100,150,200]



class Car:
    def __init__(self):
        self.all_cars =[]
        self.level = 10

    def create_car(self):
        rand_chance=random.randint(1,self.level)
        if rand_chance == 1:
                newCar = Turtle("square")
                newCar.shapesize(1.5,2.5)
                newCar.color(random.choice(colors))
                newCar.penup()
                newCar.goto(300,random.choice(y_coords))
                self.all_cars.append(newCar)
            	       

    def move_car(self):            
       for car in self.all_cars:
            car.backward(10)