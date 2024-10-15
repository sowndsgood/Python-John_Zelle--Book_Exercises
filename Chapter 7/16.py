#Archery Scorer

from graphics import *
import math

def main()->None:
    win=GraphWin("Archery Target",300,300)
    radius:int=25
    circlew=Circle(Point(150,150),50)
    circlew.setFill('white')
    circlew.draw(win)
    circleb=Circle(Point(150,150),40)
    circleb.setFill('black')
    circleb.draw(win)
    circlebl=Circle(Point(150,150),30)
    circlebl.setFill('blue')
    circlebl.draw(win)
    circler=Circle(Point(150,150),20)
    circler.setFill('red')
    circler.draw(win)
    circley=Circle(Point(150,150),10)
    circley.setFill('yellow')
    circley.draw(win)

    text=Text(Point(70,50),f"Target the point")
    text.draw(win)

    sum=0
    for i in range(5):
        p=win.getMouse()
        x=p.getX()
        y=p.getY()
        d=math.sqrt(((150-x)**2)+((150-y)**2))
        if 40< d <=50:
            point=1
        elif 30<d <=40:
            point=3
        elif 20<d <=30:
            point=5
        elif 10<d <=20:
            point=7
        elif 0<=d <=10:
            point=9
        else:
            point=0
        
        text.setText(f"The point is :{point}")
        print(point)
        sum+=point
    
    print("Total points is:",sum)
    win.close()
main()