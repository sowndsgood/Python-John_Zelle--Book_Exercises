#Program to find student's GPA

class Student:

    def __init__(self)->None:
        '''Creates a new student object with 0 credits and 0 quality points 
        '''
        self.credits:int=0
        self.quality_points:float=0

    def addGrade(self,gradePoint,credit)->None:
        '''Records a grade for the student.
        '''
        self.credits+=int(credit)
        self.quality_points+=float(gradePoint)*int(credit)

    def cal_GPA(self)->None:
        print(f"Student GPA:{self.quality_points/self.credits:.2f}")
    
def main()->None:

    #Student object
    student=Student()

    #Getting input from user
    while True:
        info:str=input("Enter the gradePoint and credits separated by comma:")
        if info:
            point,credit=info.split(',')
            student.addGrade(point,credit)
        else:
            break
    
    student.cal_GPA()

main()