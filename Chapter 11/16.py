# Class StatSet to do simple statistical calculations

class StatSet:

    def __init__(self):
        '''Creates a StatSet with no data in it. '''
        self.list=[]

    def addNumber(self,x):
        '''x is a number. Adds the value x to the statSet. '''
        self.list.append(x)

    def mean(self):
        ''' Returns the mean of the numbers in this statSet.'''
        try:
            return sum(self.list) / len(self.list)
        except ZeroDivisionError:  
            return 0
        
    def median(self):
        '''Returns the median of the numbers in this statSet. '''
        if not self.list:
            return 0
        self.sorted=sorted(self.list)
        print(f"Sorted List:{self.sorted}")
        self.n=len(self.list)
        mid=self.n//2
        if self.n%2==0:      
            return (self.sorted[mid]+self.sorted[mid-1])/2
        else:
            return self.sorted[mid]

    def stdDev(self):
        '''Returns the standard deviation of the numbers in this statSet.'''
        if not self.list:
            return 0
        self.mean=self.mean()
        self.var=sum((i-self.mean)**2 for i in self.list)/self.n
        return self.var**(1/2)

    def count(self):
        '''Returns the count of numbers in this statSet. '''
        return self.n

    def min(self):
        '''Returns the smallest value in this statSet. '''
        if not self.list:
            return 0
        return min(self.list)

    def max(self):
        ''' Returns the largest value in this statSet.'''
        if not self.list:
            return 0
        return max(self.list)

def main()->None:

    set=StatSet()

    data=[5,8,7,6,5,4,3,3,9]
    for i in data:
        set.addNumber(i)

    print(f"Mean:{set.mean():.2f}")
    print(f"Median:{set.median():.2f}")
    print(f"Standard Deviation:{set.stdDev():.2f}")
    print(f"Count:{set.count()}")
    print(f"Min:{set.min()}")
    print(f"Max:{set.max()}")

main()