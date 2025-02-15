#Shuffle Function

from random import randrange,randint

def shuffle(myList):
    n=len(myList)
    length=int(n/2)
    for i in range(length):
        k=randrange(0,n)
        l=randrange(0,n)
        myList[k],myList[l]=myList[l],myList[k]

'''
### Fisher-Yates Shuffle
def shuffle(myList):
    n = len(myList)
    for i in range(n - 1, 0, -1):  
        j = randint(0, i)   
        myList[i], myList[j] = myList[j], myList[i]  
'''
def main():

    myList=[2,5,3,4,8,6,7,9,10]
    shuffle(myList)
    print(myList)

if __name__=='__main__':
    main()
