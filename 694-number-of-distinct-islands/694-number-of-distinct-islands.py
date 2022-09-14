class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # distinct islands
        seenIslands = {}
        # visited cells
        visitedCells = set()


        def bfs(r, c, visitedCells, seenIslands):
            q = collections.deque()
            q.append((r, c))
            visitedCells.add((r, c))
            curPath = ""

            while q:
                curRow, curCol = q.popleft()

                # add cell relative to island to path
                curPath += str(curRow-r) + str(curCol-c)

                for nextR, nextC in [curRow+1, curCol], [curRow-1, curCol], [curRow, curCol+1], [curRow, curCol-1]:
                    if 0 <= nextR < ROWS and 0 <= nextC < COLS and (nextR, nextC) not in visitedCells and grid[nextR][nextC] == 1:
                        visitedCells.add((nextR, nextC))
                        q.append((nextR, nextC))

            seenIslands[curPath] = None


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visitedCells:
                    bfs(row, col, visitedCells, seenIslands)

        # return length of seenIslands which will hold all distinct islands
        return len(seenIslands)