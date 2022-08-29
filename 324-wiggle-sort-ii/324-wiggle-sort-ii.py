class Solution(object):
    def wiggleSort(self, nums: List[int]) -> None:
		#to make it work as a min-heap
        heap = [-i for i in nums]
        heapify(heap)
		
		#putting largest element into odd index
        for i in range(1,len(nums),2):
            nums[i] = -heappop(heap)
		
		#putting remaining element into even index
        for i in range(0, len(nums), 2):
            nums[i] = -heappop(heap)