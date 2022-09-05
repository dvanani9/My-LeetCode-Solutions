class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            res.append(nums2.index(i))
            i = -1
        return res