#Regression problem from Chapter 8 (Programming Exercise 13) using a Regression class.

from graphics import *
import math

class Regression:
    '''Class for regression line'''

    def __init__(self, win):
        """Creates a window with Quit button for regression line"""
        self.win = win
        self.points = []
        
        #DONE Button
        button=Rectangle(Point(50,700),Point(150,750))
        button.draw(win)

        Text(Point(100,725),"DONE").draw(win)

    def draw_point(self, pt):
        '''Draws points'''
        circle = Circle(pt, 2)
        circle.setFill("black")
        circle.draw(self.win)
        
    def add_point(self, pt):
        '''Adds points to points list'''
        self.points.append(pt)

    def predict(self, x):
        """Returns the predicted y-position for the given x-position"""
        ypos = self.ybar + self.m * (x - self.xbar)
        print(f"The y-position is:{ypos}")
        
    def draw_line(self):
        '''Draws the regression line'''
        self.m,self.xbar,self.ybar=self.find_slope(self.points)
        x1=150
        y1=self.ybar+self.m*(x1-self.xbar)
        x2=800
        y2=self.ybar+self.m*(x2-self.xbar)

        Line(Point(x1,y1),Point(x2,y2)).draw(self.win)
    
    def find_slope(self, points):
        '''Finds slope of regression line'''
        n= len(self.points)
        sum_x = 0
        sum_y = 0
        sum_x2 =0
        sum_xy = 0

        for pt in points:
            x=pt.getX()
            y=pt.getY()

            sum_x+=x
            sum_y+=y
            sum_x2+=x**2
            sum_xy+=x*y
        
        xbar=sum_x/n
        ybar=sum_y/n
        num=sum_xy-n*xbar*ybar
        den=sum_x2-n*(xbar)**2
        m=num/den

        return m,xbar,ybar
    
    def clickedQuit(self, pt):
        return (50<pt.getX()<150) and (700<pt.getY()<750)
        
def main()->None:

    win = GraphWin("Regression Line",800,800)

    line = Regression(win)

    while True:
        pt = win.getMouse()
        if line.clickedQuit(pt):
            break
        line.draw_point(pt)
        line.add_point(pt)

    line.draw_line()

    win.getMouse()
    win.close()

    x=int(input("Enter the x position to predict:"))
    line.predict(x)

main()