class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        tracker = collections.Counter([])
        
        for i, letter in enumerate(keyboard):
            tracker[letter] = i
        
        res, tmp = 0, 0
        for letter in word:
            res += abs(tracker[letter] - tmp)
            tmp = tracker[letter]
            
        return res
        