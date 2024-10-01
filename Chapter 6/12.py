#Sum of the numbers in the list.

def sumList(nums:list[float])->float:
    sum:float=0
    for i in nums:
        sum+=i
    return sum

nums:list[float]=[2,3,4,5,6,7]
print(f"The sum is:{sumList(nums)}") 