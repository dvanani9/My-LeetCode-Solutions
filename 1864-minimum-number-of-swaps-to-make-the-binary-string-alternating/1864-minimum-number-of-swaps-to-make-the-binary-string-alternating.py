class Solution:
    def minSwaps(self, s: str) -> int:
        zeros, ones = 0, 0
        for c in s:
            if c == "0":
                zeros += 1
            else:
                ones += 1
        
        if abs(zeros - ones) > 1:
            return -1
        
        first = "1" if ones > zeros else "0"
        invalid = 0
        for c in s[::2]:
            if c != first:
                invalid += 1
                
        return invalid if ones != zeros else min(invalid, (len(s)//2) - invalid)