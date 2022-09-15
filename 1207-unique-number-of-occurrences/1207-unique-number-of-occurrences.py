class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        x = Counter(arr).values()
        return len(x) == len(set(x))
    
    