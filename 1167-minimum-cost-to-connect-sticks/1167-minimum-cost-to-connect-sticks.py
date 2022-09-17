import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        
        res = 0
        while len(sticks) > 1:
            num1, num2 = heapq.heappop(sticks), heapq.heappop(sticks)
            new_num = num1 + num2
            res += new_num
            heapq.heappush(sticks, new_num)
        
        return res