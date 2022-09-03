class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        idx = {0:-1}
        cur = 0
        for i, num in enumerate(nums):
            cur = (cur + num) % k
            if cur in idx:
                if i-idx[cur] > 1:
                    return True
            else:
                idx[cur]  = i
        return False