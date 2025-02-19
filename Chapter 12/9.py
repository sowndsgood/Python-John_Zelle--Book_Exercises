# Frogger Game

# Importing libraries
from graphics import *
import random
import time

# Graphical Window design
win_width,win_height=600,400
frog_size=30
car_width,car_height=40,20
lane_height=40
num_cars=9
car_speed=15

class Frog:
    
    def __init__(self, win):
        self.win = win
        self.shape = Rectangle(Point(win_width // 2 - frog_size // 2, win_height - 40),
                               Point(win_width // 2 + frog_size // 2, win_height - 40 + frog_size))
        self.shape.setFill("green")
        self.shape.draw(win)

    def move(self, dx, dy):
        """Moves the frog in the given direction."""
        p1, p2 = self.shape.getP1(), self.shape.getP2()
        if 0 <= p1.getX() + dx <= win_width - frog_size and 0 <= p1.getY() + dy <= win_height - frog_size:
            self.shape.move(dx, dy)

    def get_position(self):
        return self.shape.getP1(), self.shape.getP2()

    def reset(self):
        """Resets the frog to the starting position."""
        self.shape.undraw()
        self.__init__(self.win)

class Car:
    
    def __init__(self, win, y):
        self.win = win
        self.x = random.randint(0, win_width - car_width)
        self.y = y
        self.speed = random.randint(2, car_speed)
        self.shape = Rectangle(Point(self.x, self.y), Point(self.x + car_width, self.y + car_height))
        self.shape.setFill(random.choice(["red", "blue", "yellow", "purple", "orange","pink"]))
        self.shape.draw(win)

    def move(self):
        """Moves the car and loops it back to the left if it goes out of bounds."""
        self.shape.move(self.speed, 0)
        p1 = self.shape.getP1()
        if p1.getX() > win_width:
            self.shape.move(-win_width - car_width, 0)

    def get_position(self):
        return self.shape.getP1(), self.shape.getP2()

class FroggerGame:
    
    def __init__(self):
        self.win = GraphWin("Frogger Game", win_width, win_height)
        self.win.setBackground("black")

        for i in range(1, 10):
            line = Line(Point(0, i * lane_height), Point(win_width, i * lane_height))
            line.setFill("white")
            line.draw(self.win)

        self.frog = Frog(self.win)
        self.cars = [Car(self.win, i * lane_height + 15) for i in range(num_cars)]
        self.running = True

    def run(self):
        while self.running:
            self.move_cars()
            self.check_collision()

            key = self.win.checkKey()
            if key in ["w", "Up"]:
                self.frog.move(0, -lane_height)
            elif key in ["s", "Down"]:
                self.frog.move(0, lane_height)
            elif key in ["a", "Left"]:
                self.frog.move(-frog_size, 0)
            elif key in ["d", "Right"]:
                self.frog.move(frog_size, 0)
            elif key == "q":
                self.running = False

            if self.frog.get_position()[0].getY() <= 0:
                self.win_message("You Won! ")
                self.frog.reset()

            time.sleep(0.05)

        self.win.close()

    def move_cars(self):
        """Moves the cars forward."""
        for car in self.cars:
            car.move()

    def check_collision(self):
        """Checks if the frog collides with any car."""
        frog_p1, frog_p2 = self.frog.get_position()
        for car in self.cars:
            car_p1, car_p2 = car.get_position()
            if not (frog_p2.getX() < car_p1.getX() or frog_p1.getX() > car_p2.getX() or
                    frog_p2.getY() < car_p1.getY() or frog_p1.getY() > car_p2.getY()):
                self.win_message("Game Over! ")
                self.frog.reset()

    def win_message(self, text):
        """Displays a win or game over message."""
        message = Text(Point(win_width // 2, win_height // 2), text)
        message.setSize(20)
        message.setTextColor("white")
        message.draw(self.win)
        time.sleep(2)
        message.undraw()

FroggerGame().run()
