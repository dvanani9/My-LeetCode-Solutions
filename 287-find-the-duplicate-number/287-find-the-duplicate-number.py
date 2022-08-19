class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict = {}
        
        # initialize hash_dict with constant value
        for i in nums:
            hash_dict[i] = 0
            
        # count the occurence of values
        for i in nums:
            hash_dict[i] = hash_dict[i] + 1
            if hash_dict[i] == 2:
                return i