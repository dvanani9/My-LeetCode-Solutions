class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = diff = [0] * length  
    
        for update in updates:
            start, end, change = update[0], update[1], update[2]
            diff[start] += change

            if end < length -1:
                diff[end + 1] -= change
        nums[0] = diff[0]

        for i in range(1, len(diff)):
            nums[i] = nums[i - 1] + diff[i]

        return nums