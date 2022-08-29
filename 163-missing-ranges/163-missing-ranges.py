class Solution:
     def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.append(upper+1)
        ans = []
        pre = lower-1
        for cur in nums:
            if pre+1 != cur:
                start = pre+1
                end = cur-1
                w = str(start)
                if start != end:
                    w += "->" + str(end)
                ans.append(w)
            
            pre = cur
        return ans
        