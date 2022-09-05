class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = set()
        
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            
            for k in graph[node]:
                dfs(k)
        
        res = 0
        for i in graph:
            if i not in seen:
                res += 1
                dfs(i)
                
        return res