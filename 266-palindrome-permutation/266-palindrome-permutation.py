class Solution:
	def canPermutePalindrome(self, s: str) -> bool:
		dic = Counter(s)

		odds = 0
		for key,val in dic.items():
			if (val % 2 == 1):
				odds += 1

		return True if odds <= 1 else False