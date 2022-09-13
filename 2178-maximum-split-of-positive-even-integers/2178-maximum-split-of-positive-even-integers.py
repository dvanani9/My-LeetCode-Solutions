class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum & 1:
            return []
        res, num = [], 2
        while finalSum - num > num:
            res.append(num)
            finalSum -= num
            num += 2
        res.append(finalSum)
        return res