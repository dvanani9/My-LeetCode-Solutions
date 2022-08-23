class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
		# Set up tuples for each winning set up on the grid
        winSet = {
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0)),
        }
        
        A = set()
        B = set()
        
        currPlayer = A
        
        for x,y in moves:
            currPlayer.add((x,y))
            currPlayer = B if currPlayer == A else A
        
		# If player's moves intersect at least 3 for each tuple in winSet, then we have a winner
        for win in winSet:
            if len(A.intersection(win)) == 3: return 'A'
            elif len(B.intersection(win)) == 3: return 'B'
			
        # If there are no winners and 9 moves are made, we have a draw
        if (len(A) + len(B)) == 9: return 'Draw'
		# else we have pending game
        return 'Pending'
    
    