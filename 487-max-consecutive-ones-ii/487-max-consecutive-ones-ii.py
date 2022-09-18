class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        last_zero_ix = -1
        max_count = 0
        count = 0  
        for i in range(len(nums)):
            
            if nums[i] == 0:
                count = i - last_zero_ix
                last_zero_ix = i
            else:
                count +=1
            
            max_count = max(max_count, count)
            
        return(max_count)
    
    
    
    