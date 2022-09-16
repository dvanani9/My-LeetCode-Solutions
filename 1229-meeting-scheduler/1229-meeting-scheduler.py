class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda z: z[0])
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            
            start1, end1 = slots1[ptr1]
            start2, end2 = slots2[ptr2]
            
            if start1<=start2 < end1 or start2<=start1 < end2:
                start = max(start1, start2)
                end = start + duration
                if end <= min(end1, end2):
                    return [start, end]
            
            if end2 < end1:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return []