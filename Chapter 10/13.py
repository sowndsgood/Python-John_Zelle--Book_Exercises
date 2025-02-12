# face.py

import math
from graphics import *

class Face:

    def __init__(self, window, center, size):
        """Draws grim face"""
        self.window = window
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.setFill("Yellow")
        self.head.draw(self.window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(self.window)

        time.sleep(1)

        
    def smile(self, center_point, radius, start_angle, end_angle, window):
        """Smiles with mouth wide open"""
        self.mouth.undraw()
        theta=start_angle
        while(theta < end_angle):
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta+=0.03

    def wink(self, center_point, radius, start_angle, end_angle, window):
        """Winks with right eye and mouth"""
        self.mouth.undraw()
        self.rightEye.undraw()
        self.smile(Point(350, 320), 45, math.pi * -0.5, math.pi * 0.5, window)

        theta = start_angle
        while(theta < end_angle):
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = -math.cos(theta) * radius + center_point.getY()

            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta += 0.03

    
    def frown(self, center_point, radius, start_angle, end_angle, window):
        """Frowns with mouth"""
        self.mouth.undraw()
        theta = start_angle
        while(theta < end_angle):
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = -math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            point1.draw(window)
            theta+=0.03
  
def main()->None:

    win = GraphWin("Face", 700, 600)

    face = Face(win, Point(350, 300), 100)
    
    
    #face.smile(Point(350, 320), 45, math.pi * -0.5, math.pi * 0.5, win)
    #face.wink(Point(380, 270), 15, math.pi * -0.5, math.pi * 0.5, win)
    face.frown(Point(350, 350), 45, math.pi * -0.5, math.pi * 0.5, win)
    
    input()
    

main()
    