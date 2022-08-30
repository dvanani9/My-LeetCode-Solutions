class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s)<=2:
            return len(s)
        
        l,r=0,0
        res=set()
        count=0
        maxcount=0
        
        for r in range(len(s)):
            if s[r] not in res:
                if count<2:
                    res.add(s[r])
                    count+=1
                else:
                    k=r-1
                    while k-1 and s[k]==s[k-1]:
                        k-=1
                    l=k
                    res=set()
                    res.add(s[r])
                    res.add(s[l])
            maxcount=max(maxcount,r-l+1)
        return maxcount