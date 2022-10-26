class Solution:
    def numberOfWeakCharacters(self, P: List[List[int]]) -> int:
        
        """
            find count of weak character. character is weak if there exist another character whose 
                1. attack > his_attack
                2. defence > his_defence
            
            
        """
        def isWeak(a, b):
            # returns True if b is weakCharacter
            return a[0] > b[0] and a[1] > b[1]
        
        P.sort(key=lambda x:(x[0], -x[1]))
        
        prev = P[-1]
        count = 0
        
        for i in range(len(P) - 2, -1, -1):
            curr = P[i]
            if isWeak(prev, curr):
                # found a weak
                count += 1
            else:
                prev = P[i]
        
        return count