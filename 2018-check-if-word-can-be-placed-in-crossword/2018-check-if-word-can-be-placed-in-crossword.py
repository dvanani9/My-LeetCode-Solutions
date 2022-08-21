class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        @functools.lru_cache(None)
        def valid_start(r, c, d):
            if d == 0:
                # horizontally right
                prev_r, prev_c = r, c - 1
            elif d == 1:
                # horizontally left
                prev_r, prev_c = r, c + 1
            elif d == 2:
                # vertically down
                prev_r, prev_c = r - 1, c
            elif d == 3:
                # vertically up
                prev_r, prev_c = r + 1, c
                
            return board[r][c] in [' ', word[0]] and (prev_r < 0 or prev_r >= rows or prev_c < 0 or prev_c >= cols or board[prev_r][prev_c] == '#')
        
        @functools.lru_cache(None)
        def dfs(r, c, d, i):                        
            if d == 0:
                # horizontally right
                nxt_r, nxt_c = r, c + 1
            elif d == 1:
                # horizontally left
                nxt_r, nxt_c = r, c - 1
            elif d == 2:
                # vertically down
                nxt_r, nxt_c = r + 1, c
            elif d == 3:
                # vertically up
                nxt_r, nxt_c = r - 1, c
                
                
            if nxt_r < 0 or nxt_r >= rows or nxt_c < 0 or nxt_c >= cols or board[nxt_r][nxt_c] == '#':
                return i == len(word) - 1
            
            if i == len(word) - 1 or board[nxt_r][nxt_c] not in (' ', word[i + 1]):
                return False

            return dfs(nxt_r, nxt_c, d, i + 1)
        

        for r in range(rows):
            for c in range(cols):
                for d in range(4):
                    if valid_start(r, c, d):
                        if dfs(r, c, d, 0):
                            return True
                    
        return False