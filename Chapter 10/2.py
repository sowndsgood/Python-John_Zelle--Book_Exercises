#Pi Approximation using Button class

from graphics import *
from random import random

class Button:
    '''It creates an instance of a button in the graphical window.'''

    def __init__(self, win, center, width, height, label):
        self.win = win

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax, self.ymin, self.ymax = x - w, x + w, y - h, h + y
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)

        self.activate()

    def clicked(self, pt):
        '''It returns 'True' if the button is clicked.'''
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def activate(self):
        '''Set this button to active.'''
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        '''Set this button to inactive.'''
        self.label.setFill('lightgrey')
        self.rect.setWidth(1)
        self.active = False

    def getLabel(self):
        '''Returns the label from the button.'''
        return self.label.getText()

# Pi Simulation
def simPi(n: int) -> float:
    hit = 0
    for _ in range(n):
        x, y = 2 * random() - 1, 2 * random() - 1
        if x**2 + y**2 <= 1:
            hit += 1
    return 4 * hit / n

# Main GUI
def main():
    win = GraphWin('Pi Simulation', 800, 600)
    win.setBackground("black")

    # Instruction
    title = Text(Point(400, 100), "Enter the number of darts:")
    title.setSize(16)
    title.setTextColor("white")
    title.draw(win)

    # Input box
    input_box = Entry(Point(400, 150), 10)
    input_box.setSize(20)
    input_box.setText("")
    input_box.draw(win)

    # Buttons
    simulate_button = Button(win, Point(300, 250), 100, 40, "Simulate")
    quit_button = Button(win, Point(500, 250), 100, 40, "Quit")

    result_text = Text(Point(400, 350), "")
    result_text.setSize(20)
    result_text.setTextColor("white")
    result_text.draw(win)

    while True:
        click = win.getMouse()

        if simulate_button.clicked(click):
            user_input = input_box.getText().strip()
            if user_input.isdigit():
                n = int(user_input)
                pi_value = simPi(n)
                result_text.setText(f"Approximate π: {pi_value:.4f}")
            else:
                result_text.setText("Invalid input. Enter a number.")

        elif quit_button.clicked(click):
            break

    win.close()

main()
