# Recursive function to print out the digits of a number in English

def print_digits(num):

    words={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

    if num<10:
        return words[num]
    
    return print_digits(num//10)+" " +words[num%10]

        
def main():

    num:int=int(input("Enter the number:"))

    print(print_digits(num))

main()