class StockPrice:

    def __init__(self):
        self.prices = defaultdict(int)
        self.max = []
        self.min = []
        self.cur = [-float('inf'), -float('inf')]

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices:
            self.prices[timestamp] += 1
        else:
            self.prices[timestamp] = 0
                
        heappush(self.max, [-price, timestamp, self.prices[timestamp]])
        heappush(self.min, [price, timestamp, self.prices[timestamp]])
        
        if self.cur[0] <= timestamp:
            self.cur = [timestamp, price]

    def current(self) -> int:
        return self.cur[1]

    def maximum(self) -> int:
        while self.max[0][2] != self.prices[self.max[0][1]]:
            heappop(self.max)
        
        return -self.max[0][0]

    def minimum(self) -> int:
        while self.min[0][2] != self.prices[self.min[0][1]]:
            heappop(self.min)
        
        return self.min[0][0]