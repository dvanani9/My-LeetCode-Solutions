class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        n = len(nums)
        forward = [0] * (n+1)
        back = [0] * (n+1)
        for i in range(1,1+n):
            forward[i] = nums[i-1] + forward[i-1]
        for i in range(n-1, -1, -1):
            back[i] = nums[i] + back[i+1]
        print(forward[1:],back[:-1])
        
        return max(max(forward[1:]), max(back[:-1]))
    
    
        