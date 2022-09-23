class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        check = sorted(nums)
        i = 0
        j = len(nums)-1
        while i<len(nums) and nums[i] == check[i]:
            i+=1
        while j>=0 and nums[j] == check[j]:
            j-=1
        if j<i:
            return 0
        else:
            return j-i+1