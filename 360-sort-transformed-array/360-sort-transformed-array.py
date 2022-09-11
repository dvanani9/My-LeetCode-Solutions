class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        ans = []
        
        for i in range(len(nums)):
            res = (a*(nums[i])**2) + (b*nums[i]) + c
            ans.append(res)

        return sorted(ans)

    
    