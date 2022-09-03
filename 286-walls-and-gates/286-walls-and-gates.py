class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:   
                    q.append([r, c])
                    
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]    
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 2147483647:
                        grid[r][c] = grid[row][col] + 1
                        q.append([r, c])