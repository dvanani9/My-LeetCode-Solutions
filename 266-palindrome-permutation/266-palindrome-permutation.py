class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        count = Counter(s)
        
        odd = False
        
        for i,j in count.items():
            if j%2 !=0:
                if odd:
                    return False
                odd = True
        
        return True