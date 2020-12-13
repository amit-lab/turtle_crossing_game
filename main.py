import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    screen.update()
    cars.move_cars()

    # When player reaches the upper boundary
    if player.ycor() > 300:
        player.restart()
        scoreboard.level_no += 1
        scoreboard.level()
        cars.car_speed *= 0.9   # Increasing cars speed once level is crossed

    # Detection of collision with cars
    for car in cars.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
