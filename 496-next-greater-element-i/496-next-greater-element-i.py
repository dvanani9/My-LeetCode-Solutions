class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Method 1: Brute Force T.C: O(nˆ3) S.C: O(1)
        
        ans = [-1] * len(nums1) 
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > nums2[j]:
                            ans[i] = nums2[k]
                            break
        return ans