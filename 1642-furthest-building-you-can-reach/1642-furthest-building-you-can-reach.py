from collections import defaultdict

class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, lad: int) -> int:
        
        l = [] #heap
        heapq.heapify(l)
        c=0
        n =len(h)
        
        for i in range(1,n):
            dif =h[i]-h[i-1]
            if dif>0:
                heapq.heappush(l,dif)
                c+=1 
                if c>lad:
                    bricks-=heapq.heappop(l)
                    c-=1
                    if bricks<0:
                        return i -1
        return n-1
    
    