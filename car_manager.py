from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()
        self.car_speed = 0.1

    def create_cars(self):
        for _ in range(15):
            new_car = Turtle()
            new_car.color(COLORS[random.randint(0, len(COLORS) - 1)])  # Assigning random color to each car
            new_car.shape('square')
            new_car.shapesize(stretch_wid=-0.5, stretch_len=1.5)
            new_car.penup()
            new_car.goto(random.randint(-100, 500), random.randint(-200, 200))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(10)
            if car.xcor() < -300:
                car.goto(random.randint(300, 500), random.randint(-200, 200))
                print("here")
