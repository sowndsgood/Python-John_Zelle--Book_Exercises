nums=[1,4,5,3,2]
target=9
def search(nums,target):
    if target in nums:
        return (nums.index(target))
    else:
        return -1
print(search(nums,target))