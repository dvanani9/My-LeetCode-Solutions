class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() 
        subsequences = 0
        l = r = 0
        while r < len(nums):
            while r < len(nums) and nums[r] - nums[l] <= k:
                r += 1
            l = r
            subsequences += 1        
        return subsequences 
    
    