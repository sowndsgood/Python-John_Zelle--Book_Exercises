#Program to find student's GPA with Letter Grade

class Student:

    def __init__(self)->None:
        '''Creates a new student object with 0 credits and 0 quality points 
        '''
        self.credits:int=0
        self.quality_points:float=0

    def addLetterGrade(self,letter_grade,credit)->None:
        '''Records a grade for the student.
        '''
        
        if letter_grade=='O':
            grade_point=10
        elif letter_grade=='A':
            grade_point=9
        elif letter_grade=='A+':
            grade_point=8
        elif letter_grade=='B':
            grade_point=7
        elif letter_grade=='B+':
            grade_point=6
        elif letter_grade=='C':
            grade_point=5
        
        self.quality_points+=float(grade_point)*int(credit)
        self.credits+=int(credit)

    def cal_GPA(self)->None:
        print(f"Student GPA:{self.quality_points/self.credits:.2f}")
    
def main()->None:

    #Student object
    student=Student()

    #Getting input from user
    while True:
        info:str=input("Enter the letter grade and credits separated by comma:")
        if info:
            point,credit=info.split(',')
            student.addLetterGrade(point.upper(),credit)
        else:
            break
    
    student.cal_GPA()

main()