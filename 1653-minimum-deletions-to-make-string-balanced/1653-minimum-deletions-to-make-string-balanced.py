class Solution:
    # Bottom Up DP
    def minimumDeletions(self, s: str) -> int:

    # b_count[i] represents the number of b's before i
        b_count, counter = [], 0
        for c in s:
            if c == 'b':
                counter += 1
            b_count.append(counter)

        dp = [0] * len(s)

        for i in range(1, len(dp)): # starting from 1 because dp[0] is always 0
            if s[i] == 'a':
                dp[i] = min(dp[i-1]+1, b_count[i]) # see point 1
            else:
                dp[i] = dp[i-1] # see point 2

        return dp[len(s)-1]
        
        
        