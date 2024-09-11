# Horizontal bar chart of student exam scores

from graphics import *

def main()->None:

    #User input for file name
    file_name=input("Enter the file name:")

    input_file=open(file_name,'r')

    count:int=int(input_file.readline().strip())

    students=[]
    marks=[]

    for line in input_file:
        content=line.strip().split()
        if len(content)==2:
            students.append(content[0])
            marks.append(int(content[1]))

    #Graphical Window Creation
    win=GraphWin("Exam Scores",400,count*30+20)

    x1,y1=50,20
    x2,y2=150,20

    for i in range(count):
        
        #Text for Name
        Text(Point(x1,y1),students[i]).draw(win)
        x3=x2+marks[i]*2
        y3=y2+10

        #Rectangle for marks
        Rectangle(Point(x2,y2),Point(x3,y3)).draw(win)

        #Updating values for next name
        y1+=30
        y2+=30

    win.getMouse()
    win.close()


main()