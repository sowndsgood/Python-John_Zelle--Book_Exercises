###Program: Sorting program for students details

from ex_3 import *

from graphics import *

class Button:
    def __init__(self, win, center, height, width, text):
        '''Creates a button in the graphical interface'''

        self.win = win
        w, h = width/2, height/2
        cx, cy = center.getX(), center.getY()
        self.xmin, self.ymax = cx-w, cy+h
        self.xmax, self.ymin = cx+w, cy-h
        pt1 = Point(self.xmax, self.ymax)
        pt2 = Point(self.xmin, self.ymin)
        self.rect = Rectangle(pt1, pt2)
        self.rect.draw(self.win)

        self.label = Text(center, text)
        self.label.draw(win)

        self.activate()
    
    def clicked(self, pt):
        '''Return True if the button is clicked'''
        return self.active and \
               (self.xmin<=pt.getX()<=self.xmax) and \
               (self.ymin<=pt.getY()<= self.ymax)
    
    def activate(self):
        '''Activates the button'''
        self.rect.setWidth(2)
        self.label.setFill("black")
        self.active = True

    def deactivate(self):
        '''Deactivates the button'''
        self.rect.setWidth(1)
        self.label.setFill("grey")
        self.active = False

    def getLable(self):
        '''Return the label of the Button'''
        return self.label.getText()
    

class Sorter:
    def __init__(self):
        self.win = GraphWin("Sorting window", 800, 600)
    
        ##Entry boxes creation
        #Info Text creation
        t1 = Text(Point(250, 200), "Input file name       : ")
        t2 = Text(Point(250, 240), "Output file name      : ")
        t3 = Text(Point(250, 280), "Sort by \n(name/gpa/hours/points): ")

        texts = [t1, t2, t3]

        for to in texts:
            to.draw(self.win)

        #Entry boxes creation
        self.e1 = Entry(Point(450, 200), 15)
        self.e2 = Entry(Point(450, 240), 15)
        self.e3 = Entry(Point(450, 280), 15)

        entries = [self.e1, self.e2, self.e3]

        for eo in entries:
            eo.draw(self.win)


        #buttons creation
        self.b1 = Button(self.win, Point(200, 400), 35, 130, "Sort Ascending")
        self.b2 = Button(self.win, Point(500, 400), 35, 130, "Sort Descending")
        self.b3 = Button(self.win, Point(550, 550), 30, 70, "Quit")

    def run(self):
        '''Entire functionality'''
        sort_values = {"name": Student.getName,
                    "hours": Student.getHours, 
                    "points": Student.getPoints,
                    "gpa": Student.getGpa,
                    "ascending": False,
                    "descending": True
                    }
    
        #functionality
        while True:
            pt = self.win.getMouse()
            infile = self.e1.getText()
            outfile = self.e2.getText()
            sortPar = self.e3.getText()
            
            if self.b3.clicked(pt):
                break
            elif self.b1.clicked(pt):
                sort_type = 'ascending'
            elif self.b2.clicked(pt):
                sort_type = 'descending'
            

            data = readStudents(infile)
            data.sort(key=sort_values[sortPar], reverse=sort_values[sort_type])
            writeStudents(data, outfile)

        self.win.close()

def main():
    app = Sorter()
    app.run()

if __name__ == "__main__":
    main()