# Another variation of Recursive Fibonacci Program

class FibCounter:

    def __init__(self):
        ''' Creates a new FibCounter, setting its count instance variable to 0.'''
        self.count=0

    def getCount(self):
        ''' Returns the value of count.'''
        return self.count

    def fib(self,n):
        ''' Recursive function to compute the nth Fibonacci number. It increments the count each time it is called.'''
        self.count+=1
        if n<3:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)
            
    def resetCount(self):
        self.count=0

def main():

    counter=FibCounter()

    print(f"The 6th Fibonacci number is: {counter.fib(6)}")
    print(f"The number of times the fib function was called is:{counter.getCount()}")

main()

