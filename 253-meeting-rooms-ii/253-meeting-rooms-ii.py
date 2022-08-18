class Solution:
    def minMeetingRooms(self, intervals):
        
        #error checking
        if not intervals:
            return 0
        
        #sort by start time
        intervals.sort(key=lambda interval: interval[0])
        
        #create heap structure
        usedRooms = [intervals[0][1]]
        heapq.heapify(usedRooms)
        
        #iterate through all intervals
        for interval in intervals[1:]:
            #if overlap:
            if interval[0] >= usedRooms[0]:
                heapq.heappop(usedRooms)
            heapq.heappush(usedRooms, interval[1])
            
            
        return len(usedRooms)
    
    
    
        
        
        