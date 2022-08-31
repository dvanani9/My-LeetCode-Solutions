class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            
            return False
        summ=sum(nums)//2
        sumset=set()
        sumset.add(0)
        sumset.add(nums[-1])
        
        for i in range(len(nums)-2,-1,-1):
            h=sumset.copy()
            for j in h:
                if j+nums[i] ==summ:
                    return True
                sumset.add(j+nums[i])
        return summ in sumset
        