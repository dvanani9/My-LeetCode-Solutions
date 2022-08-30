class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        
        for i in range(len(s)):
            char = s[i]
            last[ord(char)-ord('a')] = i
        
        j = 0
        start = 0
        ans = []
        for i in range(0, len(s)):
            char = s[i]
            j = max(j, last[ord(char)-ord('a')])
            if(i==j):
                ans.append(i-start+1)
                start = i + 1
        return ans