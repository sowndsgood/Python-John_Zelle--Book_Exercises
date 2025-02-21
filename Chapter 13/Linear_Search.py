nums=[1,4,5,3,2]
target=8
def linear_search(nums,target):
    for i,num in enumerate(nums):
        if num==target:
            return i
    return -1
print(linear_search(nums,target))