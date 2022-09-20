class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        A = [[0]*n for _ in range(n)]
        A[row][column] = 1
        
        for _ in range(k):
            B = [[0]*n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    for di, dj in [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]:
                        if 0<=i+di<n and 0<=j+dj<n:
                            B[i][j] += A[i+di][j+dj]/8
            A = B
            
        return sum(map(sum,A))