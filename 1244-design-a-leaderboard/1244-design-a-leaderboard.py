class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = score
        else:
            self.board[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(list(self.board.values()),reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.board.pop(playerId)
        
        
        