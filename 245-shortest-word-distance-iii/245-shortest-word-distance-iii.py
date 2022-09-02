class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        p1 = p2 = -1
        n = len(wordsDict)
        ans = n
        same = (word1 == word2)
        
        for i in range(n):
            if wordsDict[i] == word1:
                if same:
                    # Store the previous index of word1
                    p2 = p1
                p1 = i
            elif wordsDict[i] == word2:
                # The 2nd condition will only get hit if word1 != word2
                p2 = i
                
            if p1 >= 0 and p2 >= 0:
                ans = min(ans, abs(p1 - p2))
        
        return ans
    
    
    
    
    
        