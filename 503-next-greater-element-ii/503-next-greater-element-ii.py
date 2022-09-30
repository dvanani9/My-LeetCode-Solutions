class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        save = [-1] * len(nums)
        newn = nums + nums
        
        for i in range(len(nums)):
            for j in range(i+1, len(newn)):
                if newn[j] > nums[i]:
                    save[i] = newn[j]
                    break
        
        return save
        