class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 1:
            return k
        
        a, b = k, 1
        
        for _ in range(n-2):
            a, b = (k-1) * (a + b) , a
            
        return k * a