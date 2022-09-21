class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        
        while l < r:
            m = l + (r - l) // 2
            s = 0
            i = 0
            cnt_day = 1
            while i < len(weights):
                if s + weights[i] > m:
                    s = 0
                    i -= 1
                    cnt_day += 1
                else:
                    s += weights[i]
                i += 1
            if cnt_day > days:
                l = m + 1
            elif cnt_day <= days:
                r = m
        return l
    
    
    