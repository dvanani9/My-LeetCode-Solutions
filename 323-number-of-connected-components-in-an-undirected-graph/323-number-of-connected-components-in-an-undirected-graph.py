class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connected = 0
        visited = set()
        # Create Adjacency matrix
        dic = [set() for i in range(n)]
        for x, y in edges:
            dic[x].add(y)
            dic[y].add(x)
        
        def dfs(node):
            visited.add(node)
            for nei in dic[node]:
                if nei not in visited:
                    dfs(nei)
                    
        # Every time DFS function triggers means seperate component
        for i in range (n):
            if i not in visited:
                dfs(i)
                connected += 1
        return connected