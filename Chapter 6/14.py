# Sum of the squares of numbers read from a file

def squareEach(nums:list)->list:
    for i in range(len(nums)):
        nums[i]=nums[i]**2
    return nums

def sumList(nums:list[float])->float:
    sum:float=0
    for i in nums:
        sum+=i
    return sum

def toNumbers(strList:list[str])->None:
    for i,element in enumerate(strList):
        strList[i]=int(strList[i])

file=input("Enter the file name:")

read_file=open(file,'r')
write_file=open('14_write_file.txt','w')

str_list=read_file.readlines()
toNumbers(str_list)
new_list=squareEach(str_list)
answer=sumList(new_list)

read_file.close()
write_file.write(f"This is the answer:{answer}")
write_file.close()

