class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        resultset = set()
        def numsDiff(digits, num):
            if digits == N-1:
                resultset.add(num)
            else:
                if num % 10 + K <= 9:
                    numsDiff(digits + 1, num*10 + num % 10 + K)
                if num % 10 - K >= 0:
                    numsDiff(digits + 1, num*10 + num % 10 - K)

        if N==1:
            resultset.add(0)

        for i in range(1, 10):
            numsDiff(0, i)
        return resultset
