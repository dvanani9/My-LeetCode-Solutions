class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1
        l,r = 0,len(nums)-1

        while l<r:
            mysum = nums[l] + nums[r]
            if mysum <k:
                max_sum = max(max_sum, mysum)
                l+=1
            else:
                r-=1
        return max_sum