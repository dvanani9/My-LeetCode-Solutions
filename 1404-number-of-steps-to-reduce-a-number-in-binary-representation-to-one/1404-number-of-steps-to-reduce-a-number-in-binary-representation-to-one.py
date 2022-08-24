class Solution:
    def numSteps(self, s: str) -> int:
        
        n = int(s, 2)
        
        count = 0
        
        while n != 1:
            if n % 2 != 0:
                n += 1
            else:
                n = n // 2
                
            count += 1
            
        return count