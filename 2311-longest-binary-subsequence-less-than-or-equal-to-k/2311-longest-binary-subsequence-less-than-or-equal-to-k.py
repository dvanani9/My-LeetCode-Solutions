class Solution:
    def longestSubsequence(self, s, k):
        dp = [0]
        for v in map(int, s):
            if dp[-1] * 2 + v <= k:
                dp.append(dp[-1] * 2 + v)
            for i in range(len(dp) - 1, 0, -1):
                dp[i] = min(dp[i], dp[i - 1] * 2 + v)
        return len(dp) - 1
        