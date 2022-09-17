class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        def dfs(n):
            subs = s[n:]
            
            if len(subs) == 1:
                return 0
            elif len(subs) == 2:
                return int(subs[0] == subs[-1])
            else:
                prev = dfs(n+1)     
                
                check_str = subs[:prev+1]
                rest_str = subs[1:]
                
                if check_str in rest_str:
                    prev = prev+1

                return prev
            
        return  dfs(0)
    
    
    