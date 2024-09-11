# Program to draw a quiz score histogram

from graphics import *

def main()->None:

    #User input for file name
    file_name=input("Enter the file name:")

    input_file=open(file_name,'r')

    numbers=input_file.readlines()

    count:list(int)=[0,0,0,0,0,0,0,0,0,0,0]
    for i in numbers:
        count[int(i)]+=1

    #Graphical Window Creation
    win=GraphWin("Quiz Scores",250,120)

    x1,y1=15,100

    for i in range(11):
        Text(Point(x1+2,y1+10),i).draw(win)
        x2=x1+10
        y2=y1-count[i]
        Rectangle(Point(x1,y1),Point(x2,y2)).draw(win)

        x1+=20

    win.getMouse()
    win.close()

main()