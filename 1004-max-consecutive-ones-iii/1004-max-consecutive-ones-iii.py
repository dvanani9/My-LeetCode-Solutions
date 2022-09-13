class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start  = 0
        mini = 0
        maxFreq = 0
        for end in range(len(nums)):
            if(nums[end] == 1):
                maxFreq += 1
            if((end - start + 1) - maxFreq ) > k:
                if(nums[start] == 1):
                    maxFreq -= 1

                start += 1
            mini = max(mini , end - start + 1)
        return mini