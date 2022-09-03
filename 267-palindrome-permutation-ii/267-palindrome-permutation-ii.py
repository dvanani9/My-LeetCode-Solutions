class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans, n = [], len(s)
        
        cnts = [0] * 26
        for c in s:
            cnts[ord(c) - ord('a')] += 1
        
        def backtrack(p):
            if len(p) == n//2 + n%2:
                ans.append(p + p[:n//2][::-1])
                return
            
            min_cnt = (len(p) < n//2) + 1
            for i in range(26):
                if cnts[i] >= min_cnt:
                    cnts[i] -= min_cnt
                    backtrack(p + chr(ord('a') + i))
                    cnts[i] += min_cnt
        
        backtrack('')
        
        return ans