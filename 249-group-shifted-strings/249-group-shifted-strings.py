class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def strToAsc(s):
            
            res = str(len(s))
            
            for i in range(1,len(s)):
                res+=str((ord(s[i])-ord(s[i-1]))%26)
            return res
        
        d = {}
        
        for i in strings:
            cur = strToAsc(i)
            
            if cur in d:
                d[cur].append(i)
            else:
                d[cur] = [i]

        res = []
        
        for v in d.values():
            res.append(v)
        return res