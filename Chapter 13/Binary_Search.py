nums=[1,4,5,3,2]
target=5
def binary_search(nums,target):
    high=len(nums)-1
    low=0
    while low<=high:
        mid=(low+high)//2
        x=nums[mid]
        if x==target:
            return mid
        elif target<x:
            high=mid-1
        else:
            low=mid+1
    return -1
print(binary_search(nums,target))