class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        p = [i for i in range(R * C)]
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py
                
        points = [(x, y) for x in range(R) for y in range(C)]
        points.sort(key=lambda x:A[x[0]][x[1]], reverse=True)
        
        visited = [[False] * C for _ in range(R)]
        for x, y in points:
            visited[x][y] = True
            
            for nx, ny in [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]:
                if 0 <= nx < R and 0 <= ny < C and visited[nx][ny]:
                    union(x * C + y, nx * C + ny)
                    
            if find(0) == find(R * C - 1):
                return A[x][y]
            
        return -1