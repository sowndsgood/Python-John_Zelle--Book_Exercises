#Programming Exercise 3 from Chapter 5 

def grade(score:int)->str:
    if 100>=score>=90:
        return('A')
    elif 89>=score>=80:
        return('B')
    elif 79>=score>=70:
        return('C')
    elif 69>=score>=60:
        return('D')
    elif score<60:
        return('F') 

#Input from user 
score:int=int(input("Enter the score:"))
print(f"The score is:{grade(score)}")