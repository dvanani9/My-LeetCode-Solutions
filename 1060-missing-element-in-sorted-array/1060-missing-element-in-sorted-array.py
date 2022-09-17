class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l+ (r-l)//2
            if nums[mid] - nums[0] - mid >= k:
                r = mid - 1
            else:
                l = mid + 1
        return nums[0]+l-1 + k if l-1 < len(nums) else nums[0] + k + len(nums) - 1 
    
    