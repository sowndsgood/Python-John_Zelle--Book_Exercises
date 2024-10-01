# Modifying the list by squaring each entry.

def squareEach(nums:list)->list:
    for i in range(len(nums)):
        nums[i]=nums[i]**2
    return nums

nums:list[float]=[2,3,4,5,6,7]
print(f"The new list is:{squareEach(nums)}")   