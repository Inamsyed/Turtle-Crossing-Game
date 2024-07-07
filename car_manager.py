from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "light green", "light blue", "purple", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.allCars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        x = random.randint(1, 6)
        if(x == 1):
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.turtlesize(1,2)
            x_position = 290
            y_position = random.randint(-250, 250)
            new_car.goto(x_position, y_position)
            self.allCars.append(new_car)

    def move_cars(self):
        for car in self.allCars:
            car.forward(self.car_speed)

    def collision(self, player):
        for car in self.allCars:
            if(car.distance(player) < 25):
                return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
