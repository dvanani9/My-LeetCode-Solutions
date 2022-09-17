class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):   
            if nums[i] > nums[0] + k + i -1:  # nums[0] + k + i -1 is the missing number
                return nums[0] + k + i -1
        return nums[0] + k + len(nums) - 1  # if the missing number is larger than the last number in the array