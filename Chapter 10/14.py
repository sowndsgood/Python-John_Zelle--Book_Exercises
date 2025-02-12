from graphics import *
import math
import random

class Structure:
    def __init__(self, lst):
        self.lst = lst
           
    def draw(self, win):
        for elm in self.lst:
            elm.draw(win)

    def move(self, dx, dy):
        for elm in self.lst:
            elm.move(dx, dy)

    def undraw(self):
        for elm in self.lst:
            elm.undraw()

class Face:
    def __init__(self, win, center, size):
        self.win = win
        self.center = center
        self.size = size
        self.face = Circle(center, size)
        self.face.setFill('yellow')
        self.face.draw(win)
        
        self.left_eye = Circle(Point(center.getX() - size / 3, center.getY() - size / 3), size / 10)
        self.left_eye.setFill('black')
        self.left_eye.draw(win)
        
        self.r_eye = Circle(Point(center.getX() + size / 3, center.getY() - size / 3), size / 10)
        self.r_eye.setFill('black')
        self.right_eye = Structure([self.r_eye])
        self.right_eye.draw(win)
        
        
        mouth_object = Line(Point(center.getX() - size / 2, center.getY() + size / 3),
                          Point(center.getX() + size / 2, center.getY() + size / 3))
        self.mouth = Structure([mouth_object])
        self.mouth.draw(win)
        
    def move(self, dx, dy):
        self.face.move(dx, dy)
        self.left_eye.move(dx, dy)
        self.right_eye.move(dx, dy)
        self.mouth.move(dx, dy)
        self.center = self.face.getCenter()
    
    def drawArc(self, radius, start_angle, end_angle, center_point, a):
        theta = start_angle
        elms = []
        while theta < end_angle:
            x_coord = math.sin(theta) * radius + center_point.getX()
            y_coord = a * math.cos(theta) * radius + center_point.getY()
            point1 = Point(x_coord, y_coord)
            elms.append(point1)
            theta += 0.03

        return elms

    def drawReye(self):
        self.r_eye.undraw()
        self.r_eye = Circle(Point(self.center.getX() + self.size / 3, self.center.getY() - self.size / 3), self.size / 10)
        self.r_eye.setFill("black")
        eye_elms = [self.r_eye]
        self.right_eye = Structure(eye_elms)
        self.right_eye.draw(self.win)

    def getCenterPt(self, x=0, y = 0):
        x = self.center.getX() + x
        y = self.center.getY() + y
        return Point(x, y)
    
    def smile(self):
        '''Makes the face smile'''
        start_angle, end_angle = math.pi * -0.5, math.pi * 0.5
        radius = 45
        center_point = self.getCenterPt(y=33)
        self.mouth.undraw()
        self.right_eye.undraw()
        self.mouth = Structure(self.drawArc(radius, start_angle, end_angle, center_point, 1))
        self.mouth.draw(self.win)

        self.drawReye()
                  
    def frown(self):
        '''Changes face to frown expression'''
        self.mouth.undraw()
        self.right_eye.undraw()
        start_angle, end_angle = math.pi * -0.5, math.pi * 0.5
        radius = 40
        center_point = self.getCenterPt(y=33)
        self.mouth = Structure(self.drawArc(radius, start_angle, end_angle, center_point, -1))
        self.mouth.draw(self.win)
        self.drawReye()

    def wink(self):
        '''Changes the face to wink expression'''
        self.mouth.undraw()
        self.right_eye.undraw()
        start_angle, end_angle = math.pi * -0.5, math.pi * 0.5
        radius = 10
        center_point_1 = self.getCenterPt(x=25, y=-30)
        center_point_2 = self.getCenterPt(y=33)
        
        self.right_eye = Structure(self.drawArc(radius, start_angle, end_angle, center_point_1, -1))
        self.mouth = Structure(self.drawArc(45, start_angle, end_angle, center_point_2, 1))
        self.right_eye.draw(self.win)
        self.mouth.draw(self.win)
           
    def changeExpression(self):
        '''Changes the reaction of the face'''
        exp = random.choice([self.frown, self.wink, self.smile])
        exp()

def main():
    win = GraphWin("Bouncing Face", 700, 600)
    face = Face(win, Point(350, 300), 100)
    
    dx, dy = 5, 5
 
    while True:
        face.move(dx, dy)
        center = face.center
       
        if center.getX() - face.size <= 0 or center.getX() + face.size >= win.getWidth():
            dx = -dx
            face.changeExpression()
                    
        if center.getY() - face.size <= 0 or center.getY() + face.size >= win.getHeight():
            dy = -dy
            face.changeExpression()
            
        time.sleep(0.02)

main()