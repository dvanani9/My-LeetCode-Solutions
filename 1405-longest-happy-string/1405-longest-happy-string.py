class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {"a": a, "b": b, "c": c}
        happy = ""
        
        while True:
            max_char, max_count = None, 0
            
            for char, count in counts.items():
                if count > max_count and \
                not (len(happy) > 1 and happy[-1] == char and happy[-2] == char):
                    max_char = char
                    max_count = count
            
            if max_char is None:
                return happy
            else:
                happy += max_char
                counts[max_char] -= 1