# Sort a file of students with special key function

class Student:
    
    def __init__(self, name, hours, Qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(Qpoints)

    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours

    def getPoints(self):
        return self.qpoints
    
    def getGpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints 
    # returns a corresponding Student object 
    name, hours, qpoints = infoStr.split("\t") 
    return Student(name, hours, qpoints)

def readStudents(infile_name):
    '''Gets information from input file'''
    infile = open(infile_name, 'r')
    info = []
    for line in infile:
        info.append(makeStudent(line))
    infile.close()
    return info


def writeStudents(info, outfile):
    '''Writes the sorted info to output file'''
    outfile = open(outfile, 'w')

    print(f'{"Name":20}{"Hours":10}{"Points":10}{"GPA":10}', file=outfile)
    for student in info:
        print(f"{student.getName():12}{student.getHours():10}{student.getPoints():10}{student.getGpa():10.3f}",file=outfile)

    outfile.close()

def sort_GPA(data,order):
    decorated_list=[(student.getGpa(),student) for student in data]
    decorated_list.sort(reverse=(order=='desc'))
    return [student for gpa,student in decorated_list]

def main():

    infile = input("Enter the input file name:")
    outfile = input("Enter the output file name:")
    order=input("Enter asc or desc order:").lower()

    #Retrived info from input file
    data = readStudents(infile)

    sorted=sort_GPA(data,order)

    writeStudents(data,outfile)

if __name__ == "__main__":
    main()