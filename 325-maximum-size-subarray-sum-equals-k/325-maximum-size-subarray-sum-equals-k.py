class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        max_size = 0
        # cumulative sum
        cum_sum = 0
        
        for i in range(len(nums)):
            cum_sum += nums[i]
            # when cummulative sum equals k, the index is the most farest we can reach so far
            if cum_sum == k:
                max_size= i+1
            # when current cum_sum - previous cum_sum = k, we need index  distance between cum_sum and the previous sum
            elif cum_sum - k in d:
                max_size= max(max_size, i-d[cum_sum-k])
            # record the cum_sum and it's index 
            if cum_sum not in d:
                d[cum_sum] = i
                
        return max_size
    
    