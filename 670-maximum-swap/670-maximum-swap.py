class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        total = []
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                num1 = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                num2 = int(num1)
                if num2 > num:
                    num = num2
        return num