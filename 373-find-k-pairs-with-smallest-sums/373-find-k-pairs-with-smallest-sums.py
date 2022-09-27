import heapq as hq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        
        for i in range(min(k, len(nums1))):
            hq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        for _ in range(k):
            if not heap:
                break
            
            s, idx1, idx2 = hq.heappop(heap)
            result.append( [nums1[idx1], nums2[idx2]] )
            
            if idx2 < len(nums2) - 1:
                hq.heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
        
        return result