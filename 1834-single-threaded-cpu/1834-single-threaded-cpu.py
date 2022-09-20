class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        
        curr_time = tasks[0][0]
        i = 0
        pq = []
        ans = []
        
        while i < len(tasks):
            
            while  i < len(tasks) and tasks[i][0] <= curr_time:
                heappush(pq, (tasks[i][1], tasks[i][2]))
                i+=1
                
            if pq:
                t0, i0 = heappop(pq)
                curr_time += t0
                ans.append(i0)
            else:
                curr_time = tasks[i][0]
        
        while pq:
            _, i0 = heappop(pq)
            ans.append(i0)
        
        return ans 
    
    
    