class HitCounter:
    def __init__(self):
        self.hitCounter = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.hitCounter and self.hitCounter[-1][0] == timestamp:
            self.hitCounter[-1][1] += 1
        else:
            self.hitCounter.append([timestamp, 1])
        self.total += 1
        
    def getHits(self, timestamp: int) -> int:
        while self.hitCounter and self.hitCounter[0][0] <= timestamp - 300:
            self.total -= self.hitCounter.popleft()[1]
        return self.total
    
    