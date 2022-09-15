class Solution(object):
    def uniqueOccurrences(self, arr):
        cnt = Counter(arr)     
        x = cnt.values()
        y = set(x)
        return len(x) == len(y)