class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums = [x for x in nums if x!= 0]
        return len(list(set(nums)))
    
    
    
    
    