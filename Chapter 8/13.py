# Regression line

from graphics import  *

def main()->None:

    win=GraphWin("Regression Line",800,800)

    button=Rectangle(Point(50,700),Point(150,750))
    button.draw(win)

    Text(Point(100,725),"DONE").draw(win)
    
    n=0
    sum_x=0
    sum_y=0
    sum_x2=0
    sum_xy=0
    
    while True:
        pt=win.getMouse()
        if (50<pt.getX()<150) and (700<pt.getY()<750):
            break
        point=Circle(pt,2).draw(win)
        
        x=pt.getX()
        y=pt.getY()

        n+=1
        sum_x+=x
        sum_y+=y
        sum_x2+=x**2
        sum_xy+=x*y

    xbar=sum_x/n
    ybar=sum_y/n
    num=sum_xy-n*xbar*ybar
    den=sum_x2-n*(xbar)**2
    m=num/den

    x1=150
    y1=ybar+m*(x1-xbar)
    x2=800
    y2=ybar+m*(x2-xbar)

    Line(Point(x1,y1),Point(x2,y2)).draw(win)
    win.getMouse()
    win.close()

if __name__=='__main__':
    main()