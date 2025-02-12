# stats.py 

from math import sqrt

class Statistics:

    def __init__(self):
        pass

    def mean_fun(self,nums):
        self.mean=sum(nums)/len(nums)
        return self.mean
    
    def stdDev(self,nums):
        sum:float=0
        for i in nums:
            sum+=(self.mean-i)**2

        self.std=sqrt(sum/(len(nums)-1))
        return self.std
    
    def meanStdDev(self,nums):
        '''May not update if mean and std functions are not called'''
        mean_value=self.mean_fun(nums)
        std_value=self.stdDev(nums)
        return mean_value,std_value
    
def main()->None:

    nums=[]

    inp=int(input("Enter the first number of list:"))
    
    while inp:
        nums.append(int(inp))
        inp=input("Enter the next number of list:")
       
    print(nums)

    stat=Statistics()

    print(f"The mean of nums: {stat.mean_fun(nums):.2f}")
    print(f"The STD of nums: {stat.stdDev(nums):.2f}")
    mean,std=stat.meanStdDev(nums)
    print(f"The mean and STD of nums: {mean:.2f}, {std:.2f}")

main()


