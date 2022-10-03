class Solution:
    def findMinFibonacciNumbers(self, k):
        n1 = 1
        n2 = 1
        while n2 < k:
            temp = n2
            n1, n2 = n2, n1+n2
        if n2==k:
            return 1
        return self.findMinFibonacciNumbers(k-n1)+1