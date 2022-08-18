class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        
        for i, j in enumerate(manager):
            graph[j].append(i)
            
        def dfs(j):
            return informTime[j] + max([dfs(i) for i in graph[j]], default = 0)
         
        return dfs(headID)
    
    
    