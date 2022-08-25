class Solution:
	def minCost(self, colors: str, neededTime: List[int]) -> int:
        
		arr_len = len(colors)
		dp = [0]*arr_len
		for i in range(1,arr_len):
			if colors[i] != colors[i-1]:
				dp[i] = dp[i-1]
			elif neededTime[i-1]< neededTime[i]:
				dp[i] = dp[i-1]+min(neededTime[i],neededTime[i-1])
			else:
				dp[i] = dp[i-1]+min(neededTime[i],neededTime[i-1])
				neededTime[i],neededTime[i-1] = neededTime[i-1],neededTime[i]
		return dp[-1]