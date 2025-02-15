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

'''
def reverse(myList):
    "Reverses the list"
    new=[]
    for i in range(len(myList)-1,-1,-1):
        new.append(myList[i])
    return new
'''

def reverse(myList):
    "Reverses the list in place"
    start=0
    end=len(myList)-1
    while start<end:
        myList[start],myList[end]=myList[end],myList[start]
        start+=1
        end-=1

def sort(myList):
    '''Sorts the list in ascending order in place using Selection Sort'''
    n=len(myList)
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if myList[j]<myList[i]:
                min=j
        myList[i],myList[min]=myList[min],myList[i]

def sel_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

myList=[8,6,5,7,4,2]
print("Original List:",myList)
print(f"Count of 2:{count (myList , 2)}")
print(f"Is 8 in list:",isin(myList, 8))
print(f"Index of 2:",index (myList , 2))
reverse(myList)
print("Reversed List:",myList)
sort(myList)
print("Sorted List:",myList)





   
