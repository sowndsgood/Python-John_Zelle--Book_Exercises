# Designing inbuilt Python Operations

def count (myList , x):
    '''Returns count of the element in the list'''
    count=0
    for i in myList:
        if i==x:count+=1
    return count

def isin(myList, x):
    '''Returns true if element present in the list'''
    for i in myList:
        if i==x: return True
    return False

def index (myList , x):
    '''Returns index of the element'''
    for i,num in enumerate(myList):
        if num==x:
            return i
    return ValueError

def reverse(myList):
    '''Reverses the list'''
    new=[]
    for i in range(len(myList)-1,-1,-1):
        new.append(myList[i])
    myList=new

def sort (myList):
    