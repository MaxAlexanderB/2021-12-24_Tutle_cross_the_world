import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#-------------Setup Screen-----------#

screen = Screen()
screen.title("Turtle road cross")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#--------------Create Turtle-------#
player = Player()
screen.onkey(player.turtle_up, "Up")

#--------------Generate Cats-------#
carmanager = CarManager()

#---------- Generate scoreboard-----------#
scoreboard = Scoreboard ()

#----------Set game is on loop--------#
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.cars_move()

#--------colision instance-----#
    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

#---------screen crossed instance-----#
    if player.ycor() > 250:
        player.back_to_start()
        carmanager.speed_up()
        scoreboard.get_point()
        scoreboard.refresh()

scoreboard.game_over()
screen.exitonclick()



