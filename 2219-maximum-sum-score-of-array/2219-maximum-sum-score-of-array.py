class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
		
		# Start a lefthand and a righhand sum - left: 0, right: sum of all elements
        lh, rh = 0, sum(nums)
        maxSF = float("-inf")
        
        for i in range(len(nums)):
            
			# add to the lefthand sum
            lh += nums[i]
			
			# check if this is the maximum
            maxSF = max(max(lh,rh),maxSF)
			
			# decrement the righthand sum
            rh -= nums[i]
        
        return maxSF
    
    
        