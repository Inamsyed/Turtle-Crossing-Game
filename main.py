import time
import turtle
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgpic("road.png")


player = Player()
score = Scoreboard()
car_manager = CarManager()
car_manager.hideturtle()
screen.onkeypress(player.move_up, "Up")
game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if(player.finish() == True):
        car_manager.level_up()
        score.update_score()
    car_manager.move_cars()
    car_manager.create_cars()
    if(car_manager.collision(player) == True):
        score.game_over()
        game_is_on = False


screen.exitonclick()