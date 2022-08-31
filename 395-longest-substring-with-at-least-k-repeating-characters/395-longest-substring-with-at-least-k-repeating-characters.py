class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        for ch in set(s):
            if s.count(ch) < k:
                temp = s.split(ch)
                return max(self.longestSubstring(sub, k) for sub in temp)
        length = len(s)
        return length
    
    